from datetime import datetime as Datetime, timezone as Timezone



import pg8000.dbapi
from pg8000.converters import INET_ARRAY, INTEGER


import os
from dotenv import load_dotenv

load_dotenv()

# Replace these values with your Google Cloud SQL connection details
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
project_id = os.getenv('GCP_PROJECT_ID')
instance_name = os.getenv('GCP_SQL_INSTANCE_NAME')



import os

from google.cloud.sql.connector import Connector, IPTypes
#oauth2 for python
from google.oauth2 import service_account
import pg8000

import sqlalchemy


def connect_with_connector(db_user,db_pass,db_name,instance_connection_name,ip_type) -> sqlalchemy.engine.base.Engine:
    
    

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    # initialize Cloud SQL Python Connector object
    credentials = service_account.Credentials.from_service_account_file(
        filename='key.json',
    )
    print(credentials)
    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        # ...
    )
    return pool


connect_with_connector(db_user,db_password,db_name,instance_connection_name=instance_name,ip_type=IPTypes.PUBLIC)
#check if the connection is successful
connect_with_connector(db_user,db_password,db_name,instance_connection_name=project_id,ip_type=IPTypes.PUBLIC).connect()

#get all the data from the database
def get_all_data() -> list:
    """
    Get all data from the database
    """
    # Replace these values with your Google Cloud SQL connection details.
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    project_id = os.getenv('GCP_PROJECT_ID')
    instance_name = os.getenv('GCP_SQL_INSTANCE_NAME')

    # Initialize the connection pool using the Cloud SQL Python Connector
    pool = connect_with_connector(db_user,db_password,db_name,instance_name,ip_type=IPTypes.PUBLIC)

    # Create a new database connection and execute the query
    with pool.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sentiment")
            results = cursor.fetchall()
            return results
        
"""
    create table,
    schema
    Title : string
    Description : string
    video_id : string and primary key

"""


def create_table() -> None:
    """
    Create a table in the database

    """
   
    # Replace these values with your Google Cloud SQL connection details.
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    project_id = os.getenv('GCP_PROJECT_ID')
    instance_name = os.getenv('GCP_SQL_INSTANCE_NAME')

    # Initialize the connection pool using the Cloud SQL Python Connector
    pool = connect_with_connector(db_user,db_password,db_name,project_id,ip_type=IPTypes.PUBLIC)

    # Create a new database connection and execute the query
    with pool.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS sentiment (
                    title VARCHAR(255),
                    description VARCHAR(255),
                    video_id VARCHAR(255) PRIMARY KEY
                )
                """
            )
            conn.commit()
            print("Table created successfully")
            return None

#create_table()


def insert_data(title: str, description: str, video_id: str) -> None:
    """
    Insert data into the database

    Args:
      title: The title of the video.
      description: The description of the video.
      video_id: The ID of the video.
    """
    # Replace these values with your Google Cloud SQL connection details.
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    project_id = os.getenv('GCP_PROJECT_ID')
    instance_name = os.getenv('GCP_SQL_INSTANCE_NAME')

    # Initialize the connection pool using the Cloud SQL Python Connector
    pool = connect_with_connector(db_user,db_password,db_name,instance_name,ip_type=IPTypes.PUBLIC)

    # Create a new database connection and execute the query
    with pool.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sentiment (title, description, video_id) VALUES (%s, %s, %s)",
                (title, description, video_id),
            )
            conn.commit()
            print("Data inserted successfully")
            return None