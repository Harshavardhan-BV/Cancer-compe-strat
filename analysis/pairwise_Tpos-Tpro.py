import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0
 
pre_path='EnvEq/pairwise/Tpos-Tpro/'

# Changing the uptake rate
parm_format='{:.2E}'
mu_test_arr=np.logspace(-11,-7,20)
parm_name='mu_testTpos'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tneg=False)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tneg=False,post_path=post_path)

# Changing u_lim_o2 with fixed l_lim_o2
parm_format='{:.1f}'
o2_lim_arr=np.empty([0,2])
for ulim_Tpos in np.arange(0.1,1,0.2):
    for ulim_Tpro in np.arange(0.1,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[ulim_Tpos,ulim_Tpro]],axis=0)
parm_name='u_lim_o2Tpos-u_lim_o2Tpro'
parm_name_array=['u_lim_o2Tpos','u_lim_o2Tpro']
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True,post_path=post_path)

# Changing u_lim_test with fixed l_lim_test
parm_name='u_lim_testTpos-u_lim_testTpro'
parm_name_array=['u_lim_testTpos','u_lim_testTpro']
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True,post_path=post_path)

# Changing l_lim_o2 with fixed u_lim_o2
o2_lim_arr=np.empty([0,2])
for llim_Tpos in np.arange(0,1,0.2):
    for llim_Tpro in np.arange(0,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim_Tpos,llim_Tpro]],axis=0)
parm_name='l_lim_o2Tpos-l_lim_o2Tpro'
parm_name_array=['l_lim_o2Tpos','l_lim_o2Tpro']
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True,post_path=post_path)

# Changing l_lim_test with fixed u_lim_test
parm_name='l_lim_testTpos-l_lim_testTpro'
parm_name_array=['l_lim_testTpos','l_lim_testTpro']
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True,post_path=post_path)

# Changing l_lim_o2 & u_lim_o2 by same amount (fixed difference)
parm_name='cs_lim_o2Tpos-cs_lim_o2Tpro'
parm_name_array=['l_lim_o2Tpos','l_lim_o2Tpro']
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True,post_path=post_path)

# Changing l_lim_test & u_lim_test by same amount (fixed difference)
parm_name='cs_lim_testTpos-cs_lim_testTpro'
parm_name_array=['l_lim_testTpos','l_lim_testTpro']
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True)
## changed equation with sum over all cells for density dependence
post_path='cell_sum-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tneg=False,shareaxis=True,post_path=post_path)