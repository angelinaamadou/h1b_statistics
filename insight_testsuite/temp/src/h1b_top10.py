#https://github.com/InsightDataScience/h1b_statistics

## list files in folder
import glob
import sys

for name in glob.glob('./*'):
    print(name)


### Helper functions
def read_file(filename):
    with open(filename,'r',encoding="utf-8") as f:
        lines = [line.rstrip('\n').split(';') for line in f]
    return lines

def save_file(data,headers, filename):
    with open(filename, 'w') as f:
        f.writelines(headers)
        f.writelines("\n")
        f.writelines("%s;%s;%s\n" % (line[0],line[1],line[2]) for line in data)

    
## Filter dataset according to a key word
def select_data(lines, indices, word):
    lines = [line  for line in lines if  word in line]
    new_lines = [[line[i] for i in indices] for line in lines]
    return new_lines



## Bubble sort for two fields in descending order
def sort_by_two(lines):
    for i in range(0,len(lines)):
        flag=False
        for j in range(0, len(lines)-(i+1)):
            if lines[j][1] < lines[j+1][1]:
                temp = lines[j+1]
                lines[j+1] = lines[j]
                lines[j] = temp
                flag = True 
            if lines[j][1] == lines[j+1][1]:
                if lines[j][0] >lines[j+1][0]:
                    temp = lines[j+1]
                    lines[j+1] = lines[j]
                    lines[j] = temp
                    flag = True 
    if not flag:
            return lines
    return lines



## Select unique attributes
def get_unique_words(lines, index):
    total = []
    for line in lines:
        single = line[index]
        if single not in total:
            total.append(single)
        else:
            continue
    return total


## select column header  with key word
def find_index(line, words):
    index = None
    for i in range(0, len(line)):
        num_words = len(words)
        if num_words ==1:
            if words[num_words - 1] in line[i]:
                index = i
                return index
            else:
                continue
        else:
            while(num_words > 0):
                if words[num_words - 1] in line[i]:
                    num_words-=1
                else:
                    break
            if num_words ==0:
                index = i
            else:
                continue
            
    if index != None:
        return index
    return 'Not Found' 



## Compute total for each key word
def get_total(lines,index, word):
    total = 0
    for line in lines:
        if word in line[index]:
            total+=1
        else:
            continue
    return total

## Retrieve the top n elements for a particular column
def get_top_n(data, index,n):
    words = get_unique_words(data,index)
    total_words = [[word,get_total(data, index,word)] for word in words]
    top_n = sort_by_two(total_words)[:n]
    top_n = [[top_n[i][0],top_n[i][1],"{0:.1%}".format(top_n[i][1]/len(data))]  for i in range(len(top_n))]
    return top_n

## check for duplicate names
def remove_duplicate(data, index):
    for i in range(len(data)-2):
        if data[i][index] in data[i+1][index]:
            counter = 1
            
            while(data[i][index] in data[i+counter][index]):
                counter+=1
            if i+counter< len(data)-1:
                data[i][index] = data[i+counter-1][index]
            else:
                data[i][index] = data[len(data)-1][index]
        else:
            continue
    return data



## Get file from command line or provide input file
filename =  sys.argv[1]
lines = read_file(filename)

## Preprocessing data
line_names = lines[0]
col_names = [['STATUS'],['SOC_NAME'],['WORK','STATE']]
word = "CERTIFIED"
## Find indices  for filtering data
indices = [find_index(line_names, words) for words in col_names]
## filter data to desired rows
certified = select_data(lines, indices, word)

## check for STATES , special characters and empty fields
certified = [[certified[i][0],certified[i][1].strip('"'), certified[i][2].strip()] for i in range(len(certified)) 
               if len(certified[i][1])!= 0 and len(certified[i][2])== 2 ]


## Since there are duplicates  values  select more than the desired number and clean the output by removing the duplicate entries.
top10_occupations = get_top_n(certified,1,100)
top10_occupations = remove_duplicate(top10_occupations, 0)

## Select the desired number of elements
total_occupation = [ ]
occupations = get_unique_words(top10_occupations,0)
for occupation in occupations:
    num_occupation = select_data(top10_occupations,[0,1], occupation)[0]
    total_occupation.append([num_occupation[0],num_occupation[1],"{0:.1%}".format(num_occupation[1]/len(certified))])
    
top10_occupations=total_occupation[:10]
print(top10_occupations)

## Get top 10 states 
top10_states = get_top_n(certified,2,10)
print(sort_by_two(top10_states))


states_headers =["TOP_STATES;" "NUMBER_CERTIFIED_APPLICATIONS;", "PERCENTAGE"]
occupations_headers = ["TOP_OCCUPATIONS;","NUMBER_CERTIFIED_APPLICATIONS;","PERCENTAGE"]

## Provide filename for output
if len(sys.argv) >3:
    filename1 = sys.argv[2]
    filename2 = sys.argv[3]
else:
    filename1 = 'top_10_states.txt'
    filename2 = 'top_10_occupations.txt'

save_file(top10_states,states_headers,filename1 )
save_file(top10_occupations,occupations_headers, filename2)

