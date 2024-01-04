import pymysql
import pymysql.cursors
from pprint import pprint as print

connection = pymysql.connect(host='10.100.33.60',
                             user='mmcfowler',
                             password='220878185',
                             database='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
cursor.execute("SELECT `Name`, `HeadOfState` from `country`")
results = cursor.fetchall()
print(results[0])

for x in results:
    print(x['HeadOfState'])