def get_file_content(working_directory, file_path):
    import os

    working_directory = os.path.abspath(working_directory)
    absolute_path = os.path.normpath(os.path.join(working_directory, file_path))

    # Error handling for path traversal
    try:
        if os.path.commonpath([working_directory, absolute_path]) != working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        from config import FILE_READ_MAX_CHARS

        with open(absolute_path, "r", encoding="utf-8") as f:
            file_content_string = f.read(FILE_READ_MAX_CHARS)
            more = f.read(1)
            if more:
                file_content_string += f'[...File "{file_path}" truncated at {FILE_READ_MAX_CHARS} characters]'

        return file_content_string
    except Exception as exc:
        return f"Error: {exc}"
