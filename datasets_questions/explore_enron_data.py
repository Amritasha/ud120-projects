#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)

for key,value in enron_data.items():
    print key
    print len(value)

count=0
for key,value in enron_data.items():
    if enron_data[key]["poi"]==1:
        count = count+1

print count

for value in enron_data["PRENTICE JAMES"]:
    print value, enron_data["PRENTICE JAMES"][value]

print "Welsey to poi mails"
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

for value in enron_data["COLWELL WESLEY"]:
    print value, enron_data["COLWELL WESLEY"][value]

print "jeffrey exercised stock options" , enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "payment to lay" ,enron_data["LAY KENNETH L"]["total_payments"]

print
cnt =0
for key,value in enron_data.items():
    if enron_data[key]["salary"] != 'NaN':
        cnt=cnt+1

print "salary not present ", cnt

print
cnt =0
for key,value in enron_data.items():
    if enron_data[key]["email_address"]!= 'NaN':
        cnt=cnt+1
print "email not present", cnt

