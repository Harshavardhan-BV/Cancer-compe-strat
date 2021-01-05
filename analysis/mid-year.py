import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

# Tp - T-
fig,axes=plt.subplots(2,2,sharex=True,sharey=True,figsize=(10,5))
props=['','0.9Tp-']
rows=['0.5','0.9']
u_lims=['0.5','0.1']
cols=['testosterone limited','not testosterone limited']
path='../raw_output/EnvEq/pairwise/Tneg-Tpro/u_lim_testTpro/'
for i in range(2):
    prop=props[i]
    for j in range(2):
        u_lim=u_lims[j]
        df=pd.read_csv(path+prop+u_lim+'.csv')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Time (days)')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('No of Cells')
axes[0,0].legend()
fig.tight_layout()
fig.savefig('../writing/midyear-report/figures/Tpro-Tneg.pdf')

# T+ - Tp
## When both test limited and T+ test limited
fig,axes=plt.subplots(1,2,sharey=True,figsize=(10,3))
path='../raw_output/EnvEq/pairwise/Tpos-Tpro/u_lim_testTpos-u_lim_testTpro/cell_sum-'
u_lims=['0.7-0.9','0.5-0.3']
cols=['both testosterone limited','T+ more testosterone limited']
for i in range(2):
    u_lim=u_lims[i]
    df=pd.read_csv(path+u_lim+'.csv')
    axes[i].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
    axes[i].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
    axes[i].set_xlabel('Time (days)')
axes[0].set_ylabel('No of Cells')
for ax, col in zip(axes, cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
axes[0].legend()
fig.tight_layout()
fig.savefig('../writing/midyear-report/figures/Tpos-Tpro_testlims.pdf')

## When both o2 limited and T+ severly o2 limited
fig,axes=plt.subplots(1,2,sharey=True,figsize=(10,3))
path='../raw_output/EnvEq/pairwise/Tpos-Tpro/l_lim_o2Tpos-l_lim_o2Tpro/cell_sum-'
l_lims=['0.4-0.4','0.6-0.4']
cols=['both not oxygen limited','only T+ severly oxygen limited']
for i in range(2):
    l_lim=l_lims[i]
    df=pd.read_csv(path+l_lim+'.csv')
    axes[i].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
    axes[i].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
    axes[i].set_xlabel('Time (days)')
axes[0].set_ylabel('No of Cells')
for ax, col in zip(axes, cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
axes[0].legend()
fig.tight_layout()
fig.savefig('../writing/midyear-report/figures/Tpos-Tpro_o2lims.pdf')