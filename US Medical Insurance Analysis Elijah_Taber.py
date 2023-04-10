#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
U.S. Medical Insurance Cost Analysis 

By: Elijah Taber
Date: March 23, 2023

The purpose of this project is to analyze a relatively large csv data set that contains a few details on hundreds of client's in a 
medical insurance file. This csv file is based on real clients at a medical insurance company. As a data scientist, the job
here is to take this large csv file and determine what information is most useful/relavent to whichever goal is trying
to be attained. The way I am going about this project is analyzing the data from the point of view of a client, so I will be
doing data analytics on what I think is the most useful information for what a typical client would want to know about their 
insurance costs. Since this csv file is a real file, the client names are confidential, which means that I will not be able
to pick out a specific client and analyze their information, this will be more generalized. This will only be using python
(and the csv module for importing the file) to calculate and analyze basic information about a csv file.
"""

import csv

# First, let's open up the csv file to see what we are working with

with open('insurance.csv') as insurance_costs:
    # Remove # in front of print to see the whole csv list
    #print(insurance_costs.read())
    total_clients = 0
    # Let's iterate through each client in the list and add them to a variable to get the total amount of clients
    for client in insurance_costs:
        total_clients += 1
    print("The total amount of clients in this medical insurance file is " + "\x1B[4m" + str(total_clients) + "\x1B[0m" " clients.")
    csv_dict = csv.DictReader(insurance_costs)


# In[17]:


# Initialize an empty list for each column in the csv file in order to create workable python lists
ages = []
sexes = []
bmis = []
number_of_children = []
smoker_status = []
regions = []
insurance_charges = []

# Creates a function that goes through a specified column in the csv file and appends it to its own list
def insurance_data_file(insurance_csv_file, client_list, col_name):
    with open(insurance_csv_file) as insurance_file:
        csv_dict = csv.DictReader(insurance_file)
        for row in csv_dict:
            # Takes the specifified data from each row and adds it to a list that will be called in the function
            client_list.append(row[col_name])
        return client_list
    
insurance_data_file('insurance.csv', ages, 'age') # Column 1
insurance_data_file('insurance.csv', sexes, 'sex') # Column 2
insurance_data_file('insurance.csv', bmis, 'bmi') # Column 3
insurance_data_file('insurance.csv', number_of_children, 'children') # Column 4
insurance_data_file('insurance.csv', smoker_status, 'smoker') # Column 5
insurance_data_file('insurance.csv', regions, 'region') # Column 6
insurance_data_file('insurance.csv', insurance_charges, 'charges') # Column 7


# In[36]:


"""
1) Average insurance cost for Smokers vs Non-smokers
"""

# Average insurance cost for someone who smokes:

# Creates an isolated list of the two colums we want to address, smoker_status and insurance_charges
smoker_insurance_cost = list(zip(smoker_status, insurance_charges))

# Initialize variables that the loops will add to and analyze
total_smokers = 0
list_of_smokers = []
total_cost_for_smokers = 0

# Loop through the new list that was created and check to see if the index is a smoker or not, then add up each smoker
for client in smoker_insurance_cost:
    for smoker in client:
        if smoker == 'yes':
            total_smokers += 1
            # Adds each smoker to a new list in order to have an isolated list of smokers and their cost
            list_of_smokers.append(client) 

# Take the list of just smokers and add up the total cost of all smokers            
for client in list_of_smokers:
    for cost in client:
        if cost != 'yes':
            total_cost_for_smokers += float(cost)

# Calculates the average cost of a smoker            
average_cost_for_smokers = total_cost_for_smokers / total_smokers


# In[37]:


# Average insurance cost for someone who does not smoke:

total_non_smokers = 0
list_of_non_smokers = []
total_cost_for_non_smokers = 0

for client in smoker_insurance_cost:
    for smoker in client:
        if smoker == 'no':
            total_non_smokers += 1
            list_of_non_smokers.append(client)

for client in list_of_non_smokers:
    for cost in client:
        if cost != 'no':
            total_cost_for_non_smokers += float(cost)

average_cost_for_non_smokers = total_cost_for_non_smokers / total_non_smokers


# In[60]:


print("The average cost for a smoker is: " + str(average_cost_for_smokers))
print("The average cost for a non smoker is: " + str(average_cost_for_non_smokers))
print("The average cost for a smoker is " + str(round(average_cost_for_smokers / average_cost_for_non_smokers, 4)) + " times the cost of an average non smoker!")


# In[55]:


"""
2) Average insurance cost for Males vs Females
"""

# Average insurance cost for a male

# This is going to be almost identical to exercise 1 except we are using the 'sexes' list instead of 'smoker_status' list
sexes_insurance_cost = list(zip(sexes, insurance_charges))

total_males = 0
list_of_males = []
total_cost_for_males = 0

for client in sexes_insurance_cost:
    for sex in client:
        if sex == 'male':
            total_males += 1
            list_of_males.append(client)
            
for client in list_of_males:
    for cost in client:
        if cost != 'male':
            total_cost_for_males += float(cost)
            
average_cost_for_males = total_cost_for_males / total_males


# In[56]:


# Average insurance cost for a female

total_females = 0
list_of_females = []
total_cost_for_females = 0

for client in sexes_insurance_cost:
    for sex in client:
        if sex == 'female':
            total_females += 1
            list_of_females.append(client)
            
for client in list_of_females:
    for cost in client:
        if cost != 'female':
            total_cost_for_females += float(cost)
            
average_cost_for_females = total_cost_for_females / total_females


# In[68]:


print("The average insurance cost for a male is: $" + "\x1B[4m" + str(round(average_cost_for_males, 2)) + "\x1B[0m")
print("The average insurance cost for a female is: $" + "\x1B[4m" + str(round(average_cost_for_females, 2)) + "\x1B[0m")
difference = round(average_cost_for_males - average_cost_for_females, 2)
print("The average cost for a male is $" + "\x1B[4m" + str(difference) + "\x1B[0m" + " more than the average cost for females!")

