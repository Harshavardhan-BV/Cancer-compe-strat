import pandas as pd
import numpy as np

x0=2000
at_x_on_arr=np.arange(1.6,2,0.1)
p_min_arr=np.array([1.4e-7])

arr=[]

for p_min in p_min_arr:
  arr.append(['SOC','SOC',False,p_min,0,0])
  for at_x0_on in at_x_on_arr:
    for at_x0_off in np.arange(0.5,round(at_x0_on,1),0.1):
      name='AT-{:.2f}-{:.2f}'.format(at_x0_on,at_x0_off)
      at_x_off=at_x0_off*x0
      at_x_on=at_x0_on*x0
      arr.append([name,'AT',False,p_min,at_x_off,at_x_on])

df=pd.DataFrame(arr,columns=['Name','mode','therapy_on','p_min','at_x_off','at_x_on'])
print(df)
df.to_csv('therapy_parms_zoomed.csv',index=False)
