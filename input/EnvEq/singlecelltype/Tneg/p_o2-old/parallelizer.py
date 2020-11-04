from multiprocessing import Pool
import EnvEq as ee
import numpy as np

#parsing input into numpy arrays
from input import *
y0=np.array([y0_Tpos,y0_Tpro,y0_Tneg,y0_o2,y0_test])
p=np.array([p_o2,p_test]) #will be overwritten, preserved for legacy
mu=np.array([[mu_o2Tpos,mu_o2Tpro,mu_o2Tneg],[mu_testTpos,mu_testTpro,0]])
lam=np.array([lam_o2,lam_test])
r=np.array([r_Tpos,r_Tpro,r_Tneg])
delta=np.array([delta_Tpos,delta_Tpro,delta_Tneg])
rho=np.array([rho_Tpos,rho_Tpro,rho_Tneg])
lim=np.array([[[l_lim_o2Tpos,u_lim_o2Tpos],[l_lim_o2Tpro,u_lim_o2Tpro],[l_lim_o2Tneg,u_lim_o2Tneg]],[[l_lim_testTpos,u_lim_testTpos],[l_lim_testTpro,u_lim_testTpro],[0,0]]])


#iterator over these 
p_o2_arr=np.logspace(0,5,40) #40 values bw 10^0 to 10^5

def solve_parm(p_o2): #calls the solve_eq function with all default inputs other than p_o2
    f_name_i=f_name+'-'+"{:.2f}".format(p_o2)
    p=np.array([p_o2,p_test])
    ee.solve_eq(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name_i)
    #ee.test_parms(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name_i) #used when debugging

if __name__ == '__main__':
    pool = Pool()
    pool.map(solve_parm,p_o2_arr) #iterate over the p_o2 values in the array
