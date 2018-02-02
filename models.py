import sqlite3 as sql


def insertQueries(uid, time, query, response):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO feedback (uid,time,query,response) VALUES (?, ?, ?, ?)", (uid, time, query, response))
    con.commit()
    con.close()

def retrieveFeedback():
    con = sql.connect("database.db", detect_types=sql.PARSE_COLNAMES)
    cur = con.cursor()
    cur.execute("SELECT uid, time, query, response FROM feedback")
    responses = cur.fetchall()
    con.close()
    item = {}
    items = []
    for uid, time, query, response in responses:
        item['UID'] = uid
        item['Time'] = time
        item['Query'] = query
        item['Response'] = response
        items.append(item)
    return items