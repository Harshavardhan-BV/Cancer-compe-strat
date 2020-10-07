import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.stats import truncnorm

def lotvol(t,x,r,α,K,ϵ,mu,sig):
    #Defining a random Environment variable bounded by 0 and 1
    a, b = (0 - mu) / sig, (1 - mu) / sig
    #Truncated normal distribution sampled at every time step
    E=truncnorm.rvs(a,b,loc=mu,scale=sig)
    # Returns the array with dx_i/dt at that time
    dx1=r[0]*x[0]*(1-x[0]/(K*ϵ[0]*E)-α[1]*x[1]/(K*ϵ[0]*E))-𝛿[0]
    dx2=r[1]*x[1]*(1-x[1]/(K*ϵ[1]*E)-α[0]*x[0]/(K*ϵ[1]*E))-𝛿[1]
    return np.array([dx1,dx2])

#importing variables from input and parsing into numpy arrays
from input import *
y0=np.array([y0_1,y0_2])
r=np.array([r_1,r_2])
α=np.array([α_1,α_2])
ϵ=np.array([ϵ_1,ϵ_2])
𝛿=np.array([𝛿_1,𝛿_2])

#Timeseries arrays
t=np.arange(0,t_max,dt)
#Numerical solution of equation
sol = solve_ivp(lotvol, [0, t_max], y0, args=(r,α,K,ϵ,μ,σ),t_eval=t)
plt.plot(t,sol.y.T)
plt.xlabel("Time (days)")
plt.ylabel("Density")
df=pd.DataFrame({'t':t,'y1':sol.y[0],'y2':sol.y[1]})
plt.savefig("../../figures/Lot-Vol/"+f_name+".svg")
df.to_csv("../../raw_output/Lot-Vol/"+f_name+".csv",index=False)
