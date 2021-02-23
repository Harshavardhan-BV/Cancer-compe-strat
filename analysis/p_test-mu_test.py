import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
parm_name='p_test-mu_test'
parm_format='{:.2E}'

## OG Eq
pre_path='EnvEq/singlecelltype/Tpro/'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

### celleq=1E4-constrain: mu_test = p_test-4.4E-7 (4E-7 wasn't enough)
p_test_arr=np.logspace(-6.35,0,10)
post_path='constrain-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_test_arr,parm_format=parm_format,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_test_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tneg=False,post_path=post_path)
