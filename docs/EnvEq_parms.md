# Parametes

## Growth Rates
### Jain _et al_ @ https://www.pnas.org/cgi/doi/10.1073/pnas.1115750108
- q_1 can be taken as r
- q_3 can be taken as delta
-  T+ cell = N cells
	- Androgen dependent cells
	- r = 11.1 * 10^-4 /hr
	- delta = (0.15-0.10) * 10^-4 /hr
- T- cells = M cells
	- Castrate resistant cells
	- r = (2.8-6.6) * 10^-4 /hr
	- delta = (0.01-0.009) * 10^-4 /hr 
- Tp cells = NA :(
### ATCC population doubling time
- Cell specifications have a rough estimate of doubling time
- No data for death rate, delta =0 doesn't make sense
- T+ cells = LNCaP (CRL-1740)
	- Androgen sensitive
	- doubling time = 34 hrs 
	- r = 0.0204 /hr
- Tp cells = 22Rv1 (CRL-2505)
	- Expresses CYP17A1 -> converts cholersterol to testosterone
	- doubling time = 40 hrs 
	- r = 0.0173 /hr
- T- cells = PC-3 (CRL-1435)
	- Androgen insensitive
	- Latest website doesnt have data
		- 2012 datasheet in https://physics.cancer.gov
		- other cell line data within 1hr 
	-  doubling time =  25 hrs
	- r = 0.0277 /hr

## Uptake and Production rates
- These determine the competition levels of the cell and a parameter space exploration has to be done to observe their impact.

## Thresholds
- These determine the sensitivity of the cell to resource and in extention survival.
- Starting off with default Physicell parameters for now.

## Carrying capacity and sensitivity?
- *shrug* depends on the final equation form we're using
- no idea
