import os


# If you want to find file set is_file arg to True and is_folder arg to False and if you want to find is_folder arg to True and if_file arg to False

def find_files(application_name: str, search_path: str, is_file: bool, is_folder: bool) -> list:
    global found
    entry_path_list = []
    found = False
    for entry in os.listdir(search_path):
        try:
            entry_path = os.path.join(search_path, entry)
            if is_folder:
                if os.path.isdir(entry_path):
                    if application_name in entry:
                        found = True
                        entry_path_list.append(entry_path)
                else:
                     continue
            elif is_file:
                if os.path.isfile(entry_path):
                    if application_name in entry:
                        found = True
                        entry_path_list.append(entry_path)

            if not found:
                res = find_files(application_name, entry_path, is_file=True, is_folder=False)
                if res:
                    return res

        except (PermissionError, OSError) as e:
            pass
    return entry_path_list




print(find_files("need2search.txt", "C:\\", is_file=True, is_folder=False))

