import csv
import sys
import openpyxl
import pandas as pd


def main():
    base_name = sys.argv[1]
    dir_name = "/mnt/c//Users/ryonryon/Desktop/Research/Log/"
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

    float_acc_list = functor(float, acc_list)
    float_gyr_list = functor(float, gyr_list)

    output_name = sys.argv[2]
    df = pd.DataFrame(float_acc_list)
    df2 = pd.DataFrame(float_gyr_list)
    with pd.ExcelWriter(dir_name + output_name) as w:
        df.to_excel(w, sheet_name='sheet1')
        df2.to_excel(w, sheet_name='sheet2')


def functor(cast_type, origin_list):
    if isinstance(origin_list, list):
        return [functor(cast_type, i) for i in origin_list]
    else:
        return cast_type(origin_list)


if __name__ == '__main__':
    main()
