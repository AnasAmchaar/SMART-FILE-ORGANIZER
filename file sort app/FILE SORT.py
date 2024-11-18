#!/usr/bin/env python3
"""
File Sorting Script

This script automatically organizes files in a directory by sorting them into categorized
folders based on their file extensions. It supports multiple file types including documents,
images, videos, and programming files.

The script creates appropriate folders if they don't exist and moves files while preserving
their original names. It provides feedback about each file movement and handles invalid
paths gracefully.

Usage:
    Run the script and input the directory path when prompted.
    The script will organize all files in the specified directory.

Author: [Your Name]
Date: [Current Date]
Version: 1.0
"""

import os
import shutil

def sort_files_by_type(source_dir):
    """
    Sort files in the given directory into subdirectories based on their file extensions.
    
    This function processes all files in the source directory and moves them into appropriate
    subdirectories based on their file types. If a matching category folder doesn't exist,
    it will be created automatically.
    
    Args:
        source_dir (str): The path to the directory containing files to be sorted.
        
    Returns:
        None
        
    Raises:
        OSError: If there are permission issues or file operations fail.
        
    Example:
        >>> sort_files_by_type("C:/Users/Username/Downloads")
        Moved document.pdf to C:/Users/Username/Downloads/Documents
        Moved image.jpg to C:/Users/Username/Downloads/Images
    """
    
    # Dictionary mapping file categories to their respective extensions
    folders_by_type = {
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'rtf'],
        'Excel': ['xlsx', 'xls', 'csv'],
        'PowerPoint': ['pptx', 'ppt'],
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'eps', 'psd', 'ai', 
                  'raw', 'HEIC', 'PNG', 'img', 'jfif', 'avif'],
        'Videos': ['mp4', 'avi', 'mkv', 'mov', 'wmv'],
        'Music': ['mp3', 'wav', 'flac', 'aac', 'ogg'],
        'Blender': ['blend'],
        'CiscoPacketTracer': ['pkt'],
        'CAD': ['dwg', 'dxf', 'CATPart', 'CATProduct', 'asc'],
        'Archives': ['zip', 'rar', 'tar', '7z'],
        'Programming': ['py', 'java', 'cpp', 'html', 'css', 'js', 'm', 'm*', 'ipynb'],
        'Spreadsheets': ['ods'],
        'Presentations': ['odp', 'ppsx', 'ppSX', 'eddx', 'potx'],
        'Ebooks': ['epub', 'mobi'],
        'Fonts': ['ttf', 'otf'],
        'Scripts': ['sh', 'bat', 'ps1'],
        'Backup': ['bak', 'backup'],
        'Logs': ['log'],
        'Database': ['sqlite', 'db'],
        'VirtualMachines': ['vdi', 'vmdk', 'iso'],
        'executable': ['exe', 'msi'],
    }
    
    try:
        # Iterate through all files in the source directory
        for filename in os.listdir(source_dir):
            file_path = os.path.join(source_dir, filename)
            
            # Process only files, not directories
            if os.path.isfile(file_path):
                # Extract file extension
                file_type = filename.split('.')[-1] if '.' in filename else ''
                
                # Find matching folder for the file type
                for folder, extensions in folders_by_type.items():
                    if file_type.lower() in [ext.lower() for ext in extensions]:
                        dest_dir = os.path.join(source_dir, folder)
                        
                        # Create destination folder if it doesn't exist
                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)
                        
                        # Move the file to its appropriate folder
                        shutil.move(file_path, os.path.join(dest_dir, filename))
                        print(f"Moved {filename} to {dest_dir}")
                        break
                else:
                    print(f"No folder specified for {filename}, skipping.")
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

# Main execution block
if __name__ == "__main__":
    """
    Main execution block that handles user input and initiates the file sorting process.
    """
    user_path = input("Enter the path to sort: ")
    
    # Validate the provided path
    if os.path.exists(user_path) and os.path.isdir(user_path):
        sort_files_by_type(user_path)
    else:
        print("Invalid directory path. Please provide a valid directory path.")
