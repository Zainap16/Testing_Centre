from sqlalchemy import create_engine
import pandas as pd

# Define your database connection URI
DB_URI = "postgresql://matric_user:YlFGQ4TUvdU6937gns6IUdflTGoDnvmk@dpg-cokgiiv79t8c73ca77kg-a.oregon-postgres.render.com/matric"

def fetch_data_from_database(query):
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(DB_URI)

        # Query data from the database
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        return None
