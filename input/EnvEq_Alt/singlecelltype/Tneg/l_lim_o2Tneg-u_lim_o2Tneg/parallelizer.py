from multiprocessing import Pool
import EnvEq_Alt as ee
import numpy as np
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
lim=np.array([[[l_lim_o2Tpos,u_lim_o2Tpos],[l_lim_o2Tpro,u_lim_o2Tpro],[l_lim_o2Tneg,u_lim_o2Tneg]],[[l_lim_testTpos,u_lim_testTpos],[l_lim_testTpro,u_lim_testTpro],[0,0]]],dtype=np.float64)

#make directories for saving raw_outputs
try:
    os.makedirs("../../raw_output/EnvEq_Alt/"+f_name)
except FileExistsError:
    pass

#iterator over these 
o2_lim_arr=np.empty([0,2])
for llim in np.arange(0,1,0.2):
    for ulim in np.arange(llim+0.1,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim,ulim]],axis=0)

def solve_parm(o2_lim): #calls the solve_eq function with all default inputs other than o2_lim
    f_name_i=f_name+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])
    lim[0,2]=o2_lim
    ee.solve_eq(t_max,dt,y0,p,mu,lam,r,delta,lim,f_name_i)

if __name__ == '__main__':
    pool = Pool(4)
    pool.map(solve_parm,o2_lim_arr) #iterate over the o2_lims
    pool.close()
    pool.join()
