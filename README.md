# File Organizer

## Objective

The File Organizer is a Python automation project that automatically sorts files into categorized folders based on their file types. It helps keep directories clean and organized without manual effort.

## Features

* Automatically creates folders if they do not exist
* Sorts files into categories such as:

  * Images
  * Documents
  * Videos
  * Audio
  * Others
* Reduces clutter in directories
* Easy to customize and extend

## Technologies Used

* Python
* os module
* shutil module

## Project Structure

```text
FileOrganizer/
│
├── file_organizer.py
├── Images/
├── Documents/
├── Videos/
├── Audio/
└── Others/
```

## How It Works

1. The program scans all files in a selected directory.
2. It identifies file extensions.
3. Appropriate folders are created automatically.
4. Files are moved into their respective folders.

## How to Run

1. Install Python.
2. Open the project in VS Code or PyCharm.
3. Run:

```bash
python file_organizer.py
```

4. Files will be organized automatically.

## Output

The script organizes files into separate folders and creates a clean directory structure.

## Learning Outcomes

* File handling in Python
* Automation using Python
* Working with os and shutil modules
* Directory and file management

## Author

Ruthwika M
Synent Technologies Internship Program
