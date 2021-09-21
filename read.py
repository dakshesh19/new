import json
x = open("d.json")
transaction = json.load(x)
print (type(transaction))
#print (transaction)
for x,y in transaction.items():
    print(x)



