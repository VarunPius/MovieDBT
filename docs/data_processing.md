This file describes how the CSV processor works.

Inside the `datasets` directory, there is a `process_csv.sh` file. The file splits and merges CSV file.
Why split file? The dataset is huge and results in huge time just to see values. Also, the files can't be pushed to Github, which has a 100 mb file size limit.


# Split files:
The basic command for splitting files using shell command is using the `split` command. This is how `split` works:
```
split -l 2500000 ratings.csv split_
```
In our code, we used the option with some more values, as follows:
```
split -d -a 3 -l 1000 file.txt
```

What each parameter means:
- The `split` command is used to split a file into smaller pieces.
- The `-l` option is used to specify the number of lines per file.
    For example, `split -l 250000 file.txt` will split the `file.txt` file into multiple files, each containing 250000 lines.
- The `-d` option is used to specify that the output files should be numeric. For example, `split -d -l 1000 file.txt` will create files with names like `x00`, `x01`, etc.
- The `-a` option is used to specify the number of digits in the output file names. For example, `split -d -a 3 -l 1000 file.txt` will create files with names like `x000`, `x001`, etc
- The `tail` command is used to display the last part of a file.
    The `-n` option is used to specify the number of lines to display.
    For example, `tail -n 10 file.txt` will display the last 10 lines of the `file.txt` file.
    In the context of shell scripts, `tail -n +2` is often used to remove the first line (header) of a CSV file. This is because the first line of a CSV file usually contains column headers, which are not needed when processing the data.


# Merge files
Here’s an explanation of the script:
```
awk 'FNR==1 && NR!=1{next;}{print}' *.csv > merged.csv
```

The `awk` command is a powerful text processing tool that can be used to manipulate CSV files. Here’s what each part of the command does:
- In `awk`, `FNR` is a built-in variable that represents the record number (line number) of the current file being processed. `NR` is another built-in variable that represents the total number of records (lines) processed so far.
    `FNR==1` is used to check if the current line being processed is the first line of the current file.
    If it is, then the script checks if `NR` is not equal to 1 (i.e., if it’s not the first file being processed).
    If both conditions are true, then the “next” command is executed, which skips processing of the current line and moves on to the next line.
    The following does the reverse `awk 'FNR==1 && NR!=1{print;}{next}' part/*.csv`; it will print the first line of each file and skip the rest
- `FNR==1 && NR!=1{next;}` skips all lines except the first line of the first file.
- `{print}` prints all lines except the first line of the first file.
- `*.csv` specifies that all CSV files in the current directory should be processed.
- `> merged.csv` redirects the output to a file called `merged.csv`.
So, this script reads all CSV files in the current directory and prints all lines except the first line of all files except the first file.

The header from the first file is included only once in the output file.

# Simple commands:
- Split file: `split -l 1000 file.csv new_ --additional-suffix=.csv`
- Merge files: `cat *.csv > combined-files.csv`
- Get Difference: `diff file1.txt file2.txt > diff.txt`

# Parquet
```
import pyarrow.csv as pv
import pyarrow.parquet as pq

table = pv.read_csv(filename)
pq.write_table(table, filename.replace('csv', 'parquet'))
```