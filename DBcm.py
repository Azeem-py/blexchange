#database context manager

import mysql.connector
class UseDB:
    def __init__(self, config):
        self.config = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()
        
