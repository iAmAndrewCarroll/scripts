#!/bin/bash

# Define the source directory (your desktop)
source_dir="$HOME/Desktop"

# Define the destination directory (folder to store PNG files)
destination_dir="$HOME/Desktop/lab screenshots"

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Find all .png files on the desktop and move them to the destination directory
find "$source_dir" -type f -name "*.png" -exec mv {} "$destination_dir" \;

# Optionally, display a message indicating the operation is complete
echo "PNG files moved to the 'lab screenshots' folder on the Desktop."
