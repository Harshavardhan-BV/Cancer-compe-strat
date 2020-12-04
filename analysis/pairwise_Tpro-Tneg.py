import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

# Tp Testosterone independent
pre_path='EnvEq/pairwise/Tneg-Tpro/'
post_path='testindep-'
parm_format='{:.1f}'

## Changing u_lim_o2 with fixed l_lim_o2
o2_lim_arr=np.empty([0,2])
for ulim_Tpro in np.arange(0.1,1,0.2):
    for ulim_Tneg in np.arange(0.1,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[ulim_Tpro,ulim_Tneg]],axis=0)

parm_name='u_lim_o2Tpro-u_lim_o2Tneg'
parm_name_array=['u_lim_o2Tpro','u_lim_o2Tneg']

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_test=False,post_path=post_path,shareaxis=True)

## Changing l_lim_o2 with fixed u_lim_o2
o2_lim_arr=np.empty([0,2])
for llim_Tpro in np.arange(0,1,0.2):
    for llim_Tneg in np.arange(0,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim_Tpro,llim_Tneg]],axis=0)

parm_name='l_lim_o2Tpro-l_lim_o2Tneg'
parm_name_array=['l_lim_o2Tpro','l_lim_o2Tneg']

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_test=False,post_path=post_path,shareaxis=True)

## Changing l_lim_o2 & u_lim_o2 by same amount (fixed difference)
parm_name='cs_lim_o2Tpro-cs_lim_o2Tneg'

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_test=False,post_path=post_path,shareaxis=True)

