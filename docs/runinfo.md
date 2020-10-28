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
### p_o2
- only T- cell types present
- changed the production rate of oxygen from 10^0 to 10^5 (40 logspaced values)
- to see how it affects the equilibrium values of T_neg and o2

### p_o2-mu_o2
- only T- cell types present
- changed the production rate of oxygen from 10^0 to 10^3 (10 logspaced values)
- changed the uptake rate of oxygen from 10^-1 to 10^1 (10 logspaced values)
- to see how it affects the equilibrium values of T_neg and o2
