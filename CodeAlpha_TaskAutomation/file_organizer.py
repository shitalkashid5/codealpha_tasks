import os
import shutil

# Folder containing the files
source_folder = "source_files"

# Folder where JPG files will be moved
destination_folder = "JPG_Files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Find and move JPG files
for filename in os.listdir(source_folder):

    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)

        print(f"Moved: {filename}")

print("\nJPG files moved successfully! ✅")