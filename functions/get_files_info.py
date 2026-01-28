def get_files_info(working_directory, directory="."):
    import os

    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_directory, directory))

    valid_target_directory = os.path.commonpath([working_directory, target_directory]) == working_directory
    if not valid_target_directory:
        raise ValueError(f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory.")

    if not os.path.isdir(target_directory):
        raise ValueError(f"Error: \"{directory}\" is not a directory")

    entries = []
    for item in sorted(os.listdir(target_directory)):
        item_path = os.path.join(target_directory, item)
        try:
            size = os.path.getsize(item_path)
        except OSError:
            size = 0
        is_dir = os.path.isdir(item_path)
        entries.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

    return "\n".join(entries)

