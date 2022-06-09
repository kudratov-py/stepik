from platform import system
import time
from turtle import clear

import telebot
from config import token, user_id

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def command(message):
    bot.send_message(user_id, message)


def dog_file_win():
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    class Handler(FileSystemEventHandler):
        def on_created(self, event):
            if event.is_directory:
                command(f'Создана папка: {event.src_path}')
            else:
                command(f'Создан файл: {event.src_path}')

        def on_deleted(self, event):
            if event.is_directory:
                command(f'Удалена папка: {event.src_path}')
            else:
                command(f'Удален файл: {event.src_path}')

        def on_moved(self, event):
            if event.is_directory:
                command(f'Переименована папка: {event.src_path}')
            else:
                command(f'Переименован файл: {event.src_path}')

        def on_modified(self, event):
            if event.is_directory:
                command(f'Изменена папка: {event.src_path}')
            else:
                command(f'Изменен файл: {event.src_path}')

    observer = Observer()
    observer.schedule(Handler(), path=r'C:\Users\d.kudratov\Desktop', recursive=True)
    observer.start()

    bot.polling()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    if system() == "Windows":
        dog_file_win()


if __name__ == '__main__':
    main()
