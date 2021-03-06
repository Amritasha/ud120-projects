#!/usr/bin/python

import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    error = (net_worths - predictions)**2
    #print error
    cleaned_data = zip(ages, net_worths, error)
    cleaned_data.sort(key=lambda x:x[2])
    n = len(cleaned_data)
    del cleaned_data[ - (int(0.1*n)):]
    print len(cleaned_data)
    return cleaned_data

