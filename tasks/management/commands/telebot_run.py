from django.core.management.base import BaseCommand
from tasks.models import Tasks
import telebot

bot = telebot.TeleBot("6785187478:AAERvwCWrktpPWgiUAFsPPgnS9wAWeOr81k") # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['tasks'])
def tasks(message):
    tasks = Tasks.objects.all()
    for task in tasks:
        print(task)
        bot.send_message(message.chat.id, f'name: {task.name}\ntask: {task.task}')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f'Unknown command: {message.text}')