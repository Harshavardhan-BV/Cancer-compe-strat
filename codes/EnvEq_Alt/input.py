##--Enter all the input variables here--##
#parameters based on ATCC documentation, death rate not accurate

#Time parameters of simulation
t_max = 1000*24*60 #maximum (mins)
dt = 1  #step (mins)
#Initial Values
##cells
y0_Tpos=0
y0_Tpro=0
y0_Tneg=10
##resource
y0_o2=100 #(mmHg)
y0_test=0 #(units)
#Production rates of resources
p_o2=100 #(mmHg/min)
p_test=60 #by Tp cells (units/min/cell)
#Uptake rate of resources by cells
##oxygen
mu_o2Tpos=10 #(mmHg/min/cell)
mu_o2Tpro=10 #(mmHg/min/cell)
mu_o2Tneg=10 #(mmHg/min/cell)
##testosterone
mu_testTpos=2 #(units/min/cell)
mu_testTpro=2 #(units/min/cell)
#Decay rates of resources
lam_o2=0.1 #(1/min)
lam_test=0.1 #(1/min)
#Growth rate
r_Tpos= 3.40E-4 #(/min)
r_Tpro= 2.88E-4 #(/min)
r_Tneg= 4.62E-4 #(/min)
#Death rate
delta_Tpos= 2.5E-7 #(/min)
delta_Tpro= 2.5E-7 #(/min)
delta_Tneg= 1.7E-6 #(/min)
#Carrying capacity
K=1000
#Environmental Sensitivity? (dont think so)
rho_Tpos=1
rho_Tpro=1
rho_Tneg=1
#Resource limits
##Oxygen
###T+
l_lim_o2Tpos=5 #lower-threshold(mmHg)
u_lim_o2Tpos=35 #upper-saturation(mmHg)
###Tp
l_lim_o2Tpro=5 #(mmHg)
u_lim_o2Tpro=35 #(mmHg)
###T-
l_lim_o2Tneg=5 #(mmHg)
u_lim_o2Tneg=35 #(mmHg)
##Testosterone
###T+
l_lim_testTpos=0 #(units)
u_lim_testTpos=10 #(units)
###Tp
l_lim_testTpro=0 #(units)
u_lim_testTpro=10 #(units)
#filename to save output in
f_name='singlecelltype/testing/Tneg_alt'
