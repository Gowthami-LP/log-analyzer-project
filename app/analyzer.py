# Create a function called analyze_logs
# This function receives a list of log messages
def analyze_logs(logs):

    # Create an empty list
    # We will store ERROR and WARNING messages here
    alerts = []

    # Go through each log message one by one
    for log in logs:

        # Check whether the log contains ERROR
        # OR whether it contains WARNING
        if "ERROR" in log or "WARNING" in log:

            # Add the matching log message to the alerts list
            alerts.append(log)

    # Return all ERROR and WARNING messages
    return alerts


if __name__ == "__main__":
    # Create some sample log messages for testing
    logs = [
        "INFO: Application started",
        "WARNING: Database response time is high",
        "INFO: User logged in",
        "ERROR: Database connection failed"
    ]

    # Call the analyze_logs() function
    # Pass our logs list to the function
    alerts = analyze_logs(logs)

    # Print a heading
    print("ERROR and WARNING messages:")

    # Print every alert returned by the function
    for alert in alerts:
        print(alert)
