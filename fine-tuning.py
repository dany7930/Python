import re


def sum_numbers_in_file(filename):
  
    with open(filename, 'r') as file:
        text = file.read()


    numbers = re.findall(r'[0-9]+', text)

    numbers = [int(num) for num in numbers]

   
    total_sum = sum(numbers)

    return total_sum

sample_file = 'regex_sum_42.txt'  
actual_file = 'regex_sum_2150633.txt'  


sum_actual_data = sum_numbers_in_file(actual_file)


print(f"The sum of the numbers in the actual data file is: {sum_actual_data}")