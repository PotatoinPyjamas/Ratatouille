from flask import Flask, json, jsonify, request
import pandas as pd

data = pd.read_csv("indian_food.csv")
data.dropna(inplace=True)

data["ingredients"] = data["ingredients"].str.split(",")

app = Flask(__name__)

score = []
index_list = []

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def check(list):
  for i in data['ingredients']:
    len_intersected = len(intersection(i,list))
    len_of_product = len(i)
    diff = len_of_product - len_intersected
    score.append(diff)

def iter(var):
  for i in range(len(score)):
    if score[i] == var:
      index_list.append(i)

check(['Gram flour', 'ghee', 'sugar'])

iter(0)
iter(1)
iter(2)
iter(3)
iter(4)

d = []
for i in range(3):
    d.append(data['name'][index_list[i]])
json_d=json.dumps(d)


@app.route('/', methods=['GET', 'POST'])
def values():
    if request.method == 'POST':
        response = request.get('https://ratatouille-spaag.herokuapp.com/')
        k = response.json()
        return k
    elif request.method == 'GET':
        return json_d


if __name__ == '__main__':
    app.debug = True
    app.run()
