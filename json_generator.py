"""
This code takes the huge json file and takes a subset of its data and store them in a new json file.
In order to run the code,
1) Download the data set from this link,
	https://drive.google.com/file/d/10xudbVaIIQT3mQiwvuljQJpnu7J1oOrr/
2) Decompress the 7z file and recompress it in gz format.
3) Put the gz file beside the file of this code in the same folder and then run the program.
"""

import gzip
import json
import pandas as pd
i = 0
# a list that will hold the bulks
# acti
fillo = open('apps_sub.json','w')
raw_apps={}
with gzip.open('scrapy01.json.gz','rt') as f:
    for line in f:
        i=i+1
        #if any line is not an application. such as the first line "["
        if len(line)<10:
            continue
        clean_line = line.replace("\'", "")
        #removing the comma from the end of documents
        clean_line = clean_line[0:-2]
        try:
            #converting the json string to a dict
            clean_line = eval(clean_line)
            # making sure no missing data is being stored
            if len(clean_line['Title'])==0 or len(clean_line['ReviewsAverage'])==0:
                continue
            #creating objects with the needed fields
            url=clean_line["Url"].split("&")[0]
            title=clean_line["Title"][0]
            description=' '.join(clean_line["Description"])
            store_rating=float(clean_line["ReviewsAverage"][0])
            app = {
                "url":url,
                "title":title,
                "description":description,
                "store_rating":store_rating
            }
            #inserting data for bulks
            if app["url"] not in raw_apps.keys():
                raw_apps[app["url"]]=1 
                json_object = json.dumps(app)
                fillo.write(json_object)
                fillo.write("\n")
        except:
            None
        if i==1000000:
            break
fillo.close()
print(len(raw_apps))
