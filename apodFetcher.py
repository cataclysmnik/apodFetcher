import requests
import datetime
import os

api_key = "UTJEGxiJ3d6bpOfc2Wq9V1USLg43gp2r1ZIuoc3h"
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(api_url)
data = response.json()

image_url = data['hdurl']
title = data['title']
explanation = data['explanation']

image_response = requests.get(image_url)

t = datetime.date.today()

image_directory = "images"
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

image_name = os.path.join(image_directory, f"{t} - {title}.jpg")
text_name = os.path.join(image_directory, f"{t} - {title}.txt")

with open(image_name, 'wb') as file:
    file.write(image_response.content)

with open(text_name, 'w') as file:
    file.write(explanation)

print(f"Title: {title}")
print(f"Image saved as {image_name}")

print("Do you want to see the APOD on your birthday of last year? [y/N]")
bd = True if input().lower() == "y" else False

if bd:
    birth = input("Enter your birthday [DD,MM]:").split(",")
    day = int(birth[0])
    month = int(birth[1])

    current_year = datetime.date.today().year
    previous_year = current_year - 1

    birthday_last_year = datetime.date(previous_year, month, day)

    api_url_birthday = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={birthday_last_year}"
    response_birthday = requests.get(api_url_birthday)
    data_birthday = response_birthday.json()

    image_url_birthday = data_birthday['hdurl']
    title_birthday = data_birthday['title']
    explanation_birthday = data_birthday['explanation']

    image_response_birthday = requests.get(image_url_birthday)

    image_name_birthday = os.path.join(image_directory, f"{birthday_last_year} - {title_birthday}.jpg")
    text_name_birthday = os.path.join(image_directory, f"{birthday_last_year} - {title_birthday}.txt")

    with open(image_name_birthday, 'wb') as file:
        file.write(image_response_birthday.content)

    with open(text_name_birthday, 'w') as file:
        file.write(explanation_birthday)

    print(f"Title: {title_birthday}")
    print(f"Image saved as {image_name_birthday}")
else:
    print("Goodbye!")