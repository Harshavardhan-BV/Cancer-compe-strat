import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0
 
pre_path='EnvEq/pairwise/Tneg-Tpro/'
parm_format='{:.1f}'

parm_name='l_lim_o2Tneg-u_lim_o2Tneg-l_lim_o2Tpro-u_lim_o2Tpro-l_lim_testTpro-u_lim_testTpro'
parm_name_array=['l_lim_o2Tneg','u_lim_o2Tneg','l_lim_o2Tpro','u_lim_o2Tpro','l_lim_testTpro','u_lim_testTpro']
lim_arr=np.empty([0,6])
for llim_o2Tneg in np.arange(0,1,0.2):
    for ulim_o2Tneg in np.arange(llim_o2Tneg+0.1,1,0.2):
        for llim_o2Tpro in np.arange(0,1,0.2):
            for ulim_o2Tpro in np.arange(llim_o2Tpro+0.1,1,0.2):
                for llim_testTpro in np.arange(0,0.3,0.2):
                    for ulim_testTpro in np.arange(llim_testTpro+0.1,0.6,0.2):
                        lim_arr=np.append(lim_arr,[[llim_o2Tneg,ulim_o2Tneg,llim_o2Tpro,ulim_o2Tpro,llim_testTpro,ulim_testTpro]],axis=0)

firsttime=False
if firsttime:
    cf.timeseries_split(no_fig=9,sub_arr_len=125,pre_path=pre_path,parm_name=parm_name,parm_array=lim_arr,parm_format=parm_format,plot_Tpos=False)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=lim_arr,parm_format=parm_format,parm_name_array=parm_name_array)

df=pd.read_csv('../analysed_data/'+pre_path+parm_name+'/eq_values.csv')

#to find correlation bw equilibrium values and parameters
corr_df=df.corr()
corr_df.to_csv('../analysed_data/'+pre_path+parm_name+'/corr.csv')

df=cf.round_df(df,parm_name_array)
cf.cell_eq_ratio(df,'Tneg','Tpro')

sns.relplot(data=df,x='l_lim_o2Tpro',y='Tneg_ratio',hue='u_lim_o2Tpro',row='l_lim_o2Tneg',col='u_lim_o2Tneg',style='l_lim_testTpro',size='u_lim_testTpro',kind='line',marker='o')
plt.ylim(0,1.1)
plt.tight_layout()
plt.savefig('../figures/'+pre_path+parm_name+'/eq-vs-l_lim_o2Tneg.svg')
plt.close()

#Find parameters where Tp doesnt go extinct
df_nonTpextinct=df[df['Tpro_eq']>=1]
df_nonTpextinct.to_csv('../analysed_data/'+pre_path+parm_name+'/eq_values-nonTpextinct.csv',index=False)

#When ulim_testTpro=0.1, looking at the oxygen limits 
df_ultTp=df[df['u_lim_testTpro']==0.1]
df_ultTp.to_csv('../analysed_data/'+pre_path+parm_name+'/eq_values-u_lim_testTpro=0.1.csv',index=False)
sns.relplot(data=df_ultTp,x='l_lim_o2Tpro',y='Tneg_ratio',hue='u_lim_o2Tpro',row='l_lim_o2Tneg',col='u_lim_o2Tneg',kind='line',marker='o')
plt.ylim(0,1.1)
plt.tight_layout()
plt.savefig('../figures/'+pre_path+parm_name+'/eq-vs-l_lim_o2Tneg-u_lim_testTpro=0.1.svg')
plt.close()
