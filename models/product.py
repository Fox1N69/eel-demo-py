import sqlite3 as sql


def showallprod():
    try:
        connect = sql.connect('/database/storage.db')
        curs = connect.cursor()
        curs.execute('SELECT * FROM prod')
        register = []
        for item in curs.fetchall():
            test = item[1]
            print(test)
            register.append(item)
        return register
    except Exception as err:
        print(err)
        msg = "ERROR"
        return msg
