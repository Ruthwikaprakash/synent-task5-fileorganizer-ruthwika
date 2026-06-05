import os
import shutil

folder_path = "test_folder"

documents_folder = os.path.join(folder_path, "Documents")
images_folder = os.path.join(folder_path, "Images")
music_folder = os.path.join(folder_path, "Music")

os.makedirs(documents_folder, exist_ok=True)
os.makedirs(images_folder, exist_ok=True)
os.makedirs(music_folder, exist_ok=True)

files = os.listdir(folder_path)

for file in files:

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        file_name, extension = os.path.splitext(file)

        if extension in [".pdf", ".txt", ".docx"]:
            shutil.move(file_path, os.path.join(documents_folder, file))
            print(f"{file} moved to Documents")

        elif extension in [".jpg", ".png"]:
            shutil.move(file_path, os.path.join(images_folder, file))
             print(f"{file} moved to Images")
            
        elif extension in [".mp3"]:
            shutil.move(file_path, os.path.join(music_folder, file))
            print(f"{file} moved to Music")

print("\nFile Organization Completed!")