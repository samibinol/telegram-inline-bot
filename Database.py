import re
import sqlite3
from ast import literal_eval

conn = sqlite3.connect('stickers.db', check_same_thread=False)

c = conn.cursor()

# Basic database structure as of now:
# sid (string, representing the sticker id passed over by telegram)
# tags (list, the user-defined tags used to search the sticker)


def search(query) -> list:
    qc = re.sub(r'\W', '', query)
    q = "%" + qc + "%"
    cursor = conn.execute("""SELECT sid FROM stickers WHERE tags LIKE ?""", (q,))
    fa = cursor.fetchall()
    string = repr(fa)
    return string


def remove(sid):
    sc = re.sub(r'\W', '', sid)
    c.execute("""DELETE FROM stickers WHERE sid = ?""", (sc,))
    conn.commit()
    return 0


def add(sid, tags):
    # Fetch row with matching SID and remove the sid to get the tags
    # Structure: "tag1,tag2,tag3"

    # TODO: change sql syntax to only select tags

    cursor = conn.execute("""SELECT * FROM stickers WHERE sid == ?""", (sid,))
    fa = cursor.fetchall()

    if len(fa) == 0:
        # Adding a new entry in the database
        c.execute("""INSERT INTO stickers VALUES (?, ?)""", (sid, tags))
        conn.commit()
        return 0
    else:
        # Removing the SID and adding the new tags
        fa2 = fa.pop(0)
        fa3 = fa2[:][1]
        result = fa3 + "," + tags
        # Updating the database
        c.execute("""UPDATE stickers SET tags = ? WHERE sid == ?""", (result, sid,))
        conn.commit()
        return 0
