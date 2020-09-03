#### pymysql

```
import pymysql

host = 'localhost'
user = 'root'
password = 'rootroot'
type = 'mysql'
port = 3306

if __name__ == '__main__':
    conn = pymysql.connect(host=host, port=port, user = user, password = password, db = type)

    query = """
        select user, host from user
    """
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()

    for i in res:
        print(i)

    conn.close()

```
