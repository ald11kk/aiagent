import os

def get_files_info(working_directory, directory="."):
    try:
        abs_path = os.path.abspath(working_directory)
        target_directory = os.path.join(abs_path, directory)
        target_directory = os.path.normpath(target_directory)
        valid_target_directory = os.path.commonpath([abs_path, target_directory]) == abs_path

        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(target_directory)
        lines = []

        for name in entries:
            full_path = os.path.join(target_directory, name)
            size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {e}"