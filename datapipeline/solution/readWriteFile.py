# Imports
import csv
import json, os
import pandas as pd

"""
readFile function takes a variable of the path and filename of a csv file and returns a pandas dataframe
"""
def readFile(file):
    # Exception handling for Files not found or other Exceptions
    try:
        # Reads file provided and turns csv into pandas DataFrame
        df = pd.read_csv(file)
   
    except FileNotFoundError:
        print("Error: The file was not found.")
    except csv.Error as e:
        print(f"Error: There was a problem reading the CSV file. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Returns DataFrame
    return df

"""
writeFile function takes a pandas dataframe, looks for the unique years within the year column of the dataframe,
and writes a json file per year to the file path datapipeline/results
"""
def writeFile(df):
    # Extract all unique years from the 'year' column
    years = df['year'].unique()
    
    # Iterate through years
    for year in years:

        # Filter the DataFrame for the current year
        filtered_df = df[df['year'] == year]
        # Create new DataFrame to only include required columns for the output file
        newdf=filtered_df[['Race Name','Race Round','Race Datetime','Race Winning driverId','Race Fastest Lap']] 
        # Translate the DataFrame to list as required by the README Specs
        year_data_list = newdf.to_dict(orient='records')
              
        # Checks     
        if year_data_list:
            # Write filtered DataFrame to a JSON file for that year
            subfolder = 'datapipeline/results'

            # Checks if the required subfolder exists and if not creates the folder
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)

            # Builds the filename with iterated year and filepath together to write to the correct location
            filename = f'stats_{year}.json'
            file_path = os.path.join(subfolder, filename)

            # Error handling for writing file
            try:
                with open(file_path, 'w') as json_file:
                    json.dump(year_data_list, json_file, indent=4)
            except Exception as e:
                print(f"Error writing file {filename}: {e}")        
        else:
            print(f"No races found for the year {year}.")