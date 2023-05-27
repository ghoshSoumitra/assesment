Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135]

ans--

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example usage
arr = [5, 416, 54, 21, 6135, 15, 741]
sorted_arr = selection_sort(arr)
print(sorted_arr)

# output
[5, 15, 21, 54, 416, 741, 6135]


Q2. Dictionary, what?
Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs
E.g.
f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]) should return
{
"abc.jpg": "image",
"xyz.xls": "spreadsheet",
"Text.csv": "unknown",
"123": "unknown"
}

ans--

def get_file_type(extension_type_string, filenames):
    extension_type_pairs = extension_type_string.split(';')
    extension_type_dict = {}
    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        extension_type_dict[extension] = file_type

    result_dict = {}
    for filename in filenames:
        extension = filename.split('.')[-1]
        file_type = extension_type_dict.get(extension, 'unknown')
        result_dict[filename] = file_type

    return result_dict

extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_type(extension_type_string, filenames)
print(result)

# output
{
"abc.jpg": "image",
"xyz.xls": "spreadsheet",
"Text.csv": "unknown",
"123": "unknown"
}


Q3. Column Sorting, yay!

Given a list of dicts, write a program to sort the list according to a key given in input.
E.g.
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")
Should Output
[
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"}
]
AND
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "color")
Should Output
[
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"}
]

ans--
def sort_list_of_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

# Example usage
input_list = [
    
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}

]
key = "color"

output_list = sort_list_of_dicts(input_list, key)
print(output_list)

# output
[{'fruit': 'blueberry', 'color': 'blue'}, 
          {'fruit': 'orange', 'color': 'orange'}, 
          {'fruit': 'apple', 'color': 'red'}, 
          {'fruit': 'banana', 'color': 'yellow'}]




Q4. The power of one line -
Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
key becomes value. The function's body shouldn't have more than one statement.
f({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}) should return
{
"value1": "key1",
"value2": "key2",
"value3": "key3",
"value4": "key4",
"value5": "key5"
}
ans--

def switch_key_value(dictionary):
    return {v: k for k, v in dictionary.items()}

# Example usage
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

output_dict = switch_key_value(input_dict)
print(output_dict)

# output

{'value1': 'key1',
 'value2': 'key2', 
 'value3': 'key3', 
 'value4': 'key4', 
 'value5': 'key5'}


Q5. Common, Not Common
Given 2 lists in input. Write a program to return the elements, which are common to both
lists(set intersection) and those which are not common(set symmetric difference) between the
lists.
Input:
Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death
Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
On Titan"]
f(mainstream, must_watch) should return:
["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
"One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

ans--

def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    uncommon_elements = list(set(list1) ^ set(list2))

    return common_elements, uncommon_elements

# Example usage
mainstream = [
    "One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online",
    "Bleach", "Dragon Ball Z", "One Piece"
]
must_watch = [
    "Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate",
    "The Devil is a Part Timer!", "One Piece", "Attack On Titan"
]

common, uncommon = compare_lists(mainstream, must_watch)
print(common)
print(uncommon)

# output
['Attack On Titan', 'One Piece']
['The Devil is a Part Timer!',
  'Code Geass', 
  'Death Note',
    'Bleach', 
    'Sword Art Online', 
    'Dragon Ball Z', 
    "Stein's Gate", 
    'One Punch Man',
      'Full Metal Alchemist']



Q6. Every other sub-list
Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
contain every second element.
E.g.
Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
Return [5, 11, 17, 23]

ans--

def get_sublist(lst, start, end):
    return lst[start:end:2]

# Example usage
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

sublist = get_sublist(input_list, start_index, end_index)
print(sublist)

# output 
[5, 11, 17, 23]


Q7. Calculate the factorial of a number using lambda function.
ans--

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Test
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")
# output
The factorial of 5 is: 120




Q8. Some neat tricks up her sleeve:
Looking at the below code, write down the final values of A0, A1, ...An
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])
                                  
ans--
The value of A0 will be a dictionary with the keys 'a', 'b', 'c', 'd', 'e' mapped to the values 1, 2, 3, 4, 5, respectively. So, A0 will be {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.

The value of A1 will be a range object representing numbers from 0 to 9. So, A1 will be range(0, 10).

A2 will be a sorted list containing elements from A1 that are also present as keys in A0. In this case, A2 will be [1, 2, 3, 4, 5] because these values exist as keys in A0.

A3 will be a sorted list containing the values from A0, sorted by the keys. In this case, A3 will be [1, 2, 3, 4, 5] because the keys ('a', 'b', 'c', 'd', 'e') are sorted alphabetically.

A4 will be a list containing elements from A1 that are also present in A3. In this case, A4 will be [1, 2, 3, 4, 5] because these values exist in both A1 and A3.

A5 will be a dictionary with keys from A1 and corresponding values equal to the square of the keys. So, A5 will be {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}.

A6 will be a list of lists, where each inner list contains two elements: the number itself and its square. So, A6 will be [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]].


The reduce function applies the lambda function (in this case, addition) cumulatively to the elements of the given list. In this example, it will perform the following operations:

Step 1: 10 + 23 = 33
Step 2: 33 + (-45) = -12
Step 3: -12 + 33 = 21
So, the final output will be 21

A8 will [2, 4, 6, 8]
The map function applies the lambda function (doubling the value) to each element in the list [1, 2, 3, 4]. The resulting values are returned as a list.

A9 will be  ['want', 'learn', 'python']
The filter function filters out elements from the given list based on the length condition (length greater than 3). Only the strings 'want', 'learn', and 'python' have lengths greater than 3, so they are returned as a list.



Q9.
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days away from each other, else
returns False.

ans--
from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert string dates to datetime objects
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference in days
    delta = to_date - from_date

    # Check if the difference is less than the specified number of days
    if delta < timedelta(days=difference):
        return True
    else:
        return False

# Test
from_date = '21-05-15'
to_date = '21-05-20'
difference = 7

result = check_date_difference(from_date, to_date, difference)
print(result)

# output
True


Q10. Of date and days
Write a func that takes 2 args:
date - string representing a date in the form of 'yy-mm-dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16-12-10', 11) should return '16-11-29'


ans--

from datetime import datetime, timedelta

def get_previous_date(date, n):
    # Convert string date to datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting timedelta
    previous_date = date_obj - timedelta(days=n)

    # Convert the datetime object back to string representation
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str

# Test
date = '16-12-10'
n = 11

result = get_previous_date(date, n)
print(result)

# output
16-11-29


Q11. Something fishy there -
Find output of following:
def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
f(2)
f(3,[3,2,1])
f(3)

ans--

output of the code
f(2)=[0, 1]
f(3, [3, 2, 1])=[3, 2, 1, 0, 1, 4]
f(3)=[0, 1, 0, 1, 4]
In this code, the function f takes two arguments: x and l. The default value of l is an empty list []. When the function is called multiple times without explicitly passing a value for l, the same list is used and modified.

In the given code snippet:

f(2) is called, and it appends [0, 1] to the default list and prints it.
f(3, [3, 2, 1]) is called, and it appends [0, 1, 4] to the provided list [3, 2, 1] and prints it.
f(3) is called again without providing a value for l, so it continues using the modified default list from the previous calls. It appends [0, 1, 4] to the existing list and prints it.