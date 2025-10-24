import sqlite3

class Wrapper: # SQLite Warpper
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def exec(self, query, params=()):
        if not self.conn:
            self.connect()
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def getAll(self, query, params=()):
        cursor = self.exec(query, params)
        return cursor.fetchall()

    def getOne(self, query, params=()):
        cursor = self.exec(query, params)
        return cursor.fetchone()

# Usage example:
# db = Wrapper("my_database.db")
# db.exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
# db.exec("INSERT INTO users (name) VALUES (?)", ("Alice",))
# users = db.getAll("SELECT * FROM users")
# print(users)
# db.close()