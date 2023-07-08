import os

cwd = os.getcwd()

complete_list = os.listdir(cwd)
files_list = [i for i in complete_list if os.path.isfile(i) and '.py' not in i]

#retornando as extensões
types = list(set([i.split('.')[1] for i in files_list]))

for file_type in types:
    os.mkdir(file_type)
    
for file in files_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split('.')[-1], file)
    
    os.replace(from_path, to_path)
