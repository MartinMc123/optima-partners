# Solution README
Add your solution documentation here

# Stretch Requirements

# Deploying to Cloud Provider
There are some considerations to make for the current solution to be deployed to a cloud solution. The current code is written to be specific to reading a csv with the provided file path and write a file back to a specific file path. Code changes would be required to read and write to a new location and could be written in a way which allows for more flexability and scalability. 

Also, currently the is a single file for all races and all results, whereas as written in the README, it may make sense to have multiple files per race so that the program would only process the new race information as to not create duplicated processing for each run. This would also require the write file to check for an existing file and append the new results to the results file per race per year. This would allow for an on-going/ continuous process going forward rather than today's requirement of 

Based on the above, AWS would be a suitable cloud provider to deploy this type of functionality. Code can be deployed to AWS Lambda for serverless running that can be completed within 15 minutes as per Lambda restrictions. Future files to be written can be stored within AWS S3, which would allow for easy file reading and writing within AWS. Step Functions can be used to set up a regular scheduler if appropriate depending on Formula 1 schedule or event based triggers can be set up watching for a file upload to S3 before triggering the program to run.