# Python script to read a text file
def read_file(file_path):
    try:
        # Open the file
        with open(file_path, 'r') as fh:
            print("File Contents:\n")
            for line in fh:
                print(line.strip())  # Print each line without extra newlines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the exact file path
    file_path = r"D:\Cyber security\pyip\mbox-short.txt.txt"
    read_file(file_path)
