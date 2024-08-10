'''
Country Animal

1) Study the content and format of "country_animals.txt" file carefully. It consists a list of animals available in a particular country. (data randomly generated, not based on real world distribution)

The number on the right of the country name indicates the total number of animals available in that country. The animal lists are recorded in another line.

2) Take note that the file consists of unprocessed raw data, which means there might be same animal appearing more than once in a country.

3) You are to read the input from "country_animals.txt" and process the data to remove duplicates. 

Instead of categorizing by countries in the original file, you should now categorize all data by animals now, followed by a row of countries that this animal can be found.

4) Sort the clean data according to alphabetical order for animals and for countries that the animals live in.

You should use list.sort() method for now, we will be learning sorting algorithms in details in future chapters.

Store the sorted data into a text file named "results.txt". You may analyse the file "expected_results.txt" to check the expected output and its format.

5) check_result() is a helper function to check if the "results.txt" produced has exact same content and format as the expected results. 

This function has already been implemented at the back end, you do not need to re-implement this function.

---------------------------------------------
'''
import os

def bubble_sort(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        j = i - 1
        while j >= 0 and curr < lst[j]:
            j -= 1
        lst.pop(i)
        lst.insert(j+1, curr)
    return lst

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def merge(lst_a, lst_b):
    lst_c = []
    while len(lst_a) > 0 and len(lst_b) > 0:
        lst_c.append(lst_a.pop(0) if lst_a[0] < lst_b[0] else lst_b.pop(0))
    return lst_c + lst_a + lst_b

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        return merge(sorted_left, sorted_right)

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left, right = [], []

        for item in lst[1:]:
            if item <= pivot:
                left.append(item)
            else:
                right.append(item)
        
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return sorted_left + [pivot] + sorted_right


basedir = os.path.abspath(os.path.dirname(__file__))

file = os.path.join(basedir, "assignment_data_files/country_animals.txt")
with open(file, "r") as f:
    line = f.readline()
    animal_country_dict = {}
    while line:
        # get country name
        country = line[line.find('<')+1:line.find('>')]
        # print(country)

        # get animal names
        line = f.readline()
        animal_lst = line.strip(";\n").split(";")
        # print(animal_lst)

        # add animal names to dict as key
        # add country names as items (set)
        for animal in animal_lst:
            if animal in animal_country_dict:
                animal_country_dict[animal].add(country)
            else:
                animal_country_dict[animal] = set([country])

        # read next line
        line = f.readline()

# print(animal_country_dict)

file = os.path.join(basedir, "assignment_data_files/results.txt")
with open(file, "w") as f:
    # sort animals alphabetically
    animal_lst = quick_sort(list(animal_country_dict.keys()))
    # print(animal_lst)

    # add sorted animals one by one
    for animal in animal_lst:
        f.write("<{}>:{}\n".format(animal, len(animal_country_dict[animal])))
        # country set -> sorted list
        country_lst = bubble_sort(list(animal_country_dict[animal]))
        # add sorted countries
        f.write(";".join(country_lst) + ";\n")
