import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0

pre_path='EnvEq/All3/'
parm_format='{:.1f}'
parm_name='Case-Tpos-Tpro-Tneg_initratio-Totcell'
parm_name_array=['Tpos_ir','Tpro_ir','Tneg_ir','Totcell']

tot_cell_arr=np.array([1000,2000,4000])
cases=pd.read_csv('../input/EnvEq/All3/Case-Tpos-Tpro-Tneg_initratio-Totcell/All3_cases.csv')
cases=cases.Case

initial_ratios=np.array([0.11,0.33,0.56,0.78])
parms_array=np.empty([0,4])
for i in initial_ratios:
    for j in initial_ratios:
        k=1-(i+j)
        if (k<0):
            break
        else:
            for tc in tot_cell_arr:
                parms_array=np.append(parms_array,[[i,j,k,tc]],axis=0)

for case in cases:
    post_path='Case{:.1f}-'.format(case)
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,parm_name_array=parm_name_array,post_path=post_path)
    df['Tpos_0']=df['Tpos_ir']*df['Totcell']
    df['Tpro_0']=df['Tpro_ir']*df['Totcell']
    df['Tneg_0']=df['Tneg_ir']*df['Totcell']

    #correlation between the columns -> final ratio depends on initial ratios/absolute numbers?
    corr_df=df.corr()
    corr_df.to_csv('../analysed_data/'+pre_path+parm_name+'/'+post_path+'corr.csv')

    cf.eqratio_v_parm(df=df,plot_parm='Tpro_0',pre_path=pre_path,parm_name=parm_name,post_path=post_path)
