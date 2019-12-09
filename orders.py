def open_print(file_name):
    try:
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            print(line.strip('\n'))

        opened_file.close() # closes the file, so can be saved without conflict

    except FileNotFoundError as error_message: # original error message
        print('Check file name/path - File can not be found')
        print(error_message)
        # raise

def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('Program ending')

open_print_close('order2.txt')