"""
cse6242 s22
wrangling.py - utilities to supply data to the templates.

This file contains a pair of functions for retrieving and manipulating data
that will be supplied to the template for generating the table. """
import csv
import http.client
import json

def username():
    return 'csowers3'

def data_wrangling():
    with open('data/movies.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        table = list()
        # Feel free to add any additional variables
        ...
        
        # Read in the header
        for header in reader:
            break
        
        i=0
        # Read in each row
        for row in reader:
            if i < 100:
                table.append(row)
            i+=1
            
            # Only read first 100 data rows - [2 points] Q5.a
            ...
        
        # Order table by the last column - [3 points] Q5.b
        table.sort(key=lambda row: (float(row[2])), reverse=True)
    
    return header, table    

def rating_wrangling():
    with open('data/average-rating.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        data = list()
        for row in reader:
            data.append(row)
    
    return data    

def get_actor(actor):
    conn = http.client.HTTPSConnection("api.themoviedb.org")

    reqstr = "/3/person/" + actor + "/movie_credits?api_key=" + 'e4dd2fa8ad747256f4ca5e940ec79700'

    conn.request("GET", reqstr)
    r1 = conn.getresponse()
    data1 = r1.read().decode('utf-8')
    filtcast = json.loads(data1)['cast']
    
    return filtcast    
