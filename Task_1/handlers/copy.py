import os
import shutil

def copy_and_categorize_files(source, destination):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"📁 Created directory: {destination}")

        for item in os.listdir(source):
            source_path = os.path.join(source, item)
            
            if os.path.isdir(source_path):
                print(f"➡️ Entering directory: {source_path}")
                copy_and_categorize_files(source_path, destination)
            
            elif os.path.isfile(source_path):
                file_extension = os.path.splitext(item)[1].lstrip('.').lower()
                
                if not file_extension:
                    file_extension = 'no_extension'
                
                destination_subdir = os.path.join(destination, file_extension)
                
                if not os.path.exists(destination_subdir):
                    os.makedirs(destination_subdir)
                    print(f"📦 Created subdirectory for '{file_extension}' files: {destination_subdir}")
                
                destination_path = os.path.join(destination_subdir, item)
                
                print(f"📝 Copying '{source_path}' to '{destination_path}'")
                shutil.copy2(source_path, destination_path)
                
    except OSError as e:
        print(f"⛔️ File or directory access error: {e}")
    except Exception as e:
        print(f"❗️ An unexpected error occurred: {e}")