from random import sample
from node import Node

def kmeans_std(data,k):
    """Data is list of node objects"""
    centroids = sample(data,k)

    #Fronteir is all nodes that weren't selected as centroids
    fronteir = [i for i in data if i not in centroids]

    #set selected centroids as selected value.
    for centroid in centroids:
        centroid.setValue('s')


    #possible simple implementation (testing puroses only)
    #PSEUDOCODE
    #create fronteir containing all non-centroid nodes
    #create list of children for each centroid
    #while len(fronteir) > 0
    #   for each centroid
    #       add nearest node to list of children
    #       remove that node from the fronteir
    #   
    #