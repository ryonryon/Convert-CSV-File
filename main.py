import csv
import sys
import openpyxl
import pandas as pd

import functor
import settings


def main():
    base_name = sys.argv[1]
    dir_name = settings.DIR_NAME
    print(dir_name)

    abs_name = dir_name + base_name
    acc_list = []
    gyr_list = []

    with open(abs_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == '1':
                gyr_list.append(row)
            elif row[0] == '0':
                acc_list.append(row)
            else:
                pass

    float_acc_list = functor.convert_list(float, acc_list)
    float_gyr_list = functor.convert_list(float, gyr_list)

    output_name = sys.argv[2]
    df = pd.DataFrame(float_acc_list)
    df2 = pd.DataFrame(float_gyr_list)
    with pd.ExcelWriter(dir_name + output_name) as w:
        df.to_excel(w, sheet_name='sheet1')
        df2.to_excel(w, sheet_name='sheet2')


if __name__ == '__main__':
    main()
