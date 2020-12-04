import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

parm_name='y0_Tpro'
parm_format='{:.2E}'

# OG Eq
pre_path='EnvEq/singlecelltype/Tpro/'
## rho=2000
y0_arr=np.logspace(1,3,20)
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)
## rho=2000
y0_arr=np.logspace(1,6,20)
post_path='rhoTpro=2E6-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False,post_path=post_path)

# Alt Eq
pre_path='EnvEq_Alt/singlecelltype/Tpro/'
y0_arr=np.logspace(1,3,20)
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=y0_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)