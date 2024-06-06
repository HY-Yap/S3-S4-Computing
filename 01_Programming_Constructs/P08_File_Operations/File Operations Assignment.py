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

basedir = os.path.abspath(os.path.dirname(__file__))

# transfer data into dictionary
data_file_name = os.path.join(
    basedir, "assignment_data_files/country_animals.txt")
with open(data_file_name, "r") as f:
    raw_data = {}
    line_counter = 0
    for line in f:
        if line_counter % 2 == 0: # to read every alternate line
            country = line[line.find('<')+1:line.find('>')]
        else:
            while ';' in line: # while line is not empty
                animal = line[0:line.find(';')]

                # update raw_data
                if animal in raw_data:
                    if country not in raw_data[animal]:
                        raw_data[animal].append(country)
                else:
                    raw_data[animal] = [country]

                line = line[line.find(';')+1:] # slice off animal
        line_counter += 1

# sort dictionary keys alphabetically
my_keys = list(raw_data.keys())
my_keys.sort()
sorted_data = {i: raw_data[i] for i in my_keys}

# sort values alphabetically
for animal in sorted_data:
    sorted_data[animal].sort()

# write data to new txt file
data_file_name = os.path.join(
    basedir, "assignment_data_files/results.txt")
with open(data_file_name, "w") as f:
    for animal in sorted_data:
        f.write(f"<{animal}>:{len(sorted_data[animal])}\n") # animal name
        f.write(";".join(sorted_data[animal]) + ';\n') # countries

# for more concise: use sets to prevent duplicate while adding country
# also can sort dictionary better
