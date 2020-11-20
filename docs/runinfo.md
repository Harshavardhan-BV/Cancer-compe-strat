# Run info
Documentation of what each run means and what parameters are changed

## Lot Vol
deprecated model
### r
- only 1 celltype considered
- growth and death rate pair varied with values from Berges _et al_ @ https://clincancerres.aacrjournals.org/content/1/5/473 (6 pairs)
- to see how equilibrium and dynamics changes

### mu-sig
- only 1 celltype considered
- mean and standard deviation varied from 0.25 to 0.75 (3x3 combinations)
- to see how the equilibrium value and oscillations near equilibrium changes

### mu-sig-eps
- only 1 celltype considered
- mean and standard deviation varied from 0.25 to 0.75 (3x3 combinations)
- environmental sensitivity varied from 0.25 to 1 (4 values)
- to see how the equilibrium value and oscillations near equilibrium changes
- eps < 1 took too long to compute, run canceled

## EnvEq and EnvEq_Alt
### old
deprecated bcos of issues with other parameter
#### p_o2
- only T- cell types present
- changed the production rate of oxygen from 10^0 to 10^5 (40 logspaced values)
- to see how it affects the equilibrium values of T_neg and o2

#### p_o2-mu_o2
- only T- cell types present
- changed the production rate of oxygen from 10^0 to 10^3 (10 logspaced values)
- changed the uptake rate of oxygen from 10^-1 to 10^1 (10 logspaced values)
- to see how it affects the equilibrium values of T_neg and o2

#### p_o2-r_Tneg
- only T- cell types present
- to see how it affects the equilibrium values of T_neg and o2
- og
    - changed the production rate of oxygen from 10^0 to 10^3 (10 logspaced values)
    - changed the growth rate from 10^-3 to 10^1 (death rate change constrained to doubling time)
- ext
    - equilibrium values of o2 didnt lie within thresholds so re ran
    - changed the production rate of oxygen from 10^3 to 10^6 (10 logspaced values)
    - changed the growth rate from 10^-3 to 10^1 (death rate change constrained to doubling time)
- lin
    - some linear space exploration to find more suitable values that give o2 eq between thresholds and the behaviour of these eq when the parameters are changed
    - EnvEq
        - changed the growth rate from 4.62E-4 to 1E-3 (10 linspaced values)
        - production rate of oxygen fixed at 10^3
    - EnvEq_Alt
        - changed the production rate of oxygen from 2500 to 4500 (10 linspaced values)
        - changed the growth rate from 0.001 to 0.02 (5 linspaced values)

### p_o2
- only T- cell type present
- changed the production rate of oxygen from 10^-4 to 10^0 (10 logspaced values)
- lower limit chosen bcos uptake rate in orders of 10^-5
- to see how it affects the equilibrium values of T_neg and o2

### l_lim_o2Tneg x u_lim_o2Tneg
- chose p_o2=8.86E-2 (proportion/min) for both OG & Alt Eq with an additional p_o2=3.36E-2 (proportion/min) for Alt Eq
- changed (l_lim_o2Tneg,u_lim_o2Tneg) as (0,0.1),(0,0.3),...(0.2,0.3)(0.2,0.5)...(0.8,0.9)
- to see how the limits affect the equilibrium values of Tneg and o2

### r

