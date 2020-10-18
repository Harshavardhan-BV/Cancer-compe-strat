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
p_o2=np.logspace(0,3,20) #20 values bw 10^0 to 10^3
p=np.empty([0,2])
f_name_arr=np.empty(0)
for i in p_o2: #pretty sure there's a more efficient way but too lazy
    p=np.append(p,[[i,p_test]],axis=0)
    f_name_arr=np.append(f_name_arr,f_name+'-'+"{:.2f}".format(i))

if __name__ == '__main__':
    pool = Pool(processes=8)
    pool.starmap(ee.test_parms,(t_max,dt,y0,p,mu,lam,r,K,delta,rho,lim,f_name_arr)) #im probably doing something wrong here
