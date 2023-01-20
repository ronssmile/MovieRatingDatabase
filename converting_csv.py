import csv
import json

#from csv file to list of tuple
def convert_csv(file_name):
    with open(f"{file_name}","r") as f:
        reader = csv.reader(f)
        next(reader) # this will not include the header
        data1 = []
        for row in reader:
            data1.append(row)
        
        #convert list of list into list of tuple
        data = [tuple(x) for x in data1]
    return data


#converting csv to json
def csv_json(file_name,new_filename):
    with open(f"{file_name}.csv","r") as f:
        reader = csv.reader(f)
        next(reader) #to bypass or ignore header title
        jdata ={"reviewer_records":[]}
        for row in reader:
            jdata["reviewer_records"].append({"first_name":row[0], "last_name":row[1]})

    with open (f"{new_filename}.json","w") as f:
        json.dump(jdata,f,indent=4) 

