import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
o2_lim_arr=np.empty([0,2])
for llim in np.arange(0,1,0.2):
    for ulim in np.arange(llim+0.1,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim,ulim]],axis=0)
parm_format='{:.1f}'

# T-
parm_name='l_lim_o2Tneg-u_lim_o2Tneg'
parm_name_array=np.array(['l_lim_o2Tneg','u_lim_o2Tneg'])
## OG Equation
pre_path='EnvEq/singlecelltype/Tneg/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tpro=False,plot_test=False)
### celleq=1E4: rho s.t T- at equilibrium is 10^4
post_path='celleq=1E4-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)

## Alt Equation 
### with p_o2=3.36E-2
pre_path='EnvEq_Alt/singlecelltype/Tneg/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tpro=False,plot_test=False)
### with p_o2=8.86E-2
post_path='po2=8.86E-2-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
df['u_lim_o2Tneg']=df['u_lim_o2Tneg'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)


# Tp 
## OG Equation
parm_name='l_lim_o2Tpro-u_lim_o2Tpro'
parm_name_array=np.array(['l_lim_o2Tpro','u_lim_o2Tpro'])
pre_path='EnvEq/singlecelltype/Tpro/'
### testindep - testosterone independent
post_path='testindep-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['u_lim_o2Tpro']=df['u_lim_o2Tpro'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tneg=False,plot_test=False,post_path=post_path)
### celleq=1E4: rho s.t T- at equilibrium is 10^4
post_path='celleq=1E4-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['u_lim_o2Tpro']=df['u_lim_o2Tpro'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tneg=False,post_path=post_path)

# T+ - testosterone independent
## OG Equation
parm_name='l_lim_o2Tpos-u_lim_o2Tpos'
parm_name_array=np.array(['l_lim_o2Tpos','u_lim_o2Tpos'])
pre_path='EnvEq/singlecelltype/Tpos/'
post_path='testindep-'

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,plot_Tneg=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=o2_lim_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['l_lim_o2Tpos']=df['l_lim_o2Tpos'].round(1)
df['u_lim_o2Tpos']=df['u_lim_o2Tpos'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpro=False,plot_Tneg=False,plot_test=False,post_path=post_path)