# Задание 2
#
# Загрузить данные
#
# Загрузите все комментарии из выбранного вами сабреддита,
# используя URL: https://api.pushshift.io/reddit/comment/search/ .
#
# В результате все комментарии сохраняются в хронологическом порядке в формате JSON и выгружаются в файл.

import requests
import json
import os

subreddit = input('Please write subbreddit name: ').strip()

url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size=1000"


def get_unique_filename(base_name: str, extension: str) -> str:
    """Создаёт уникальное имя файла, добавляя номер, если файл уже существует."""
    file_name = f"{base_name}.{extension}"
    counter = 1

    while os.path.exists(file_name):
        file_name = f"{base_name}_{counter}_task_2.{extension}"
        counter += 1

    return file_name


try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    with open('task2.json', 'w') as file:
        result = file.read()
        print(result)

    comments = data.get('data', [])
    if not comments:
        print("No comments found for this subreddit.")
    else:
        comments.sort(key=lambda x: x["created_utc"])

        file_name = get_unique_filename(f"{subreddit}_comments", "json")

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(comments, file, indent=4, ensure_ascii=False)

        print(f"{len(comments)} comments downloaded and saved as {file_name}.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
