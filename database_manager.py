import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        """Connects the database and creates a table if it does not exist"""
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('create table if not exists user (datetime text, email text, hash text)')

    def set_user_hash(self, email, hashcode):
        """Takes email and hashcode as input and stores it in the database"""
        self.cursor.execute('select * from user where email=:c', {'c': email})
        if not self.cursor.fetchall():
            self.cursor.execute('insert into user values (?,?,?)', (datetime.now(), email, hashcode))
            return True
        return False

    def verify_user_hash(self, email, hashcode):
        """Checks if the email and the matching hashcode is in the database"""
        self.cursor.execute(
            'select * from user where email=:c', {'c': email})
        info = self.cursor.fetchall()
        if info and info[0][2] == hashcode:
            return True
        return False
