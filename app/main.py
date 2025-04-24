def copy_file(files: str) -> None:
    files_split = files.split()
    if len(files_split) < 3:
        return
    file_obj = files_split[1]
    file_new = files_split[2]
    command = files_split[0]
    if file_obj == file_new:
        return
    try:
        if command == "cp":
            with (open(file_obj, "r") as file_obj,
                  open(file_new, "a") as file_new):
                for line in file_obj:
                    file_new.write(line)
    except FileNotFoundError:
        return
    return
