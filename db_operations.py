from sqlalchemy import create_engine
import pandas as pd

# Define your database connection URI
DB_URI = "postgresql://matric_user:YlFGQ4TUvdU6937gns6IUdflTGoDnvmk@dpg-cokgiiv79t8c73ca77kg-a.oregon-postgres.render.com/matric"

def fetch_data_from_database(query, limit=None):
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(DB_URI)

        # Append LIMIT clause to the query if limit is specified
        if limit is not None:
            query += f" LIMIT {limit}"

        # Query data from the database
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        return None
