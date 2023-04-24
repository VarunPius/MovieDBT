# System libraries
import argparse     

# External libraries
#import pyarrow as pyr
import pyarrow.csv as pv
import pyarrow.parquet as pq

import pandas as pd


def convert_to_parquet(filename):
    table = pv.read_csv(filename)
    pq.write_table(table, filename.replace('csv', 'parquet'))


def convert_to_csv(filename):
    df = pq.read_table(filename).to_pandas()
    op_file = filename.split('.')[0] + '_1.csv'
    df.to_csv(op_file, sep=',', index=False, mode='w', line_terminator='\n', encoding='utf-8')


def analyze_parquet(filename):
    extension = filename.split('.')[-1]

    if extension == 'csv':
        df = pd.read_csv(filename)
    elif extension == 'parquet':
        df = pd.read_parquet(filename)
    print("Number of rows:", len(df.index))
    print("Sample data:")
    print(df.head())
    print(df.info())


if __name__=='__main__':
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('-f', '--filename', type=str, required=True, help = "Name of the file to process")
    parser.add_argument("-c", "--convertcsv", action="store_const", const=True, default=False, help = "Flag to convert csv to parquet")
    parser.add_argument("-p", "--convertpqt", action="store_const", const=True, default=False, help = "Flag to convert parquet to csv")
    parser.add_argument("-a", "--analytics", action="store_const", const=True, default=False, help = "Flag to analyse parquet")

    args = parser.parse_args()

    if args.convertcsv:
        print("Inside Convert to Parquet")
        filename = args.filename
        convert_to_parquet(filename)

    if args.convertpqt:
        print("Inside Convert to CSV")
        filename = args.filename
        convert_to_csv(filename)

    if args.analytics:
        print("Inside Analytics")
        filename = args.filename
        analyze_parquet(filename)


