import os
import glob

def rename_files(directory, prefix):
    files = glob.glob(directory + '/*')
    for index, file in enumerate(files):
        file_extension = os.path.splitext(file)[1]
        new_name = f"{prefix}_{index}{file_extension}"
        os.rename(file, os.path.join(directory, new_name))
    print(f"Renamed {len(files)} files in {directory}")

# Example usage
rename_files('/path/to/your/directory', 'image')
