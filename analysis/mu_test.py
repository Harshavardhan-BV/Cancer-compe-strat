import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
parm_name='mu_test'
parm_format='{:.2E}'

## OG Eq
pre_path='EnvEq/singlecelltype/Tpro/'
### noup: p_test = 1.08E-9
mu_test_arr=np.linspace(1E-9,1.08E-9,20)
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False)