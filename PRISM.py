# 'importing the file'
import csv

Values = []
Features = []

with open('data_heart.csv', 'r') as fp:
    csv_reader = csv.reader(fp)
    for line in csv_reader:
        Values.append(line)

    Features.append(Values[0])
    del (Values[0])

print('Features=', Features)
row = len(Values)
print('row in the file=', row)
key = len(Features[0])
print('Features=', key)
T = []
R = []

k = 0
# 'putting each feature and its values in a list--this list is not unified'
while k != key:
    for j in range(k, k + 1):
        for item in Values:
            if item[j] not in T:
                T.append(item[j])
        R.append(T)
    k = k + 1
    T = []

m = 0
Value_sets = []
unique_Value_sets = []
fixed_data = []
A = []
Probability_values = []
maximum = 0
c = key - 1
dic1 = {}  # 'value:probability'
DIC1 = {}  # 'value:number of values'
# 'getting the fixed data'
for i in range(c, key):
    for item in Values:
        if item[i] not in fixed_data:
            fixed_data.append(item[i])
print('fixed data is=', fixed_data)
# 'counting probability and number of values in each pair feature and making a Dictionary'
while m < c:

    for j in range(m, m + 1):
        for item in Values:
            Value_sets.append(item[j])
            unique_Value_sets = []
        for item in Values:
            if item[j] not in unique_Value_sets:
                unique_Value_sets.append(item[j])

        for k in unique_Value_sets:

            count = 0
            # 'p is the number of a value compare to last column'
            p = 0
            for i in range(len(Value_sets)):
                if k == Value_sets[i]:
                    count = count + 1

            DIC1[k] = count

            for i in range(row):
                for j in range(c):

                    if Values[i][j] == k and Values[i][c] == '<50':
                        p = p + 1

            A.append(k)

            probability = p / count
            Probability_values.append(probability)

            dic1[k] = probability

        Value_sets = []
    m = m + 1

# ' make dic1 into tuples'
H = list(dic1.items())

# 'finding highest probability and first_Value:'
for i in range(len(H)):
    for j in range(1, 2):
        if H[i][j] > maximum:
            maximum = H[i][j]

first_value = H[i][0]

# 'finding which feature the first_value belongs to:'
for i in range(len(R)):
    for j in R[i]:
        if j == first_value:
            target_column = i

first_feature = Features[0][target_column]
# 'make a list where first_value and the fixed data meet'
new_list = []

for i in range(len(Values)):
    for j in range(len(Values[0])):
        if Values[i][j] == first_value:
            new_list.append(Values[i])

# 'counting probability and number of values in each pair feature and making a Dictionary'

m = 0
Value_sets = []
unique_Value_sets = []
fixed_data = []
A = []
Probability_values = []
maximum = 0
c = (len(new_list[0])) - 1
dic1 = {}  # 'value:probability'
DIC1 = {}  # 'value:number of values'

while m < c:

    for j in range(m, m + 1):

        for item in new_list:
            Value_sets.append(item[j])

            unique_Value_sets = []

        for item in new_list:
            if item[j] not in unique_Value_sets:
                unique_Value_sets.append(item[j])

        for k in unique_Value_sets:

            count = 0
            # 'p is the number of a value compare to last column'
            p = 0
            for i in range(len(Value_sets)):
                if k == Value_sets[i]:
                    count = count + 1
            p = 0
            DIC1[k] = count
            for i in range(len(new_list)):

                for j in range(len(new_list[0])):

                    if new_list[i][j] == k and new_list[i][c] == '<50':
                        p = p + 1

                    probability = p / count
                    Probability_values.append(probability)

                    dic1[k] = probability
        Value_sets = []
    m = m + 1

# ' make dic1 into tuples'
H = list(dic1.items())
# 'delete the first value from H'
for i in range(len(H)):
    for j in range(1):
        if H[i][j] == first_value:
            del H[i]

# 'finding highest probability and second_value:'
for i in range(len(H)):
    for j in range(1, 2):
        if H[i][j] > maximum:
            maximum = H[i][j]

second_value = H[i][0]

# 'finding which feature the first_value belongs to:'
for i in range(len(R)):
    for j in R[i]:
        if j == second_value:
            target_column = i

Second_feature = Features[0][target_column]
# 'make the second list where it has second_value'
second_list=[]
for i in range(len(new_list)):
    for j in range(len(new_list[0])):
        if new_list[i][j]==second_value:
            second_list.append(new_list[i])


# 'make a list where first_value and the fixed data meet'
m = 0
Value_sets = []
unique_Value_sets = []
fixed_data = []
A = []
Probability_values = []
maximum = 0
c = (len(second_list[0])) - 1
dic1 = {}  # 'value:probability'
DIC1 = {}  # 'value:number of values'

while m < c:

    for j in range(m, m + 1):

        for item in second_list:
            Value_sets.append(item[j])

            unique_Value_sets = []

        for item in second_list:
            if item[j] not in unique_Value_sets:
                unique_Value_sets.append(item[j])

        for k in unique_Value_sets:

            count = 0
            # 'p is the number of a value compare to last column'
            p = 0
            for i in range(len(Value_sets)):
                if k == Value_sets[i]:
                    count = count + 1
            p = 0
            DIC1[k] = count
            for i in range(len(second_list)):

                for j in range(len(second_list[0])):

                    if second_list[i][j] == k and second_list[i][c] == '<50':
                        p = p + 1

                    probability = p / count
                    Probability_values.append(probability)

                    dic1[k] = probability
        Value_sets = []
    m = m + 1

# ' make dic1 into tuples'
H = list(dic1.items())

# 'delete the first value  and second value from H'
for i in range(len(H)):
    for j in range(1):
        if H[i][j] == first_value:
            del H[i]
for i in range(len(H)):
    for j in range(1):
        if H[i][j] == second_value:
            del H[i]

# 'finding highest probability and third_value:'
for i in range(len(H)):
    for j in range(1, 2):
        if H[i][j] > maximum:
            maximum = H[i][j]
third_value = H[i][0]

# 'finding which feature the third_value belongs to:'
for i in range(len(R)):
    for j in R[i]:
        if j == third_value:
            target_column = i

Third_feature = Features[0][target_column]


Third_list=[]
for i in range(len(second_list)):
    for j in range(len(second_list[0])):
        if second_list[i][j]==third_value:
            Third_list.append(second_list[i])

print(Third_list)
# 'make a list where first_value and second value and third value and the fixed data meet'
m = 0
Value_sets = []
unique_Value_sets = []
fixed_data = []
A = []
Probability_values = []
maximum = 0
c = (len(Third_list[0])) - 1
dic1 = {}  # 'value:probability'
DIC1 = {}  # 'value:number of values'

while m < c:

    for j in range(m, m + 1):

        for item in Third_list:
            Value_sets.append(item[j])

            unique_Value_sets = []

        for item in Third_list:
            if item[j] not in unique_Value_sets:
                unique_Value_sets.append(item[j])

        for k in unique_Value_sets:

            count = 0
            # 'p is the number of a value compare to last column'
            p = 0
            for i in range(len(Value_sets)):
                if k == Value_sets[i]:
                    count = count + 1
            p = 0
            DIC1[k] = count
            for i in range(len(Third_list)):

                for j in range(len(Third_list[0])):

                    if Third_list[i][j] == k and Third_list[i][c] == '<50':
                        p = p + 1

                    probability = p / count
                    Probability_values.append(probability)

                    dic1[k] = probability
        Value_sets = []
    m = m + 1

# ' make dic1 into tuples'
H = list(dic1.items())

# 'delete the first value  and second value and third value from H'
for i in range(len(H)):
    for j in range(1):
        if H[i][j] == first_value:
            del H[i]
for i in range(len(H)):
    for j in range(1):
        if H[i][j] == second_value:
            del H[i]
for i in range(len(H)):
    for j in range(1):
        if H[i][j] == third_value:
            del H[i]
# 'finding highest probability and forth_value:'
for i in range(len(H)):
    for j in range(1, 2):
        if H[i][j] > maximum:
            maximum = H[i][j]
forth_value = H[i][0]

# 'finding which feature the forth_value belongs to:'
for i in range(len(R)):
    for j in R[i]:
        if j == forth_value:
            target_column = i

forth_feature = Features[0][target_column]
print(forth_feature,forth_value)
print('if',first_feature,'=',first_value,'and',
      'if',Second_feature,'=',second_value,'and',
      'if',Third_feature,'=',third_value, 'and',
      'if',forth_feature,'=',forth_value, 'then num <50')