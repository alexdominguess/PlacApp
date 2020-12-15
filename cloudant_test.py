import json

datadic = {'teste': 'teste'}
with open('teste.json') as file:
    data = json.load(file)

data.append(datadic)

with open('teste.json', 'w') as file:
    json.dump(data, file)

print(data)