#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]=0

# ## OG Equation

# In[2]:


#Input parms
rho_arr=np.logspace(3.5,6,20)


# ### p_o2=8.86E-3
# In[3]:


lis=[]
fig,ax=plt.subplots(20,2,sharex=True,figsize=(10,60))
i=0
for rho_Tneg in rho_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/rho_Tneg/"+"{:.2E}".format(rho_Tneg)+'.csv')
    lis.append([rho_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("rho="+"{:.2E}".format(rho_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[4]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/rho_Tneg/timeseries.svg')


# In[5]:


df1=pd.DataFrame(lis,columns=['rho_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/rho_Tneg/eq_values.csv',index=False)


# In[6]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.rho_Tneg,df1.o2_eq,color=color,marker='.',label='o2')
ax1.set_xlabel("rho_Tneg")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.rho_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/rho_Tneg/eq-vs-rho.svg')


# ### p_o2=1E-1

# In[8]:


lis=[]
fig,ax=plt.subplots(20,2,sharex=True,figsize=(10,60))
i=0
for rho_Tneg in rho_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1E-1-"+"{:.2E}".format(rho_Tneg)+'.csv')
    lis.append([rho_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("rho="+"{:.2E}".format(rho_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[9]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1E-1-timeseries.svg')


# In[10]:


df1=pd.DataFrame(lis,columns=['rho_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1E-1-eq_values.csv',index=False)


# In[11]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.rho_Tneg,df1.o2_eq,color=color,marker='.',label='o2')
ax1.set_xlabel("rho_Tneg")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.rho_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[12]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1E-1-eq-vs-rho.svg')



# ### p_o2=1.5E-1

# In[13]:


lis=[]
fig,ax=plt.subplots(20,2,sharex=True,figsize=(10,60))
i=0
for rho_Tneg in rho_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1.5E-1-"+"{:.2E}".format(rho_Tneg)+'.csv')
    lis.append([rho_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("rho="+"{:.2E}".format(rho_Tneg))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[14]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1.5E-1-timeseries.svg')


# In[15]:


df1=pd.DataFrame(lis,columns=['rho_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1.5E-1-eq_values.csv',index=False)


# In[16]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.rho_Tneg,df1.o2_eq,color=color,marker='.',label='o2')
ax1.set_xlabel("rho_Tneg")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.rho_Tneg,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[17]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/rho_Tneg/p_o2=1.5E-1-eq-vs-rho.svg')
