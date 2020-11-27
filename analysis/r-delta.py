#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]=0


# ## r_Tneg, delta=1.72E-3 /min

# In[2]:


#Input array
r_Tneg_arr=np.array([2.01E-3,2.06E-3,2.18E-3])


# ### OG Eq

# In[3]:


lis=[]
fig,ax=plt.subplots(3,2,sharex=True,figsize=(10,10))
i=0
for r_Tneg in r_Tneg_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/r_Tneg/"+"{:.2E}".format(r_Tneg)+'.csv')
    lis.append([r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("r_Tneg="+"{:.2E}".format(r_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[4]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/r_Tneg/timeseries.svg')


# In[5]:


df1=pd.DataFrame(lis,columns=['r_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/r_Tneg/eq_values.csv',index=False)


# In[6]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.r_Tneg,df1.o2_eq,color=color,marker='.')
ax1.set_xlabel("r_Tneg (prop/min)")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.r_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/r_Tneg/eq-vs-r_Tneg.svg')


# ### Alt Eq

# In[8]:


lis=[]
fig,ax=plt.subplots(3,2,sharex=True,figsize=(10,10))
i=0
for r_Tneg in r_Tneg_arr:
    df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/r_Tneg/"+"{:.2E}".format(r_Tneg)+'.csv')
    lis.append([r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("r_Tneg="+"{:.2E}".format(r_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[9]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/r_Tneg/timeseries.svg')


# In[10]:


df1=pd.DataFrame(lis,columns=['r_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/r_Tneg/eq_values.csv',index=False)


# In[11]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.r_Tneg,df1.o2_eq,color=color,marker='.')
ax1.set_xlabel("r_Tneg (prop/min)")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.r_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[12]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/r_Tneg/eq-vs-r_Tneg.svg')


# ## delta_Tneg, r=2.08E-3 /min

# In[13]:


delta_Tneg_arr=np.array([1.62E-3,1.74E-3, 1.79E-3])


# ### OG Eq

# In[14]:


lis=[]
fig,ax=plt.subplots(3,2,sharex=True,figsize=(10,10))
i=0
for delta_Tneg in delta_Tneg_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/delta_Tneg/"+"{:.2E}".format(delta_Tneg)+'.csv')
    lis.append([delta_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("delta_Tneg="+"{:.2E}".format(delta_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[15]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/delta_Tneg/timeseries.svg')


# In[16]:


df1=pd.DataFrame(lis,columns=['delta_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/delta_Tneg/eq_values.csv',index=False)


# In[17]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.delta_Tneg,df1.o2_eq,color=color,marker='.')
ax1.set_xlabel("delta_Tneg (prop/min)")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.delta_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[18]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/delta_Tneg/eq-vs-delta_Tneg.svg')


# ### Alt Eq

# In[19]:


lis=[]
fig,ax=plt.subplots(3,2,sharex=True,figsize=(10,10))
i=0
for delta_Tneg in delta_Tneg_arr:
    df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/delta_Tneg/"+"{:.2E}".format(delta_Tneg)+'.csv')
    lis.append([delta_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("delta_Tneg="+"{:.2E}".format(delta_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[20]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/delta_Tneg/timeseries.svg')


# In[21]:


df1=pd.DataFrame(lis,columns=['delta_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/delta_Tneg/eq_values.csv',index=False)


# In[22]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.delta_Tneg,df1.o2_eq,color=color,marker='.')
ax1.set_xlabel("delta_Tneg (prop/min)")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.delta_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[23]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/delta_Tneg/eq-vs-delta_Tneg.svg')

