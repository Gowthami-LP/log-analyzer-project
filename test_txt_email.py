# Import the text file reader
from app.file_reader import read_text_file

# Import the analyzer
from app.analyzer import analyze_logs

# Import the email service
from app.email_service import send_email

# Location of the text file
file_path = "data/abc.txt"

# Read logs from the text file
logs = read_text_file(file_path)

# Analyze the logs
alerts = analyze_logs(logs)

# Check whether ERROR or WARNING was found
if alerts:

    # Print the alerts
    print("ERROR/WARNING messages found:")

    for alert in alerts:
        print(alert)

    # Send the alerts through email
    send_email(alerts)

else:

    # No ERROR or WARNING was found
    print("No ERROR or WARNING messages found.")

    # Don't send email
    print("No email will be sent.")
