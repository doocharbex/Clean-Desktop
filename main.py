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

