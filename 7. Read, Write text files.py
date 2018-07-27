################### READ FROM TEXT FILES ######################

#Absolute path
file = "D:\\Python Workspcae\\DemoPython\\sample.txt"
#Relative Path. finds the file in the location of the python program location
file = "sample.txt"

reader = open(file,'r')

for line in reader:
    print(line.lower(), end='') #end is used to eliminate newlinecharacter at end of each line from original file.

reader.close();

#smarter way of using file. this don't need explicit close()
with open(file,'r') as read_file:
    for line in read_file:
        print(line, end='')


#read line by line in traditional way of other languages
with open(file,'r') as read_file:
    line = read_file.readline()
    while line:
        print(line,end='')
        line = read_file.readline()


#read all lines at once. This will return a list of strings of all lines
with open(file,'r') as read_file:
    lines = read_file.readlines()
print(lines)

for items in lines[::-1]: #this will have a reverse loop of the files content
    print(items,end='')
    

#Use of strip() to eliminate extra new line

cities = [] #empty list
cities_other = []

with open(file,'r') as read_file:
    for line in read_file:
        cities.append(line.strip()) #strip() helps to remove starting and trailing character. Default '\n'
        cities_other.append(line.strip('\t')) #removes starting and trailing tabs

print(cities)

for city in cities:
    print(city)    


################### APPEND TO TEXT FILES ######################
## Note : Write works as same, only difference is if file is having contents it will be replaced
with open(file,'a') as append_file:
    for i in range(1,10):
        for j in range(1,10):
            print("{:4}    x {:4} = {:4}".format(i,j,i*j), file=append_file)
        print("-" * 25, file=append_file)



##########
# Writing a tuple into file and read from it again

print("=" * 40)
tup = (1, "A", ((1,"X"),(2,"Y")), "B")

with open(file,'w') as v_file:
    print(tup, file=v_file) #wrtie tuple to file


with open(file,'r') as v_file:
    contents = v_file.readline()

tup_cont = eval(contents) #convert tuple shaped string to tuple
print(tup_cont)

val1, val2, val3, val4 = tup_cont
print(val2)
print(val3)
        
