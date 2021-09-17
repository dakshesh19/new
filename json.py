import json
from datetime import date
Date = date.today()
print (Date)
x = open("test.json")
transactions = json.load(x)
print (type(x))
print (type(transactions))
for k,v in transactions.items():
    #print(k)
    if k == "events":
        for item in v:
            #print(item)
            #for event in item:
                for final,y in item.items():
                    #print (final)
                    if final == "event" and (y == "bot" or y == "user"):
                        for z in item:
                            print (item["text"])