import json
from datetime import date
Date = date.today()
print (Date)
x = open("convo_object_3.json")
transactions = json.load(x)
print (type(x))
print (type(transactions))
for k,v in transactions.items():
    if k == "events":
        for item in v:
            for final,y in item.items():
                if final == "event":
                    if  y == "bot":
                        print ("bot : {} " .format(item["text"]))
                    if  y == "user":
                        print ("user : {} " . format(item["text"]))
              