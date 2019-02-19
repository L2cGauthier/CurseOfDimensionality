# -*- coding: utf-8 -*-
"""
An illustration of the so-called "curse of dimensionality"

""" 

#_____________________________________________________
#IMPORTS

from math import sqrt
from random import random
from matplotlib import pyplot as plt
from sys import stdout
"""
sys.stdout is only used for the loading percentage when generating a long list of distance between pairs
of random vectors
"""

#_____________________________________________________
#FUNCTION TOOLBOX

def AverageListElt(l):
    """
    Returns the average of a list of numerical values, here representing a vector of dimension len(l).
    """
    buffer = 0
    for i in range(0,len(l)):
        buffer += float(l[i]) 
    return buffer/len(l)

def EuclideanDistance(v1,v2):
    """
    Returns the distance between to Euclidean Vectors (v1 and v2). For this application,
    we assume that v1 and v2 are vectors of the same dimension.
    """
    if len(v1)==len(v2):
        sumSquaredBuffer = 0
        for i in range(len(v1)):
            sumSquaredBuffer += (v1[i]-v2[i])**2
        return sqrt(sumSquaredBuffer)       
    else:
        raise Exception("The 2 vectors passed don't have the same dimension ("+str(len(v1)) + " & "+str( len(v2))+")")


def MinimumEltList(l):
    """
    Returns the smallest element of a list.
    """
    minValue = float(l[0])
    for index,elt in enumerate(l):
        if float(elt)<minValue:
            minValue = float(elt)
    return minValue


def RandomVectorGenerator(d):
    """
    Generate a random euclidean vector of dimension d which coordinates
    are uniformely distributed in [0,1].
    """
    randomVector = []
    for i in range (0,d):
        randomVector.append(random())
    return randomVector

def DistanceRandomPairs(d, num_pairs):
    """
    Generate a list of distance of num_pairs pairs of random vectors of dimension d,
    which coordinates are uniformely distributed in [0,1]. As a consequence, 
    the length of the list it returns is num_pairs.
    """
    distancePairs = []
    for i in range(0,num_pairs):
        distancePairs.append(EuclideanDistance(RandomVectorGenerator(d), RandomVectorGenerator(d)))
    return distancePairs


#_____________________________________________________
#ACTUAL SCRIPT

if __name__ == "__main__":
    
    maxDimension = 100
    numberOfPairs = 10000
    
    averageDistance = []
    minimumDistance = []
    ratioDistance = []
    
    """
    Then, we iterate through spaces of dimension 1 to maxDimension.
    For each of these spaces, we compute the smallest and the average distance between random vectors
    as well as the ratio of the 2 measures compare their variations when the number of dimension increases.
    """

    for i in range (1,maxDimension+1):
        l = DistanceRandomPairs(i,numberOfPairs)
        averageDistance.append(AverageListElt(l))
        minimumDistance.append(MinimumEltList(l))
        ratioDistance.append(minimumDistance[i-1]/averageDistance[i-1])
        
        #The 2 following lines allow us to keep track of the completion as it might take some time
        stdout.write("\rPercentage done : "+str(round(i/maxDimension*100, 4))+"%")
        stdout.flush()
        
    #We can now represent the minimum, average and ratio distance with respect to the dimension
    plt.plot(minimumDistance)
    plt.plot(averageDistance)
    plt.plot(ratioDistance)
    plt.ylabel("Distance")
    plt.xlabel("Dimension") 
    plt.title("Illustration of the curse of dimensionality")
    plt.legend(['Minimum distance', 'Average Distance', 'Minimum / average distance'], loc='upper left')
    plt.show()

