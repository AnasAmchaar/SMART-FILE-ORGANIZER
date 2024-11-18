# File Sorter

A Python script that automatically organizes files in a directory by their file types into appropriate folders.

## Features

- Automatically sorts files into categorized folders based on their extensions
- Supports 21 different file categories including:
  - Documents (PDF, DOC, TXT, etc.)
  - Images (JPG, PNG, GIF, etc.)
  - Videos (MP4, AVI, MKV, etc.)
  - Programming files (PY, JAVA, CPP, etc.)
  - And many more...
- Creates folders automatically if they don't exist
- Preserves original file names
- Provides feedback about file movements
- Handles invalid paths gracefully

## Requirements

- Python 3.x
- Standard Python libraries:
  - os
  - shutil

## Installation

1. Clone this repository or download the script
2. No additional package installation required as it uses only standard Python libraries

## Usage

1. Run the script:
```bash
python file_sorter.py
```

2. When prompted, enter the full path to the directory you want to organize:
```
Enter the path to sort: C:/Users/YourName/Downloads
```

3. The script will automatically:
   - Create category folders if they don't exist
   - Move files to appropriate folders
   - Print progress information

## Supported File Types

The script organizes files into the following categories:

- Documents: pdf, doc, docx, txt, rtf
- Images: jpg, jpeg, png, gif, bmp, webp, etc.
- Videos: mp4, avi, mkv, mov, wmv
- Music: mp3, wav, flac, aac, ogg
- Programming: py, java, cpp, html, css, js
- And many more...

## Contributing

Feel free to fork this project and submit pull requests with improvements. Some ideas for contributions:
- Add more file types
- Add functionality to customize folder names
- Implement undo functionality
- Add GUI interface



## Author

ANAS AMCHAAR 

## Acknowledgments

DEAR FRIEND YOUSSEF HACHHOUCH
