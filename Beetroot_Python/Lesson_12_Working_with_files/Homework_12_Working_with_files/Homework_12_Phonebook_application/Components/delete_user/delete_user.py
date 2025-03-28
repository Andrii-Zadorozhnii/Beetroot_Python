from Lesson_12_Working_with_files.Homework_12_Working_with_files.Homework_12_Phonebook_application.Components.working_with_files.open_read_file import \
    open_read_file
from Lesson_12_Working_with_files.Homework_12_Working_with_files.Homework_12_Phonebook_application.Components.working_with_files.open_write_file import \
    open_write_file


def delete_user(variable, filename):
    deleting_number = input('Please write here phone number for delete it from data base: ')

    open_read_file(filename)

    if deleting_number in variable:
        del variable[deleting_number]

        open_write_file(variable, filename)

        print('User deleted successfully')
    else:
        print('No current user in the data base')
