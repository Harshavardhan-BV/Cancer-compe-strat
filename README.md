# Cancer-compe-strat
A repository for modelling competitive strategies in cancer and their effect on adaptive therapy

## Structure of the repo
- codes
	- contains the base code for simulation
- input
	- contains the input file for parameters of a particular simulation run
- raw_output
	- contains output of the simulation run
- analysis
	- analysis scripts for processing data in raw_output
- figures
	- figures produced by the analysis scripts are stored here
- doc
	- contains a brief description of each simulation run
- writing
	- contains the report/thesis drafts

## How to run
- You'll need all the packages listed in [requirements.txt](./requirements.txt).
	- If you use anaconda all the packages are installed by default
	- If you use vanilla python, do ``` pip install -r requirements.txt```
- If you plan to recreate pre-existing simualtion runs
	- Navigate to ./input/EnvEq/path/to/parameters/of/interest/
	- copy the files from the said folder to ./codes/EnvEq_sum/
	- Rename any files with prefixes by removing the prefixes to input.py or parallelizer.py
	- Some runs also have an accompanying csv files for input
	- In parallelizer.py you may have to change ```pool = Pool(no_of_cores_of_your_machine)```
- If you plan to modify some parameters, keep the following in mind and change accordingly
	- EnvEq.py:
	 	- contains all the code for differential equations, solver call, non negative check, therapy functions, etc
		- fixed code, do not modify unless necessary
	- input.py
		- contains the fixed parameters used by the simulation
		- change parameters and output file paths here
		- some parameters might be changed in
	- parallelizer.py
		- contains the code for parsing input.py file, parallelization and the parameter ranges to (parallel) loop over
		- might need to know some basic python to understand and modify parameters here
	- somefile.csv
		- these files are present for some simualtion runs
		- parallelizer.py loops over each row as input
		- rows can be added without any other changes but adding columns would require modifying parallelizer.py to be useful
