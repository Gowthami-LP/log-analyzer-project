# Import the Excel reader
from app.excel_reader import read_excel_file

# Import the analyzer
from app.analyzer import analyze_logs

# Import the email service
from app.email_service import send_email

# Location of the Excel file
file_path = "data/logs.xlsx"

# Read logs from the Excel file
logs = read_excel_file(file_path)

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
