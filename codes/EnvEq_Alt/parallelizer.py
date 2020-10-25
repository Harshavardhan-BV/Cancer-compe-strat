from multiprocessing import Pool
import EnvEq_Alt as ee
import numpy as np
import itertools as it

#parsing input into numpy arrays
from input import *
y0=np.array([y0_Tpos,y0_Tpro,y0_Tneg,y0_o2,y0_test])
p=np.array([p_o2,p_test]) 
mu=np.array([[mu_o2Tpos,mu_o2Tpro,mu_o2Tneg],[mu_testTpos,mu_testTpro,0]])
lam=np.array([lam_o2,lam_test])
r=np.array([r_Tpos,r_Tpro,r_Tneg])
delta=np.array([delta_Tpos,delta_Tpro,delta_Tneg])
lim=np.array([[[l_lim_o2Tpos,u_lim_o2Tpos],[l_lim_o2Tpro,u_lim_o2Tpro],[l_lim_o2Tneg,u_lim_o2Tneg]],[[l_lim_testTpos,u_lim_testTpos],[l_lim_testTpro,u_lim_testTpro],[0,0]]])


#iterator over these 
p_o2_arr=np.logspace(0,3,10) #10 values bw 10^0 to 10^3
p_test_arr=np.logspace(0,3,10) #10 values bw 10^0 to 10^3
mu_o2Tpro_arr=np.logspace(-1,1,10) #10 values bw 10^-1 to 10^1
mu_testTpro_arr=np.logspace(-1,1,10) #10 values bw 10^-1 to 10^1

def solve_parm(p_o2,p_test,mu_o2Tpro,mu_testTpro): #calls the solve_eq function with all default inputs other than p_o2,mu_o2Tneg
    f_name_i=f_name+'-'+"{:.2f}".format(p_o2)+'-'+"{:.2f}".format(p_test)+'-'+"{:.2f}".format(mu_o2Tpro)+'-'+"{:.2f}".format(mu_testTpro)
    p[0]=p_o2
    p[1]=p_test
    mu[0,1]=mu_o2Tpro
    mu[1,1]=mu_testTpro
    ee.solve_eq(t_max,dt,y0,p,mu,lam,r,delta,lim,f_name_i)
    #ee.test_parms(t_max,dt,y0,p,mu,lam,r,delta,lim,f_name_i) #used when debugging

if __name__ == '__main__':
    pool = Pool()
    pool.starmap(solve_parm,it.product(p_o2_arr,p_test_arr,mu_o2Tpro_arr,mu_testTpro_arr)) #iterate over the p_o2,p_test,mu_o2Tpro,mu_testTpro values in the array
