# Parametes

## Growth Rates
### ATCC population doubling time
- Cell specifications have a rough estimate of doubling time
- doubling time can be approximated to ln(2)/(r-delta)
- T+ cells = LNCaP (CRL-1740)
	- Androgen sensitive
	- population doubling time = 34 hrs 
	- r - delta = 0.0204 /hr
- Tp cells = 22Rv1 (CRL-2505)
	- Expresses CYP17A1 -> converts cholersterol to testosterone
	- population doubling time = 40 hrs 
	- r - delta = 0.0173 /hr
- T- cells = PC-3 (CRL-1435)
	- Androgen insensitive
	- Latest website doesnt have data
		- 2012 datasheet in https://physics.cancer.gov
		- other cell line data within 1hr 
	- population doubling time =  25 hrs
	- r - delta = 0.0277 /hr
- delta could be taken as a free parameter with r being determined from it. 
- Or delta can be taken from Jain et al and r fixed from it.

## Mean tissue resource level
### Stewart _et al_ @ https://bjui-journals.onlinelibrary.wiley.com/doi/full/10.1111/j.1464-410X.2009.08921.x
- Oxygen:
	- Normal Muscle tissue = 30mmHg
	- Hypoxic Prostate Cancer = 2.5mmHg

## Uptake and Production rates
- These determine the competition levels of the cell and a parameter space exploration has to be done to observe their impact.
- converting to concentration by fixing volume and normalising with respect to known tissue concentrations.
### Hail Jr _et al_ @ https://www.sciencedirect.com/science/article/pii/S1476558610800041
- Main paper details unrelated
- oxygen consumption rate given in nmol/min/10^6cells
-  T+ cell = LNCaP
	- mu_o2 ~= 5.5 nmol/min/10^6cells
- T- cells = PC-3
	- mu_o2 ~= 3.5 nmol/min/10^6cells
- Tp cells = NA :(
- considering a mean tumour volume from a 2mm spherical tumour = 3.35E-5 L, 1.35 μM/mmHg
	- T+ = 5.5E-9/(3.35E-5 * 1.35 * 2.5) = 4.86E-5 proportion/min
	- Tp = assumed same as T+
	- T- = 3.5E-9/(3.35E-5 * 1.35 * 2.5) = 3.10E-5 proportion/min

## Thresholds
- These determine the sensitivity of the cell to resource and in extention survival.
- By normalising with respect to known tissue concentrations, the thresholds can be constrained to [0,1] and could be explored.

## Carrying capacity and sensitivity?
- *shrug* depends on the final equation form we're using
- no idea
