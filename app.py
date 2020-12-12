from flask import Flask, jsonify, request

app = Flask(__name__)
lst1 = ['Milk', 'Sugar', 'Ghee']
lst2 = ['Milk', 'Sugar']
lst3 = []
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
'''for i in range(2):
    temp = input()
    lst3.append(temp)'''

@app.route('/', methods=['GET', 'POST'])
def values():
    d = {}
    d = intersection(lst1, lst2)
    return jsonify(d)


if __name__ == '__main__':
    app.debug = True
    app.run()
