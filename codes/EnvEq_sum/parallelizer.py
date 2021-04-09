from multiprocessing import Pool
import EnvEq as ee
import numpy as np
import pandas as pd
import itertools as it
import os

#parsing input into numpy arrays
from input import *
y0=np.array([y0_Tpos,y0_Tpro,y0_Tneg,y0_o2,y0_test])
p=np.array([p_o2,p_test])
mu=np.array([[mu_o2Tpos,mu_o2Tpro,mu_o2Tneg],[mu_testTpos,mu_testTpro,0]])
lam=np.array([lam_o2,lam_test])
t_D=np.array([t_DTpos,t_DTpro,t_DTneg])
r=np.array([r_Tpos,r_Tpro,r_Tneg])
delta=np.array([delta_Tpos,delta_Tpro,delta_Tneg])
rho=np.array([rho_Tpos,rho_Tpro,rho_Tneg])
lim=np.array([[[l_lim_o2Tpos,u_lim_o2Tpos],[l_lim_o2Tpro,u_lim_o2Tpro],[l_lim_o2Tneg,u_lim_o2Tneg]],[[l_lim_testTpos,u_lim_testTpos],[l_lim_testTpro,u_lim_testTpro],[0,0]]],dtype=np.float64)

#make directories for saving raw_outputs
try:
    os.makedirs("../../raw_output/EnvEq/"+f_name)
except:
    pass

#iterator over these
parms_array=[]
cases=pd.read_csv('./therapy_parms.csv')
for i in range(len(cases)):
    parms_array.append(cases.loc[i])

def solve_parm(parms): #calls the solve_eq function with all default inputs other than lims
    f_name_i=f_name+parms['Name']
    ee.solve_eq(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name_i,therapy=True,therapy_parms=parms)

if __name__ == '__main__':
    pool = Pool(20)
    pool.map(solve_parm,parms_array) #iterate over the lims
    pool.close()
    pool.join()
