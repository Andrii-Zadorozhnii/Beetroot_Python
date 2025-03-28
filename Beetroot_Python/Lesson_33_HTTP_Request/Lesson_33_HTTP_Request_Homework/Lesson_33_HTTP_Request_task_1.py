# Задание 1
#
# Роботы.txt
#
# Загрузите и сохраните в файл robots.txt с сайтов Википедии, Твиттера и т. д.

import requests
import os
import time

# Some Links:
# Поисковые системы:
# 	•	Google: https://www.google.com/robots.txt
# 	•	Bing: https://www.bing.com/robots.txt
# 	•	Yahoo: https://www.yahoo.com/robots.txt
# 	•	DuckDuckGo: https://duckduckgo.com/robots.txt
# 	•	Yandex: https://yandex.com/robots.txt
#
# Социальные сети:
# 	•	Facebook: https://www.facebook.com/robots.txt
# 	•	Twitter (X): https://twitter.com/robots.txt
# 	•	Instagram: https://www.instagram.com/robots.txt
# 	•	TikTok: https://www.tiktok.com/robots.txt
# 	•	LinkedIn: https://www.linkedin.com/robots.txt
# 	•	Reddit: https://www.reddit.com/robots.txt
#
# Новости и энциклопедии:
# 	•	Wikipedia: https://www.wikipedia.org/robots.txt
# 	•	BBC: https://www.bbc.com/robots.txt
# 	•	CNN: https://www.cnn.com/robots.txt
# 	•	The New York Times: https://www.nytimes.com/robots.txt
#
# Популярные сервисы:
# 	•	Amazon: https://www.amazon.com/robots.txt
# 	•	YouTube: https://www.youtube.com/robots.txt
# 	•	Netflix: https://www.netflix.com/robots.txt
# 	•	GitHub: https://github.com/robots.txt


continue_requests = True


def loading_data():
    """Loading Animation."""
    print("Loading data: 25%")
    time.sleep(1)
    print("Loading data: 50%")
    time.sleep(1)
    print("Loading data: 75%")
    time.sleep(1)
    print("Loading data: 100%\n")
    time.sleep(2)


def get_unique_filename(base_name: str, extension: str) -> str:
    """Creating unicaly file name"""
    file_name = f'{base_name}.{extension}'
    counter = 1

    while os.path.exists(file_name):
        file_name = f'{base_name}_{counter}_task_1.{extension}'
        counter += 1

    return file_name


try:
    while continue_requests == True:
        # Request url
        url = input('Please insert url for download txt: ')
        # Get Request
        response = requests.get(url)
        response.raise_for_status()  # Displaying error code

        file_name = get_unique_filename('url', 'txt')

        print("\nConnection completed with positive results\n")

        # File reocrding
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.write(response.text)

        print(f"File downloaded successfully and saved as {file_name}.\n")

        loading_data()

        # File Reading and displaying
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)

        continue_requests = True if input('Do you wand to continue?(y/n): ') == 'y' else False


except requests.exceptions.HTTPError:
    status_messages = {
        201: "Resource created successfully",
        204: "No content, but request was successful",
        301: "Resource permanently moved to another location",
        302: "Resource temporarily moved to another location",
        400: "Bad request - server couldn't understand the request",
        401: "Unauthorized - authentication required",
        403: "Forbidden - access denied",
        404: "Not found - resource doesn't exist",
        500: "Internal server error - something went wrong on the server",
        502: "Bad gateway - received an invalid response from an upstream server",
        503: "Service unavailable - server is overloaded or down",
        504: "Gateway timeout - server took too long to respond"
    }
    print(f"HTTP error occurred: {status_messages.get(response.status_code, 'Unknown error')}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
