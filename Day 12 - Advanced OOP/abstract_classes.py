from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MySQL...")
    
    def execute_query(self, query):
        print(f"Executing MySQL query: {query}")

# Usage
# db = DatabaseConnector()  # Raises error
mysql = MySQLConnector()
mysql.connect()