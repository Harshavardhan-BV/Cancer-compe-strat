import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
rho_arr=np.logspace(3.5,6,20)
parm_format='{:.2E}'

## T_pro - rho_Tpro
parm_name='rho_Tpro'
pre_path='EnvEq/singlecelltype/Tpro/'

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)

## T_neg - rho_Tneg
parm_name='rho_Tneg'
pre_path='EnvEq/singlecelltype/Tneg/'

### Default Values
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False)

### p_o2=1E-1
post_path='p_o2=1E-1-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format,post_path=post_path,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,post_path=post_path,plot_Tpos=False,plot_Tpro=False,plot_test=False)

### p_o2=1.5E-1
post_path='p_o2=1.5E-1-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format,post_path=post_path,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=rho_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,post_path=post_path,plot_Tpos=False,plot_Tpro=False,plot_test=False)
