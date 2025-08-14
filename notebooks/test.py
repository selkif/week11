import os
import pandas as pd
import pyodbc

# Database connection settings
server = 'localhost'  # Change if necessary
database = 'VBT_HH_Prioritization'  # Change to your database
table_name = 'hh_prioritization2'  # Change to your target table

dsn = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

# Folder containing the Excel files
folder_path = 'C:/Users/bethelhem.teka/OneDrive - Catholic Relief Services/Desktop/KAIM_Week_8_and_9/week_8_and_9/scripts/'  # Change to your local folder path

sheet_name='HH Prioritization sheet'
columns_to_read = list(range(0, 58))

# Establish database connection
conn = pyodbc.connect(dsn)
cursor = conn.cursor()

# Scan the folder for all Excel files
excel_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]

print(f"Found {len(excel_files)} Excel files to process...")

# Function to load an Excel file into SQL Server
def load_excel_to_sql(file_path):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_to_read)
        df.head()
        if df.empty:
            print(f"Skipping {file_path} (empty file).")
            return

        # Convert DataFrame to a list of tuples (ensure all values are strings)
        values = [tuple(str(x) for x in row) for row in df.to_records(index=False)]
        
        # Generate SQL Insert statement dynamically
        columns = ', '.join([f"[{col}]" for col in df.columns.str.strip()])
        placeholders = ', '.join(['?' for _ in df.columns])
        sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        # Execute the insert operation
        cursor.executemany(sql_query, values)
        conn.commit()
        print(f"Successfully loaded {file_path} into {table_name}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Process each Excel file in the folder
for file in excel_files:
    load_excel_to_sql(file)

# Close the connection
cursor.close()
conn.close()
print("Data loading complete!")
