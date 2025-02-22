# Solution README
## Run Program
The program can be run by using cmd (or another terminal) by navigating to the folder in which the main.py file is stored and typing python main.py. If requested by the assignment, the program can be compiled and run as a batch file or similar to avoid any cmd navigation.

# Description of the solution provided
The solution provided consists of 2 python files: main.py and a readWriteFile.py. This would allow for future programs that require similar readWriteFile functionality to import the readWriteFile.py file. Within the main.py file, functions have been provided to split the work out in clear and appropriate chunks as per the work required. Pandas library has been used for the data manipulation and storage throughout the program as it is a powerful and open-source Python library for data manipulation and analysis. Pandas consist of data structures and functions to perform efficient operations on data. It is a good fit for the assignment provided, where there may be a dataset that does not fit in memory, PySpark can be utilised for this.

# Key Components
Files
    
    Modules
        
        Imports

main.py
   
    racesDateTime
    racesDataManipulation
    main
        
        import pandas as pd
        import readWriteFile as readWriteFile

readWriteFile.py
    
    readFile(file):
    writeFile
        
        import csv
        import json, os
        import pandas as pd

# List of requirements that you have met
The Core requirements of the assignment have been met as required for the Core Data Engineering application. Cloud Provider considerations have also been noted below as to what changes would be required before deploying to the Cloud, and advice on best practice for ongoing use of the program. 

Developed a data pipeline that produces JSON files which have the same structure as provided.
Each element in the JSON list is for one race from the races.csv file.
One file per year produced in the results folder.
JSON files have the correct naming convention and are placed in the results folder
Where the timewas not available in races.csv, nulls have been replaced with 00:00:00
Winning driver was determined by position 1 in results.csv converted to integer to remove decimal places
JSON Values remain as their provided variable type

# Any supporting documentation that you have provided
Within the results folder, the results json files have been written from years 2018-2024.

# Stretch Requirements - Deploying to Cloud Provider
There are some considerations to make for the current solution to be deployed to a cloud solution. The current code is written to be specific to reading a csv with the provided file path and write a file back to a specific file path. Code changes would be required to read and write to a new location and could be written in a way which allows for more flexability and scalability. 

Also, currently the is a single file for all races and all results, whereas as written in the README, it may make sense to have multiple files per race so that the program would only process the new race information as to not create duplicated processing for each run. This would also require the write file to check for an existing file and append the new results to the results file per race per year. This would allow for an on-going/ continuous process going forward rather than today's requirement of 

Based on the above, AWS would be a suitable cloud provider to deploy this type of functionality. Code can be deployed to AWS Lambda for serverless running that can be completed within 15 minutes as per Lambda restrictions. Future files to be written can be stored within AWS S3, which would allow for easy file reading and writing within AWS. Step Functions can be used to set up a regular scheduler if appropriate depending on Formula 1 schedule or event based triggers can be set up watching for a file upload to S3 before triggering the program to run.