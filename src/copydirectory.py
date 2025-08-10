import os
import shutil

def copy_files(from_filepath, dst_filepath):
    if not os.path.exists(dst_filepath):
        os.mkdir(dst_filepath)

    from_content = os.listdir(from_filepath)              # list
    
    for item in from_content:
        item_filepath = os.path.join(from_filepath, item)

        if os.path.isfile(item_filepath):
            shutil.copy(item_filepath, dst_filepath)
            item_dst_filepath = os.path.join(dst_filepath, item)
            print(f"* Moving file: {item} {item_filepath} --> {item_dst_filepath}\n")

        elif os.path.isdir(item_filepath):
            new_dir_filepath = os.path.join(dst_filepath, item)
            os.mkdir(new_dir_filepath)
            print(f"** Moving Directory: {item} {item_filepath} --> {new_dir_filepath}")
            copy_files(item_filepath, new_dir_filepath)