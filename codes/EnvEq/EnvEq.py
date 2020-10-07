import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.stats import truncnorm

def f_res(res,lim):
    if res<=lim[0]:
        return 0
    elif res<=lim[1]:
        return (res-lim[0])/(lim[1]-lim[0])
    else:
        return 1

def enveq(t,x,p,mu,lam,r,K,delta,rho,lim):
    #Equation for oxygen: constant production, uptake by all 3 cells, decay
    do2=p[0]-mu[0,0]*x[0]-mu[0,1]*x[1]-mu[0,2]*x[2]-lam[0]*x[3]
    #Equation for testosterone: production by Tp, uptake by all Tp, T+, decay
    dtest=p[1]*x[0]-mu[1,0]*x[0]-mu[1,1]*x[1]-lam[1]*x[4]
    #Equation for T+
    dTpos=r[0]*x[0]*(1-x[0]/(K+rho[0]*f_res(x[3],lim[0,0])*f_res(x[4],lim[1,0])))-delta[0]*x[0]
    #Equation for Tp
    dTpro=r[1]*x[1]*(1-x[1]/(K+rho[1]*f_res(x[3],lim[0,1])*f_res(x[4],lim[1,1])))-delta[1]*x[1]
    #Equation for T-
    dTneg=r[2]*x[2]*(1-x[2]/(K+rho[2]*f_res(x[3],lim[0,2])))-delta[2]*x[2]
    # Returns the array with dx_i/dt at that time
    return np.array([dTpos,dTpro,dTneg,do2,dtest])

#importing variables from input and parsing into numpy arrays
from input import *
y0=np.array([y0_Tpos,y0_Tpro,y0_Tneg,y0_o2,y0_test])
p=np.array([p_o2,p_test])
mu=np.array([[mu_o2Tpos,mu_o2Tpro,mu_o2Tneg],[mu_testTpos,mu_testTpro,0]])
lam=np.array([lam_o2,lam_test])
r=np.array([r_Tpos,r_Tpro,r_Tneg])
delta=np.array([delta_Tpos,delta_Tpro,delta_Tneg])
rho=np.array([rho_Tpos,rho_Tpro,rho_Tneg])
lim=np.array([[[l_lim_o2Tpos,u_lim_o2Tpos],[l_lim_o2Tpro,u_lim_o2Tpro],[l_lim_o2Tneg,u_lim_o2Tneg]],[[l_lim_testTpos,u_lim_testTpos],[l_lim_testTpro,u_lim_testTpro],[0,0]]])

#Timeseries arrays
t=np.arange(0,t_max,dt)
#Numerical solution of equation
sol = solve_ivp(enveq, [0, t_max], y0, args=(p,mu,lam,r,K,delta,rho,lim),t_eval=t,dense_output=True)
plt.plot(t,sol.y.T)
plt.xlabel("Time (days)")
plt.ylabel("Density")
df=pd.DataFrame({'t':t,'y1':sol.y[0],'y2':sol.y[1],'y3':sol.y[2],'o2':sol.y[3],'test':sol.y[4]})
plt.savefig("../../figures/EnvEq/"+f_name+".svg")
df.to_csv("../../raw_output/EnvEq/"+f_name+".csv",index=False)
