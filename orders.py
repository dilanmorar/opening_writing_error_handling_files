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

def open_write_txt(file, item):
    try:
        with open(file, 'a') as file_to_write:
            file_to_write.write(item + '\n')
    except FileNotFoundError as error:
        print('Check your file/path')
        print(error)
    finally:
        print('Program ending')

open_write_txt('order2.txt', 'cupcake')
open_write_txt('order2.txt', 'OJ with carrot')
open_write_txt('order2.txt', 'Beans on toast')
open_write_txt('order2.txt', 'Eggs Benedict')
open_print_close('order2.txt')
