#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["svg.hashsalt"]=0


# ## p_o2 from 10^0 to 10^3 x r_Tnef from 10^-3 to 10^1
# Later realised that o2 levels dont go upto threshold levels 

# In[2]:


#Input parms
p_o2_arr=np.logspace(0,3,10) #10 values bw 10^0 to 10^3
r_Tneg_arr=np.logspace(-3,1,10) #10 values bw 10^-3 to 10^1
p_o2_arr=p_o2_arr[:-1]


# ### OG Equation

# In[3]:


lis=[]
for p_o2 in p_o2_arr:
    for r_Tneg in r_Tneg_arr:
        df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/"+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)+'.csv')
        lis.append([p_o2,r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])


# In[4]:


df1=pd.DataFrame(lis,columns=['po2','r_Tneg','o2_eq','Tneg_eq'])
df1.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values.csv',index=False)


# ### Alt Equation

# In[5]:


lis=[]
for p_o2 in p_o2_arr:
    for r_Tneg in r_Tneg_arr:
        df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/"+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)+'.csv')
        lis.append([p_o2,r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])


# In[6]:


df2=pd.DataFrame(lis,columns=['po2','r_Tneg','o2_eq','Tneg_eq'])
df2.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values.csv',index=False)


# ## p_o2 from 10^3 to 10^6 x r_Tnef from 10^-3 to 10^1
# cant compare with previous data as o2 inital is different

# In[7]:


#Input parms
p_o2_arr=np.logspace(3,6,10) #10 values bw 10^3 to 10^4
r_Tneg_arr=np.logspace(-3,1,10) #10 values bw 10^-3 to 10^1


# ### OG Equation

# In[8]:


lis=[]
for p_o2 in p_o2_arr:
    for r_Tneg in r_Tneg_arr:
        df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/"+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)+'.csv')
        lis.append([p_o2,r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])


# In[9]:


df3=pd.DataFrame(lis,columns=['po2','r_Tneg','o2_eq','Tneg_eq'])
df3.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-ext.csv',index=False)


# ### Alt Equation

# In[10]:


lis=[]
for p_o2 in p_o2_arr:
    for r_Tneg in r_Tneg_arr:
        df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/"+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)+'.csv')
        lis.append([p_o2,r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])


# In[11]:


df4=pd.DataFrame(lis,columns=['po2','r_Tneg','o2_eq','Tneg_eq'])
df4.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-ext.csv',index=False)


# ## p_o2 @ 10^3 x r_Tnef from 4.62E-4 to 1E-3
# Some linear space exploration for OG equation

# In[12]:


#Input parms
p_o2_arr=np.logspace(3,3,1) #Just 10^3
r_Tneg_arr=np.linspace(4.62E-4,1E-3,10) #10 values bw 4.62E-4 to 1E-3


# In[13]:


lis=[]
for p_o2 in p_o2_arr:
    for r_Tneg in r_Tneg_arr:
        df=pd.read_csv("../raw_output/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/"+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)+'.csv')
        lis.append([p_o2,r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])


# In[14]:


df5=pd.DataFrame(lis,columns=['po2','r_Tneg','o2_eq','Tneg_eq'])
df5.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-lin.csv',index=False)


# ## p_o2 @ 2500 to 4500 x r_Tnef from 0.001 to 0.02
# Some linear space exploration for Alt equation

# In[15]:


p_o2_arr=np.linspace(2500,4500,10) #10 values b/w 2500 to 4500
r_Tneg_arr=np.linspace(0.001,0.02,5) #5 values b/w 0.001 to 0.02


# In[16]:


lis=[]
for p_o2 in p_o2_arr:
    for r_Tneg in r_Tneg_arr:
        df=pd.read_csv("../raw_output/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/"+"{:.2E}".format(p_o2)+'-'+"{:.2E}".format(r_Tneg)+'.csv')
        lis.append([p_o2,r_Tneg,df.o2.iloc[-1],df.Tneg.iloc[-1]])


# In[17]:


df6=pd.DataFrame(lis,columns=['po2','r_Tneg','o2_eq','Tneg_eq'])
df6.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-lin.csv',index=False)


# ## Looking at analysed data

# ### Alt Equation (extended) 
# po2 10^3 to 10^6 considered, <10^3 doesnt satisfy the conditions
# 

# In[18]:


df4=pd.read_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-ext.csv')


# In[19]:


df4=df4[(df4.Tneg_eq>1)&(df4.o2_eq>6750)&(df4.o2_eq<47250)] #taking values only when Tneg is non zero at eq and o2 is inbetween thresholds
df4.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-satifactory.csv',index=False)
df4


# In[20]:


plt.scatter(df4.po2,df4.o2_eq,c=df4.r_Tneg)
plt.xlabel('po2 (nmol/min)')
plt.ylabel('o2_eq (nmol)')
plt.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/o2eq-v-po2.svg')


# In[21]:


plt.scatter(df4.r_Tneg,df4.o2_eq,c=df4.po2)
plt.xlabel('r_Tneg (/min)')
plt.ylabel('o2_eq (nmol)')
plt.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/o2eq-v-rTneg.svg')


# In[22]:


plt.scatter(df4.po2,df4.Tneg_eq,c=df4.r_Tneg)
plt.xlabel('po2 (nmol/min)')
plt.ylabel('Tneg_eq')
plt.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/Tnegeq-v-po2.svg')


# In[23]:


plt.scatter(df4.r_Tneg,df4.Tneg_eq,c=df4.po2)
plt.xlabel('r_Tneg (/min)')
plt.ylabel('Tneg_eq')
plt.savefig('../figures/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/Tnegeq-v-rTneg.svg')


# In[24]:


df4.corr()


# ### OG Equation (extended) 
# po2 10^3 to 10^6 considered, <10^3 doesnt satisfy the conditions

# In[25]:


df3=pd.read_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-ext.csv')


# In[26]:


df3=df3[(df3.Tneg_eq>1)&(df3.o2_eq>6750)&(df3.o2_eq<47250)] #taking values only when Tneg is non zero at eq and o2 is inbetween thresholds
df3.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-satifactory.csv',index=False)
df3


# In[27]:


df3.corr()


# In[28]:


plt.scatter(df3.po2,df3.o2_eq,c=df3.r_Tneg)
plt.xlabel('po2 (nmol/min)')
plt.ylabel('o2_eq (nmol)')
plt.savefig('../figures/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/o2eq-v-po2.svg')


# In[29]:


plt.scatter(df3.r_Tneg,df3.o2_eq,c=df3.po2)
plt.xlabel('r_Tneg (/min)')
plt.ylabel('o2_eq (nmol)')
plt.savefig('../figures/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/o2eq-v-rTneg.svg')


# In[30]:


plt.scatter(df3.po2,df3.Tneg_eq,c=df3.r_Tneg)
plt.xlabel('po2 (nmol/min)')
plt.ylabel('Tneg_eq')
plt.savefig('../figures/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/Tnegeq-v-po2.svg')


# In[31]:


plt.scatter(df3.r_Tneg,df3.Tneg_eq,c=df3.po2)
plt.xlabel('r_Tneg (/min)')
plt.ylabel('Tneg_eq')
plt.savefig('../figures/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/Tnegeq-v-rTneg.svg')


# ### Alt Equation - Linear exploration

# In[32]:


df6=pd.read_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-lin.csv')


# In[33]:


df6=df6[(df6.Tneg_eq>1)&(df6.o2_eq>6750)&(df6.o2_eq<47250)] #taking values only when Tneg is non zero at eq and o2 is inbetween thresholds
df6.to_csv('../analysed_data/EnvEq_Alt/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-lin-satifactory.csv',index=False)
df6


# In[34]:


df6.corr()


# ### OG Equation - Linear exploration

# In[35]:


df5=pd.read_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-lin.csv')


# In[36]:


df5=df5[(df5.Tneg_eq>1)&(df5.o2_eq>6750)&(df5.o2_eq<47250)] #taking values only when Tneg is non zero at eq and o2 is inbetween thresholds
df5.to_csv('../analysed_data/EnvEq/singlecelltype/Tneg/p_o2-r_Tneg/eq_values-lin-satifactory.csv',index=False)
df5


# In[37]:


df5.corr()


# In[ ]:




