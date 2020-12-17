import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0
 
pre_path='EnvEq/pairwise/Tpos-Tpro/'

# Changing the uptake rate
parm_format='{:.2E}'
mu_test_arr=np.logspace(-11,-7,20)
parm_name='mu_testTpos'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format,plot_Tneg=False)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=mu_test_arr,parm_format=parm_format)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tneg=False)


