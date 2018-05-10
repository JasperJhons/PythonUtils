# -*- coding: utf-8 -*-

import csv
import os
import sys


class android_ids_checker(object):
    def __init__(self):
        self.r_file = sys.argv[1]
        self.android_csvs_dir = sys.argv[2]
        self.all_ids_from_r_file = []
        self.all_changes_counter = 0

    def check_locators(self):
        self.get_ids_from_rfile()
        self.get_ids_from_csv_files()
        print("*Всего изменений*")
        print(self.all_changes_counter)

    def get_ids_from_rfile(self):
        r_file_data = open(self.r_file).read()
        r_file_data = r_file_data.replace("public static final int ", "").split("\n")
        for line in r_file_data:
            if "=" in line:
                self.all_ids_from_r_file.append(line.split("=")[0].strip())

    def get_ids_from_csv_files(self):
        for file in os.listdir(self.android_csvs_dir):
            if "WebView" not in file:
                with open(self.android_csvs_dir + file, "r", encoding="utf-8") as csv_page:
                    all_ids_locators_from_csv = []
                    reader = csv.reader(csv_page)
                    row_counter = 1
                    for row in reader:
                        if row[2] is not "" and row_counter > 2:
                            all_ids_locators_from_csv.append([row[0], row[2]])
                        row_counter += 1
                    self.check_locators_in_current_csv(file, all_ids_locators_from_csv)

    def check_locators_in_current_csv(self, file, all_ids_locators):
        matches = 0
        result = "*" + file + "* : \\n "
        for id in all_ids_locators:
            if id[1] not in self.all_ids_from_r_file and id[1] != []:
                result += "*" + id[0] + "*" + " : " + id[1] + "\\n"
                matches += 1
        if matches > 0:
            self.all_changes_counter += matches
            print(repr(result))


if __name__ == "__main__":
    android_ids_checker().check_locators()
