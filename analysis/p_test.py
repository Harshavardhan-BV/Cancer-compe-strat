import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
parm_name='p_test'
parm_format='{:.2E}'

## OG Eq
pre_path='EnvEq/singlecelltype/Tpro/'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

### celleq=1E4 & noup: mu_test = 0
p_test_arr=np.linspace(1E-7,1E-6,19)
post_path='noup-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_test_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_test_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
