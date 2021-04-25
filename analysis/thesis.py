import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
import common_fn as cf
plt.rcParams["svg.hashsalt"]=0

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
axes[0,0].legend()
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
axes[0].legend()
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_o2lims.pdf')
fig.clf()
plt.close(fig)

## Megarun
path='../analysed_data/EnvEq/pairwise/Tneg-Tpro/l_lim_o2Tneg-u_lim_o2Tneg-l_lim_o2Tpro-u_lim_o2Tpro-l_lim_testTpro-u_lim_testTpro/eq_values.csv'
df=pd.read_csv(path)
cf.allcell_eq_ratio(df)
parm_name_array=['l_lim_o2Tneg','u_lim_o2Tneg','l_lim_o2Tpro','u_lim_o2Tpro','l_lim_testTpro','u_lim_testTpro']
cf.round_df(df,parm_name_array)
### o2 lower limit Tp
fig,ax1=plt.subplots()
sns.scatterplot(data=df,x='l_lim_o2Tpro',y='Tpro_ratio',color='tab:blue',label="Tp",ax=ax1,alpha=0.5)
#sns.stripplot(data=df,x='l_lim_o2Tpro',y='Tpro_ratio',color='tab:blue',label="Tp",ax=ax1,jitter=True)
ax1.set_ylim(-0.1,1.1)
ax1.set_ylabel('Tp Final ratio')
ax1.set_xlabel('Tp oxygen lower limit')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_llo2Tp.pdf')
fig.clf()
plt.close(fig)
### test lower limit Tp
fig,ax1=plt.subplots()
sns.scatterplot(data=df,x='l_lim_testTpro',y='Tpro_ratio',color='tab:blue',label="Tp",ax=ax1,alpha=0.5)
#sns.stripplot(data=df,x='l_lim_testTpro',y='Tpro_ratio',color='tab:blue',label="Tp",ax=ax1,jitter=True)
ax1.set_ylim(-0.1,1.1)
ax1.set_ylabel('Tp Final ratio')
ax1.set_xlabel('Tp testosterone lower limit')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_lltestTp.pdf')
fig.clf()
plt.close(fig)
### test upper limit Tp
fig,ax1=plt.subplots()
df['llo2Tneg']=np.where(df['l_lim_o2Tneg']<=0.4,'≤0.4',df['l_lim_o2Tneg'])
sns.scatterplot(data=df,x='u_lim_testTpro',y='Tpro_ratio',color='tab:blue',style='llo2Tneg',label="Tp",ax=ax1,alpha=0.5)
#sns.stripplot(data=df,x='u_lim_testTpro',y='Tpro_ratio',color='tab:blue',style='l_lim_o2Tneg',label="Tp",ax=ax1,jitter=0.05)
ax1.set_ylim(-0.1,1.1)
ax1.set_ylabel('Tp Final ratio')
ax1.set_xlabel('Tp testosterone upper limit')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_ultestTp.pdf')
fig.clf()
plt.close(fig)

## Cases
### normal o2 production
cases=np.array([[1,4,3],[10,11,12],[6,2,8]])
path='../analysed_data/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/'
cols=['no','moderate','severe']
rows=['no','high','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j])
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
axes[0,0].legend()
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_cases_normal.pdf')
fig.clf()
plt.close(fig)

### low o2 production
cases=np.array([[13,14,15],[7,5,9],[16,17,18]])
path='../analysed_data/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/'
cols=['no','moderate','severe']
rows=['no','high','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j])
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
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpro-Tneg_cases_poor.pdf')
fig.clf()
plt.close(fig)

# T+ - Tp
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
axes[0].legend()
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
axes[0].legend()
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_o2lims.pdf')
fig.clf()
plt.close(fig)

## Cases
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
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j])
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
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_cases_test.pdf')
fig.clf()
plt.close(fig)

### oxygen limits
cases=np.array([[7,14,15],[16,17,18],[19,20,21]])
path='../analysed_data/EnvEq/pairwise/Tpos-Tpro/Case-Tp_initratio-Totcell/'
cols=['no','moderate','severe']
rows=['no','moderate','severe']
fig,axes=plt.subplots(3,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(3):
    for j in range(3):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j])
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
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_cases_o2.pdf')
fig.clf()
plt.close(fig)

### combination
cases=np.array([[7,1,2,9],[14,22,23,24],[16,25,26,27],[17,28,29,30]])
path='../analysed_data/EnvEq/pairwise/Tpos-Tpro/Case-Tp_initratio-Totcell/'
cols=['no,no','no,moderate','moderate,no','moderate,moderate']
rows=['no,no','no,moderate','moderate,no','moderate,moderate']
fig,axes=plt.subplots(4,4,sharex=True,sharey=True,figsize=(20,11))
for i in range(4):
    for j in range(4):
        df=pd.read_csv(path+'Case{:.1f}-eq_values.csv'.format(cases[i,j]))
        cf.allcell_eq_ratio(df,-0.1)
        df['Tpro_0']=df['Tp_initratio']*df['Totcell']
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='Totcell',markers=True,ax=axes[i,j])
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
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/Tpos-Tpro_cases.pdf')
fig.clf()
plt.close(fig)

# All3
## Efficiency

row_effs=['HE','LE']
rows=['High Efficiency','Low Efficiency']
col_effs=['LE','Null','HE']
cols=['Low Efficiency','Null Efficiency','High Efficiency']
path='../analysed_data/EnvEq/All3/efficiency/'
#proportions=['Case-','Case-0.8Tp-']
#initial_conditions=['1000','2000','4000']
df1=pd.read_csv(path+'Case-eq_values.csv')
df1['Tp_initratio']=0.3
df2=pd.read_csv(path+'0.8Tp-Case-eq_values.csv')
df2['Tp_initratio']=0.8
df1=df1.append(df2,ignore_index=True)
cf.allcell_eq_ratio(df1,-0.1)
df1['Tpro_0']=df1['Tp_initratio']*df1['TotCell']
custom_lines = [Line2D([0], [0], color='tab:green', lw=1),
                Line2D([0], [0], color='tab:blue', lw=1),
                Line2D([0], [0], color='tab:red', lw=1)]
cell_lines = ['T+','Tp','T-']
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,8))
for i in range(2):
    testeff='test_'+row_effs[i]
    for j in range(3):
        o2eff='o2_'+col_effs[j]
        df=df1[(df1['Test_Eff']==testeff) & (df1['O2_Eff']==o2eff)]
        leg1=axes[i,j].legend(custom_lines, cell_lines,loc='center right',title='CellLine')
        sns.lineplot(data=df,x='Tpro_0',y='Tpro_ratio',color='tab:blue',style='TotCell',markers=True,ax=axes[i,j])
        sns.lineplot(data=df,x='Tpro_0',y='Tpos_ratio',color='tab:green',style='TotCell',markers=True,ax=axes[i,j],legend=False)
        sns.lineplot(data=df,x='Tpro_0',y='Tneg_ratio',color='tab:red',style='TotCell',markers=True,ax=axes[i,j],legend=False)
        axes[i,j].legend(loc='upper right',title='TotCell')
        axes[i,j].set_ylim(-0.2,1.3)
        axes[i,j].add_artist(leg1)
pad = 5 # in points
for ax, ax2, col in zip(axes[0], axes[1], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')
    ax2.set_xlabel('Initial Tp seeding')
for ax, row in zip(axes[:,0], rows):
    ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')
    ax.set_ylabel('Final ratio')
fig.tight_layout()
fig.savefig('../writing/MSThesis/figures/All3_efficiency.pdf')
fig.clf()
plt.close(fig)

#for ic in initial_conditions:
    #for prop in proportions:
        #fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(15,5))
        #for i in range(2):
            #testeff=row_effs[i]
            #for j in range(3):
                #o2eff=col_effs[j]
                #df=pd.read_csv(path+prop+'Case-o2_'+o2eff+'-test_'+testeff+'-'+ic+'.csv')
                #axes[i,j].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
                #axes[i,j].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
                #axes[i,j].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        #pad = 5 # in points
        #for ax, ax2, col in zip(axes[0], axes[1], cols):
            #ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                        #xycoords='axes fraction', textcoords='offset points',
                        #size='large', ha='center', va='baseline')
            #ax2.set_xlabel('Time (days)')
        #for ax, row in zip(axes[:,0], rows):
            #ax.annotate(row, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                        #xycoords=ax.yaxis.label, textcoords='offset points',
                        #size='large', ha='right', va='center')
            #ax.set_ylabel('No of Cells')
        #axes[0,0].legend()
        #fig.tight_layout()
        #fig.savefig('../writing/MSThesis/figures/All3_efficiency_'+prop+ic+'.pdf')
        #fig.clf()
        #plt.close(fig)
