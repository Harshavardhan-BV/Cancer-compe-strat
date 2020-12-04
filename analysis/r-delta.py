import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

## r_Tneg, delta=1.72E-3 /min
parm_name='r_Tneg'
r_Tneg_arr=np.array([2.01E-3,2.06E-3,2.18E-3])
parm_format='{:.2E}'
parm_unit='(/min)'

### OG Eq
pre_path='EnvEq/singlecelltype/Tneg/'
### K=1000, rho=1
post_path='K=1000-rho=1-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
### K=1000, rho=1000
post_path='K=1000-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
#### K=1, rho=2000
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False)

### Alt Eq
pre_path='EnvEq_Alt/singlecelltype/Tneg/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=r_Tneg_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False)


## delta_Tneg, r=2.08E-3 /min
parm_name='delta_Tneg'
delta_Tneg_arr=np.array([1.62E-3,1.74E-3, 1.79E-3])

### OG Eq
pre_path='EnvEq/singlecelltype/Tneg/'
### K=1000, rho=1
post_path='K=1000-rho=1-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
### K=1000, rho=1000
post_path='K=1000-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
#### K=1, rho=2000
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False)

### Alt Eq
pre_path='EnvEq_Alt/singlecelltype/Tneg/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=delta_Tneg_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False)