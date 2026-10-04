import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z"],
    }

    for category in categories:
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in categories.items():
            if extension in extensions:
                destination = os.path.join(folder_path, category, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename} -> {category}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    print("Python File Organizer")
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
    print("File organization completed.")
