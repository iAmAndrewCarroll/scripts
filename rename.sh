#!/bin/bash

# Define the source directory (your desktop)
source_dir="$HOME/Desktop"

# verify source_dir
echo "Source dir: $source_dir"

# current date in YYY-MM-DD
current_date=$(date + '%Y-%m-%d')

# Find all files with "screenshot" in their name on the desktop
screenshot_files=$(find "$source_dir" -type f -name "*screenshot*" -newermt $(date +%Y-%m-%d) ! -newermt $(date -d "tomorrow" +%Y-%m-%d))

# Prompt the user to enter a value for 'x'
read -p "Enter a value for 'lab number': " lab_number

# show lab_number
echo "lab_number: $lab_number"

# Initialize a counter for consecutive numbers
counter=1

# Loop through the screenshot files and rename them
for file in $screenshot_files; do
    # Extract the file extension
    file_extension="${file##*.}"
    
    # Generate the new filename in the format "labx-y"
    new_filename="lab${lab_number}-${counter}.${file_extension}"

    # show renaming op
    echo "Renaming $file to $new_filename"
    
    # Rename the file
    mv "$file" "$source_dir/$new_filename"
    
    # Increment the counter
    ((counter++))
done

# Optionally, display a message indicating the operation is complete
echo "Files renamed successfully."

# list contents of desktop
ls "$source_dir"
