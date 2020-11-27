#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]=0


# In[2]:


#Input parms
p_o2_arr=np.logspace(-4,0,20) #10^-4 to 1


# ## OG Equation

# In[3]:


lis=[]
fig,ax=plt.subplots(20,2,sharex=True,figsize=(10,60))
i=0
for p_o2 in p_o2_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/p_o2/"+"{:.2E}".format(p_o2)+'.csv')
    lis.append([p_o2,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("p_o2="+"{:.2E}".format(p_o2))
    ax[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[4]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/p_o2/timeseries.svg')


# In[5]:


df1=pd.DataFrame(lis,columns=['po2','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2/eq_values.csv',index=False)


# In[6]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.po2,df1.o2_eq,color=color,marker='.')
ax1.set_xlabel("po2 (prop/min)")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.po2,df1.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/singlecelltype/Tneg/p_o2/eq-vs-po2.svg')


# ## Alt Equation

# In[8]:


lis=[]
fig,ax2=plt.subplots(20,2,sharex=True,figsize=(10,60))
i=0
for p_o2 in p_o2_arr:
    df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/p_o2/"+"{:.2E}".format(p_o2)+'.csv')
    lis.append([p_o2,df.o2.iloc[-1],df.Tneg.iloc[-1]])
    ax2[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax2[i,0].set_ylabel("O2 (proportion)")
    ax2[i,0].set_title("p_o2="+"{:.2E}".format(p_o2))
    ax2[i,1].plot(df.t/24/60,df.Tneg,color="tab:red")
    ax2[i,1].set_ylabel("No of Cells")
    i+=1
ax2[i-1,0].set_xlabel('Time (days)')
ax2[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()


# In[9]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/p_o2/timeseries.svg')


# In[10]:


df2=pd.DataFrame(lis,columns=['po2','o2_eq','Tneg_eq'])
df2.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2/eq_values.csv',index=False)


# In[11]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df2.po2,df2.o2_eq,color=color,marker='.')
ax1.set_xlabel("po2 (prop/min)")
ax1.set_ylabel("o2_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df2.po2,df2.Tneg_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tneg_eq",color=color)
fig.tight_layout()


# In[12]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/p_o2/eq-vs-po2.svg')


# In[ ]:




