##--Enter all the input variables here--##
#parameters based on ATCC documentation

#Time parameters of simulation
t_max = 1000*24*60 #maximum (mins)
dt = 60  #step (mins)
#Initial Values
##cells
y0_Tpos=0
y0_Tpro=0
y0_Tneg=10
##resource
y0_o2=7000 #(nmol)
y0_test=0 #(units)
#Production rates of resources
p_o2=100 #(nmol/min)
p_test=60 #by Tp cells (units/min/cell)
#Uptake rate of resources by cells
##oxygen
mu_o2Tpos=5.5E-6 #(nmol/min/cell)
mu_o2Tpro=5.5E-6 #(nmol/min/cell)
mu_o2Tneg=3.5E-6 #(nmol/min/cell)
##testosterone
mu_testTpos=2 #(units/min/cell)
mu_testTpro=2 #(units/min/cell)
#Decay rates of resources
lam_o2=0.1 #(1/min)
lam_test=0.1 #(1/min)
#Doubling time
t_DTpos=34*60 #(min)
t_DTpro=40*60 #(min)
T_DTneg=25*60 #(min)
#Growth rate
r_Tpos= 3.40E-4 #(/min)
r_Tpro= 2.88E-4 #(/min)
r_Tneg= 4.62E-4 #(/min)
#Resource limits
##Oxygen
###T+
l_lim_o2Tpos=5*1.35*1E3 #lower-threshold(nmol)
u_lim_o2Tpos=35*1.35*1E3 #upper-saturation(nmol)
###Tp
l_lim_o2Tpro=5*1.35*1E3 #(nmol)
u_lim_o2Tpro=35*1.35*1E3 #(nmol)
###T-
l_lim_o2Tneg=5*1.35*1E3 #(nmol)
u_lim_o2Tneg=35*1.35*1E3 #(nmol)
##Testosterone
###T+
l_lim_testTpos=0 #(units)
u_lim_testTpos=10 #(units)
###Tp
l_lim_testTpro=0 #(units)
u_lim_testTpro=10 #(units)
#filename to save output in
f_name='singlecelltype/Tneg/p_o2-r_Tneg/'
