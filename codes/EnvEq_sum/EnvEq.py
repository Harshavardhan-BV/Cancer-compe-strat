import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp,odeint,ode
from scipy.stats import truncnorm
import pandas as pd

def f_res(res,lim):
    if res>=lim[1]:
        return 1
    elif res>=lim[0]:
        return (res-lim[0])/(lim[1]-lim[0])
    else:
        return 0

def check_therapy_keys(therapy_parms): #set default parameters if keys dont exist
    if not ('abi_mode' in therapy_parms.index):
        therapy_parms['abi_mode']='NA' #if no mode specified assume no therapy
    if not ('dtx_mode' in therapy_parms.index):
        therapy_parms['dtx_mode']='NA' #if no mode specified assume no therapy
    if not ('abi_therapy_on' in therapy_parms.index):
        therapy_parms['abi_therapy_on']=False #therapy off by default
    if not ('dtx_therapy_on' in therapy_parms.index):
        therapy_parms['dtx_therapy_on']=False #therapy off by default
    if not ('abi_change_time' in therapy_parms.index):
        therapy_parms['abi_change_time']=0
    if not ('dtx_change_time' in therapy_parms.index):
        therapy_parms['dtx_change_time']=0
    if not ('abi_delay' in therapy_parms.index):
        therapy_parms['abi_delay']=0 #no delay by default
    if not ('dtx_delay' in therapy_parms.index):
        therapy_parms['dtx_delay']=0 #no delay by default

def abi_SOC(t,x,therapy_parms):
    if not therapy_parms['abi_therapy_on']: #check if therapy is on already
        therapy_parms['abi_therapy_on']=True #set therapy on
    #else make no changes

def abi_AT(t,x,therapy_parms):
    if therapy_parms['abi_therapy_on']: #check if therapy is on already
        if (x[0:3].sum() <= therapy_parms['abi_at_x_off']): #turn off therapy if cell count drop below threshold
            therapy_parms['abi_therapy_on']=False
    else: #therapy is not on already
        if (x[0:3].sum() >= therapy_parms['abi_at_x_on']): #turn on therapy if cell count rises above threshold
            therapy_parms['abi_therapy_on']=True

def abi_AT_nn(t,x,therapy_parms):
    if therapy_parms['abi_therapy_on']: #check if therapy is on already
        if (x[0:2].sum() <= therapy_parms['abi_at_x_off']): #turn off therapy if cell count drop below threshold
            therapy_parms['abi_therapy_on']=False
    else: #therapy is not on already
        if (x[0:2].sum() >= therapy_parms['abi_at_x_on']): #turn on therapy if cell count rises above threshold
            therapy_parms['abi_therapy_on']=True

def abi_MT(t,x,therapy_parms):
    if therapy_parms['abi_therapy_on']: #check if therapy is on already
        if (t >= therapy_parms['abi_mt_t_off'] + therapy_parms['abi_change_time']): #turn off therapy if current time higher than time window
            therapy_parms['abi_change_time']=t
            therapy_parms['abi_therapy_on']=False
    else: #therapy is not on already
        if (t >= therapy_parms['abi_mt_t_on'] + therapy_parms['abi_change_time']): #turn off therapy if current time higher than time window
            therapy_parms['abi_change_time']=t
            therapy_parms['abi_therapy_on']=True

def abi_therapy(t,x,therapy_parms):
    if t >= therapy_parms['abi_delay']:
        if therapy_parms['abi_mode']=='SOC':
            abi_SOC(t,x,therapy_parms)
        elif therapy_parms['abi_mode']=='AT':
            abi_AT(t,x,therapy_parms)
        elif therapy_parms['abi_mode']=='AT_nn':
            abi_AT_nn(t,x,therapy_parms)
        elif therapy_parms['abi_mode']=='MT':
            abi_MT(t,x,therapy_parms)
        else:
            return None #do nothing if none of the above
    else:
        return None #do nothing if delay window not crossed

def dtx_SOC(t,x,therapy_parms):
    if not therapy_parms['dtx_therapy_on']: #check if therapy is on already
        therapy_parms['dtx_therapy_on']=True #set therapy on
    #else make no changes

def dtx_AT(t,x,therapy_parms):
    if therapy_parms['dtx_therapy_on']: #check if therapy is on already
        if (x[0:3].sum() <= therapy_parms['dtx_at_x_off']): #turn off therapy if cell count drop below threshold
            therapy_parms['dtx_therapy_on']=False
    else: #therapy is not on already
        if (x[0:3].sum() >= therapy_parms['dtx_at_x_on']): #turn on therapy if cell count rises above threshold
            therapy_parms['dtx_therapy_on']=True

def dtx_MT(t,x,therapy_parms):
    if therapy_parms['dtx_therapy_on']: #check if therapy is on already
        if (t >= therapy_parms['dtx_mt_t_off'] + therapy_parms['dtx_change_time']): #turn off therapy if current time higher than time window
            therapy_parms['dtx_change_time']=t
            therapy_parms['dtx_therapy_on']=False
    else: #therapy is not on already
        if (t >= therapy_parms['dtx_mt_t_on'] + therapy_parms['dtx_change_time']): #turn on therapy if current time higher than time window
            therapy_parms['dtx_change_time']=t
            therapy_parms['dtx_therapy_on']=True

def dtx_therapy(t,x,therapy_parms):
    if t >= therapy_parms['dtx_delay']:
        if therapy_parms['dtx_mode']=='SOC':
            dtx_SOC(t,x,therapy_parms)
        elif therapy_parms['dtx_mode']=='AT':
            dtx_AT(t,x,therapy_parms)
        elif therapy_parms['dtx_mode']=='MT':
            dtx_MT(t,x,therapy_parms)
        else:
            return None #do nothing if none of the above
    else:
        return None #do nothing if delay window not crossed

def f_therapy(f_ode,t,x,p,mu,lam,r,K,delta,rho,lim,therapy_parms):
    check_therapy_keys(therapy_parms)
    abi_therapy(t,x,therapy_parms)
    p_therapy=p.copy()
    if therapy_parms['abi_therapy_on']: #check if abiraterone therapy is set to on
        p_therapy[1]=therapy_parms['p_min'] #lower testosterone production rate due to effect of drug
    dtx_therapy(t,x,therapy_parms)
    r_therapy=r.copy()
    if therapy_parms['dtx_therapy_on']: #check if docetaxel therapy is set to on
        r_therapy*=[therapy_parms['T_pos_r_mult'],therapy_parms['T_pro_r_mult'],therapy_parms['T_neg_r_mult']] #lower growth rate due to effect of drug
    f_ode.set_f_params(p_therapy,mu,lam,r_therapy,K,delta,rho,lim)

def enveq(t,x,p,mu,lam,r,K,delta,rho,lim):
    #Equation for oxygen: constant production, uptake by all 3 cells, decay
    do2=p[0]-mu[0,0]*x[0]-mu[0,1]*x[1]-mu[0,2]*x[2]-lam[0]*x[3]
    #Equation for testosterone: production by Tp, uptake by all Tp, T+, decay
    dtest=p[1]*x[1]-mu[1,0]*x[0]-mu[1,1]*x[1]-lam[1]*x[4]
    #Equation for T+
    dTpos=r[0]*x[0]*(1-(x[0:3].sum()/(K+rho[0]*f_res(x[3],lim[0,0])*f_res(x[4],lim[1,0]))))-delta[0]*x[0]
    #Equation for Tp
    dTpro=r[1]*x[1]*(1-(x[0:3].sum()/(K+rho[1]*f_res(x[3],lim[0,1])*f_res(x[4],lim[1,1]))))-delta[1]*x[1]
    #Equation for T-
    dTneg=r[2]*x[2]*(1-(x[0:3].sum()/(K+rho[2]*f_res(x[3],lim[0,2]))))-delta[2]*x[2]

    # Returns the array with dx_i/dt at that time
    dx=np.array([dTpos,dTpro,dTneg,do2,dtest])
    return dx

def solve_eq(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name,therapy=False,therapy_parms=None):
    #just dump the input to some text file for reference
    inp=pd.DataFrame([t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name])
    inp.to_csv("../../raw_output/EnvEq/"+f_name+"_inp.log",index=False)
    #Timeseries arrays
    t0=0
    t=np.array([[t0]])
    y=np.array([y0])
    y_t=y0
    if therapy:
        therapy_parms=therapy_parms.copy()
        therapy_log=np.array([[False,False]])
    #ODE declaration
    f_ode = ode(enveq).set_integrator('lsoda').set_initial_value(y0,t0).set_f_params(p,mu,lam,r,K,delta,rho,lim)
    while f_ode.t < t_max:
        if therapy:
            f_therapy(f_ode,f_ode.t,y_t,p,mu,lam,r,K,delta,rho,lim,therapy_parms)
            therapy_log=np.append(therapy_log,[[therapy_parms['abi_therapy_on'],therapy_parms['dtx_therapy_on']]],axis=0)
        t=np.append(t,[[f_ode.t+dt]],axis=0)
        y_t=f_ode.integrate(f_ode.t+dt)
        if (np.logical_and( y[0:3]>0 , y[0:3]<1).any() or (y_t<0.).any()): # if any values goes negative or cell numbers go less than 1....
            y_t = np.maximum(y_t, np.zeros(np.shape(y_t))) #set negative values to 0
            y_t[0:3] = np.where(y_t[0:3] >= 1, y_t[0:3], np.zeros(np.shape(y_t[0:3]))) #set cell < 1  to 0
            f_ode.set_initial_value(y_t,f_ode.t) #if anomaly detected, reset initial conditions to zero set values at that time t
        y=np.append(y,[y_t],axis=0)
        if not f_ode.successful(): #Check if integration fails
            print('Failure @',f_name,f_ode.t)
    #Save data to file
    df=pd.DataFrame(np.append(t,y,axis=1) ,columns=['t','Tpos','Tpro','Tneg','o2','test'])
    if therapy:
        df['abi_therapy']=therapy_log[:,0]
        df['dtx_therapy']=therapy_log[:,1]
    df.to_csv("../../raw_output/EnvEq/"+f_name+".csv",index=False)

def test_parms(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name): #for debugging purposes
    print(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name)
