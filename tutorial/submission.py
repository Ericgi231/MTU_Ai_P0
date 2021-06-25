# submission.py
# ----------------
# Attribution Information: This part of the project was adapted from CS221 and 
# the PacMan Projects. 
# For the PacMan Projects: 
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# 08-2020
 

from __future__ import print_function
import math 
import collections
from re import split
import shop


############################################################
# Question 1 - addition 

def add(a, b): 
    "Return the sum of a and b"
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    return a + b
    # END_YOUR_CODE


############################################################
# Question 2 - buyLotsOfFruit 
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order. If some fruit is not in list, print an error 
    message and return None.
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    fruitFound = 0
    for purchase in orderList:
        fruitFound = 0
        for fruit, price in fruitPrices.items():
            if purchase[0] == fruit:
                fruitFound = 1
                totalCost += price * purchase[1]
        if fruitFound == 0:
            print(purchase[0],"not for sale.")
            return None
    return totalCost
    # END_YOUR_CODE


############################################################
# Question 3 - shopSmart 

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops

    Return the FruitShop where your order costs the least.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    bestShop = fruitShops[0]
    bestShopPrice = fruitShops[0].getPriceOfOrder(orderList)
    for shop in fruitShops:
        if shop.getPriceOfOrder(orderList) < bestShopPrice:
            bestShop = shop
            bestShopPrice = shop.getPriceOfOrder(orderList)
    return bestShop
    # END_YOUR_CODE


############################################################
# Question 4 - findAlphabetLastWord 

def findAlphabetLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(text.split())
    # END_YOUR_CODE


############################################################
# Question 5 - euclideanDistance 

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt(math.pow(loc1[0]-loc2[0],2) + math.pow(loc1[1]-loc2[1],2))
    # END_YOUR_CODE


############################################################
# Question 6 - findSingletonWords

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    If no singleton words exist return the emptyset.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    uniqueWords = []
    for word1 in text.split():
        occurences = 0
        for word2 in text.split():
            if word1 == word2:
                occurences += 1
        if occurences == 1:
            uniqueWords.append(word1)
    return set(uniqueWords)
    # END_YOUR_CODE


############################################################
# Question 7 - lenLongestPalindrome

def lenLongestPalindrome(text): 
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana'). 
    Computer the length of the longest palindrome that can be obtained by 
    deleting letters from text. 
    Do not try a brute force approach on this function.  Your algorithm should 
    run in O(len(text)^2) time. 
    Consider defining a recurrence before you begin coding. 
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE 

    #really threw in a curve ball for this last one
    n = len(text) #length of word for use through the algorithm
    table = [[0 for i in range(n)] for j in range(n)] #initialize empty 2D array, thanks stack overflow for this method of doing it rather than my nested append for loops

    #fill diagonal with 1, representing the fact that each letter on its own is a palindrome of size 1
    for i in range(n):
        table[i][i] = 1

    #typicall run through and fill in upper triangular by adding 2 if matching letters found or taking max of neighbors if no match
    for i in range(2,n+1): #substring length
        for j in range(n - i + 1): #start point
            k = j + i - 1 #end point
            if text[j] == text[k] and i == 2:
                table[j][k] = 2
            elif text[j] == text[k]:
                table[j][k] = table[j+1][k-1] + 2
            else:
                table[j][k] = max(table[j][k-1],table[j+1][k])
    
    #the final value in the triangle will be the largest value found
    return table[0][n-1]
    #END_YOUR_CODE    


############################################################
#  Extra Functions you may want to define