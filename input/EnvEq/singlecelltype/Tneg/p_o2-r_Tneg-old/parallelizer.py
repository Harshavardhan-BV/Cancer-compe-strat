from multiprocessing import Pool
import EnvEq as ee
import numpy as np
import itertools as it
import os

#parsing input into numpy arrays
from input import *
y0=np.array([y0_Tpos,y0_Tpro,y0_Tneg,y0_o2,y0_test])
p=np.array([p_o2,p_test])
mu=np.array([[mu_o2Tpos,mu_o2Tpro,mu_o2Tneg],[mu_testTpos,mu_testTpro,0]])
lam=np.array([lam_o2,lam_test])
t_D=np.array([t_DTpos,t_DTpro,T_DTneg])
r=np.array([r_Tpos,r_Tpro,r_Tneg])
delta=r-np.log(2)/t_D
rho=np.array([rho_Tpos,rho_Tpro,rho_Tneg])
lim=np.array([[[l_lim_o2Tpos,u_lim_o2Tpos],[l_lim_o2Tpro,u_lim_o2Tpro],[l_lim_o2Tneg,u_lim_o2Tneg]],[[l_lim_testTpos,u_lim_testTpos],[l_lim_testTpro,u_lim_testTpro],[0,0]]])

#make directories for saving raw_outputs
try:
    os.makedirs("../../raw_output/EnvEq/"+f_name)
except:
    pass

#iterator over these 
p_o2_arr=np.logspace(0,3,10) #10 values bw 10^0 to 10^3
r_Tneg_arr=np.logspace(-3,1,10) #10 values bw 10^-3 to 10^1

def solve_parm(p_o2,r_Tneg): #calls the solve_eq function with all default inputs other than p_o2,r_Tneg
    f_name_i=f_name+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)
    p[0]=p_o2
    r[2]=r_Tneg
    delta=r-np.log(2)/t_D
    ee.solve_eq(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name_i)

if __name__ == '__main__':
    pool = Pool(10)
    pool.starmap(solve_parm,it.product(p_o2_arr,r_Tneg_arr)) #iterate over the p_o2,r_Tneg
    pool.close()
    pool.join()
