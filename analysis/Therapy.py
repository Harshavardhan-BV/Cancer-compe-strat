import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
import os
plt.rcParams["svg.hashsalt"]=0

# O2 efficiency

## Null o2 efficiency, High test efficiency
pre_path='EnvEq/All3/therapy/'
parm_format='{}'
parm_name='o2-Null_test-HE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

cases=pd.read_csv('../input/EnvEq/All3/therapy/therapy_parms.csv')
parms_array=cases.Name.unique()

scenarios=np.array([
    '', ### Tp:T+:T- 1:1:1 x 666 (total ~2000), threshold at 1*y0 - 0.5*y0
    '0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000), threshold at 1*y0 - 0.5*y0
    'ATThresh=4000-3500_', ### Tp:T+:T- 1:1:1 x 666 (total ~2000), threshold at 4000 - 3500
    'ATThresh=4000-3500_0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000), threshold at 4000 - 3500
    ])

for scenario in scenarios:
    post_path=scenario
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
    
## Low o2 efficiency, High test efficiency
parm_name='o2-LE_test-HE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

for scenario in scenarios:
    post_path=scenario
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
    
## High o2 efficiency, High test efficiency
parm_name='o2-HE_test-HE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

for scenario in scenarios:
    post_path=scenario
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
    
# Test efficiency
    
## Null o2 efficiency, Low test efficiency
parm_name='o2-Null_test-LE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)
scenarios=np.array([
    '0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000), threshold at 1*y0 - 0.5*y0
    'ATThresh=4000-3500_0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000), threshold at 4000 - 3500
    ])

for scenario in scenarios:
    post_path=scenario
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)
