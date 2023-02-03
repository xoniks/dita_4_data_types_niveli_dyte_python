import glob, os
# from pathlib import Path

# p = Path(__file__)
# # os.chdir("/data")

# print(os.chdir('data/'))

os.chdir('data/')
empt_list = []
for file in glob.glob("*.csv"):
    print(str(file))
    data = open(file)
    for element in data.readlines():
        empt_list.append(element)

print(empt_list)
with open('new_file.txt', mode='w') as new_file:
    
    for i in empt_list:
        new_file.write(i+'\n')
    
    
