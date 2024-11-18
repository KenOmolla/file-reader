# Declare file and and assign path. Path can be relative to the python file. 
file_path = 'file.txt'

# Definition of method to read file line by line
def read_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file line by line
            content = [line for line in file]
            return content
    except FileNotFoundError:
        print(f"Error: No file was found at '{file_path}' path.")
        return None
    
def check_for_duplicates():
    file_contents = read_file(file_path)
    unique_items = []
    duplicate_items = []

    for item in file_contents:
        # Remove any whitespace from the line
        item = item.strip()

        # Check if the line exists in the list with unique items
        if item in unique_items and item not in duplicate_items:
            # Add the item to the duplicates if it's in the unique list but not added on the duplicates already
            duplicate_items.append(item)
        else:
            # Add the item to the unique list if it does not exist
            unique_items.append(item)

    # Output results on the duplicate check
    if duplicate_items:
        print(f"Duplicate items  found in the file {duplicate_items}")
    else:
        print("Horray!! There were no duplicates found in the file.")

check_for_duplicates()