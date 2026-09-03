# Import the JSON reader
from app.json_reader import read_json_file

# Import the common pipeline
from app.pipeline import process_logs

# JSON file location
file_path = "data/abc.json"

# Read logs
logs = read_json_file(file_path)

# Send logs to the common pipeline
process_logs(logs)
