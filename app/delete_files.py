import os

def delete_files_in_folder(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)

        # Iterate through the files and delete them one by one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a regular file (not a directory)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        print(f"All files in '{folder_path}' have been deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the folder path where you want to delete files
audio_folder_path = '/home/alchris/Video_Transcriber/app/static/audio'
video_folder_path = '/home/alchris/Video_Transcriber/app/static/videos'

# Call the function to delete files in the specified folder
delete_files_in_folder(audio_folder_path)
delete_files_in_folder(video_folder_path)
