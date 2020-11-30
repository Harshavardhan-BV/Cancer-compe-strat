#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]=0

# ## OG Equation with rho=2000

# In[2]:


#Input parms
y0_arr=np.logspace(1,3,20)



# In[3]:


lis=[]
fig,ax=plt.subplots(20,3,sharex=True,figsize=(15,60))
i=0
for y0_Tpro in y0_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tpro/y0_Tpro/"+"{:.2E}".format(y0_Tpro)+'.csv')
    lis.append([y0_Tpro,df.o2.iloc[-1],df.Tpro.iloc[-1],df.test.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("y0="+"{:.2E}".format(y0_Tpro))
    ax[i,1].plot(df.t/24/60,df.Tpro,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    ax[i,2].plot(df.t/24/60,df.test,color="tab:orange")
    ax[i,2].set_ylabel("Testosterone (proportion)")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
ax[i-1,2].set_xlabel('Time (days)')
fig.tight_layout()


# In[4]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/y0_Tpro/timeseries.svg')


# In[5]:


df1=pd.DataFrame(lis,columns=['y0_Tpro','o2_eq','Tpro_eq','test_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tpro/y0_Tpro/eq_values.csv',index=False)


# In[6]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.y0_Tpro,df1.o2_eq,color=color,marker='.',label='o2')
ax1.plot(df1.y0_Tpro,df1.test_eq,color='tab:orange',marker='.',label='test')
ax1.set_xlabel("y0_Tpro")
ax1.set_ylabel("o2_eq/test_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.y0_Tpro,df1.Tpro_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tpro_eq",color=color)
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/y0_Tpro/eq-vs-y0.svg')

# ## OG Equation with rho=2E6

# In[8]:


#Input parms
y0_arr=np.logspace(1,6,20)



# In[9]:


lis=[]
fig,ax=plt.subplots(20,3,sharex=True,figsize=(15,60))
i=0
for y0_Tpro in y0_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tpro/y0_Tpro/rhoTpro=2E6-"+"{:.2E}".format(y0_Tpro)+'.csv')
    lis.append([y0_Tpro,df.o2.iloc[-1],df.Tpro.iloc[-1],df.test.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("y0="+"{:.2E}".format(y0_Tpro))
    ax[i,1].plot(df.t/24/60,df.Tpro,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    ax[i,2].plot(df.t/24/60,df.test,color="tab:orange")
    ax[i,2].set_ylabel("Testosterone (proportion)")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
ax[i-1,2].set_xlabel('Time (days)')
fig.tight_layout()


# In[10]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/y0_Tpro/rhoTpro=2E6-timeseries.svg')


# In[11]:


df1=pd.DataFrame(lis,columns=['y0_Tpro','o2_eq','Tpro_eq','test_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tpro/y0_Tpro/rhoTpro=2E6-eq_values.csv',index=False)


# In[12]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.y0_Tpro,df1.o2_eq,color=color,marker='.',label='o2')
ax1.plot(df1.y0_Tpro,df1.test_eq,color='tab:orange',marker='.',label='test')
ax1.set_xlabel("y0_Tpro")
ax1.set_ylabel("o2_eq/test_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.y0_Tpro,df1.Tpro_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tpro_eq",color=color)
fig.tight_layout()


# In[13]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/y0_Tpro/rhoTpro=2E6-eq-vs-y0.svg')

# ## Alt Equation

# In[14]:


#Input parms
y0_arr=np.logspace(1,3,20)



# In[15]:


lis=[]
fig,ax=plt.subplots(20,3,sharex=True,figsize=(15,60))
i=0
for y0_Tpro in y0_arr:
    df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tpro/y0_Tpro/"+"{:.2E}".format(y0_Tpro)+'.csv')
    lis.append([y0_Tpro,df.o2.iloc[-1],df.Tpro.iloc[-1],df.test.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("y0="+"{:.2E}".format(y0_Tpro))
    ax[i,1].plot(df.t/24/60,df.Tpro,color="tab:red")
    ax[i,1].set_ylabel("No of Cells")
    ax[i,2].plot(df.t/24/60,df.test,color="tab:orange")
    ax[i,2].set_ylabel("Testosterone (proportion)")
    i+=1
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
ax[i-1,2].set_xlabel('Time (days)')
fig.tight_layout()


# In[16]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tpro/y0_Tpro/timeseries.svg')


# In[17]:


df1=pd.DataFrame(lis,columns=['y0_Tpro','o2_eq','Tpro_eq','test_eq'])
df1.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tpro/y0_Tpro/eq_values.csv',index=False)


# In[18]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.y0_Tpro,df1.o2_eq,color=color,marker='.',label='o2')
ax1.plot(df1.y0_Tpro,df1.test_eq,color='tab:orange',marker='.',label='test')
ax1.set_xlabel("y0_Tpro")
ax1.set_ylabel("o2_eq/test_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.y0_Tpro,df1.Tpro_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tpro_eq",color=color)
fig.tight_layout()


# In[19]:


fig.savefig('../figures/EnvEq_Alt/singlecelltype/Tpro/y0_Tpro/eq-vs-y0.svg')
