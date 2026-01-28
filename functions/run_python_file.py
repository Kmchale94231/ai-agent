def run_python_file(working_directory, file_path, args=None):
    import os 
    
    working_directory = os.path.abspath(working_directory)
