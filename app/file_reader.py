# Create a function to read a text file
def read_text_file(file_path):

    # Create an empty list
    # We will store every line from the file here
    logs = []

    # Open the text file in read mode
    with open(file_path, "r") as file:

        # Read the file one line at a time
        for line in file:

            # Remove the extra newline character
            line = line.strip()

            # Add the line to the logs list
            logs.append(line)

    # Return all the logs
    return logs

# This part runs only when we directly run file_reader.py
if __name__ == "__main__":

    # Location of the text file
    file_path = "data/abc.txt"

    # Read the logs
    logs = read_text_file(file_path)

    # Print the logs
    print("TXT Logs:")

    for log in logs:
        print(log)
