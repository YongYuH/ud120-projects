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

# print "total people in enron dataset", len(enron_data)

# print "total features in enron dataset", len(enron_data.itervalues().next())

sum = 0
for v in enron_data.itervalues():
    if v['poi']:
        sum += 1
print 'sum of poi', sum

# print "dataset of a person: ", enron_data.itervalues().next()


# for index, value in enumerate(enron_data.iterkeys()):
#     print index+1, value


# print enron_data.get('PRENTICE JAMES')
# print "James Prentice's total stock value is: ", enron_data['PRENTICE JAMES']['total_stock_value']

# print "Wesley Colwell's from this person to poi is: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# print enron_data.get('SKILLING JEFFREY K')
# print "Jeff Skilling's exercised stock options is: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']


# print "Ken Lay's total payments is: ", enron_data['LAY KENNETH L']['total_payments']
# print "Jeff Skilling's total payments is: ", enron_data['SKILLING JEFFREY K']['total_payments']
# print "Andrew Fastow's total payments is: ", enron_data['FASTOW ANDREW S']['total_payments']

# sumOfS = 0
# sumOfE = 0
# for v in enron_data.itervalues():
#     if v['salary'] != "NaN":
#         sumOfS += 1
#     if v['email_address'] != "NaN":
#         sumOfE += 1
# print 'sum of quantified salary', sumOfS, ', and sum of known email address', sumOfE

# totalPaymentsNaN = 0
# for v in enron_data.itervalues():
#     if v['total_payments'] == "NaN":
#         totalPaymentsNaN += 1
# print 'totalPaymentsNaN is: ', totalPaymentsNaN


totalPaymentsNaNOfPOI = 0
for v in enron_data.itervalues():
    if v['total_payments'] == "NaN" and v['poi']:
        totalPaymentsNaNOfPOI += 1
print 'totalPaymentsNaNOfPOI is: ', totalPaymentsNaNOfPOI