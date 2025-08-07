# Open the file
with open('mbox-short.txt', 'r') as file:
    hour_counts = {}  # Dictionary to store the counts of each hour

    # Read through each line in the file
    for line in file:
        if line.startswith('From '):  # Check if the line starts with 'From '
            # Split the line to extract the time part
            time_part = line.split()[5]
            # Extract the hour from the time part
            hour = time_part.split(':')[0]
            # Update the count for the hour in the dictionary
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

    # Sort the hours and print the counts
    for hour in sorted(hour_counts):
        print(f"{hour} {hour_counts[hour]}")