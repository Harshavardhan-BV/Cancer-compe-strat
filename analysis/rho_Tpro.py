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



# In[3]:


lis=[]
fig,ax=plt.subplots(20,3,sharex=True,figsize=(15,60))
i=0
for rho_Tpro in rho_arr:
    df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tpro/rho_Tpro/"+"{:.2E}".format(rho_Tpro)+'.csv')
    lis.append([rho_Tpro,df.o2.iloc[-1],df.Tpro.iloc[-1],df.test.iloc[-1]])
    ax[i,0].plot(df.t/24/60,df.o2,color="tab:blue")
    ax[i,0].set_ylabel("O2 (proportion)")
    ax[i,0].set_title("rho="+"{:.2E}".format(rho_Tpro))
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


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/rho_Tpro/timeseries.svg')


# In[5]:


df1=pd.DataFrame(lis,columns=['rho_Tpro','o2_eq','Tpro_eq','test_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tpro/rho_Tpro/eq_values.csv',index=False)


# In[6]:


fig,ax1=plt.subplots()
color="tab:blue"
ax1.plot(df1.rho_Tpro,df1.o2_eq,color=color,marker='.',label='o2')
ax1.plot(df1.rho_Tpro,df1.test_eq,color='tab:orange',marker='.',label='test')
ax1.set_xlabel("rho_Tpro")
ax1.set_ylabel("o2_eq/test_eq",color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2=ax1.twinx()
color="tab:red"
ax2.plot(df1.rho_Tpro,df1.Tpro_eq,color=color,marker='.')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel("Tpro_eq",color=color)
fig.tight_layout()


# In[7]:


fig.savefig('../figures/EnvEq/singlecelltype/Tpro/rho_Tpro/eq-vs-rho.svg')
