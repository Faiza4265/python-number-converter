import pandas as pd

list1=[]

for i in range (0,6):
    x=int(input())
    list1.append(x)
list1


def funk(list1):
    return list1*40/30
    
    
result=list(map(funk,list1))  
     
x={ "input": list1, "converted": result
                     }     

put_dataframe=pd.DataFrame(data=x)
put_dataframe

