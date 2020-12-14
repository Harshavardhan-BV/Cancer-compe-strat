import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

#Input parms
parm_name='p_o2-mu_o2'
parm_format='{:.2E}'

## OG Eq
pre_path='EnvEq/singlecelltype/Tneg/'
### constrain: mu_o2 = p_o2/2.1E8
p_o2_arr=np.logspace(-4,0,10)
post_path='constrain-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_o2_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_o2_arr,parm_format=parm_format,post_path=post_path)
cf.eqvparm(df,pre_path=pre_path,parm_name=parm_name,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)

### cross: p_o2 and mu_o2 vary and all combinations explored
p_o2_arr=np.linspace(1E-1,5E-1,5)
mu_o2_arr=np.linspace(5E-10,5E-9,5)
post_path='cross-'
parm_arr=np.array(np.meshgrid(p_o2_arr, mu_o2_arr)).T.reshape(-1, 2)
parm_name_array=np.array(['p_o2','mu_o2'])
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parm_arr,parm_format=parm_format,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parm_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df['p_o2']=df['p_o2'].round(1)
cf.heatmap_eqvparm(df,pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,plot_Tpos=False,plot_Tpro=False,plot_test=False,post_path=post_path,shareaxis=True)

