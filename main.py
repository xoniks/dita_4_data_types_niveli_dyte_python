# import pathlib

import pathlib
from pathlib import Path

p = Path(__file__)
data_path = str(p.cwd())+'\data\\'

file_input = data_path+'data_input.csv'

try:
    data = open(file_input)
    
except  OSError:
    print("File not found!")
    


data_list = data.readlines()
data_range = len(data_list)
# print(data_range)
for i in range(1,data_range):
    print(i)
    row_read = data_list[i].split(',')
    email_read = row_read[2].split('@')
    try:
        domain_read = email_read[1]
        print(domain_read)
    except:
        print("Error line")
        
    



# with open('data/data_input.csv') as data:
    
#     print(data.readline())
