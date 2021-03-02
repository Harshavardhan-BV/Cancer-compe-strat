import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import common_fn as cf
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0
cmap1 = LinearSegmentedColormap.from_list("mycmap", ['tab:red','white','tab:blue'])

pre_path='EnvEq/pairwise/Tneg-Tpro/'
parm_format='{:.1f}'
parm_name='Case-Tp_initratio-Totcell'
# parm_name_array=['Tp_initratio','Totcell']
ratio="0.5-2000"
#Normal o2 production
cases=np.array([[6.0,2.0,8.0],[10.0,11.0,12.0],[1.0,4.0,3.0]])

ratios=np.empty(np.shape(cases))
for i in range(np.shape(cases)[0]):
    for j in range(np.shape(cases)[1]):
        df=pd.read_csv('../analysed_data/'+pre_path+parm_name+'/Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df)
        df=df.loc[(df.Tp_initratio==0.5) & (df.Totcell==2000)]
        ratios[i,j]=df.Tpro_ratio

df=pd.DataFrame(ratios,columns=['no','mod','severe'],index=['severe','high','no'])

fig,ax=plt.subplots(1,figsize=(10,6))
sns.heatmap(df,ax=ax,vmin=0,vmax=1,cmap=cmap1,square=True)
ax.set_xlabel('Tp test limitation')
ax.set_ylabel('T- o2 limitation')
ax.set_title('Normal O2 production 1000:1000')
fig.savefig('../figures/'+pre_path+parm_name+'/heatmap_normalo2-'+ratio+'.svg')
fig.clf()
plt.close(fig)

#Low o2 production
cases=np.array([[16.0,17.0,18.0],[7.0,5.0,9.0],[13.0,14.0,15.0]])

ratios=np.empty(np.shape(cases))
for i in range(np.shape(cases)[0]):
    for j in range(np.shape(cases)[1]):
        df=pd.read_csv('../analysed_data/'+pre_path+parm_name+'/Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df)
        df=df.loc[(df.Tp_initratio==0.5) & (df.Totcell==2000)]
        ratios[i,j]=df.Tpro_ratio

df=pd.DataFrame(ratios,columns=['no','mod','severe'],index=['severe','high','no'])

fig,ax=plt.subplots(1,figsize=(10,6))
sns.heatmap(df,ax=ax,vmin=0,vmax=1,cmap=cmap1,square=True)
ax.set_xlabel('Tp test limitation')
ax.set_ylabel('T- o2 limitation')
ax.set_title('Low O2 production 1000:1000')
fig.savefig('../figures/'+pre_path+parm_name+'/heatmap_lowo2-'+ratio+'.svg')
fig.clf()
plt.close(fig)
