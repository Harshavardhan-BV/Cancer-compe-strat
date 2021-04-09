#!/bin/bash

# Ask user for the filematch string
echo Enter directory
read drctry
echo Enter beginning string to match with
read findwhat
echo Replace matched part with what
read replaceto
for f in $drctry/$findwhat*
do
  echo $f to ${f/$findwhat/$replaceto}
done
read -r -p "Are you sure? [y/N] " response
response=${response,,}    # tolower
if [[ "$response" =~ ^(yes|y)$ ]]
then
  for f in $drctry/$findwhat*
  do
    mv -v -- "$f" "${f/$findwhat/$replaceto}"
  done
fi
