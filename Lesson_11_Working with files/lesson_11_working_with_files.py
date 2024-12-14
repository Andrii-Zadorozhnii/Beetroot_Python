import json
# my_dict = {"name": "Анна", "age": 25}
#
# with open('workfile.json', 'w', encoding='utf-8') as file_object:
#     json.dump(my_dict, file_object, ensure_ascii=False)


my_dict = {
    'first_name' : 'Chereshnia',
    'name' : 'Alex',
    'birth_date' : 1975
}
with open('workfile_person.txt', 'w') as file_object:
    json.dump(my_dict, file_object)