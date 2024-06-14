import pandas as pd
from astropy.table import Table, vstack, hstack, join, unique
from astropy.io import fits
from astropy.time import Time
import numpy as np
import fitsio
from datetime import datetime
from dateutil import parser
from multiprocessing import Pool
from tqdm import tqdm
import sys, os, warnings, time

##########################
# KEY WORD (change for different iterations)
kw = '1'
#########################

# Load each file as a pandas df
def get_cleandf(file):
    folder_path = '/global/cfs/projectdirs/desi/users/sgontcho/mirror_temp/telemetry_data/'
    file_path = folder_path + file + '.pkl'
    df = pd.read_pickle(file_path)
    return df.dropna(axis=0)

tcs = get_cleandf('tcs_info')
print('\nGrabbed tcs_info.pkl\n')
environment_tower = get_cleandf('environmentmonitor_tower')
print('Grabbed environmentmonitor_tower.pkl\n')
environment_telescope = get_cleandf('environmentmonitor_telescope')
print('Grabbed environmentmonitor_telescope.pkl\n')

# Define a function to round each timestamp to the nearest 10 minutes
def round_10M(index_value): # returns the night (in MJD) that a time in time_recorded belongs to, taking into account noon to noon being one observing day
    string = str(index_value)
    rounded = string[2:15]+':0.000000000'
    return rounded
##################################################################################################
pbar = tqdm(total=os.cpu_count())

def process_row(index_value):
    pbar.update(1)
    return round_10M(index_value)

##################################################################################################

df = tcs
df_name = 'tcs'
print('Rounding times for:', df_name)

if __name__ == "__main__":
    # Number of processes to use
    num_processes = os.cpu_count()

    # Create a multiprocessing pool with the specified number of processes
    with Pool(num_processes) as pool:
        # Apply the process_row function to each index value using the pool
        rounded_times = pool.map(process_row, df.index.values)

    # Store the results in a new DataFrame, assuming nights is a list of tuples containing start and end times
    rounded_times_df = pd.DataFrame(rounded_times, columns=['rounded_time'], index=df.index)

# Output DataFrame with calculated nights
fits_table = Table.from_pandas(rounded_times_df)
fits_table.write('rounded_times'+df_name+kw+'.fits', format='fits', overwrite=True)
print('Finished rounding times for '+df_name+', writing to file as rounded_times_df'+df_name+kw+'.fits')
##################################################################################################
df = environment_tower
df_name = 'environment_tower'
print('Rounding times for:', df_name)

if __name__ == "__main__":
    # Number of processes to use
    num_processes = os.cpu_count()

    # Create a multiprocessing pool with the specified number of processes
    with Pool(num_processes) as pool:
        # Apply the process_row function to each index value using the pool
        rounded_times = pool.map(process_row, df.index.values)

    # Store the results in a new DataFrame, assuming nights is a list of tuples containing start and end times
    rounded_times_df = pd.DataFrame(rounded_times, columns=['rounded_time'], index=df.index)

# Output DataFrame with calculated nights
fits_table = Table.from_pandas(rounded_times_df)
fits_table.write('rounded_times'+df_name+kw+'.fits', format='fits', overwrite=True)
print('Finished rounding times for '+df_name+', writing to file as rounded_times_df'+df_name+kw+'.fits')
##################################################################################################

df = environment_telescope
df_name = 'environment_telescope'
print('Rounding times for:', df_name)

if __name__ == "__main__":
    # Number of processes to use
    num_processes = os.cpu_count()

    # Create a multiprocessing pool with the specified number of processes
    with Pool(num_processes) as pool:
        # Apply the process_row function to each index value using the pool
        rounded_times = pool.map(process_row, df.index.values)

    # Store the results in a new DataFrame, assuming nights is a list of tuples containing start and end times
    rounded_times_df = pd.DataFrame(rounded_times, columns=['rounded_time'], index=df.index)

# Output DataFrame with calculated nights
fits_table = Table.from_pandas(rounded_times_df)
fits_table.write('rounded_times'+df_name+kw+'.fits', format='fits', overwrite=True)
print('Finished rounding times for '+df_name+', writing to file as rounded_times_df'+df_name+kw+'.fits')