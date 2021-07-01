#%%
#import relevant libraries 
import pandas as pd 
from sqlalchemy import create_engine 
import numpy as np
import json
import csv
#%%

class VeteranDataCleaning:
    '''Cleans all the data, converting numbers to int, dates to datetime objects, categorical data is similarly assiged, and all is dumped in csv'''
    def __init__(self):
        self.vet_df = pd.read_json('soldier_data.json')
        self.veteranDictionary = {}
    def int_convert(self):
        self.vet_df['age_at_death'] = self.vet_df['age_at_death'].str.replace(r'\D','').astype(int)

    def datetime_convert(self):
        '''converts to datetime object, then returns to string format since JSON is not serializable'''
        self.vet_df['date_of_birth'] = pd.to_datetime(self.vet_df['date_of_birth'], format="%m/%d/%Y")
        self.vet_df['start_of tour'] = pd.to_datetime(self.vet_df['start_of tour'], format="%m/%d/%Y", errors='coerce')
        self.vet_df['date_of_death'] = pd.to_datetime(self.vet_df['date_of_death'], format="%m/%d/%Y", errors='coerce')
        
        self.vet_df['date_of_birth'] = self.vet_df['date_of_birth'].astype(str)
        self.vet_df['start_of tour'] = self.vet_df['start_of tour'].astype(str)
        self.vet_df['date_of_death'] = self.vet_df['date_of_death'].astype(str) 
        
    def categorical_convert(self):
        self.vet_df['service_branch'] = self.vet_df['service_branch'].astype('category')
        self.vet_df['hometown'] = self.vet_df['hometown'].astype('category')
        self.vet_df['soldier_rank'] = self.vet_df['soldier_rank'].astype('category')
        self.vet_df['military_occupational_speciality_code'] = self.vet_df['military_occupational_speciality_code'].astype('category')
        self.vet_df['unit'] = self.vet_df['unit'].astype('category')
        self.vet_df['location_of_death'] = self.vet_df['location_of_death'].astype('category')
        self.vet_df['remains_status'] = self.vet_df['remains_status'].astype('category')
        self.vet_df['casualty_type'] = self.vet_df['casualty_type'].astype('category')
        self.vet_df['casualty_reason'] = self.vet_df['casualty_reason'].astype('category')
        self.vet_df['casualty_detail'] = self.vet_df['casualty_detail'].astype('category')
    def clean_csv_dump(self):
        self.vet_df.to_csv('/Users/Tareq/Desktop/VietnamWar/cleaned_soldier_data.csv')
    def jsonDump(self):
        self.veteranDictionary = self.vet_df.to_dict(orient='records')         
        with open('cleaned_soldier_data.json', 'w') as f:
            json.dump(self.veteranDictionary, f, indent=4)    


#%%        
Vetclean = VeteranDataCleaning()
#%%
Vetclean.int_convert()
#%%
Vetclean.datetime_convert()
#%%
Vetclean.categorical_convert()
#%%
Vetclean.jsonDump()
#%%
veteranDictionary = 
#%%
type(Vetclean.vet_df.to_dict)
#%%
Vetclean.vet_df
#%%
dict(veteranDictionary)
#%%
with open('cleaned_soldier_data.json', 'w') as f:
    json.dump(veteranDictionary, f, indent=4)    

#Vetclean.vet_df.to_csv('/Users/Tareq/Desktop/VietnamWar/cleaned_soldier_data.csv')




# %%
