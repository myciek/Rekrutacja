import json, re

with open('json_data.json') as file:
    data = json.load(file)

as_text = json.dumps(data)
numbers = re.findall(r'[-+]?[0-9]+', as_text)
sum = 0

for num in numbers:
    sum += int(num)

file = open("answers.txt","a+")
file.write("Sum of all numbers in document is {}.".format(sum))
