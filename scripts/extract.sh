#!/bin/bash
input="categories.txt"
while IFS= read -r var
do
  echo "Category: $var"
  grep ",$var"  data_library_small_02.csv >books_$var.csv
  grep ",$var," pictures_database.csv     >photos_$var.csv
done < "$input"

