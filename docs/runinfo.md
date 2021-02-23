# Run info
Documentation of what each run means and what parameters are changed

## Archived models
Details of these runs not provided here
- LotVol
- EnvEq_Alt
- EnvEq (without sum over all cells)
- EnvEq_Sum with alternate parameters

## singlecelltype
### T-
#### Oxygen Limits (l_lim_o2Tneg-u_lim_o2Tneg)
- Combinations of varying the lower limit and upper limit of oxygen for T-
- analysis: [o2_lim.py](../analysis/o2_lim.py)

#### Oxygen Production (p_o2)
- Varying the production rate of oxygen close to the values estimated from equilibrium and constraints
- analysis: [p_o2.py](../analysis/p_o2.py)

### Tp
#### Oxygen Limits (l_lim_o2Tpro-u_lim_o2Tpro)
- Combinations of varying the lower limit and upper limit of oxygen for T-
- analysis: [o2_lim.py](../analysis/o2_lim.py)

#### Oxygen Limits (l_lim_o2Tpro-u_lim_o2Tpro)
- Combinations of varying the lower limit and upper limit of oxygen for T-
- analysis: [test_lim.py](../analysis/test_lim.py)

## Testosterone Production (p_test)
- No uptake of testosterone by Tp
- Varying the production rate of testosterone close to the values estimated from equilibrium and constraints
- analysis: [p_test.py](../analysis/p_test.py)

## Testosterone Production and Uptake (p_test-mu_test)
- Varying the production rate and uptake rate of testosterone subject to constraints
- Constraint slightly higher than theoretically estimated as got from p_test
- analysis: [p_test-mu_test.py](../analysis/p_test-mu_test.py)

## pairwise
### Tp - T-
#### Oxygen Lower Limit (l_lim_o2Tpro-l_lim_o2Tneg)
- Combinations of varying the lower limit of oxygen while keeping upper limit fixed over both the cells
- Testosterone limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Oxygen Upper Limit (u_lim_o2Tpro-u_lim_o2Tneg)
- Combinations of varying the upper limit of oxygen while keeping lower limit fixed  over both cells
- Testosterone limits at (0,1)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Oxygen Constant Slope Limit (cs_lim_o2Tpro-cs_lim_o2Tneg)
- Combinations of varying both the lower limit and upper limit by the same amount to maintain the same slope over both the cells
- Testosterone limits at (0,1)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Testosterone Lower Limit (l_lim_testTpro)
- Varying the lower limit of testosterone while keeping upper limit fixed for Tp
- Oxygen limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Testosterone Upper Limit (u_lim_testTpro)
- Varying the upper limit of testosterone while keeping lower limit fixed for Tp
- Oxygen limits at (0,1)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Testosterone Constant Slope Limit (cs_lim_testTpro)
- Varying the  both the lower limit and upper limit by the same amount to maintain the same slope for Tp
- Oxygen limits at (0,1)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Oxygen and Testosterone Production (p_o2-p_test)
- T- is oxygen limited (in base case still took over the population)
- Combinations of varying the production rate of oxygen and testosterone to give a better chance for Tp in the initial period
- analysis: [pairwise_Tpro-Tneg_p_o2-p_test.py](../analysis/pairwise_Tpro-Tneg_p_o2-p_test.py)
pairwise_Tpro-Tneg_p_o2-p_test

#### Oxygen Production (p_o2)
- T- is oxygen limited (in base case still took over the population)
- p_test = 1E-6 /cell/min
- Looking closely at the region where there is a phase transition in the above case (p_o2-p_test) to look for possibility of coexistence
- analysis: [pairwise_Tpro-Tneg_p_o2-p_test.py](../analysis/pairwise_Tpro-Tneg_p_o2-p_test.py)
pairwise_Tpro-Tneg_p_o2-p_test

#### Oxygen Production and Testosterone Upper Limit (p_o2-u_lim_testTpro)
- T- is oxygen limited (in base case still took over the population)
- Combinations of varying the production rate of oxygen and upper limit of testosterone for Tp
- Lowered testosterone limitation for Tp
- analysis: [pairwise_Tpro-Tneg_p_o2-p_test.py](../analysis/pairwise_Tpro-Tneg_p_o2-p_test.py)


#### Megarun (l_lim_o2Tneg-u_lim_o2Tneg-l_lim_o2Tpro-u_lim_o2Tpro-l_lim_testTpro-u_lim_testTpro)
- Brute force method of exploring over (almost) the entire parameter space of
- All combinations of lower limit and upper limit for all the resources across both the cell types done
- lower limit of testosterone limited to 0.0 - 0.2 and upper limit to (lowerlimit+0.1) - 0.5
- analysis: [pairwise_Tpro-Tneg-megarun.py](../analysis/pairwise_Tpro-Tneg-megarun.py)

#### Cases (Case-Tp_initratio-Totcell)
- Different cases based on previous pairwise run outcomes as given in [All3_Cases](../input/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/Tpro-Tneg_cases.csv)
  - Case1: T- not o2 limited, Tp not test limited
  - Case2: T- o2 limited, Tp moderately test limited
  - Case3: T- not o2 limited, Tp severly test limited
  - Case4: T- not o2 limited, Tp moderately test limited
  - Case5: Not enought o2 production & T- o2 limited, Tp moderately test limited
  - Case6: T- severly o2 limited,  Tp not test limited
  - Case7: Not enought o2 production & T- o2 limited,  Tp not test limited
  - Case8: T- severly o2 limited, Tp severly test limited
  - Case9: Not enought o2 production & T- o2 limited, Tp severly test limited
- Cases_v1.1 are variants of the original cases but attemted at extending parameters for All3 (not utilised anymore)
- Varied over different initial conditions of Tp cell ratio and Total cells
- analysis: [pairwise_Tpro-Tneg_initratio.py](../analysis/pairwise_Tpro-Tneg_initratio.py)

### Tp - T+
#### Testosterone uptake (mu_testTpos)
- Varying uptake rate of testosterone by T+
- Oxygen and Testosterone limits of both cells at (0,1)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)
- mu_testTpos value obtained from older run (older model and code) which gave stable population... not the case anymore

#### Oxygen Lower Limit (l_lim_o2Tpro-l_lim_o2Tpos)
- Combinations of varying the lower limit of oxygen while keeping upper limit fixed over both the cells
- Testosterone limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Oxygen Upper Limit (u_lim_o2Tpro-u_lim_o2Tpos)
- Combinations of varying the upper limit of oxygen while keeping lower limit fixed over both cells
- Testosterone limits at (0,1)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Oxygen Constant Slope Limit (cs_lim_o2Tpro-cs_lim_o2Tpos)
- Combinations of varying both the lower limit and upper limit by the same amount to maintain the same slope over both the cells
- Testosterone limits at (0,1)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Testosterone Lower Limit (l_lim_testTpro-l_lim_testTpos)
- Combinations of varying the lower limit of testosterone while keeping upper limit fixed over both the cells
- Oxygen limits at (0,1)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Testosterone Upper Limit (u_lim_testTpro-u_lim_testTpos)
- Combinations of varying the upper limit of testosterone while keeping lower limit fixed over both cells
- Oxygen limits at (0,1)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Testosterone Constant Slope Limit (cs_lim_testTpro-cs_lim_testTpos)
- Combinations of varying both the lower limit and upper limit by the same amount to maintain the same slope over both the cells
- Oxygen limits at (0,1)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Cases (Case-Tp_initratio-Totcell)
- Different cases as given in [Tpro-Tneg_cases](../input/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/Tpro-Tneg_cases.csv)
- Case1: Tp more testosterone limited than T+
- Case2: T+ more testosterone limited than Tp
- Case3: T+ oxygen limited, Tp moderately oxygen limited
- Case4: T+ oxygen limited, Tp not oxygen limited
- Cases_v1.1 are variants of the original cases but attemted at extending parameters for All3 (not utilised anymore)
- Varied over different initial conditions of Tp cell ratio and Total cells
- analysis: [pairwise_Tpos-Tpro_initratio.py](../analysis/pairwise_Tpos-Tpro_initratio.py)

## All3
### Cases (Case-Tpos-Tpro-Tneg_initratio-Totcell)
- Different cases as given in [All3_cases](../input/EnvEq/All3/Case-Tpos-Tpro-Tneg_initratio-Totcell/All3_cases.csv)
  - Casex.y
  - x: They follow the same pattern as pairwise Tp - T-
  - y: They follow the same pattern as pairwise Tp - T+ (upto 2)
- Varied over different initial conditions of cell ratio and Total cells
- analysis: [All3.py](../analysis/All3.py)
