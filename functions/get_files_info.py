import os


def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    items = os.listdir(target_dir)

    info = []

    for item in items:
        try:
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
        except OSError as e:
            return f"Error: {e}"
        info.append(f"  - {item}: file_size={file_size} bytes, is_dir={is_dir}")

    files_info = "\n".join(info)
    return files_info


# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# os.path.normpath(): Normalize a path (handles things like ..)
# os.path.commonpath(): Get the common sub-path shared by multiple paths
# os.listdir(): List the contents of a directory
# os.path.isdir(): Check if a path points to an existing directory
# os.path.isfile(): Check if a path points to an existing regular file
# os.path.getsize(): Get the size of a file (in bytes)
# .join(): Join a list of strings together with a given separator
