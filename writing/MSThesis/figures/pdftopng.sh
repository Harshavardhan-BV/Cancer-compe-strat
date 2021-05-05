#!/bin/bash

for i in *.pdf;do
	pdftoppm -png $i "../figures_png/${i%.pdf}"
done
