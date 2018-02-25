import sqlite3
from sqlite3 import Error
import re
class User():
    username,password='','';


    def executeQuery(self,query):
      try:
        connectionObject.execute(query);
      except Error as databaseErrorMessage:
        print(databaseErrorMessage)
    
    def getUserCredentials(self):
        try:
            self.username=str(input("Choose your username :"))
            self.password=str(input("Choose your password : "))
            print("Welcome to ZenithPomdoro {}".format(self.username))
        except ValueError:
            print("Enter a valid username")
        
    
    
    def __init__(self,db_file):
        try:
            conn = sqlite3.connect(db_file)
            connectionObject = conn.cursor();
            print(sqlite3.version)

            initializationQuery= """CREATE TABLE users (
                                   user_id int(255) INTEGER PRIMARY KEY,
                                   username varchar(255),
                                  password varchar(255),
                                  pointcounter int(255)
                                  );
                                  """
            connectionObject.execute(initializationQuery);
            #print(connection.execute("SELECT * from users")); Assert act arrange ? how to implement unit tests
            
        except Error as e:
            print(e)



      def insertUserName(self):
        
        connectionObject.execute();

    


newUser = User(r'C://Users/jeffl/OneDrive/ZenithPomodoro/database/users.db');
newUser.getUserCredentials();

