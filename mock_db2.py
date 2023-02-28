import json
import sqlite3
import random

tags = ['learning', 'dance', 'gardening', 'writing', 'shopping', 'painting', 'cooking', 'handicraft', 'photography', 'video game', 'drawing', 'woodworking', 
        'board game', 'singing', 'brewing', 'chess', 'sewing', 'toy', 'genealogy', 'computer programming', 'marketing', 'interior design', 'wine', 'guitar', 'exercise', 'scotter',
        'acting', 'hunting']

companies = ["amazon", "google", "facebook", "oracle", "uber", "airbnb", "microsoft", "apple", "netflix"]


schema1 = ["customer_id", "customer_name", "email", "phone", "home_phone"]
schema2 = ["order_id", "order_date", "total_amount", "customer_id"]
f = open("customer.json")
f2 = open("order.json")
data = json.load(f)
data2 = json.load(f2)

con = sqlite3.connect("customers2.db")
cur = con.cursor()

rows = []
rows2 = []
for ele in data:
    new_json = {}
    if random.randint(1,100) > 20:
        new_json["email"] = ele["email"]
    if random.randint(1,100) > 20:
        new_json["home_phone"] = ele["home_phone"]
    
    print(ele.keys())
    # print(ele['postal_code'])
    # if random.randint(1,100) > 20:
    #     new_json["postal_code"] = ele["postal_code"]

    tag_num = random.randint(1,10)
    new_tag = random.choices(tags, k = tag_num)

    new_json["tags"] = new_tag
    # new_json["tags"] = new_tag
    # new_tuple = (ele[i] for i in schema1)
    # new_tuple2 = (list(new_tuple) + [json.dumps(new_json)]) 
    rows.append((ele["customer_id"], ele["customer_name"], ele["email"], ele["phone"], json.dumps(new_json)))




for ele in data2:

    rows2.append((ele["order_id"], ele["order_date"], ele["total_amount"], ele["customer_id"]))

print(rows)
print(len(rows))
print(rows2)
print(len(rows2))


sql = '''drop table if exists Customers
'''
cur.execute(sql)

sql = '''drop table if exists Order
'''
cur.execute(sql)


sql = '''create table Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
	extra JSON
)'''
cur.execute(sql)

sql = '''create table Order (
order_id INT PRIMARY KEY,
order_date DATA NOT NULL,
total_amount INT NOT NULL,
customer_id INT NOT NULL
)'''
cur.execute(sql)

cur.executemany("INSERT INTO Customers VALUES(?,?,?,?,?)", rows)
cur.executemany("INSERT INTO Orders VALUES(?,?,?,?)", rows2)
con.commit()
#    cur.execute("INSERT INTO User VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(ele['id'], ele['user_id'], ele['username'], ele['first_name'], ele['last_name'], ele['gender'], ele['city'], json.dumps(new_json), ele['register_date'], ele['recent_login_date']))
#    con.commit()


