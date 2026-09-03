# Import the json module
# Used to read JSON files
import json

# Create a function to read a JSON file
def read_json_file(file_path):

    # Open the JSON file
    # utf-8-sig handles files that contain a BOM marker
    with open(file_path, "r", encoding="utf-8-sig") as file:

        # Convert JSON data into Python data
        data = json.load(file)

    # Get the list of logs
    logs = data["logs"]

    # Return the logs to the caller
    return logs

# This part runs only when we directly run json_reader.py
if __name__ == "__main__":

    # Location of our JSON file
    file_path = "data/abc.json"

    # Read the JSON file
    logs = read_json_file(file_path)

    # Print the logs
    print("JSON Logs:")

    for log in logs:
        print(log)
