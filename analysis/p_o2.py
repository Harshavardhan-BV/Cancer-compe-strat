import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
p_o2_arr=np.logspace(-4,0,20) #10^-4 to 1
parm_name='p_o2'
parm_format='{:.2E}'
parm_unit='(prop/min)'

## OG Eq
pre_path='EnvEq/singlecelltype/Tneg/'

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_o2_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_o2_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_unit=parm_unit,plot_Tpos=False,plot_Tpro=False,plot_test=False)


## Alt Eq
pre_path='EnvEq_Alt/singlecelltype/Tneg/'

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_o2_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_o2_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_unit=parm_unit,plot_Tpos=False,plot_Tpro=False,plot_test=False)