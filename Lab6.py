#Author: Zulfiqar Ali
#Institution: University of the Fraser Valley
#Academic Session: Summer, 2021

#-------------------------------------------# Problem Analysis #-------------------------------------------#
#list of integers provided lst = [1; 4; 9; 16; 25; 28; 36; 33; 49; 64; 100; 81; 33]
#Step1 create function of odd-indexed elements
#     1.1 if the denominator == 1 it is odd
#                       return = it is odd 
#Step2 create function of even-indexed elements
#     2.1 if the denominator == 0 
#                       return = it is even
#Step3 use sum function of greaterSumList functions
#     3.1 if there is are no integers in the list print list is empty 
#      3.2 if sum of odd list or greater then even list or vice versa return oddlist or evenlist

#-------------------------------------------# End of Problem Analysis #-------------------------------------------#  

#Step1 and Step 1.1
def oddIndexedElements(lst1):#function to return odd indexed elements
  oddList = []
  size=len(lst1)
  for i in range(size):#iterating over lst1
    if (i%2 == 1):#if current index element is odd 
      oddList.append(lst1[i]) #add current element to odd list
  return oddList

#Step 2 and Step 2.1
def EvenIndexedElements(lst1):#function to return Even indexed elements
  evenList = []
  size=len(lst1)
  for i in range(size): #iterating over lst1
    if (i%2 == 0):#if current index element is even 
      evenList.append(lst1[i]) #add current element to even list

  return evenList

#Step 3 , Step 3.1 and Step 3.2
def greaterSumList(oddList,evenList):#function to find greater sum list
    #if (len(oddList)==0) and (len(evenList) == 0): #if list are empty return empty list if we have user input
    #return print("list is empty")
    if sum(oddList)>sum(evenList): #chechking sum of oddlist and evenlist
      return oddList
    else:
      return evenList

# to take inputs from ther user we can use this code segment and comment out the lst1 on line 56.
""" 
number = input("enter how many elements are in the list:")
number = int(number)
lst1 = []
for i in range(number):
  x = input("Enter the integers in the list:")
  x = int(x)
  lst1.append(x)  
"""

#print statements
lst1 = [1,4,9,16,25,28,36,33,49,64,100,81,33]
print("List:",lst1)
oddList = oddIndexedElements(lst1)
print("Odd Indexed Elements:",oddList)
evenList = EvenIndexedElements(lst1)
print("Even Indexed elements:", evenList)
print("The sum of odd indexed elemets is: ",sum(oddList))
print("The sum of even indexed elemets is: ",sum(evenList))
print("Greater sum list is:",greaterSumList(oddList,evenList))
