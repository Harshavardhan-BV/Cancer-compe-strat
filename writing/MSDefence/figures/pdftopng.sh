#!/bin/bash

#Converts pdf plots to png for better use with 
for i in *.pdf; do
	pdftoppm -png $i "../figures_png/${i%.pdf}"
done

