# Downloads Organizer

The Downloads Organizer is a Python script that automatically organizes files in the 'Downloads' folder by moving them into subfolders based on their file extensions.

## How It Works

The script periodically scans the 'Downloads' folder and identifies files within it. It then examines the file extensions of these files and creates subfolders corresponding to each unique extension. Files are subsequently moved into their respective subfolders.

## Features

- Automatic file organization: The script eliminates the hassle of manually sorting files by automatically organizing them based on their file extensions.
- Dynamic subfolder creation: New subfolders are created on-the-fly as files with unrecognized extensions are encountered.
- Customizable scan intervals: You can adjust the interval at which the 'Downloads' folder is scanned and files are organized.

## Usage

1. Ensure you have Python installed on your system.
2. Clone the repository or download the code files.
3. Create a folder in your downloads folder called: `Folders`
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the script using the command: `python downloads_organizer.py`.
6. Sit back and let the script do the work! The 'Downloads' folder will be organized automatically based on file extensions.

## Requirements

The following modules are required to run the script:

- shutil
- pathlib
- time
- os

You can install these modules using the following command: "pip install -r requirements.txt".

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, suggest improvements, and report issues through GitHub's issue tracker.
