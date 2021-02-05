import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

pre_path='EnvEq/pairwise/Tneg-Tpro/'
parm_format='{:.2e}'

# p_o2 and p_test over a range
p_arr=np.empty([0,2])
for po2 in np.linspace(0.05,0.12,5):
    for ptest in np.linspace(1E-7,1E-6,5):
        p_arr=np.append(p_arr,[[po2,ptest]],axis=0)

#When T- is severely oxygen limited
parm_name='p_o2-p_test'
parm_name_array=['p_o2','p_test']
post_path='Tneg-o2limited_'

cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_arr,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')
cf.plot_2parm(df=df,pre_path=pre_path,parm_name=parm_name,post_path=post_path,pri_parm=parm_name_array[0],sec_parm=parm_name_array[1],plot_y='Tneg_ratio')

# Looking closely between the phase transition
p_arr=np.linspace(0.0675,0.085,10)
parm_name='p_o2'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=p_arr,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=p_arr,parm_format=parm_format,post_path=post_path)
df=cf.cell_eq_ratio(df,'Tneg','Tpro')