def check_if_input_is_a_menu_option(choices):
    try:
        user_input = int(input("Please select a choice: "))
        print('')
        if user_input not in(choices):
            return -1
        return user_input
    except:
        return -1

def write_to_file(file_content):
    f = open('Products.txt', 'w')
    if len(file_content) > 0:
        f.write(file_content[0])
        for x in range(1, len(file_content)):
            f.write('\n' + file_content[x])
    f.close()
    return 1

def check_if_file_exists_and_load_content():
    try:
        f = open('Products.txt')
        file_content = [x.replace('\n','') for x in f.readlines()]
        f.close()
        return file_content
    except (NameError, FileNotFoundError):
        return False