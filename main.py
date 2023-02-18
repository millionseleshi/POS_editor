# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pandas as pd


def csv_create(file_location):
    if os.path.isfile(file_location):
        csv_new, pos_data = read_pos_file(file_location)

        pos_csv = open(csv_new, 'w+')
        pos_csv.write(pos_data)

        new_csv_formatter(csv_new)

        return pd.read_csv(csv_new, index_col=False)

    else:
        print("The file already exists")


def read_pos_file(file_location):
    pos_file = open(file_location, "r")
    pos_data = pos_file.read()
    base = os.path.splitext(file_location)[0]
    csv_new = base + '.csv'
    return csv_new, pos_data


def new_csv_formatter(csv_new):
    new_pos = pd.read_csv(csv_new, delim_whitespace=True)
    new_pos.to_csv(csv_new)


def pos_extract(file_location):
    pos = csv_create(file_location)
    pos.drop(columns=pos.columns.difference(['Height(m)', 'Latitude(deg)', 'Longitude(deg)', 'H_Ell(m)']),
             axis=1,
             inplace=True)
    pos_formatter(pos)


def pos_formatter(pos):
    val = input("Select [0] for {'Latitude','Longitude','Altitude'}\nSelect [1] for {'Longitude,'Latitude',"
                "'Altitude'}\nDefault is [0]")
    if int(val) == 0:
        print("you selected: " + val)
        sequence_format = ['Latitude(deg)', 'Longitude(deg)', 'H_Ell(m)']
        reorder_csv(pos, sequence_format, 'lan_first_pos.csv')
    if int(val) == 1:
        print("you selected: " + val)
        sequence_format = ['Longitude(deg)', 'Latitude(deg)', 'H_Ell(m)']
        reorder_csv(pos, sequence_format, 'lon_first_pos.csv')


def reorder_csv(pos, sequence_format, csv_name):
    reordered_pos = pos[sequence_format]
    reordered_pos.to_csv(csv_name, index=False)


def input_pos_file():
    file_path = input('Enter a file path: ')
    print(file_path)
    if os.path.exists(file_path):
        print('The file exists')
        with open(file_path, 'r', encoding='utf-8-sig'):
            pos_extract(file_path)
    else:
        print('The specified file does NOT exist')


if __name__ == '__main__':
    input_pos_file()
