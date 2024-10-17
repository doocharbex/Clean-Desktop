import os
import shutil
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Desktop path
desktop_path = os.path.join(os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop'))

# Definition of formats and folders for each type of file
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz'],
    'Other': []  # Folder for unknown file types
}

# Path to put the grouped folders (made by the tool)
organized_tool_created_path = os.path.join(desktop_path, 'OrganizedFoldersCreatedByTool')

# The path to put the root folders that were already on the desktop
organized_original_folders_path = os.path.join(desktop_path, 'OriginalFoldersOrganized')


# Function to move files to the appropriate folder (built by the tool)
def organize_files():
    # First, make sure that the root folder for the files sorted by the tool exists
    if not os.path.exists(organized_tool_created_path):
        os.makedirs(organized_tool_created_path)

    # Make sure folders for each file type exist inside the tool's root folder
    for folder in file_types:
        folder_path = os.path.join(organized_tool_created_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # List of files on the desktop
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # only process files (not folders)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            moved = False
            
            # Move files to the appropriate folder
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    dest_folder = os.path.join(organized_tool_created_path, folder)
                    dest_file_path = os.path.join(dest_folder, item)
                    
                    # Check if the file already exists, remove it
                    if os.path.exists(dest_file_path):
                        os.remove(dest_file_path)
                    
                    try:
                        shutil.move(item_path, dest_folder)
                        logging.info(f'Moved {item} to {folder}')
                        moved = True
                    except PermissionError:
                        logging.error(f"PermissionError: Could not move {item}. It may be open in another program.")
                    break
            
            # If file was not moved, move it to "Other"
            if not moved:
                other_folder = os.path.join(organized_tool_created_path, 'Other')
                shutil.move(item_path, other_folder)
                logging.info(f'Moved {item} to Other')


# Function to move the main desktop folders to the new folder
def organize_folders():
    # First, make sure the root folder exists to move the main desktop folders
    if not os.path.exists(organized_original_folders_path):
        os.makedirs(organized_original_folders_path)

    # List of items on the desktop (we only move folders)
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # We only process folders (not files) and do not move new folders created by the tool
        if os.path.isdir(item_path) and item not in ['OrganizedFoldersCreatedByTool', 'OriginalFoldersOrganized']:
            dest_folder = os.path.join(organized_original_folders_path, item)
            try:
                shutil.move(item_path, dest_folder)
                logging.info(f'Moved folder {item} to OriginalFoldersOrganized')
            except PermissionError:
                logging.error(f"PermissionError: Could not move folder {item}. It may be open in another program.")


if __name__ == "__main__":
    # First, categorize the files and move them to a special folder
    organize_files()

    # Then move the folders on the desktop to another folder
    organize_folders()
    
    
    
    print("""
          
          Create By : Dayan Ghanbari
          
          Github : https://github.com/doocharbex/
          
          Instagram : @o_369_o
          
          Telegram : @o_369_o
          
          
          """)
