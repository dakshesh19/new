import json
from datetime import date
from datetime import datetime
Date = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print ("{}                                                                  {}" .format(current_time,Date))
x = open("d.json")
count = 0
for i in x.readline():
    transactions = json.loads(i)
    #print (type(x))
    #print (type(transactions))
    for k,v in transactions.items():
        if k == "events":
            for item in v:
                for final,y in item.items():
                    if final == "event":
                        if  y == "bot":
                            print ("bot : {} " .format(item["text"]))
                        if  y == "user":
                            print ("user : {} " . format(item["text"]))
                