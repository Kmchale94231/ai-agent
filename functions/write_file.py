def write_file(working_directory, file_path, content):
    import os

    working_directory = os.path.abspath(working_directory)
    absolute_path = os.path.normpath(os.path.join(working_directory, file_path))

    try:
        if os.path.commonpath([working_directory, absolute_path]) != working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(absolute_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        dir_name = os.path.dirname(absolute_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(absolute_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as exc:
        return f"Error: {exc}"
