import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
import seaborn as sns
import os
plt.rcParams["svg.hashsalt"]=0

# O2 efficiency

## Null o2 efficiency, High test efficiency
pre_path='EnvEq/All3/therapy-abi/'
parm_format='{}'
parm_name='o2-Null_test-HE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

cases=pd.read_csv('../input/EnvEq/All3/therapy-abi/therapy_parms.csv')
parms_array=cases.Name.unique()
p_min_arr=np.array([1.4e-7,1e-7,1.2e-7]) #### The max dose response to abiraterone is testosterone = 1 -> 0.2, 0.1, 0.15

scenarios=np.array([
    '', ### Tp:T+:T- 1:1:1 x 666 (total ~2000)
    '0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000)
    'nonT_neg-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) but therapy only works with T+ and Tp numbers
    'nonT_neg-0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) but therapy only works with T+ and Tp numbers
    'y0eq-', ### Tp:T+:T- with initial values same as eq_values from no therapy scenario
    'timescaled-', ### Tp:T+:T- 1:1:1 x 666 (total ~2000) with both r and delta scaled by 10^-2
    'timescaled-0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) with both r and delta scaled by 10^-2
    'nonT_neg-timescaled-', ### Tp:T+:T- 1:1:1 x 666 (total ~2000) with both r and delta scaled by 10^-2 but therapy only works with T+ and Tp numbers
    'nonT_neg-timescaled-0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) with both r and delta scaled by 10^-2 but therapy only works with T+ and Tp numbers
    'timescaled_tauconst-', ### Tp:T+:T- 1:1:1 x 666 (total ~2000) with delta scaled by 10^-2, tau fixed
    'timescaled_tauconst-0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) with delta scaled by 10^-2, tau fixed
    'nonT_neg-timescaled_tauconst-0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) with delta scaled by 10^-2, tau fixed but therapy only works with T+ and Tp numbers
    'cunningham-', ### Tp:T+:T- 1:1:1 x 666 (total ~2000) with doubling times from Cunningham et al for check
    '0.8Tp-cunningham-', ### Tp:T+:T- 8:1:1 x 200 (total 2000) with doubling times from Cunningham et al for chec
    'nonT_neg-cunningham-',### Tp:T+:T- 1:1:1 x 666 (total ~2000) with doubling times from Cunningham et al for check but therapy only works with T+ and Tp numbers
    'nonT_neg-0.8Tp-cunningham-' ### Tp:T+:T- 8:1:1 x 200 (total 2000) with doubling times from Cunningham et al for check but therapy only works with T+ and Tp numbers
])

### 
for scenario in scenarios:
    for p_min in p_min_arr:
        post_path=scenario+'p={:.1e}-'.format(p_min)
        cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
        df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)

## High o2 efficiency, High test efficiency
parm_name='o2-HE_test-HE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)
scenarios=np.array([
    '', ### Tp:T+:T- 1:1:1 x 666 (total ~2000)
    '0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000)
])

for scenario in scenarios:
    for p_min in p_min_arr:
        post_path=scenario+'p={:.1e}-'.format(p_min)
        cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
        df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)

## Low o2 efficiency, High test efficiency
parm_name='o2-LE_test-HE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

scenarios=np.array([
    '', ### Tp:T+:T- 1:1:1 x 666 (total ~2000)
    '0.8Tp-', ### Tp:T+:T- 8:1:1 x 200 (total 2000)
])

for scenario in scenarios:
    for p_min in p_min_arr:
        post_path=scenario+'p={:.1e}-'.format(p_min)
        cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
        df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)

## Null o2 efficiency, Low test efficiency
parm_name='o2-Null_test-LE'
cf.mkdirs(pre_path=pre_path,parm_name=parm_name)

### Tp:T+:T- 8:1:1 x 200 (total 2000)
for p_min in p_min_arr:
    post_path='0.8Tp-p={:.1e}-'.format(p_min)
    cf.timeseries(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path,plot_tot=True)
    df=cf.eq_values(pre_path=pre_path,parm_name=parm_name,parm_array=parms_array,parm_format=parm_format,post_path=post_path)



# looking at the 0-100 days timewindow for Tp:T+:T- 1:1:1 x 666 (total ~2000)
parm_name='o2-Null_test-HE'
post_path='p=1.4e-07-'
fig,ax=plt.subplots(len(parms_array),2,sharex=True,figsize=(10,3*len(parms_array)))
i=0
for parm in parms_array:
    string=parm_format.format(parm)
    df=pd.read_csv('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
    df=df.head(2400)
    ## Plotting Resources
    ax[i,1].plot(df.t/24/60,df.o2,color="tab:cyan",label='o2')
    ax[i,1].plot(df.t/24/60,df.test,color="tab:orange",label='test')
    ax[i,1].set_ylabel("Resource (proportion)")
    ax[i,1].legend()
    ## Plotting Cell Number
    ax[i,0].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
    ax[i,0].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
    ax[i,0].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
    ax[i,0].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
    ax[i,0].set_ylabel("No of Cells")
    ax[i,0].legend()
    ax[i,0].set_title(parm_name+'='+string)
    i+=1
## Add Xaxis label for the last row only
ax[i-1,0].set_xlabel('Time (days)')
ax[i-1,1].set_xlabel('Time (days)')
fig.tight_layout()
fig.savefig('../figures/'+pre_path+parm_name+'/'+post_path+'timeseries-100days.svg')
fig.clf()
plt.close(fig)
