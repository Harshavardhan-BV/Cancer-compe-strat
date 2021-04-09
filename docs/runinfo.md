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
- prefix=
  - none: Initial cell seeding 1:1 Tp:T-
  - 0.9Tp-: Initial cell seeding 9:1 Tp:T-
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Oxygen Upper Limit (u_lim_o2Tpro-u_lim_o2Tneg)
- Combinations of varying the upper limit of oxygen while keeping lower limit fixed  over both cells
- Testosterone limits at (0,1) (llim,ulim)
- prefix=
  - none: Initial cell seeding 1:1 Tp:T-
  - 0.9Tp-: Initial cell seeding 9:1 Tp:T-
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Oxygen Constant Slope Limit (cs_lim_o2Tpro-cs_lim_o2Tneg)
- Combinations of varying both the lower limit and upper limit by the same amount to maintain the same slope over both the cells
- Testosterone limits at (0,1) (llim,ulim)
- prefix=
  - none: Initial cell seeding 1:1 Tp:T-
  - 0.9Tp-: Initial cell seeding 9:1 Tp:T-
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Testosterone Lower Limit (l_lim_testTpro)
- Varying the lower limit of testosterone while keeping upper limit fixed for Tp
- Oxygen limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Testosterone Upper Limit (u_lim_testTpro)
- Varying the upper limit of testosterone while keeping lower limit fixed for Tp
- Oxygen limits at (0,1) (llim,ulim)
- prefix=
  - none: Initial cell seeding 1:1 Tp:T-
  - 0.9Tp-: Initial cell seeding 9:1 Tp:T-
  - 0.9Tp-0.5test: Initial cell seeding 9:1 Tp:T- and initial testosterone level 0.5
- analysis: [pairwise_Tpro-Tneg.py](../analysis/pairwise_Tpro-Tneg.py)

#### Testosterone Constant Slope Limit (cs_lim_testTpro)
- Varying the  both the lower limit and upper limit by the same amount to maintain the same slope for Tp
- Oxygen limits at (0,1) (llim,ulim)
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
- Cases: combinations of Tp test limitation (no, moderate, severe) x T- o2 limitation (no, high, severe) x o2 production (normal, low)
- Case numbers not in sequential order
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
- Testosterone limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Oxygen Constant Slope Limit (cs_lim_o2Tpro-cs_lim_o2Tpos)
- Combinations of varying both the lower limit and upper limit by the same amount to maintain the same slope over both the cells
- Testosterone limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Testosterone Lower Limit (l_lim_testTpro-l_lim_testTpos)
- Combinations of varying the lower limit of testosterone while keeping upper limit fixed over both the cells
- Oxygen limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Testosterone Upper Limit (u_lim_testTpro-u_lim_testTpos)
- Combinations of varying the upper limit of testosterone while keeping lower limit fixed over both cells
- Oxygen limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Testosterone Constant Slope Limit (cs_lim_testTpro-cs_lim_testTpos)
- Combinations of varying both the lower limit and upper limit by the same amount to maintain the same slope over both the cells
- Oxygen limits at (0,1) (llim,ulim)
- analysis: [pairwise_Tpos-Tpro.py](../analysis/pairwise_Tpos-Tpro.py)

#### Cases (Case-Tp_initratio-Totcell)
- Different cases as given in [Tpro-Tneg_cases](../input/EnvEq/pairwise/Tneg-Tpro/Case-Tp_initratio-Totcell/Tpro-Tneg_cases.csv)
- Case1: Tp more testosterone limited than T+
- Case2: T+ more testosterone limited than Tp
- Case3: T+ oxygen limited, Tp moderately oxygen limited
- Case4: T+ oxygen limited, Tp not oxygen limited
- Cases subject to change in near future
- Cases_v1.1 are variants of the original cases but attemted at extending parameters for All3 (not utilised anymore)
- Varied over different initial conditions of Tp cell ratio and Total cells
- analysis: [pairwise_Tpos-Tpro_initratio.py](../analysis/pairwise_Tpos-Tpro_initratio.py)

## All3
### Cases (Case-Tpos-Tpro-Tneg_initratio-Totcell)
- Different cases as given in [All3_cases](../input/EnvEq/All3/Case-Tpos-Tpro-Tneg_initratio-Totcell/All3_cases.csv)
  - Casex.y
  - x: They follow the same pattern as pairwise Tp - T- (Cases 1 to 9)
  - y: They follow the same pattern as pairwise Tp - T+ (Cases 1 to 2)
- Varied over different initial conditions of cell ratio and Total cells
- Not used anymore -> defunct
- analysis: [All3_Cases.py](../analysis/All3_Cases.py)

### Oxygen efficiency (o2-efficiency)
- 3 cases of oxygen efficiency (via oxygen limits):
  - null = (0,1) (llim,ulim)
  - low  = (0,0.1) (llim,ulim)
  - high = (0.4,1) (llim,ulim)
- Testosterone at high efficiency = (0,0.1) (llim,ulim)
- prefix=
  - none: Initial cell seeding 1:1:1 Tp:T+:T-
  - 0.8Tp-: Initial cell seeding 8:1:1 Tp:T+:T-
- analysis: [All3_efficiency.py](../analysis/All3_efficiency.py)

### Testosterone efficiency (test-efficiency)
- Cases for testosterone efficiency (via ulim) explored where all 3 celltypes can coexist
- 2 cases of testosterone efficiency (formulated post run):
  - high = (0,0.1) (llim,ulim)
  - low = (0,0.3) (llim,ulim)
- prefix=
  - Caseo2-Null: oxygen limits = (0,1) (llim,ulim) with 1:1:1 Tp:T+:T- initial seeding
  - Caseo2-HE:  oxygen limits = (0,0.1) (llim,ulim) with 1:1:1 Tp:T+:T- initial seeding
  - 0.8Tp-Caseo2-Null: oxygen limits = (0,1) (llim,ulim) with 8:1:1 Tp:T+:T- initial seeding
  - 0.8Tp-Caseo2-Null: oxygen limits = (0,0.1) (llim,ulim) with 8:1:1 Tp:T+:T- initial seeding
- analysis: [All3_efficiency.py](../analysis/All3_efficiency.py)

### Abiraterone only therapy (therapy-abi)
- Different adaptive therapy regimens (on and off thresholds) for abiraterone explored
  - 4 subfolders for oxygen and testosterone efficieny cases:
    - o2-Null_test-HE
    - o2-HE_test-HE
    - o2-LE_test-HE
    - o2-Null_test-LE
  - File Labeled as: TherapyMode-TestProd-OnThreshold-OffThreshold
  - Therapy Mode:
    - AT: adaptive Therapy
    - SOC: Standard of care
  - TestProd: 3 testosterone production (due to large error bar for abiraterone dose response)
    - p=1.4e-07: 1.4 x 10^-7 /min/cell
    - p=1.2e-07: 1.2 x 10^-7 /min/cell
    - p=1.0e-07: 1.0 x 10^-7 /min/cell
  - OnThreshold-OffThreshold: (only for AT)
    - Multiplier for 2000x cell number for threshold
    - Eg: 1.0-0.5 -> therapy on when x >= 2000 & therapy off when x <= 1000
- Not code compatible with current therapy implementation (results still hold)
- Not all input files present -> _needs cleanup_
- prefixes=
  - 3 initial conditions:
    - none: 1:1:1 Tp:T+:T- initial seeding (not for test-LE)
    - 0.8Tp-: 8:1:1 Tp:T+:T- initial seeding
    - y0_eq: Initial condition same as final population/resource level at 1000 days in absence of therapy (only for o2-Null_test-HE)
  - Cells considered for adaptive therapy:
    - None: Sum over all three cells control on/off
    - nonT_neg: Sum over only T+ and Tp cell types control on/off
  - r & delta changes: (only for o2-Null_test-HE)
    - none: default r & delta
    - timescaled: r & delta = default x 10^-2
    - timescaled_tauconst: delta = default x 10^-2, tau_D = default -> r & K_max (rho) from constraint equations
    - cunningham: Doubling time (tau_D) from Cunningham et al used, delta = default, r & K_max (rho) from constraint equations
- analysis: [therapy_abi.py](../analysis/therapy_abi.py)

### Abiraterone + Docetaxel combination therapy (therapy)
- Different
- 4 subfolders for oxygen and testosterone efficieny cases:
  - o2-Null_test-HE
  - o2-HE_test-HE
  - o2-LE_test-HE
  - o2-Null_test-LE
- File Labeled as: AbirateroneTherapyMode-DocetaxelTherapyMode
- Therapy Mode:
  - NA: No therapy applied
  - AT: Adaptive Therapy -> Sum over all three cells control on/off
  - AT_nn: Adaptive Therapy non negative -> Sum over only T+ and Tp cell types control on/off (only for abi)
  - MT: Metronomic Therapy -> Therapy changes based on time
- Error in how therapy works in combination
- prefixes=
  - none: 1:1:1 Tp:T+:T- initial seeding (not for test-LE)
  - 0.8Tp-: 8:1:1 Tp:T+:T- initial seeding
- Threshold:
  - MT: 7 days without therapy - 1 day with therapy cycle
  - AT: on=2000 to off=1000 (ie x_0 to 0.5 x_0)
  - AT_nn:
    - for 1:1:1 seeding: on=1332 to off=666 (ie (Tp+T+) x_0 to 0.5 x_0)
    - for 8:1:1 seeding: on=1800 to off=900 (ie (Tp+T+) x_0 to 0.5 x_0)
  - AT thresholds needs to be changed
- analysis: [therapy.py](../analysis/therapy.py)
