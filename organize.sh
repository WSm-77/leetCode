#!/bin/bash

# List of files to copy (fill this list with your file paths)
# easyHashing=("1" "217" "242")
# easyHashingNames=("two_sum" "contains_duplicate" "valid_anagram")
# mediumHashing=("49" "347" "238" "36" "128")
# mediumHashingNames=("group_anagram" "top_k_frequent_elements" "product_of_array_except_self" "valid_sudoku" "longest_consecutive_sequence")
# easyPointers=("125")
# easyPointersNames=("valid_palindrom")
# mediumPointers=("167" "15" "11")
# mediumPointersNames=("two_sum_II" "3sum" "container_with_most_water")
# hardPointers=("42")
# hardPointersNames=("traping_rain_water")
# easyStack=("20")
# easyStackNames=("valid_paranthasis")
# mediumStack=("155" "150" "22" "739" "853")
# mediumStackNames=("min_stack" "evaluate_reversed_polish_notation" "generate_parentheses" "daily_temperatures" "car_fleet")
# easyBinSearch=("704")
# easyBinSearchNames=("binary_search")
# mediumBinSearch=("74" "875")
# mediumBinSearchNames=("search_2D_matrix" "koko_eating_bananas")
# easyLinked=("206" "21" "141")
# easyLinkedNames=("reverse_linked_list" "merge_two_sorted_lists" "linked_list_cycle")
# mediumLinked=("19" "287")
# mediumLinkedNames=("remove_nth_node_from_end_of_list" "find_duplicate")
# easyTrees=("226" "104" "543" "110" "100" "572")
# easyTreesNames=("invert_binary_tree" "maximum_depth_of_binary_tree" "diameter_of_binary_tree" "balanced_binary_tree" "same_tree" "subtree_of_another_tree")
# mediumTrees=("235")
# mediumTreesNames=("lowest_common_ancestor")
# mediumBacktracking=("78" "39" "46" "90" "40" "79" "17")
# mediumBacktrackingNames=("subsets" "combination_sum" "permutations" "subsets_II" "combination_sum_II" "word_search" "letter_combinations_of_phone_number")
# mediumGraphs=("200" "695" "133" "994" "417" "130" "207" "210" "684" "127")
# mediumGraphsNames=("number_of_islands" "max_area_of_island" "clone_graph" "rotting_oranges" "pacific_atlantic_water_flaw" "surrounded_regions" "course_schedule" \
#                    "course_schedule_II" "redundant_connection" "word_ladder")
# easyDP=("70" "746")
# easyDPNames=("climbing_stairs" "min_cost_climbing_stairs")
mediumDP=("198" "213")
mediumDPNames=("house_robber" "house_robber_II")
files=("${mediumDP[@]}")
newNames=("${mediumDPNames[@]}")

if (( ${#files[@]} != ${#newNames[@]} )); then
    echo "Arrays are not of the same length!!!"
    exit 1
fi

# sourceDir="easy"
sourceDir="medium"
# sourceDir="hard"

# Directory to copy files to (fill this with your target directory)
# targetDir="arrays_and_hashing"
# targetDir="two_pointers"
# targetDir="binary_search"
# targetDir="linked_list"
# targetDir="trees"
# targetDir="backtracking"
# targetDir="graphs"
targetDir="dynamic_programming1"

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
    echo "Copied ${file} to ${newFile}"
    echo "Mv $file to ${mvName}"
  else
    echo "File $file does not exist."
  fi
  echo ""
done

echo "All files have been copied."