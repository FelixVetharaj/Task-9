# Task-9-Question-2-Lambda function to check every element in list is integer or string

# def find(lists):
#     newLists=[]
#     for i in lists:
#         if(type(i) == int):
#             newLists.append("Int")
#         else:
#             newLists.append("Str")
#     return newLists                

lists = [10, "felix", 20, "Jane", "Jianna"]

l = filter(lambda x: type(x)==int, lists) 
s = filter(lambda x: type(x)==str, lists)
    
print("Integer in list is:",list(l))
print("String in list is:",list(s))
