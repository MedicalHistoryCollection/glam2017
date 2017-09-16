#!/bin/bash
input="categories.txt"
while IFS= read -r var
do
  echo "Category: $var"
  awk 'BEGIN {FS = ","}; {print $2}' photos_$var.csv >name_picutes_files_category_$var.csv
done < "$input"

