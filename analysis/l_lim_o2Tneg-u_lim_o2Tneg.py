#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0


# In[2]:


#Input parms
o2_lim_arr=np.empty([0,2])
for llim in np.arange(0,1,0.2):
    for ulim in np.arange(llim+0.1,1,0.2):
        o2_lim_arr=np.append(o2_lim_arr,[[llim,ulim]],axis=0)


# # T-

# ## OG Equation

# In[3]:


lis=[]
fig,ax=plt.subplots(15,2,sharex=True,figsize=(10,50))
i=0
for o2_lim in o2_lim_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/"+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])+'.csv')
    lis.append([o2_lim[0],o2_lim[1],df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("l_lim="+"{:.1f}".format(o2_lim[0])+",u_lim="+"{:.1f}".format(o2_lim[1]))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[4]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/timeseries.svg')


# In[5]:


df1=pd.DataFrame(lis,columns=['l_lim_o2Tneg','u_lim_o2Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/eq_values.csv',index=False)


# In[6]:


fig,ax1=plt.subplots(1,2,figsize=(20,6))
df1['l_lim_o2Tneg']=df1['l_lim_o2Tneg'].round(1)
df1['u_lim_o2Tneg']=df1['u_lim_o2Tneg'].round(1)
o2df=df1.pivot("l_lim_o2Tneg", "u_lim_o2Tneg", "o2_eq")
Tnegdf=df1.pivot("l_lim_o2Tneg", "u_lim_o2Tneg", "Tneg_eq")
sns.heatmap(o2df,annot=True,ax=ax1[0])
sns.heatmap(Tnegdf,annot=True,ax=ax1[1])
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/eq-vs-lims.svg')


# ## Alt Equation

# ### p_o2 = 3.36E-2 (prop/min)

# In[8]:


lis=[]
fig,ax=plt.subplots(15,2,sharex=True,figsize=(10,50))
i=0
for o2_lim in o2_lim_arr:
    df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/"+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])+'.csv')
    lis.append([o2_lim[0],o2_lim[1],df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("l_lim="+"{:.1f}".format(o2_lim[0])+",u_lim="+"{:.1f}".format(o2_lim[1]))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[9]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=3.36E-2-timeseries.svg')


# In[10]:


df2=pd.DataFrame(lis,columns=['l_lim_o2Tneg','u_lim_o2Tneg','o2_eq','Tneg_eq'])
df2.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=3.36E-2-eq_values.csv',index=False)


# In[11]:


fig,ax1=plt.subplots(1,2,figsize=(20,6))
df2['l_lim_o2Tneg']=df2['l_lim_o2Tneg'].round(1)
df2['u_lim_o2Tneg']=df2['u_lim_o2Tneg'].round(1)
o2df=df2.pivot("l_lim_o2Tneg", "u_lim_o2Tneg", "o2_eq")
Tnegdf=df2.pivot("l_lim_o2Tneg", "u_lim_o2Tneg", "Tneg_eq")
sns.heatmap(o2df,annot=True,ax=ax1[0])
sns.heatmap(Tnegdf,annot=True,ax=ax1[1])
fig.tight_layout()


# In[12]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=3.36E-2-eq-vs-lims.svg')


# ### with p_o2=8.86E-2 (prop/min)

# In[13]:


lis=[]
fig,ax=plt.subplots(15,2,sharex=True,figsize=(10,50))
i=0
for o2_lim in o2_lim_arr:
    df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=8.86E-2-"+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])+'.csv')
    lis.append([o2_lim[0],o2_lim[1],df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("l_lim="+"{:.1f}".format(o2_lim[0])+",u_lim="+"{:.1f}".format(o2_lim[1]))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[14]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=8.86E-2-timeseries.svg')


# In[15]:


df3=pd.DataFrame(lis,columns=['l_lim_o2Tneg','u_lim_o2Tneg','o2_eq','Tneg_eq'])
df3.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=8.86E-2-eq_values.csv',index=False)


# In[16]:


fig,ax1=plt.subplots(1,2,figsize=(20,6))
df3['l_lim_o2Tneg']=df3['l_lim_o2Tneg'].round(1)
df3['u_lim_o2Tneg']=df3['u_lim_o2Tneg'].round(1)
o2df=df3.pivot("l_lim_o2Tneg", "u_lim_o2Tneg", "o2_eq")
Tnegdf=df3.pivot("l_lim_o2Tneg", "u_lim_o2Tneg", "Tneg_eq")
sns.heatmap(o2df,annot=True,ax=ax1[0])
sns.heatmap(Tnegdf,annot=True,ax=ax1[1])
fig.tight_layout()


# In[17]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/l_lim_o2Tneg-u_lim_o2Tneg/po2=8.86E-2-eq-vs-lims.svg')


# # Tp
# 

# In[18]:


lis=[]
fig,ax=plt.subplots(15,3,sharex=True,figsize=(15,50))
i=0
for o2_lim in o2_lim_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tpro/l_lim_o2Tpro-u_lim_o2Tpro/testindep-"+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])+'.csv')
    lis.append([o2_lim[0],o2_lim[1],df.o2.iloc[-1],df.Tpro.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("l_lim="+"{:.1f}".format(o2_lim[0])+",u_lim="+"{:.1f}".format(o2_lim[1]))
    ax[i,1].plot(df.t/24/60,df.Tpro,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    ax[i,2].plot(df.t/24/60,df.test,color="tab:green")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[19]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/l_lim_o2Tpro-u_lim_o2Tpro/testindep-timeseries.svg')


# In[20]:


df3=pd.DataFrame(lis,columns=['l_lim_o2Tpro','u_lim_o2Tpro','o2_eq','Tpro_eq'])
df3.to_csv('../analysed_data/EnvEq/singlecelltype/Tpro/l_lim_o2Tpro-u_lim_o2Tpro/testindep-eq_values.csv',index=False)


# In[21]:


fig,ax1=plt.subplots(1,2,figsize=(20,6))
df3['l_lim_o2Tpro']=df3['l_lim_o2Tpro'].round(1)
df3['u_lim_o2Tpro']=df3['u_lim_o2Tpro'].round(1)
o2df=df3.pivot("l_lim_o2Tpro", "u_lim_o2Tpro", "o2_eq")
Tprodf=df3.pivot("l_lim_o2Tpro", "u_lim_o2Tpro", "Tpro_eq")
sns.heatmap(o2df,annot=True,ax=ax1[0])
sns.heatmap(Tprodf,annot=True,ax=ax1[1])
fig.tight_layout()


# In[22]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/l_lim_o2Tpro-u_lim_o2Tpro/testindep-eq-vs-lims.svg')


# # T+

# In[23]:


lis=[]
fig,ax=plt.subplots(15,3,sharex=True,figsize=(15,50))
i=0
for o2_lim in o2_lim_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tpos/l_lim_o2Tpos-u_lim_o2Tpos/testindep-"+"{:.1f}".format(o2_lim[0])+"-"+"{:.1f}".format(o2_lim[1])+'.csv')
    lis.append([o2_lim[0],o2_lim[1],df.o2.iloc[-1],df.Tpos.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("l_lim="+"{:.1f}".format(o2_lim[0])+",u_lim="+"{:.1f}".format(o2_lim[1]))
    ax[i,1].plot(df.t/24/60,df.Tpos,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    ax[i,2].plot(df.t/24/60,df.test,color="tab:green")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[24]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpos/l_lim_o2Tpos-u_lim_o2Tpos/testindep-timeseries.svg')


# In[25]:


df3=pd.DataFrame(lis,columns=['l_lim_o2Tpos','u_lim_o2Tpos','o2_eq','Tpos_eq'])
df3.to_csv('../analysed_data/EnvEq/singlecelltype/Tpos/l_lim_o2Tpos-u_lim_o2Tpos/testindep-eq_values.csv',index=False)


# In[26]:


fig,ax1=plt.subplots(1,2,figsize=(20,6))
df3['l_lim_o2Tpos']=df3['l_lim_o2Tpos'].round(1)
df3['u_lim_o2Tpos']=df3['u_lim_o2Tpos'].round(1)
o2df=df3.pivot("l_lim_o2Tpos", "u_lim_o2Tpos", "o2_eq")
Tposdf=df3.pivot("l_lim_o2Tpos", "u_lim_o2Tpos", "Tpos_eq")
sns.heatmap(o2df,annot=True,ax=ax1[0])
sns.heatmap(Tposdf,annot=True,ax=ax1[1])
fig.tight_layout()


# In[27]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpos/l_lim_o2Tpos-u_lim_o2Tpos/testindep-eq-vs-lims.svg')


# In[ ]:




