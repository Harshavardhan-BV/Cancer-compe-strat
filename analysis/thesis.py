import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0
plt.rcParams["font.size"]=11

# f_i(res)
fig,axes=plt.subplots(figsize=(5,3))
x=np.linspace(0,1,1000)
lim=np.array([0.2,0.8])
def f(x,lim):
    if x<lim[0]:
        return 0
    elif x<lim[1]:
        return (x-lim[0])/(lim[1]-lim[0])
    else:
        return 1
y=[f(i,lim) for i in x]
axes.plot(x,y)
axes.set_xticks(lim)
axes.set_xticklabels(['ll','ul'])
axes.set_ylabel('$f_{i}(res)$')
axes.set_xlabel('res')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/f_res.pdf')
fig.clf()
plt.close(fig)

# Tp - T-
## testosterone limits
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_testlims.pdf')
fig.clf()
plt.close(fig)

## oxygen limits
fig,axes=plt.subplots(1,2,sharex=True,sharey=True,figsize=(10,3))
p_o2_u_lim=['1.10e-01-5.00e-01','6.75e-02-5.00e-01']
cols=['normal production','poor production']
path='../raw_output/EnvEq/pairwise/Tneg-Tpro/p_o2-u_lim_testTpro/Tneg-o2limited_'
for i in range(2):
    po2=p_o2_u_lim[i]
    df=pd.read_csv(path+po2+'.csv')
    axes[i].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
    axes[i].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
    axes[i].set_xlabel('Time (days)')
pad = 5 # in points
for ax, col in zip(axes, cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
axes[0].set_ylabel('No of Cells')
axes[1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_o2lims.pdf')
fig.clf()
plt.close(fig)

## Cases
plt.rcParams["font.size"]=16
### normal o2 production
cases=np.array([[1,4,3],[10,11,12],[6,2,8]])
path='../analysed_data/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/'
cols=['no','moderate','severe']
rows=['low','high','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j],legend=(i==0 and j==2))
        axes[i,j].set_ylim(-0.2,1.1)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[2], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Tp seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final Tp ratio')
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Initial Total Seeding')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_cases_normal.pdf')
fig.clf()
plt.close(fig)

### low o2 production
cases=np.array([[13,14,15],[7,5,9],[16,17,18]])
path='../analysed_data/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/'
cols=['no','moderate','severe']
rows=['low','high','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j],legend=(i==0 and j==2))
        axes[i,j].set_ylim(-0.2,1.1)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[2], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Tp seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final Tp ratio')
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Initial Total Seeding')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_cases_poor.pdf')
fig.clf()
plt.close(fig)

# T+ - Tp
plt.rcParams["font.size"]=11
## When Tp test limited and T+ test limited
fig,axes=plt.subplots(1,2,sharey=True,figsize=(10,3))
path='../raw_output/EnvEq/pairwise/Tpos-Tpro/u_lim_testTpos-u_lim_testTpro/'
u_lims=['0.3-0.5','0.5-0.3']
cols=['Tp more testosterone limited','T+ more testosterone limited']
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
axes[1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_testlims.pdf')
fig.clf()
plt.close(fig)

## When both not o2 limited and T+ more o2 limited
fig,axes=plt.subplots(1,2,sharey=True,figsize=(10,3))
path='../raw_output/EnvEq/pairwise/Tpos-Tpro/l_lim_o2Tpos-l_lim_o2Tpro/'
l_lims=['0.0-0.0','0.6-0.4']
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
axes[1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_o2lims.pdf')
fig.clf()
plt.close(fig)

## Cases
plt.rcParams["font.size"]=16
### test limits
cases=np.array([[7,1,8],[2,9,10],[11,12,13]])
path='../analysed_data/EnvEq/pairwise/Tpos-Tpro/Case-Tp_initratio-Totcell/'
cols=['no','moderate','severe']
rows=['no','moderate','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j],legend=(i==0 and j==2))
        axes[i,j].set_ylim(-0.2,1.1)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[2], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Tp seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final Tp ratio')
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Initial Total Seeding')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_cases_test.pdf')
fig.clf()
plt.close(fig)

### oxygen limits
cases=np.array([[7,14,15],[16,17,18],[19,20,21]])
path='../analysed_data/EnvEq/pairwise/Tpos-Tpro/Case-Tp_initratio-Totcell/'
cols=['low','moderate','severe']
rows=['low','moderate','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j],legend=(i==0 and j==2))
        axes[i,j].set_ylim(-0.2,1.1)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[2], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Tp seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final Tp ratio')
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Initial Total Seeding')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_cases_o2.pdf')
fig.clf()
plt.close(fig)

### combination
plt.rcParams["font.size"]=19
cases=np.array([[7,1,2,9],[14,22,23,24],[16,25,26,27],[17,28,29,30]])
path='../analysed_data/EnvEq/pairwise/Tpos-Tpro/Case-Tp_initratio-Totcell/'
cols=['no,no','no,moderate','moderate,no','moderate,moderate']
rows=['low,low','low,moderate','moderate,low','moderate,moderate']
fig,axes=plt.subplots(4,4,sharex=True,sharey=True,figsize=(20,11))
for i in range(4):
    for j in range(4):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j],legend=(i==0 and j==3))
        axes[i,j].set_ylim(-0.2,1.1)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[3], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Tp seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final Tp ratio')
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Initial Total Seeding')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_cases.pdf')
fig.clf()
plt.close(fig)

# All3
## Efficiency
plt.rcParams["font.size"]=16
### proportions 1:1:1 Tp:T+:T-
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../analysed_data/EnvEq/All3/efficiency/'
df1=pd.read_csv(path+'Case-eq_values.csv')
cf.allcell_eq_ratio(df1,-0.1)
df1['TotCell']=df1['TotCell'].astype(str)
colors=['tab:green','tab:blue','tab:red']
labels=['T+','Tp','T-']
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=df1[(df1['Test_Eff']==testeff) & (df1['O2_Eff']==o2eff)]
        df.plot.bar(x='TotCell',y=['Tpos_ratio','Tpro_ratio','Tneg_ratio'],color=colors,stacked=True,ax=axes[i,j],legend=None)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Total seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
axes[0,-1].legend(labels,bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_1:1:1.pdf')
fig.clf()
plt.close(fig)

### proportions 8:1:1 Tp:T+:T-
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../analysed_data/EnvEq/All3/efficiency/'
df1=pd.read_csv(path+'0.8Tp-Case-eq_values.csv')
cf.allcell_eq_ratio(df1,-0.1)
colors=['tab:green','tab:blue','tab:red']
labels=['T+','Tp','T-']
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=df1[(df1['Test_Eff']==testeff) & (df1['O2_Eff']==o2eff)]
        df.plot.bar(x='TotCell',y=['Tpos_ratio','Tpro_ratio','Tneg_ratio'],color=colors,stacked=True,ax=axes[i,j],legend=None)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Total seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
axes[0,-1].legend(labels,bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_8:1:1.pdf')
fig.clf()
plt.close(fig)

### timeseries, proportions 1:1:1 Tp:T+:T-, totalcell=1000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/efficiency/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+'Case-'+o2eff+'-'+testeff+'-1000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_1:1:1-1000.pdf')
fig.clf()
plt.close(fig)

### timeseries, proportions 1:1:1 Tp:T+:T-, totalcell=2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/efficiency/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+'Case-'+o2eff+'-'+testeff+'-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_1:1:1-2000.pdf')
fig.clf()
plt.close(fig)

### timeseries, proportions 1:1:1 Tp:T+:T-, totalcell=4000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/efficiency/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+'Case-'+o2eff+'-'+testeff+'-4000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_1:1:1-4000.pdf')
fig.clf()
plt.close(fig)

### timeseries, proportions 8:1:1 Tp:T+:T-, totalcell=1000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/efficiency/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+'0.8Tp-Case-'+o2eff+'-'+testeff+'-1000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_8:1:1-1000.pdf')
fig.clf()
plt.close(fig)

### timeseries, proportions 8:1:1 Tp:T+:T-, totalcell=2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/efficiency/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+'0.8Tp-Case-'+o2eff+'-'+testeff+'-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_8:1:1-2000.pdf')
fig.clf()
plt.close(fig)

### timeseries, proportions 8:1:1 Tp:T+:T-, totalcell=4000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/efficiency/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+'0.8Tp-Case-'+o2eff+'-'+testeff+'-4000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
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
axes[0,-1].legend(bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency_8:1:1-4000.pdf')
fig.clf()
plt.close(fig)

## Efficiency-mixed
### proportions 1:1:1 Tp:T+:T-
Tpos_effs=['Null','Null','LE']
Tpro_effs=['Null','LE','Null']
rows=['low,low','low,moderate','moderate,low']
Tneg_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../analysed_data/EnvEq/All3/efficiency-mixed/'
df1=pd.read_csv(path+'Case-eq_values.csv')
cf.allcell_eq_ratio(df1,-0.1)
colors=['tab:green','tab:blue','tab:red']
labels=['T+','Tp','T-']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    Tposo2eff='Tpos_o2_'+Tpos_effs[i]
    Tproo2eff='Tpro_o2_'+Tpro_effs[i]
    for j in range(3):
        Tnego2eff='Tneg_o2_'+Tneg_effs[j]
        df=df1[(df1['Tpos_o2_Eff']==Tposo2eff) & (df1['Tpro_o2_Eff']==Tproo2eff) & (df1['Tneg_o2_Eff']==Tnego2eff)]
        df.plot.bar(x='TotCell',y=['Tpos_ratio','Tpro_ratio','Tneg_ratio'],color=colors,stacked=True,ax=axes[i,j],legend=None)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[-1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Total seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
axes[0,-1].legend(labels,bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency-mixed_1:1:1.pdf')
fig.clf()
plt.close(fig)

### proportions 8:1:1 Tp:T+:T-
Tpos_effs=['Null','Null','LE']
Tpro_effs=['Null','LE','Null']
rows=['low,low','low,moderate','moderate,low']
Tneg_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../analysed_data/EnvEq/All3/efficiency-mixed/'
df1=pd.read_csv(path+'0.8Tp-Case-eq_values.csv')
cf.allcell_eq_ratio(df1,-0.1)
colors=['tab:green','tab:blue','tab:red']
labels=['T+','Tp','T-']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    Tposo2eff='Tpos_o2_'+Tpos_effs[i]
    Tproo2eff='Tpro_o2_'+Tpro_effs[i]
    for j in range(3):
        Tnego2eff='Tneg_o2_'+Tneg_effs[j]
        df=df1[(df1['Tpos_o2_Eff']==Tposo2eff) & (df1['Tpro_o2_Eff']==Tproo2eff) & (df1['Tneg_o2_Eff']==Tnego2eff)]
        df.plot.bar(x='TotCell',y=['Tpos_ratio','Tpro_ratio','Tneg_ratio'],color=colors,stacked=True,ax=axes[i,j],legend=None)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[-1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Total seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
axes[0,-1].legend(labels,bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency-mixed_8:1:1.pdf')
fig.clf()
plt.close(fig)

## Therapy-standardization
plt.rcParams["font.size"]=19
### Only Tp and T+ considered for threshold
#### 2000 window
props=['','0.8Tp-']
rows=['1:1:1','8:1:1']
limits=['2000-1000','4000-2000','6000-4000','8000-6000']
cols=['2000-1000','4000-2000','6000-4000','8000-6000']
path='../raw_output/EnvEq/All3/therapy-abi-threshold/'
fig,axes=plt.subplots(2,4,sharex=True,sharey=True,figsize=(20,8))
for i in range(2):
    prop=props[i]
    for j in range(4):
        limit=limits[j]
        df=pd.read_csv(path+prop+'AT_nn-'+limit+'.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-standardization.pdf')
fig.clf()
plt.close(fig)

#### 500 window
props=['','0.8Tp-']
rows=['1:1:1','8:1:1']
limits=['2000-1500','4000-3500','6000-5500','8000-7500']
cols=['2000-1500','4000-3500','6000-5500','8000-7500']
path='../raw_output/EnvEq/All3/therapy-abi-threshold/'
fig,axes=plt.subplots(2,4,sharex=True,sharey=True,figsize=(20,8))
for i in range(2):
    prop=props[i]
    for j in range(4):
        limit=limits[j]
        df=pd.read_csv(path+prop+'AT_nn-'+limit+'.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-standardization-sw.pdf')
fig.clf()
plt.close(fig)

### All 3 celltypes considered for threshold
#### 2000 window
props=['','0.8Tp-']
rows=['1:1:1','8:1:1']
limits=['2000-1000','4000-2000','6000-4000','8000-6000']
cols=['2000-1000','4000-2000','6000-4000','8000-6000']
path='../raw_output/EnvEq/All3/therapy-abi-threshold/'
fig,axes=plt.subplots(2,4,sharex=True,sharey=True,figsize=(20,8))
for i in range(2):
    prop=props[i]
    for j in range(4):
        limit=limits[j]
        df=pd.read_csv(path+prop+'AT-'+limit+'.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-standardization-total.pdf')
fig.clf()
plt.close(fig)

#### 500 window
props=['','0.8Tp-']
rows=['1:1:1','8:1:1']
limits=['2000-1500','4000-3500','6000-5500','8000-7500']
cols=['2000-1500','4000-3500','6000-5500','8000-7500']
path='../raw_output/EnvEq/All3/therapy-abi-threshold/'
fig,axes=plt.subplots(2,4,sharex=True,sharey=True,figsize=(20,8))
for i in range(2):
    prop=props[i]
    for j in range(4):
        limit=limits[j]
        df=pd.read_csv(path+prop+'AT-'+limit+'.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-standardization-total-sw.pdf')
fig.clf()
plt.close(fig)

## Therapy-SOC
plt.rcParams["font.size"]=16
### proportions 1:1:1 Tp:T+:T- 
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../analysed_data/EnvEq/All3/therapy-abi-SOC/'
colors=['tab:green','tab:blue','tab:red']
labels=['T+','Tp','T-']
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/eq_values.csv')
        cf.allcell_eq_ratio(df,-0.1)
        df.plot.bar(x='Totcell',y=['Tpos_ratio','Tpro_ratio','Tneg_ratio'],color=colors,stacked=True,ax=axes[i,j],legend=None)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Total seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
axes[0,-1].legend(labels,bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-SOC_1:1:1.pdf')
fig.clf()
plt.close(fig)

### proportions 8:1:1 Tp:T+:T- - Total; 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../analysed_data/EnvEq/All3/therapy-abi-SOC/'
colors=['tab:green','tab:blue','tab:red']
labels=['T+','Tp','T-']
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/0.8Tp-eq_values.csv')
        cf.allcell_eq_ratio(df,-0.1)
        df.plot.bar(x='Totcell',y=['Tpos_ratio','Tpro_ratio','Tneg_ratio'],color=colors,stacked=True,ax=axes[i,j],legend=None)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Total seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
axes[0,-1].legend(labels,bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-SOC_8:1:1.pdf')
fig.clf()
plt.close(fig)

## Therapy-abi
### No delay
#### proportions 1:1:1 Tp:T+:T- - total cell 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/AT_nn-0-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_1:1:1-2000.pdf')
fig.clf()
plt.close(fig)

#### proportions 8:1:1 Tp:T+:T- - total cell 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/0.8Tp-AT_nn-0-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_8:1:1-2000.pdf')
fig.clf()
plt.close(fig)

#### proportions 1:1:1 Tp:T+:T- - total cell 1000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/AT_nn-0-1000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_1:1:1-1000.pdf')
fig.clf()
plt.close(fig)

#### proportions 8:1:1 Tp:T+:T- - total cell 1000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/0.8Tp-AT_nn-0-1000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_8:1:1-1000.pdf')
fig.clf()
plt.close(fig)

#### proportions 1:1:1 Tp:T+:T- - total cell 4000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/AT_nn-0-4000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_1:1:1-4000.pdf')
fig.clf()
plt.close(fig)

#### proportions 8:1:1 Tp:T+:T- - total cell 4000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/0.8Tp-AT_nn-0-4000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_8:1:1-4000.pdf')
fig.clf()
plt.close(fig)

### 200day delay
#### proportions 1:1:1 Tp:T+:T- - total cell 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/AT_nn-200-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_200day_1:1:1.pdf')
fig.clf()
plt.close(fig)

#### proportions 8:1:1 Tp:T+:T- - total cell 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-abi-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/0.8Tp-AT_nn-200-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy_200day_8:1:1.pdf')
fig.clf()
plt.close(fig)

## Therapy-combination
#### proportions 1:1:1 Tp:T+:T- - total cell 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/AT_nn-0-AT-0-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        df['dtx_itherapy']=np.where((df['dtx_therapy'])|(df['dtx_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
        axes[i,j].plot(df.t/24/60,df.dtx_itherapy,color="tab:orange",linewidth=5,label='DTX')

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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-combi_1:1:1.pdf')
fig.clf()
plt.close(fig)

#### proportions 8:1:1 Tp:T+:T- - total cell 2000
row_effs=['HE','LE']
rows=['no','moderate']
col_effs=['HE','Null','LE']
cols=['no','low','moderate']
path='../raw_output/EnvEq/All3/therapy-w-delay/'
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=pd.read_csv(path+o2eff+'-'+testeff+'/0.8Tp-AT_nn-0-AT-0-2000.csv')
        axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        axes[i,j].plot(df.t/24/60,df.Tpos+df.Tpro+df.Tneg,color="tab:grey",label='Total')
        df['abi_itherapy']=np.where((df['abi_therapy'])|(df['abi_therapy'].shift(1)),-200,np.nan)
        df['dtx_itherapy']=np.where((df['dtx_therapy'])|(df['dtx_therapy'].shift(1)),-200,np.nan)
        axes[i,j].plot(df.t/24/60,df.abi_itherapy,color="tab:purple",linewidth=5,label='ABI')
        axes[i,j].plot(df.t/24/60,df.dtx_itherapy,color="tab:orange",linewidth=5,label='DTX')

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
handles, labels = ax.get_legend_handles_labels()
axes[0,-1].legend(handles=handles[0:4], bbox_to_anchor=(1,1), loc="upper left",title='Cell Type')
axes[1,-1].legend(handles=handles[4:], bbox_to_anchor=(1,1), loc="upper left",title='Therapy')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_therapy-combi_8:1:1.pdf')
fig.clf()
plt.close(fig)
