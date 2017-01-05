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

#####################################################################################
##### How many data points (people) are in the dataset?
len(enron_data) # 146

##### For each person, how many features are available?
len( enron_data["SKILLING JEFFREY K"].keys()) # 21

##### The “poi” feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
len( [1 for person in enron_data if enron_data[person]['poi'] ] ) # 18

##### What is the total value of the stock belonging to James Prentice?

[s for s in enron_data.keys() if "PRENTICE" in s] # ['PRENTICE JAMES']
enron_data['PRENTICE JAMES'].keys()
enron_data['PRENTICE JAMES']['total_stock_value'] # 1095040

##### How many email messages do we have from Wesley Colwell to persons of interest?
[s for s in enron_data.keys() if "WESLEY" in s] # ['COLWELL WESLEY']
enron_data['COLWELL WESLEY']['from_this_person_to_poi'] # 11

##### What’s the value of stock options exercised by Jeffrey Skilling?
[s for s in enron_data.keys() if "SKILLING" in s] # ['SKILLING JEFFREY K']
enron_data['SKILLING JEFFREY K']['exercised_stock_options'] # 19250000

##### Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? 
##### How much money did that person get?
execs = [s for s in enron_data.keys() if ("SKILLING" in s) or ("LAY" in s) or ("FASTOW" in s) ] 
max( [(enron_data[person]['total_payments'],person) for person in execs] ) # (103559793, 'LAY KENNETH L')

##### How many folks in this dataset have a quantified salary? What about a known email address?
len([enron_data[person]['salary'] for person in enron_data if enron_data[person]['salary'] != 'NaN']) # 95
len([enron_data[person]['email_address'] for person in enron_data if enron_data[person]['email_address'] != 'NaN' ] # 111

##### How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?

float(len([enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] == 'NaN' ]) ) / float( len( enron_data.keys() ) )*100. # 14.383561643835616

##### How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?

poi_names_f =  open("../final_project/poi_names.txt", "r")
poi_names = poi_names_f.readlines()
poi_names_f.close()
poi_names = poi_names[2:]
poi_names = [ name.split(' ',1)[1].strip('\n') for name in poi_names]
poi_names2 = [name.split(', ') for name in poi_names]
len(poi_names) # 35

len([ enron_data[person]['total_payments'] for person in enron_data if (enron_data[person]['poi']) ] # 18

##### If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change. 
##### What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?

len( [ enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] =='NaN' ] ) # 21 
len(enron_data) # 146

