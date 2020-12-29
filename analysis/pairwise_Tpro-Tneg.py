import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0
 
pre_path='EnvEq/pairwise/Tneg-Tpro/'
parm_format='{:.1f}'

# Changing u_lim_o2 with fixed l_lim_o2
o2_lim_arr=np.empty([0,2])
for ulim_Tpro in np.arange(0.1,1,0.2):
    for ulim_Tneg in np.arange(0.1,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[ulim_Tpro,ulim_Tneg]],axis=0)

parm_name='u_lim_o2Tpro-u_lim_o2Tneg'
parm_name_array=['u_lim_o2Tpro','u_lim_o2Tneg']
## testindep - Testosterone independent
post_path='testindep-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['u_lim_o2Tpro']=df['u_lim_o2Tpro'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_test=False,post_path=post_path,shareaxis=True)
## rho s.t T- at equilibrium is 10^4
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df['u_lim_o2Tpro']=df['u_lim_o2Tpro'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,shareaxis=True)
## the above but with odeint, dt=60 for solving as well
post_path='odeint-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['u_lim_o2Tpro']=df['u_lim_o2Tpro'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['u_lim_o2Tpro']=df['u_lim_o2Tpro'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)

# Changing l_lim_o2 with fixed u_lim_o2
o2_lim_arr=np.empty([0,2])
for llim_Tpro in np.arange(0,1,0.2):
    for llim_Tneg in np.arange(0,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim_Tpro,llim_Tneg]],axis=0)

parm_name='l_lim_o2Tpro-l_lim_o2Tneg'
parm_name_array=['l_lim_o2Tpro','l_lim_o2Tneg']
## testindep - Testosterone independent
post_path='testindep-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_test=False,post_path=post_path,shareaxis=True)
## rho s.t T- at equilibrium is 10^4
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)

# Changing l_lim_o2 & u_lim_o2 by same amount (fixed difference)
parm_name='cs_lim_o2Tpro-cs_lim_o2Tneg'
## testindep - Testosterone independent
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_test=False,post_path=post_path,shareaxis=True)
## rho s.t T- at equilibrium is 10^4
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)

