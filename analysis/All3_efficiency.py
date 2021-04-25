import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
import os
plt.rcParams["svg.hashsalt"]=0

# O2 efficiency
## Tp:T+:T- 1:1:1 x 666 (total ~2000)
### High test efficiency
pre_path='EnvEq/All3/'
parm_format='{}'
parm_name='o2-efficiency'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

cases=pd.read_csv('../input/EnvEq/All3/o2-efficiency/All3_o2-eff_cases.csv')
parms_array='Case'+cases.Case
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format)

## Tp:T+:T- 1:8:1 x 200 (total 2000)
post_path='0.8Tp-'
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)


# test efficiency
parm_name='test-efficiency'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)
## Tp:T+:T- 1:1:1 x 666 (total ~2000)
### Null o2 efficiency
cases=pd.read_csv('../input/EnvEq/All3/test-efficiency/All3_test-eff_cases.csv')
parms_array='Case'+cases.Case[0:len(cases)//2]
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format)
os.rename('../figures/'+pre_path+parm_name+'/timeseries.svg','../figures/'+pre_path+parm_name+'/o2-null_timeseries.svg')
os.rename('../analysed_data/'+pre_path+parm_name+'/eq_values.csv','../analysed_data/'+pre_path+parm_name+'/o2-null_eq_values.csv')

## High o2 efficiency
parms_array='Case'+cases.Case[len(cases)//2:]
parms_array=parms_array.reset_index(drop=True)
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format)
os.rename('../figures/'+pre_path+parm_name+'/timeseries.svg','../figures/'+pre_path+parm_name+'/o2-HE_timeseries.svg')
os.rename('../analysed_data/'+pre_path+parm_name+'/eq_values.csv','../analysed_data/'+pre_path+parm_name+'/o2-HE_eq_values.csv')

## Tp:T+:T- 1:8:1 x 200 (total 2000)
### Null o2 efficiency
post_path='0.8Tp-'
parms_array='Case'+cases.Case[0:len(cases)//2]
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
os.rename('../figures/'+pre_path+parm_name+'/'+post_path+'timeseries.svg','../figures/'+pre_path+parm_name+'/'+post_path+'o2-null_timeseries.svg')
os.rename('../analysed_data/'+pre_path+parm_name+'/'+post_path+'eq_values.csv','../analysed_data/'+pre_path+parm_name+'/'+post_path+'o2-null_eq_values.csv')

## High o2 efficiency
parms_array='Case'+cases.Case[len(cases)//2:]
parms_array=parms_array.reset_index(drop=True)
cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
os.rename('../figures/'+pre_path+parm_name+'/'+post_path+'timeseries.svg','../figures/'+pre_path+parm_name+'/'+post_path+'o2-HE_timeseries.svg')
os.rename('../analysed_data/'+pre_path+parm_name+'/'+post_path+'eq_values.csv','../analysed_data/'+pre_path+parm_name+'/'+post_path+'o2-HE_eq_values.csv')

# Combination of o2 and test efficieny
parm_name='efficiency'
parm_name_array=['O2_Eff','Test_Eff','TotCell']
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

ratios=['','0.8Tp-']
totcell=['1000','2000','4000']
o2_cases=['o2_Null','o2_HE','o2_LE']
test_cases=['test_HE','test_LE']
parms_array=[]
for o2case in o2_cases:
    for testcase in test_cases:
        for tc in totcell:
            parms_array.append([o2case,testcase,tc])
            
for ratio in ratios:
    post_path=ratio+'Case-'
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_name_array=parm_name_array,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
