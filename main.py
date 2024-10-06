import vk
import vk_api
from vk_api.exceptions import VkApiError
from image import generate_joke_image
from joke import get_random_joke
from posting import post_joke_image
from tkinter import ttk
from datetime import datetime, timedelta
import threading
import tkinter as tk
from tkinter import *
import requests
import matplotlib.pyplot as plt


def post_to_vk():
    image_file_name = 'joke.png'
    token = "ВАШ_ТОКЕН"
    owner_id = 223198837 #Введите ваш id группы
    version_vk = "5.154" #Введите вашу версию ВК
    album_id = 297497653 #Введите ваш id альбома

    post_text = text_entry.get()  # Получение текста поста

    post_joke_image(
        token=token,
        owner_id=owner_id,
        album_id=album_id,
        version_vk=version_vk,
        image_file_name=image_file_name,
        message=post_text  # Передача текста поста в функцию post_joke_image()
    )
    pass


def joke_to_vk():
    image_file_name = 'joke.png'
    token = "ВАШ_ТОКЕН"
    owner_id = 223198837
    version_vk = "5.154"
    joke = get_random_joke()
    generate_joke_image(joke=joke, image_file_name=image_file_name)
    pass


def schedule_post():
    selected_time = time_entry.get()
    current_time = datetime.now().strftime("%H:%M:%S")

    if selected_time <= current_time:
        selected_time = (datetime.now() + timedelta(days=1)).date().strftime("%Y-%m-%d") + " " + selected_time
    else:
        selected_time = datetime.now().date().strftime("%Y-%m-%d") + " " + selected_time

    scheduled_time = datetime.strptime(selected_time, "%Y-%m-%d %H:%M:%S")

    time_diff = (scheduled_time - datetime.now()).total_seconds()

    # Планирование выполнения функции publish_post() через указанное количество секунд
    threading.Timer(time_diff, post_to_vk).start()

    print(f"Пост будет опубликован в {selected_time}")


# Получение статистики постов в группе
# Создание экземпляра класса API ВКонтакте
vk_session = vk_api.VkApi(
    token='ВАШ_ТОКЕН')

try:
    # Авторизация пользователя
    vk_session.auth()
except VkApiError as e:
    print('Ошибка авторизации:', e)

# Получение экземпляра API ВКонтакте
vk = vk_session.get_api()


def get_posts_stats(group_id):
    try:
        response = vk.wall.get(owner_id=group_id, count=100)

        likes_count = 0
        comments_count = 0
        reposts_count = 0

        for item in response['items']:
            likes_count += item['likes']['count']
            comments_count += item['comments']['count']
            reposts_count += item['reposts']['count']

        # Создание графика
        labels = ['Likes', 'Comments', 'Reposts']
        values = [likes_count, comments_count, reposts_count]

        plt.bar(labels, values)
        plt.xlabel('Type')
        plt.ylabel('Count')
        plt.title('Post Statistics')

        # Отображение графика
        plt.show()

        return {
            'likes_count': likes_count,
            'comments_count': comments_count,
            'reposts_count': reposts_count,
            'post_count': len(response['items']),
        }

    except VkApiError as e:
        print('Ошибка получения статистики постов:', e)
        return None


# Обработчик события нажатия кнопки
def show_stats():
    group_id = group_entry.get()
    posts_stats = get_posts_stats(group_id)

    if posts_stats is not None:
        likes_count = posts_stats['likes_count']
        comments_count = posts_stats['comments_count']
        reposts_count = posts_stats['reposts_count']
        post_count = posts_stats['post_count']

        result_label.config(
            text=f"Статистика постов в группе:\n\n"
                 f"Количество постов: {post_count}\n"
                 f"Количество лайков: {likes_count}\n"
                 f"Количество комментариев: {comments_count}\n"
                 f"Количество репостов: {reposts_count}"
        )


def post_preview():
    group_id = "ВАШ_ID"
    access_token = "ВАШ_ТОКЕН"
    url = f"https://api.vk.com/method/wall.get?owner_id=-{group_id}&count=10&access_token={access_token}&v=5.103"

    response = requests.get(url)
    data = response.json()

    # Разбираем полученные данные и отображаем предпросмотр постов
    for item in data['response']['items']:
        post_text = item['text']
        post_attachments = item['attachments']

        print(f"Текст поста: {post_text}")
        print(f"Вложения: {post_attachments}")
        print("")


# Создание основного окна приложения

window = tk.Tk()

window.title("Автопостинг в ВК")

# Создание элементов интерфейса
text_label = tk.Label(window, text="Введите текст поста:")
text_label.pack()

text_entry = tk.Entry(window)
text_entry.pack()

photo_label = tk.Label(window, text="Создать шутку программиста:")
photo_label.pack()

photo_button = tk.Button(window, text="Создать", command=joke_to_vk)
photo_button.pack()

time_label = tk.Label(window, text="Выберите время публикации:")
time_label.pack()

time_entry = ttk.Combobox(window,
                          values=["08:00:00", "09:00:00", "10:00:00", "11:00:00", "11:30:00", "12:00:00", "12:30:00",  "12:40:00", "13:00:00",
                                  "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00", "19:00:00", "20:00:00",
                                  "21:00:00", "22:00:00", "23:00:00"])
time_entry.pack()

schedule_button = tk.Button(window, text="Запланировать", command=schedule_post)
schedule_button.pack()

post_button = tk.Button(window, text="Опубликовать сейчас", command=post_to_vk)
post_button.pack()

group_label = ttk.Label(window, text="ID группы ВКонтакте:")
group_label.pack()

group_entry = ttk.Entry(window)
group_entry.pack()

get_stats_button = ttk.Button(window, text="Показать статистику", command=show_stats)
get_stats_button.pack()

result_label = ttk.Label(window, text="")
result_label.pack()

button2 = ttk.Button(window, text="Предпросмотр постов", command=post_preview)
button2.pack(side=LEFT)

# Запуск главного цикла приложения
window.mainloop()
