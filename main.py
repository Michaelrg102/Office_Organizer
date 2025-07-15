import os
import shutil

# Get the current logged-in username
system = os.environ
user = system['USERNAME']

# Define source path (Downloads) and destination folders for each file type
source_path = fr'C:\Users\{user}\Downloads'
destination ={
    '.xlsx': fr'C:\Users\{user}\Documents\Excel',
    '.docx': fr'C:\Users\{user}\Documents\Word',
    '.ppt': fr'C:\Users\{user}\Documents\PowerPoint',
    '.pptx': fr'C:\Users\{user}\Documents\PowerPoint',
    }

# List all files currently in the Downloads folder
files_in_source = os.listdir(source_path)

# (Optional) Filter files by extension, in case you want to use these lists later
xlsx_files = [file for file in files_in_source if file.endswith('.xlsx')]
ppt_files = [file for file in files_in_source if file.endswith('.ppt')]
docx_files = [file for file in files_in_source if file.endswith('.docx')]

# Loop through each file found in Downloads
for file in files_in_source:

    # Convert filename to lowercase to ensure case-insensitive matching
    file_lower = file.lower()

    # Check if the file extension matches any key in the 'destination' dictionary
    for ext, dest_path in destination.items():
        if file_lower.endswith(ext):
            # Create the destination folder if it doesn't already exist
            os.makedirs(dest_path, exist_ok=True)

             # Build full source and destination file paths
            source_file = os.path.join(source_path, file)
            destination_file = os.path.join(dest_path, file)

            # Move the file from Downloads to the corresponding folder
            shutil.move(source_file, destination_file)
            print(f'Moved: {file} - {dest_path}')
            break # Exit inner loop after moving the file to avoid duplicates