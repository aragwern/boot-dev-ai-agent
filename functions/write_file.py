import os


def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    is_valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not is_valid_target_dir:
        return (
            f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        )
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    # create directory
    try:
        os.makedirs(os.path.dirname(target_file), mode=0o777, exist_ok=True)
    except OSError as e:
        return f"Error: {e}"

    try:
        # open file to write in
        file = open(target_file, mode="w")
        # write
        file.writelines(content)
    except OSError as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
