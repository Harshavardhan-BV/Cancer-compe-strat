import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["svg.hashsalt"]=0

def timeseries(pre_path,parm_name,parm_array,parm_format='{:.2E}',post_path='',plot_Tpos=True,plot_Tpro=True,plot_Tneg=True,plot_o2=True,plot_test=True,save=True):
    fig,ax=plt.subplots(len(parm_array),2,sharex=True,figsize=(10,3*len(parm_array)))
    i=0
    for parm in parm_array:
        if isinstance(parm,(list,pd.core.series.Series,np.ndarray)): #If the parameter explored is multidimensional
            string=parm_format.format(parm[0])
            for pp in parm[1:]:
                string+='-'+parm_format.format(pp)
        else:
            string=parm_format.format(parm)
        #print('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
        df=pd.read_csv('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
        ## Plotting Resources
        if plot_o2:
            ax[i,1].plot(df.t/24/60,df.o2,color="tab:cyan",label='o2')
        if plot_test:
            ax[i,1].plot(df.t/24/60,df.test,color="tab:orange",label='test')
        ax[i,1].set_ylabel("Resource (proportion)")
        ax[i,1].legend()
        ## Plotting Cell Number
        if plot_Tpos:
            ax[i,0].plot(df.t/24/60,df.Tpos,color="tab:green",label='T+')
        if plot_Tpro:
            ax[i,0].plot(df.t/24/60,df.Tpro,color="tab:blue",label='Tp')
        if plot_Tneg:    
            ax[i,0].plot(df.t/24/60,df.Tneg,color="tab:red",label='T-')
        ax[i,0].set_ylabel("No of Cells")
        ax[i,0].legend()
        ax[i,0].set_title(parm_name+'='+string)
        i+=1
    ## Add Xaxis label for the last row only
    ax[i-1,0].set_xlabel('Time (days)')
    ax[i-1,1].set_xlabel('Time (days)')
    fig.tight_layout()
    if save:
        fig.savefig('../figures/'+pre_path+parm_name+'/'+post_path+'timeseries.svg')
    return fig,ax

def eq_values(pre_path,parm_name,parm_array,parm_format='{:.2E}',post_path='',save=True,parm_name_array=None):
    lis=[]
    if isinstance(parm_array[0],(list,pd.core.series.Series,np.ndarray)): #If the parameter explored is multidimensional
        for parm in parm_array:
            string=parm_format.format(parm[0])
            for pp in parm[1:]:
                string+='-'+parm_format.format(pp)
            #print('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
            df=pd.read_csv('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
            lis.append(np.append(parm,[df.o2.iloc[-1],df.test.iloc[-1],df.Tpos.iloc[-1],df.Tpro.iloc[-1],df.Tneg.iloc[-1]]))
        df=pd.DataFrame(lis,columns=np.append(parm_name_array,['o2_eq','test_eq','Tpos_eq','Tpro_eq','Tneg_eq']))
    else:
        for parm in parm_array:
            string=parm_format.format(parm)
            #print('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
            df=pd.read_csv('../raw_output/'+pre_path+parm_name+'/'+post_path+string+'.csv')
            lis.append([parm,df.o2.iloc[-1],df.test.iloc[-1],df.Tpos.iloc[-1],df.Tpro.iloc[-1],df.Tneg.iloc[-1]])
        df=pd.DataFrame(lis,columns=[parm_name,'o2_eq','test_eq','Tpos_eq','Tpro_eq','Tneg_eq'])
    if save:
        df.to_csv('../analysed_data/'+pre_path+parm_name+'/'+post_path+'eq_values.csv',index=False)
    return df

def eqvparm(df,pre_path,parm_name,post_path='',parm_unit='',plot_Tpos=True,plot_Tpro=True,plot_Tneg=True,plot_o2=True,plot_test=True,save=True):
    fig,ax1=plt.subplots()
    ax2=ax1.twinx()
    ## Plotting Resources
    if plot_o2:
        ax2.plot(df.loc[:,parm_name],df.o2_eq,color='tab:cyan',marker='.',label='o2')
    if plot_test:
        ax2.plot(df.loc[:,parm_name],df.test_eq,color='tab:orange',marker='.',label='test')
    ax2.set_ylabel("Resource Eq",color='tab:cyan')
    ax2.tick_params(axis='y', labelcolor='tab:cyan')
    ax2.legend()
    ## Plotting Cell Number
    if plot_Tpos:
        ax1.plot(df.loc[:,parm_name],df.Tpos_eq,color='tab:green',marker='.',label='T+')
    if plot_Tpro:
        ax1.plot(df.loc[:,parm_name],df.Tpro_eq,color='tab:blue',marker='.',label='Tp')
    if plot_Tneg:
        ax1.plot(df.loc[:,parm_name],df.Tneg_eq,color='tab:red',marker='.',label='T-')
    ax1.set_ylabel("Cell Eq",color='tab:red')
    ax1.tick_params(axis='y', labelcolor='tab:red')
    ax1.legend()
    ax1.set_xlabel(parm_name+parm_unit)
    fig.tight_layout()    
    if save:
        fig.savefig('../figures/'+pre_path+parm_name+'/'+post_path+'eq-vs-'+parm_name+'.svg')

def heatmap_eqvparm(df,pre_path,parm_name,parm_name_array,post_path='',parm_unit='',plot_Tpos=True,plot_Tpro=True,plot_Tneg=True,plot_o2=True,plot_test=True,save=True,shareaxis=False):
    sp_size=plot_Tpos+plot_Tpro+plot_Tneg+plot_o2+plot_test
    fig,ax=plt.subplots(1,sp_size,figsize=(10*sp_size,6))
    i=0
    # df[parm_name_array[0]]=df[parm_name_array[0]].round(1)
    # df[parm_name_array[1]]=df[parm_name_array[1]].round(1)
    if shareaxis:
        vmin_res=min(min(plot_o2*df.o2_eq),min(plot_test*df.test_eq))
        vmax_res=max(max(plot_o2*df.o2_eq),max(plot_test*df.test_eq))
        vmin_cell=min(min(plot_Tpos*df.Tpos_eq),min(plot_Tpro*df.Tpro_eq),min(plot_Tneg*df.Tneg_eq))
        vmax_cell=max(max(plot_Tpos*df.Tpos_eq),max(plot_Tpro*df.Tpro_eq),max(plot_Tneg*df.Tneg_eq))
    else:
        vmin_res=vmax_res=vmin_cell=vmax_cell=0
    ## Plotting Cell Number
    if plot_Tpos:
        pdf=df.pivot(parm_name_array[0], parm_name_array[1], "Tpos_eq").sort_index(ascending=False)
        sns.heatmap(pdf,annot=True,ax=ax[i],vmin=shareaxis*vmin_cell,vmax=shareaxis*vmax_cell)
        ax[i].set_title("T+ eq")
        i+=1
    if plot_Tpro:
        pdf=df.pivot(parm_name_array[0], parm_name_array[1], "Tpro_eq").sort_index(ascending=False)
        sns.heatmap(pdf,annot=True,ax=ax[i],vmin=shareaxis*vmin_cell,vmax=shareaxis*vmax_cell)
        ax[i].set_title("Tp eq")
        i+=1
    if plot_Tneg:
        pdf=df.pivot(parm_name_array[0], parm_name_array[1], "Tneg_eq").sort_index(ascending=False)
        sns.heatmap(pdf,annot=True,ax=ax[i],vmin=shareaxis*vmin_cell,vmax=shareaxis*vmax_cell)
        ax[i].set_title("T- eq")
        i+=1
    ## Plotting Resources
    if plot_o2:
        pdf=df.pivot(parm_name_array[0], parm_name_array[1], "o2_eq").sort_index(ascending=False)
        sns.heatmap(pdf,annot=True,ax=ax[i],vmin=shareaxis*vmin_res,vmax=shareaxis*vmax_res)
        ax[i].set_title("o2 eq")
        i+=1
    if plot_test:
        pdf=df.pivot(parm_name_array[0], parm_name_array[1], "test_eq").sort_index(ascending=False)
        sns.heatmap(pdf,annot=True,ax=ax[i],vmin=shareaxis*vmin_res,vmax=shareaxis*vmax_res)
        ax[i].set_title("test eq")
        i+=1
    fig.tight_layout()
    if save:
        fig.savefig('../figures/'+pre_path+parm_name+'/'+post_path+'eq-vs-'+parm_name+'.svg')