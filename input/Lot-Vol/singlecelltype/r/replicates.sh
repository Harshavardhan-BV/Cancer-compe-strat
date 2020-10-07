# !/bin/bash
parm="r"
line=""
line1="r_1="
line2="𝛿_1="
line3="f_name='singlecelltype/$parm/"
val1=(1.54 1.46 2.90 2.04 2.77 2.42)
val2=(1.42 1.32 0.85 0.76 2.22 1.68)
mkdir -p ../../figures/Lot-Vol/singlecelltype/$parm ../../raw_output/Lot-Vol/singlecelltype/$parm
for i in {0..5}; do
	echo $parm-${val1[$i]}-${val2[$i]}
	line="$line1${val1[$i]}"
	sed -i "7s|.*|$line|" input.py 
	line="$line2${val2[$i]}"
	sed -i "16s|.*|$line|" input.py
	line="$line3${val1[$i]}-${val2[$i]}'"
	sed -i "27s|.*|$line|" input.py
	python Lot-Vol.py      
done
