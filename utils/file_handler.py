import os
import pandas as pd
import numpy as np

from params import folder_path
# 1. be kell adatbázis tölteni a file-ok tartalmát
#   minden file egy külön tábla legyen

# létre kell hoznunk a táblákat
#  táblák mezőire -> ezt elp kell állítnai
#  minden mezőnek egy adatbázis típust kell "osztanunk" -> dinamikusan meg kell vizsgálnom az adatot

# le kellene gyártani minden táblához egy insert into utasítást
# a futási logikát elő kellene állítani

class FileHandler:

    def __init__(self):
        self.table_name = None
        self.data_types = None

    def get_data_from_csv(self, file_path):
        return pd.read_csv(file_path)

    def get_files_list(self):
        return os.listdir(folder_path)

    def get_data_type(self, csv_data):
        # mapping - dataframe object = postgesql text
        cols_types = {}
        for key, value in csv_data.dtypes.to_dict().items():
            if value == 'object':
                cols_types[key] = "text"
            if value == 'int64':
                cols_types[key] = "int"
            if value == 'float64':
                cols_types[key] = "numeric"

            #print(f"{key} - {max(csv_data[key])}")

        return cols_types

    def create_table_script(self):
        create_table = f"create table if not exists {self.table_name} ("
        for key, value in self.data_types.items():
            create_table += f"{key} {value}, \n"

        create_table += "creation_date date default now() )"
        return create_table

    def create_insert_script(self):
        insert_script = f"insert into {self.table_name} "
        insert_cols = "("
        insert_values = " values ("
        for idx, key in enumerate(self.data_types.keys()):
            test = "%s"
            # if len(data_types) - 1 > idx:
            #     insert_cols += f"{key}, "
            # else:
            #     insert_cols += f"{key})"
            insert_cols += f"{key}, " if len(self.data_types) - 1 > idx else f"{key})"
            insert_values += f"%s, " if len(self.data_types) - 1 > idx else f"%s)"

        insert_statement = insert_script + insert_cols + insert_values
        return insert_statement


if __name__ == '__main__':
    handler = FileHandler()

    file_list = handler.get_files_list()

    for item in file_list:
        file_path = os.path.join(folder_path, item)
        data = handler.get_data_from_csv(file_path)

        # create table script előállítása
        """create table tábla_neve (mezo1 mezo_adattipus)"""
        handler.table_name = item[:-4]
        # típusosítás
        handler.data_types = handler.get_data_type(data)

        create_table = handler.create_table_script()
        insert_script = handler.create_insert_script()

        print(create_table)
        print('-------------')
        print(insert_script)
        print("##########################################")
        

        