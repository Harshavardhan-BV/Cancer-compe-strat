# !/bin/bash
parm="mu-sig-eps"
line=""
line1="μ ="
line2="σ ="
line3="ϵ_1="
line4="f_name='singlecelltype/$parm/"
val1=(0.25 0.5 0.75)
val2=(0.25 0.5 0.75 1)
val3=(1 0.75 0.5 0.25)
mkdir -p ../../figures/Lot-Vol/singlecelltype/$parm ../../raw_output/Lot-Vol/singlecelltype/$parm

for i in "${val1[@]}"; do
	for j in "${val2[@]}";do
		for k in "${val3[@]}";do
			echo $parm-$i-$j-$k
			line="$line1$i"
			sed -i "21s|.*|$line|" input.py 
			line="$line2$j"
			sed -i "22s|.*|$line|" input.py
			line="$line3$k"
			sed -i "13s|.*|$line|" input.py
			line="$line4$i-$j-$k'"
			sed -i "27s|.*|$line|" input.py
			python Lot-Vol.py
		done
	done
done
