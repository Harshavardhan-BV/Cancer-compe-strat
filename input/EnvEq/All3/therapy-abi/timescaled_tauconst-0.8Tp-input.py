##--Enter all the input variables here--##
#Refer doc/EnvEq_parms for further info

#Time parameters of simulation
t_max = 10000*24*60 #maximum (mins)
dt = 60  #step (mins)
#Initial Values
##cells
y0_Tpos=200
y0_Tpro=1600
y0_Tneg=200
##resource
y0_o2=0.5 #(prop)
y0_test=0 #(prop)
#Production rates of resources
p_o2=0.11 #(prop/min)
p_test=5E-7 #by Tp cells (prop/min/cell)
#Uptake rate of resources by cells
##oxygen
mu_o2Tpos=1.63E-6 #(prop/min/cell)
mu_o2Tpro=1.63E-6 #(prop/min/cell)
mu_o2Tneg=1.04E-6 #(prop/min/cell)
##testosterone
mu_testTpos=2.34E-8 #(prop/min/cell)
mu_testTpro=6E-8 #(prop/min/cell)
#Decay rates of resources
lam_o2=0.1 #(1/min)
lam_test=0.004 #(1/min)
#Doubling time
t_DTpos=34*60 #(min)
t_DTpro=40*60 #(min)
t_DTneg=25*60 #(min)
#Growth rate
r_Tpos= 0.0204 #(/min)
r_Tpro= 0.0174 #(/min)
r_Tneg= 0.0277 #(/min)
#Death rate
delta_Tpos= 2.5E-5 #(/min)
delta_Tpro= 2.5E-5 #(/min)
delta_Tneg= 1.6E-6 #(/min)
#Min Carrying capacity
K=1
#Environmental Carrying capacity (Scaling Factor)
rho_Tpos=10012
rho_Tpro=10014
rho_Tneg=10001
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
u_lim_testTpos=0.1 #(prop)
###Tp
l_lim_testTpro=0 #(prop)
u_lim_testTpro=0.1 #(prop)
#filename to save output in
f_name='All3/therapy/o2-Null_test-HE/nonT_neg-timescaled_tauconst-0.8Tp-'
