lines = ['Welcome to file handling, Mounika!!']
with open('data.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

more_lines = ['welcome to data file,here we do some operations on file']
with open('data.txt', 'a+') as f:
    f.write('\n'.join(more_lines)+'\n')
    f.seek(0)
    data=f.read()
    print(data)