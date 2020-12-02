##--Enter all the input variables here--##
#Refer doc/EnvEq_parms for further info

#Time parameters of simulation
t_max = 1000*24*60 #maximum (mins)
dt = 60  #step (mins)
#Initial Values
##cells
y0_Tpos=0
y0_Tpro=0
y0_Tneg=10
##resource
y0_o2=0.5 #(prop)
y0_test=0 #(prop)
#Production rates of resources
p_o2=1E-1 #(prop/min)
p_test=2.52E-7 #by Tp cells (prop/min/cell)
#Uptake rate of resources by cells
##oxygen
mu_o2Tpos=4.86E-5 #(prop/min/cell)
mu_o2Tpro=4.86E-5 #(prop/min/cell)
mu_o2Tneg=3.10E-5 #(prop/min/cell)
##testosterone
mu_testTpos=0 #(prop/min/cell)
mu_testTpro=0 #(prop/min/cell)
#Decay rates of resources
lam_o2=0.1 #(1/min)
lam_test=0.004 #(1/min)
#Doubling time
t_DTpos=34*60 #(min)
t_DTpro=40*60 #(min)
t_DTneg=25*60 #(min)
#Growth rate
r_Tpos= 2.84E-3 #(/min)
r_Tpro= 2.79E-3 #(/min)
r_Tneg= 6.23E-4 #(/min)
#Death rate
delta_Tpos= 2.5E-3 #(/min)
delta_Tpro= 2.5E-3 #(/min)
delta_Tneg= 1.6E-4 #(/min)
#Min Carrying capacity
K=1
#Environmental Carrying capacity (Scaling Factor)
rho_Tpos=2000
rho_Tpro=2000
rho_Tneg=2000
#Resource limits
##Oxygen
###T+
l_lim_o2Tpos=0 #lower-threshold(prop)
u_lim_o2Tpos=1 #upper-saturation(prop)
###Tp
l_lim_o2Tpro=0 #(prop)
u_lim_o2Tpro=1 #(prop)
###T-
l_lim_o2Tneg=0 #(prop)
u_lim_o2Tneg=1 #(prop)
##Testosterone
###T+
l_lim_testTpos=0 #(prop)
u_lim_testTpos=1 #(prop)
###Tp
l_lim_testTpro=0 #(prop)
u_lim_testTpro=1 #(prop)
#filename to save output in
f_name='singlecelltype/Tneg/rho_Tneg/p_o2=1E-2-'
