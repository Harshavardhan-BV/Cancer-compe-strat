#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0


# In[2]:


o2_lim_arr=np.empty([0,2])
for llim_Tpro in np.arange(0,1,0.2):
    for llim_Tneg in np.arange(0,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim_Tpro,llim_Tneg]],axis=0)
cs_diff=0.2


# ## Pairwise Tp & T- (Tp testosterone independent)

# In[3]:


lis=[]
fig,ax=plt.subplots(25,2,sharex=True,figsize=(10,75))
i=0
for o2_lim in o2_lim_arr:
    df=pd.read_csv("../raw_output/EnvEq/pairwise/Tneg-Tpro/cs_lim_o2Tpro-cs_lim_o2Tneg/testindep-"+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])+"-cs_diff="+"{:.1f}".format(cs_diff)+'.csv')
    lis.append([o2_lim[0],o2_lim[1],df.o2.iloc[-1],df.Tpro.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("l_lim_Tpro="+"{:.1f}".format(o2_lim[0])+",l_lim_Tneg="+"{:.1f}".format(o2_lim[1]))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-',linewidth=3)
    ax[i,1].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
    ax[i,1].legend()
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[4]:


fig.savefig('../figures/EnvEq/pairwise/Tneg-Tpro/cs_lim_o2Tpro-cs_lim_o2Tneg/testindep-timeseries'+"-cs_diff="+"{:.1f}".format(cs_diff)+'.svg')


# In[5]:


df=pd.DataFrame(lis,columns=['l_lim_o2Tpro','l_lim_o2Tneg','o2_eq','Tpro_eq','Tneg_eq'])
df.to_csv('../analysed_data/EnvEq/pairwise/Tneg-Tpro/cs_lim_o2Tpro-cs_lim_o2Tneg/testindep-eq_values'+"-cs_diff="+"{:.1f}".format(cs_diff)+'.csv',index=False)


# In[6]:


fig,ax1=plt.subplots(1,3,figsize=(30,6))
df['l_lim_o2Tpro']=df['l_lim_o2Tpro'].round(1)
df['l_lim_o2Tneg']=df['l_lim_o2Tneg'].round(1)
o2df=df.pivot("l_lim_o2Tpro", "l_lim_o2Tneg", "o2_eq").sort_index(ascending=False)
Tprodf=df.pivot("l_lim_o2Tpro", "l_lim_o2Tneg", "Tpro_eq").sort_index(ascending=False)
Tnegdf=df.pivot("l_lim_o2Tpro", "l_lim_o2Tneg", "Tneg_eq").sort_index(ascending=False)
sns.heatmap(o2df,annot=True,ax=ax1[0])
ax1[0].set_title("o2 eq")
sns.heatmap(Tprodf,annot=True,ax=ax1[1],vmin=min(min(df.Tpro_eq),min(df.Tneg_eq)),vmax=max(max(df.Tpro_eq),max(df.Tneg_eq)),cbar=False)
ax1[1].set_title("Tpro eq")
sns.heatmap(Tnegdf,annot=True,ax=ax1[2],vmin=min(min(df.Tpro_eq),min(df.Tneg_eq)),vmax=max(max(df.Tpro_eq),max(df.Tneg_eq)))
ax1[2].set_title("Tneg eq")
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/pairwise/Tneg-Tpro/cs_lim_o2Tpro-cs_lim_o2Tneg/testindep-eq-vs-lims'+"-cs_diff="+"{:.1f}".format(cs_diff)+'.svg')

