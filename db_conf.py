import mysql.connector


class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
    def add_client(self, first_name, last_name,address,city,phone):
        query = 'INSERT INTO clients (first_name, last_name,address,city,phone) VALUES (%s,%s,%s,%s,%s)'
        self.cursor.execute(query, (first_name, last_name,address,city,phone))
        self.connection.commit()

    def add_car(self, reg_no, client_id,make,model,distance,engine_t,prod_year):
        query = 'INSERT INTO cars (reg_no, client_id,make,model,distance,engine_t,prod_year) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(query, (reg_no, client_id,make,model,distance,engine_t,prod_year))
        self.connection.commit()
    
    def add_service(self,client_id,reg_no,date_of_service,service_desrcipt,cost,comments):
         query = 'INSERT INTO services (client_id,reg_no,date_of_service,service_descript,cost,comments) VALUES (%s,%s,%s,%s,%s,%s)'
         self.cursor.execute(query, (client_id,reg_no,date_of_service,service_desrcipt,cost,comments))
         self.connection.commit()

def display_table(connector,):
    query = f"SHOW TABLES "
    data = connector.fetch_data(query)

    if data:
        print(f"Data from table:")
        for row in data:
            print(row)
    else:
        print(f"No data found in table ")
