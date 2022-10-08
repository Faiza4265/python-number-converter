import pandas as pd #import pandas inorder to put the result in a dataframe

list1=[]

for i in range (0,6): #create a loop using for loop for reciving input of grade result from a user
    x=int(input())
    list1.append(x)
list1


def funk(list1): #create a function that returns the mathimathical formula or equation we want to apply 
    return list1*40/30
    
    
result=list(map(funk,list1)) #then mapping the input list with the mathimathical formula function for new result
     
x={ "input": list1, "converted": result 
                     }     

put_dataframe=pd.DataFrame(data=x) # create a dataframe inorder to display the result in a more visible way
put_dataframe # at the end print out the result






