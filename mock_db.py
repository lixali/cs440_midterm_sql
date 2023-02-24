import json
import sqlite3
import random

tags = ['learning', 'dance', 'gardening', 'writing', 'shopping', 'painting', 'cooking', 'handicraft', 'photography', 'video game', 'drawing', 'woodworking', 
        'board game', 'singing', 'brewing', 'chess', 'sewing', 'toy', 'genealogy', 'computer programming', 'marketing', 'interior design', 'wine', 'guitar', 'exercise', 'scotter',
        'acting', 'hunting']

f = open("MOCK_DATA.json")
f2 = open("MOCK_DATA2.json")
data = json.load(f)
data2 = json.load(f2)

con = sqlite3.connect("employee.db")
cur = con.cursor()

rows = []
rows2 = []
for ele in data:
    new_json = {}
    if random.randint(1,100) > 20:
        new_json["email"] = ele["email"]
    if random.randint(1,100) > 20:
        new_json["cell_phone"] = ele["cell_phone"]
    if random.randint(1,100) > 20:
        new_json["home_phone"] = ele["home_phone"]
    
    print(ele.keys())
    # print(ele['postal_code'])
    # if random.randint(1,100) > 20:
    #     new_json["postal_code"] = ele["postal_code"]

    tag_num = random.randint(1,10)
    new_tag = random.choices(tags, k = tag_num)

    new_json["tags"] = new_tag

    rows.append( (ele['employee_id'], ele['first_name'], ele['last_name'], ele['age'], ele['gender'], ele['department'], ele['country'], ele['salary'], json.dumps(new_json)) )




for ele in data2:

    rows2.append((ele["country"], ele["security_clearance"]))

print(rows)
print(len(rows))
print(rows2)
print(len(rows2))


sql = '''drop table employee 
'''
cur.execute(sql)

sql = '''drop table company_info 
'''
cur.execute(sql)


sql = '''create table employee (
	employee_id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	age INT,
	gender VARCHAR(50),
	department VARCHAR(50),
	country VARCHAR(50),
	salary INT,
	extra JSON
)'''
cur.execute(sql)

sql = '''create table company_info (
	country VARCHAR(50),
	security_clearance INT
)'''
cur.execute(sql)


cur.executemany("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)", rows)
cur.executemany("INSERT INTO company_info VALUES(?,?)", rows2)
con.commit()
#    cur.execute("INSERT INTO User VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(ele['id'], ele['user_id'], ele['username'], ele['first_name'], ele['last_name'], ele['gender'], ele['city'], json.dumps(new_json), ele['register_date'], ele['recent_login_date']))
#    con.commit()


