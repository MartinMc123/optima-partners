# Imports
import pandas as pd
import readWriteFile as readWriteFile

"""
This program reads the files 'races.csv' and 'results.csv' from source-data into pandas DataFrames, completes several DataFrame manipulations and
writes JSON files to the 'datapipeline/results' file path with the required output as specified in the overall program README 
"""

# This function takes a DataFrame with a time and date column, fills time nulls with 00:00:00 and merges the columns into a Timestamp column
def racesDateTime(df):
    # Fill null time values with specified time 00:00:00
    df['time']=df['time'].fillna('00:00:00')

    # Merge date and time and convert to timestamp as required by README Specifications
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%dT%H:%M:%S.000')
    return df

# The function takes a DataFrame of races, and merges columns to add the winning driver ID of each race and the fastest lap of each place
def racesDataManipulation(races_df):
    # Call readFile function from readWriteFile module to read results csv.
    results_df = readWriteFile.readFile(r"C:\dev\Git\engineering-recruitment-assignments\data-engineering\datapipeline\source-data\results.csv")

    # Call function racesDateTime to merge Columns 'date' and 'time' into one timestamp Column
    races_df=racesDateTime(races_df)

    # Create a winners DataFrame based on position = 1 from the results DataFrame, 
    # Then merge with races DataFrame based on race ID to provide a winning Driver ID per race
    winners_df = results_df[results_df['position'] == 1]
    races_df = pd.merge(races_df, winners_df[['raceId', 'driverId']], on='raceId', how='left')

    # Create duplicate results DataFrame with fastest lap nulls removed for the purpose of finding the fastestLapTime without error
    results_df_fast_lap_nulls_removed = results_df.dropna(subset=['fastestLapTime'])

    # Create a fastest lap DataFrame by grouping fastest lap by race ID and then finding the minimum fastest lap
    fastest_lap_df = results_df_fast_lap_nulls_removed.loc[results_df_fast_lap_nulls_removed.groupby('raceId')['fastestLapTime'].idxmin()]

    # Merge into races DataFrame the fastest lap time per race id on race id
    races_df = pd.merge(races_df, fastest_lap_df[['raceId', 'fastestLapTime']], on='raceId', how='left')

    # Convert driver ID to int to remove decimal places using Int64 to handle Null Values
    races_df['driverId']= races_df['driverId'].astype('Int64')

    # Rename specific columns for writing to json files as required by the README Specifications
    races_df = races_df.rename(columns={
        'name': 'Race Name',
        'round': 'Race Round',
        'datetime': 'Race Datetime',
        'driverId': 'Race Winning driverId',
        'fastestLapTime': 'Race Fastest Lap',
    })

    return races_df

def main():
    
    # Call readFile function from readWriteFile module to read races csv.
    races_df = readWriteFile.readFile(r"C:\dev\Git\engineering-recruitment-assignments\data-engineering\datapipeline\source-data\races.csv")

    # Call function racesDateTime to merge Columns 'date' and 'time' into one timestamp Column
    races_df=racesDateTime(races_df)

    # Call function racesDataManipulation to complete the required data manipulation to join races and results for fastest lap and winning driver id
    races_df=racesDataManipulation(races_df)
 
    # Call module readWriteFile, function writeFile, to pass the dataframe to be written to json file in datapipeline/results folder 
    readWriteFile.writeFile(races_df)
    
if __name__ == "__main__":
  main()