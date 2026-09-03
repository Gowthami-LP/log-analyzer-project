# Import the JSON reader function
from app.json_reader import read_json_file

# Import the analyzer function
from app.analyzer import analyze_logs

# Import the email function
from app.email_service import send_email

# Location of the JSON file
file_path = "data/abc.json"

# Read logs from the JSON file
logs = read_json_file(file_path)

# Analyze the logs
alerts = analyze_logs(logs)

# Check whether ERROR or WARNING was found
if alerts:

    # Print the alerts
    print("ERROR/WARNING messages found:")

    for alert in alerts:
        print(alert)

    # Send email
    send_email(alerts)

else:

    # No alerts were found
    print("No ERROR or WARNING messages found.")

    # Don't send email
    print("No email will be sent.")
