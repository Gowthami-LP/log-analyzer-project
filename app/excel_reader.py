# Import pandas
# Pandas is used to read Excel files
import pandas as pd

# Create a function to read an Excel file
def read_excel_file(file_path):

    # Read the Excel file
    # This returns a pandas DataFrame
    data = pd.read_excel(file_path)

    # Create an empty list
    # We will store the logs here
    logs = []

    # Read each row one by one
    for index, row in data.iterrows():

        # Get the Level value
        level = row["Level"]

        # Get the Message value
        message = row["Message"]

        # Convert the row into one log message
        log = f"{level}: {message}"

        # Add the log to our list
        logs.append(log)

    # Return all logs
    return logs

# This part runs only when we directly run excel_reader.py
if __name__ == "__main__":

    # Location of the Excel file
    file_path = "data/logs.xlsx"

    # Read the Excel file
    logs = read_excel_file(file_path)

    # Print all logs
    print("Excel Logs:")

    for log in logs:
        print(log)
