import os
import shutil


# Desktop path
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


# Definition of formats and folders for each type of file
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz'],
}


# Path to put the grouped folders (made by the tool)
organized_tool_created_path = os.path.join(desktop_path, 'OrganizedFoldersCreatedByTool')

# The path to put the root folders that were already on the desktop
organized_original_folders_path = os.path.join(desktop_path, 'OriginalFoldersOrganized')
