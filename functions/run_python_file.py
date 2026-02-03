import subprocess
import os

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory = os.path.abspath(working_directory)
        absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not absolute_file_path.startswith(working_directory + os.sep):
            return f'Error: "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"
