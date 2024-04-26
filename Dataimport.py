import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String

# Define your database connection URI
DB_URI = "postgresql://matric_user:YlFGQ4TUvdU6937gns6IUdflTGoDnvmk@dpg-cokgiiv79t8c73ca77kg-a.oregon-postgres.render.com/matric"

def create_table_and_insert_data(excel_file, db_uri, table_name, sheet_name="Sheet1"):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet_name)

        # Extract column names from the first row of the DataFrame
        column_names = list(df.columns)

        # Create a SQLAlchemy engine
        engine = create_engine(db_uri)

        # Create metadata and Table object
        metadata = MetaData()
        table = Table(
            table_name,
            metadata,
            *[Column(col, String) for col in column_names]  # Assuming all columns are of type String
        )

        # Create the table if it doesn't exist
        metadata.create_all(engine, checkfirst=True)

        # Insert data into the table
        with engine.connect() as connection:
            df.to_sql(table_name, connection, if_exists='replace', index=False)

        print(f"Table '{table_name}' created successfully and data inserted.")
    except Exception as e:
        print(f"An error occurred while creating the table and inserting data: {e}")

if __name__ == "__main__":
    excel_file = "data/data.xlsx"  # Update with the path to your Excel file
    table_name = "schools"  # Specify the name of the table
    sheet_name = "data"  # Specify the sheet name in the Excel file (optional, defaults to "Sheet1")

    create_table_and_insert_data(excel_file, DB_URI, table_name, sheet_name)
