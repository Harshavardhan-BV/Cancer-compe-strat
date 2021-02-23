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
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

## changed equation with sum over all cells for density dependence
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df=cf.round_df(df,parm_name_array)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,shareaxis=True)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')
## the above with 0.9Tp y0
post_path='0.9Tp-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df=cf.round_df(df,parm_name_array)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,post_path=post_path,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')

# Changing l_lim_o2 with fixed u_lim_o2
o2_lim_arr=np.empty([0,2])
for llim_Tpro in np.arange(0,1,0.2):
    for llim_Tneg in np.arange(0,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim_Tpro,llim_Tneg]],axis=0)

parm_name='l_lim_o2Tpro-l_lim_o2Tneg'
parm_name_array=['l_lim_o2Tpro','l_lim_o2Tneg']
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

## changed equation with sum over all cells for density dependence
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df=cf.round_df(df,parm_name_array)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,shareaxis=True)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')
## the above with 0.9Tp y0
post_path='0.9Tp-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df=cf.round_df(df,parm_name_array)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,post_path=post_path,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')

# Changing l_lim_o2 & u_lim_o2 by same amount (fixed difference)
parm_name='cs_lim_o2Tpro-cs_lim_o2Tneg'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

## changed equation with sum over all cells for density dependence
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df=cf.round_df(df,parm_name_array)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,shareaxis=True)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')
## the above with 0.9Tp y0
post_path='0.9Tp-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df=cf.round_df(df,parm_name_array)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,post_path=post_path,shareaxis=True)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,post_path=post_path,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')

# Changing u_lim_testTpro with others limits fixed
parm_name='u_lim_testTpro'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)
test_lim_arr=np.arange(0.1,1,0.2)

## changed equation with sum over all cells for density dependence
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format)
## The above with higher initial Tp
post_path='0.9Tp-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,post_path=post_path)
## The above with higher initial testosterone and Tp
post_path='0.9Tp-0.5test-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,post_path=post_path)

# Changing l_lim_testTpro with others limits fixed
parm_name='l_lim_testTpro'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)
test_lim_arr=np.arange(0,1,0.2)

## changed equation with sum over all cells for density dependence
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format)

# Changing l_lim_testTpro & u_lim_testTpro by same amount (fixed difference)
parm_name='cs_lim_testTpro'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

## changed equation with sum over all cells for density dependence
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format,plot_Tpos=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=test_lim_arr,parm_format=parm_format)
