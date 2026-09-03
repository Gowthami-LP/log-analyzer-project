from app.analyzer import analyze_logs
from app.email_service import send_email

# Sample log data
logs = [
    "INFO: Application started",
    "WARNING: CPU usage is high",
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: Application stopped"
]

# Analyze the logs
alerts = analyze_logs(logs)

# Check whether ERROR or WARNING was found
if alerts:

    print("Alerts found:")
    print(alerts)

    # Send email
    send_email(alerts)

else:

    print("No ERROR or WARNING found.")
    print("No email will be sent.")
