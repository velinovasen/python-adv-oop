import os
while True:
    tokens = input().split("-")
    if tokens[0] == 'End':
        break

    elif tokens[0] == 'Create':
        file_name = tokens[1]
        with open(f"{file_name}", "w+") as created_file:
            created_file.write("")

    elif tokens[0] == 'Add':
        file_name = tokens[1]
        content = tokens[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")

    elif tokens[0] == "Replace":
        file_name = tokens[1]
        old_string = tokens[2]
        new_string = tokens[3]
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                text = file.read()
            text.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(text)
        else:
            print(f'Error occurred')

    elif tokens[0] == "Delete":
        file_name = tokens[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")