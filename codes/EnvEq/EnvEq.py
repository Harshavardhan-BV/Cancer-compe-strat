import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp,odeint
from scipy.stats import truncnorm
import pandas as pd

def f_res(res,lim):
    if res>=lim[1]:
        return 1
    elif res>=lim[0]:
        return (res-lim[0])/(lim[1]-lim[0])
    else:
        return 0

def enveq(t,x,p,mu,lam,r,K,delta,rho,lim):
    #Equation for oxygen: constant production, uptake by all 3 cells, decay
    do2=p[0]-mu[0,0]*x[0]-mu[0,1]*x[1]-mu[0,2]*x[2]-lam[0]*x[3]
    #Equation for testosterone: production by Tp, uptake by all Tp, T+, decay
    dtest=p[1]*x[1]-mu[1,0]*x[0]-mu[1,1]*x[1]-lam[1]*x[4]
    #Equation for T+
    dTpos=r[0]*x[0]*(1-x[0]/(K+rho[0]*f_res(x[3],lim[0,0])*f_res(x[4],lim[1,0])))-delta[0]*x[0]
    #Equation for Tp
    dTpro=r[1]*x[1]*(1-x[1]/(K+rho[1]*f_res(x[3],lim[0,1])*f_res(x[4],lim[1,1])))-delta[1]*x[1]
    #Equation for T-
    dTneg=r[2]*x[2]*(1-x[2]/(K+rho[2]*f_res(x[3],lim[0,2])))-delta[2]*x[2]
    # Returns the array with dx_i/dt at that time
    return np.array([dTpos,dTpro,dTneg,do2,dtest])

def solve_eq(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name):
    #just dump the input to some text file for reference
    inp=pd.DataFrame([t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name])
    inp.to_csv("../../raw_output/EnvEq/"+f_name+"_inp.log",index=False)
    #Timeseries arrays
    t=np.arange(0,t_max,dt)
    #Numerical solution of equation
    sol = odeint(enveq,y0,t,args=(p,mu,lam,r,K,delta,rho,lim),tfirst=True)
    df=pd.DataFrame({'t':t,'Tpos':sol[:,0],'Tpro':sol[:,1],'Tneg':sol[:,2],'o2':sol[:,3],'test':sol[:,4]})
    df.to_csv("../../raw_output/EnvEq/"+f_name+".csv",index=False)

def test_parms(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name): #for debugging purposes
    print(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name)
