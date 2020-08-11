from random import sample
from node import Node

def kmeans_std(data,k):
    """Data is list of node objects"""
    centroids = {}
    s = sample(data,k)
    for i in range(len(s)):
        centroids[i] = s[i]
    
    for key in centroids:
        centroids[key].setValue('s')