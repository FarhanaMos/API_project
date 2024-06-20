#denna fil skapar databas logiken 
import sqlite3
import os
from typing import Dict, Tuple


class DB():
    db_url: str

    def __init__(self, db_url):
        self.db_url = db_url
        if not os.path.exists(self.db_url): # om db inte finns, sätt upp db med __set_up_db
            self.__set_up_db()

    def __set_up_db(self):
        conn = sqlite3.connect(self.db_url)
        with open("setup.sql", "r") as file:
            script = file.read()
            conn.executescript(script)
            conn.commit()
        conn.close()

    def __call_db(self, query, params=()):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, params)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data

#skapar nya data
    def insert(self, *, table: str, fields: Dict[str, str]):
        keys = ",".join(fields.keys())
        placeholders = ",".join(["?" for _ in fields.values()])
        values = tuple(fields.values())
        query = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
        return self.__call_db(query, values)

#hämtar data 
    def get(self, *, table: str, where: Tuple[str, str] | None = None):
        query = f"SELECT * FROM {table}"
        params = ()
        if where:
            key, val = where
            query += f" WHERE {key} = ?"
            params = (val,)
        return self.__call_db(query, params)

#delete data 
    def delete(self, *, table: str, id: int):
        delete_query = f"DELETE FROM {table} WHERE id = ?"
        self.__call_db(delete_query, (id,))

#uppdaterar data 
    def update(self, *, table: str, where: Tuple[str, str], fields: Dict[str, str]):
        where_key, where_val = where
        field_query = ", ".join([f"{key} = ?" for key in fields.keys()])
        values = tuple(fields.values()) + (where_val,)
        update_query = f"UPDATE {table} SET {field_query} WHERE {where_key} = ?"
        self.__call_db(update_query, values)