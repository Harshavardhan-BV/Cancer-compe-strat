import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0

pre_path='EnvEq/pairwise/Tneg-Tpro/'
parm_format='{:.1f}'
parm_name='Case-Tp_initratio-Totcell'
parm_name_array=['Tp_initratio','Totcell']
plot_parm='Tpro_0'
style_parm='Totcell'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

#iterator over these
initial_ratio_arr=np.arange(0.1,1,0.2)
tot_cell_arr=np.array([1000,2000,4000])
cases=np.arange(1,10)

parms_array=np.empty([0,2])
for ir in initial_ratio_arr:
    for tc in tot_cell_arr:
        parms_array=np.append(parms_array,[[ir,tc]],axis=0)

for case in cases:
    post_path='Case{:.1f}-'.format(case)
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
    df['Tpro_0']=df['Tp_initratio']*df['Totcell']
    cf.eqratio_v_parm(df=df,plot_parm=plot_parm,pre_path=pre_path,parm_name=parm_name,post_path=post_path,plot_Tpos=False,plot_Tneg=False,style_parm=style_parm)

#v1.1
cases=np.array([1.1,1.2,2.1,2.2,3.1,3.2,4.1,4.2,6.1,6.2])
parms_array=np.empty([0,2])
for ir in initial_ratio_arr:
    for tc in tot_cell_arr:
        parms_array=np.append(parms_array,[[ir,tc]],axis=0)

for case in cases:
    post_path='Case{:.1f}-'.format(case)
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,plot_Tpos=False,post_path=post_path)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
