import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0

pre_path='EnvEq/All3/'
parm_format='{:.2e}'
parm_name='therapy_abi-Tneg_initratio-Totcell'
parm_name_array=['Tneg_initratio','Totcell']
post_path1='o2-Null_test-HE/'
parm_name1=parm_name+'/'+post_path1
cf.mkdirs(pre_path=pre_path,parm_name=parm_name1)

#iterator over these
ir_arr=np.logspace(-1,-3,5)
tot_cell_arr=np.array([1000,2000,4000])
cases=['No','AT','AT_nn','MT','SOC']

parms_array=np.empty([0,2])
for ir in ir_arr:
    for tc in tot_cell_arr:
        parms_array=np.append(parms_array,[[ir,tc]],axis=0)
        
for case in cases:
    post_path=post_path1+case+'-'
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path,ttp=True,limit=9000)
