# Json-Subset
Since the dataset we have contains a huge amount of duplicates (12M records with only 1.5M unique) and massive size of 29.6GB, we needed to write a code that generates a new dataset with only the unique applications and the features we need.
This code takes the unique records from the first 1M records which will end up by 370K unique records.
You can use this code to generate a JSON file that contains all the unique records by removing the lines 52 and 54.
Link to the original dataset: https://drive.google.com/file/d/10xudbVaIIQT3mQiwvuljQJpnu7J1oOrr/
