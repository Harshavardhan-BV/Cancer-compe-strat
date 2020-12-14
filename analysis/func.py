import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

parm_name='y0_Tpro'
parm_format='{:.2E}'
y0_arr=np.logspace(1,3,20)

# sqrt: f_res = sqrt(res) for res>0
pre_path='EnvEq_Fn/sqrt/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)
# exp: f_res = 1 - exp(-res) for res>0
pre_path='EnvEq_Fn/exp/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)
# hilleq: f_res = res/(K + res) for res>0
## K=0.001
pre_path='EnvEq_Fn/hilleq/'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)
## K=1
post_path='K=1'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False,post_path=post_path)