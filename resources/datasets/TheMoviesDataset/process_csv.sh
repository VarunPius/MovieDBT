#!/bin/zsh

# Setting arguments and parameters
## Defining type of operation: values can be `merge` and `split`
file_oper=$1
echo "Type of operation: $file_oper"

## File to process
orig_file=$2
echo "Input file: $orig_file"

## Output File
op_file=$3
echo "Output file: $op_file"

# Main code
# Split file
if [ "$1" = "split" ]; then
    echo "Inside loop"

    # create directory if not exists
    if [ ! -d "part" ]; then
        mkdir -p part
    fi
    
    tail -n +2 $orig_file | split -l 10000 -d -a 3 - part/$op_file
    for file in part/$op_file*; do
        head -n 1 $orig_file > tmp_file
        cat $file >> tmp_file
        mv tmp_file $file.csv
        rm $file
    done
fi

# Merge file
if [ "$1" = "merge" ]; then
    awk 'FNR==1 && NR!=1{next;}{print}' part/$orig_file* > $op_file.csv
fi



# Running the code:
# ./process_csv.sh split <input>.csv <splitFilePrefix>
# ./process_csv.sh merge <splitFilePrefix> <output>
#
# Example:
# ./process_csv.sh split ratings_small.csv ratings_split
# ./process_csv.sh merge ratings_split ratings_merge
#
# Actual run:
# Ratings
# ./process_csv.sh split ratings.csv ratings_split
# ./process_csv.sh merge ratings_split ratings_merge
# Credits
# ./process_csv.sh split credits.csv credits_split
# ./process_csv.sh merge credits_split credits_merge

