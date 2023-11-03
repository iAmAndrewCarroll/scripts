#!/bin/bash

# Define the path to the desktop directory
desktop_dir="$HOME/Desktop"

# Delete screenshot files (files starting with "Screen Shot" or "Screenshot")
find "$desktop_dir" -type f -name "Screen Shot*" -o -name "Screenshot*" -exec rm -f {} \;

# Optionally, display a message indicating the operation is complete
echo "Screenshot files deleted from the Desktop."
