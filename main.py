import csv
import sys
import openpyxl
import pandas as pd

import functor
import env


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_dir_name = env.INPUT_DIR_NAME
    output_dir_name = env.OUTPUT_DIR_NAME
    acc_list = []
    gyr_list = []
    csv_expand = ".csv"
    xlsx_expand = ".xlsx"

    try:
        with open(input_dir_name + input_file + csv_expand, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == '1':
                    gyr_list.append(row)
                elif row[0] == '0':
                    acc_list.append(row)
                else:
                    pass
    except FileNotFoundError:
        print("File does not exist!")

    float_acc_list = functor.convert_list(float, acc_list)
    float_gyr_list = functor.convert_list(float, gyr_list)

    float_acc_list.insert(0, [0, 0, "x", "y", "z"])
    float_gyr_list.insert(0, [0, 0, "x", "y", "z"])

    df = pd.DataFrame(float_acc_list)
    df2 = pd.DataFrame(float_gyr_list)
    with pd.ExcelWriter(output_dir_name + output_file + xlsx_expand) as w:
        df.to_excel(w, sheet_name='Accelerometer')
        df2.to_excel(w, sheet_name='Gyroscope')


if __name__ == '__main__':
    main()
