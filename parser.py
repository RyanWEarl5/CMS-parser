from os.path import join, exists
from datetime import datetime
import urllib.request
import pandas as pd
import numpy as np
import shutil
import json
import sys
import os

class Parser:

    def __init__(self, url, fields, quarters):
        self.url = url
        self.fields = fields
        self.quarters = {k:self.url+r"/"+v+r"/data" for k,v in quarters.items()}

    def request(self):
        """ read data from url to object in class """
        self.file, self.order = [], []
        try:
            for k, v in self.quarters.items():
                with urllib.request.urlopen(v) as f:
                    self.file.append(json.loads(f.read()))
                    self.order.append(k)
        except urllib.error.URLError as e:
            print(e.reason)

    def printReq(self):
        """ print returned JSON output from request """
        try:
            if self.file:
                print(self.file)
            else:
                print("Data has not yet been read to file")
        except Exception as e:
            print(e.message, e.args)

    def checkFields(self):
        """ verify fields match api format """
        d = self.file[0][0]
        removal = []
        for pos in range(len(self.fields)):
            field = self.fields[pos]
            if field not in d.keys():
                print(f"{field} not found in request output keys! removing from request")
                removal.append(pos)  
        for pos in removal:
            self.fields.pop(pos)
        
    def filterDicts(self):
        """ fitler down list of dictionaries to only desired fileds from input """
        if self.fields:
            # revised dictionary filter with checks for field values
            self.dictionaries = []
            for quarter in self.file:
                quarter_list = []
                for target_dict in quarter:
                    new_dict = {}
                    target_keys = target_dict.keys()
                    for key in self.fields:
                        if key in target_keys:
                            new_dict[key] = target_dict[key]
                        else:
                            new_dict[key] = np.nan
                    quarter_list.append(new_dict)
                self.dictionaries.append(quarter_list)
        else:
            sys.exit("No matching fields to filter on")

    def newFolder(self, dir_, name):
        """ create new folder in given directory with given name, delete folder tree if exists """
        try: 
            folder = join(dir_, name)
            if exists(folder):
                shutil.rmtree(folder)
                os.mkdir(folder)
            else:
                os.mkdir(folder) 
        except OSError as error: 
            sys.exit(error)
            
        return folder

    def outputData(self, output_dir):
        """ Write output data to csv files in given output location """
        out_folder = self.newFolder(output_dir,f"Hospital-data_{datetime.today().strftime('%Y-%m-%d')}")
        for date, quarter in zip(self.order, self.dictionaries):
            pd.DataFrame(quarter).to_csv(join(out_folder, f"{date}.csv"))
