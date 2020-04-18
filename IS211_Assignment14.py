# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:25:22 2020

@author: kathy
"""

#PART I: FIBONACCI SEQUENCE

#REFERENCE: ORIGINAL START FUNCTION FROM LINK: https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

"""Exception to base:
    -First value is always 0 (n = 0)
    -Second value is always 1 (n = 1)
    -Third value is always 1 (n = 2)

All else follows base formula"""

def Fibonacci(n): 
    if n==1 or n==2: 
        return 1        
    else: 
        #BASE CASE
        return Fibonacci(n-1)+Fibonacci(n-2) 

x = 10
print("Fibonacci Answer for %s: %s" % (x, Fibonacci(x)))

print('\n')
#PART II: 

def gcd_non_recursive(a, b):
    while b: # Shorthand for is False or 0
        a, b = b, a % b
    return a
        
def gcd(a, b):  
    if a == 0 : 
        return b  
    else:  
        return gcd(b%a, a)

a, b = 1071, 462

print("With Loop (Non-Recursive): %s" % (gcd_non_recursive(a, b)))
print("With If/Else (Recursive): {%s}" % gcd(a, b))


print('\n')

#PART III:
    
def compareTo(s1, s2):
    if s1 == s2:
        return 0
    else: 
        return len(s1) - len(s2)
    
s1 = "doggo"
s2 = "spaghetti"

print("compareTo() Example #1")
print("Length of s1 (%s): %s" % (s1, len(s1)))
print("Length of s2 (%s): %s" % (s2, len(s2)))
print(compareTo(s1, s2))

s1 = "pad thai"
s2 = "sushi"
print('\n')
print("compareTo() Example #2")
print("Length of s1 (%s): %s" % (s1, len(s1)))
print("Length of s2 (%s): %s" % (s2, len(s2)))
print(compareTo(s1, s2))