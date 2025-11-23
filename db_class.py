import mysql.connector
import bcrypt


class MySQLDatabase:
    def __init__(self,database):
        self.__host="localhost"
        self.__user="root"
        self.__password=""
        self.__database=database
        self.__connection=None
        self.__cursor=None

    def connection(self):
        self.__connection =mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )
        if self.__connection.is_connected():
            self.__cursor=self.__connection.cursor(buffered=True)
            print("Connection Succesful")
            
        else:
             print("Connection Failed") 
              
    def create_db(self,db_name,charset="utf8mb4",collation="utf8mb4_unicode_ci"):
        sql=f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET {charset} COLLATE {collation}"
        self.__cursor.execute(sql)    
        print(f"'{db_name}' database created successfully")

    def create_table(self,db_name,table_name,columns):
        self.__cursor.execute(f"USE {db_name}")
        sql=f"CREATE TABLE IF NOT EXISTS {table_name} ({columns}) ENGINE=InnoDB"
        self.__cursor.execute(sql)
        print(f"'{table_name}' table created successfuly")

    
    def insert_record(self,table_name,data):
        columns=", ".join(data.keys())
        values=tuple(data.values())
        placeholders=", ".join(["%s"]*len(data))
        sql=f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.__cursor.execute(sql,values)
        self.__connection.commit()
        print(f"The record has been successfully inserted!")


    def getRows(self,query,params=None):
        if params is not None:
            self.__cursor.execute(query,params or ())
        else:   
            self.__cursor.execute("query") 
        return self.__cursor.fetchall()
    
    def getRow(self,query,params=None):
        if params is not None:
            self.__cursor.execute(query,params or ())
        else:
            self.__cursor.execute("query")     
        return self.__cursor.fetchone()
    
    

    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()    

    def update_record(self,query,values):
        self.__cursor.execute(query,values)
        self.__connection.commit()
        print(f"{self.__cursor.rowcount} row(s) updated")

    def update(self,table_name,columns,conditions):
        set_clause=", ".join([f"{key}=%s" for key in columns.keys()])
        where_clause=" AND ".join([f"{key}=%s" for key in conditions.keys()])
        
        sql_query=f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        values= tuple(columns.values()) + tuple(conditions.values())

        self.__cursor.execute(sql_query,values)
        self.__connection.commit()

        print(f"{self.__cursor.rowcount} row(s) updated")

    def delete_record (self,query,values):
        self.__cursor.execute(query,values)
        self.__connection.commit()
        print(f"{self.__cursor.rowcount} row(s) deleted")

    def delete(self,table_name,conditions):
        where_clause=" AND ".join([f"{key}=%s" for key in conditions.keys()])
        sql_query=f"DELETE FROM {table_name} WHERE {where_clause}"
        values=tuple(conditions.values())
        self.__cursor.execute(sql_query,values)
        self.__connection.commit()
        print(f"{self.__cursor.rowcount} row(s) deleted") 

    def truncate_table(self,table_name):
        sql_query=f"TRUNCATE TABLE {table_name}"

        self.__cursor.execute(sql_query)
        self.__connection.commit()
        print(f"'{table_name}' tabel cleared")  

    def drop_table (self,table_name):
        sql_query=f"DROP TABLE IF EXISTS {table_name}"

        self.__cursor.execute(sql_query)
        self.__connection.commit()
        print(f"'{table_name}' was permanently deleted")     

    def drop_database (self,database_name):
        sql_query=f"DROP DATABASE IF EXISTS {database_name}"

        self.__cursor.execute(sql_query)
        self.__connection.commit()
        print(f"Database '{database_name}' was permanently deleted")                       

    def hash_password(self,password):
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed =bcrypt.hashpw(password_bytes,salt)
        hashed_string = hashed.decode("utf-8")
        return hashed_string
    

    def check_password(self,password,hashed):
        password_bytes = password.encode("utf-8")
        hashed_bytes = hashed.encode("utf-8")
        return bcrypt.checkpw(password_bytes,hashed_bytes)