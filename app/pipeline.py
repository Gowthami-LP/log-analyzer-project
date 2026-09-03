# Import the analyzer
from app.analyzer import analyze_logs

# Import the email service
from app.email_service import send_email

# Create the common log processing function
def process_logs(logs):

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

        # No ERROR or WARNING was found
        print("No ERROR or WARNING messages found.")

        # No email will be sent
        print("No email will be sent.")

    # Return the alerts
    return alerts
