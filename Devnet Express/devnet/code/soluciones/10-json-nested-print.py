"""
Script #10 - JSON nested print.
"""

VAR = {
    "donut": {
        "flavors": [
            "chocolate",
            "jelley",
            "maple",
            "plain"
        ]
    }
}

print(VAR["donut"]["flavors"][0])
print("My favorite donut flavors are:", end=" ")

for flavor in VAR["donut"]["flavors"]:
    print(flavor, end=" ")

print()
print()

VAR1 = {
    "type": "donut",
    "flavors": {
        "flavor": [{
            "type": "chocolate",
            "id": 1001
        }, {
            "type": "glazed",
            "id": 1002
        }, {
            "type": "sprinkled",
            "id": 1003
        }]
    }
}

print(
    "Id: "
    + str(VAR1["flavors"]["flavor"][0]["id"])
    + " type: "
    + VAR1["flavors"]["flavor"][0]["type"]
)

for f in VAR1["flavors"]["flavor"]:
    print("Id: " + str(f["id"]) + " type: " + f["type"])

print()

print()

# 1. Imprimir todos los valores incluidos en los JSONs declarados.

VAR3 = {
    "exercise": {
        "high impact": [
            "running",
            "jumping",
            "jump rope",
            "running down stairs",
            "skiing"
        ]
    }
}

VAR4 = {
    "author": "Stephen King",
    "famous works": {
        "novels": [{
            "title": "The Shining",
            "id": 1001
        }, {
            "title": "Carrie",
            "id": 1002
        }, {
            "title": "It",
            "id": 1003
        }, {
            "title": "Misery",
            "id": 1004
        }, {
            "title": "Night Shift",
            "id": 1005
        }]
    }
}

print(VAR3)

for exercise in VAR3["exercise"]["high impact"]:
  print(exercise)

print(VAR4)

print('Famous Works:')
for novel in VAR4["famous works"]["novels"]:
  print('\tId:', novel['id'], 'Title:', novel['title'])
