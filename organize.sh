#!/bin/bash

# List of files to copy (fill this list with your file paths)
# easyHashing=("1" "217" "242")
# easyHashingNames=("two_sum" "contains_duplicate" "valid_anagram")
# mediumHashing=("49" "347" "238" "36" "128")
# mediumHashingNames=("group_anagram" "top_k_frequent_elements" "product_of_array_except_self" "valid_sudoku" "longest_consecutive_sequence")
files=("${easyHashing[@]}")
newNames=("${easyHashingNames[@]}")

if (( ${#files[@]} != ${#newNames[@]} )); then
    echo "Arrays are not of the same length!!!"
    exit 1
fi

sourceDir="easy"
# sourceDir="medium"
# sourceDir="hard"

# Directory to copy files to (fill this with your target directory)
targetDir="arrays_and_hashing"

# Check if the target directory is specified
if [ -z "$targetDir" ]; then
  echo "Target directory is not specified. Please set the 'targetDir' variable."
  exit 1
fi

# Check if the target directory exists
if [ ! -d "$targetDir" ]; then
  echo "Target directory does not exist. Creating new $(pwd)/${targetDir}."
  mkdir "$targetDir"
fi

lenght=${#files[@]}

for ((idx=0; idx<lenght; idx++)); do
  file="${files[$idx]}"
  file="${sourceDir}/${file}.py"
  newName="${files[$idx]}_${newNames[$idx]}.py"
  mvName="${sourceDir}/${newName}"
  newFile="${targetDir}/${newName}"
  if [ -f "$file" ]; then
    cp "$file" "$newFile"
    mv "$file" "$mvName"
    echo "Mv $file to ${mvName}"
    echo "Copied ${file} to ${newFile}"
  else
    echo "File $file does not exist."
  fi
done

echo "All files have been copied."