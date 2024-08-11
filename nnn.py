from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '7302109315:AAEI8ipmLm7NHHCCbiddiNYmVI9Z8eNSGj8'
CHANNEL_USERNAME = '@ggkatka777'  # Замените на юзернейм вашего канала
FILE_PATH = r'C:\Users\Пользователь\Downloads\cxema09.docx'
# Новый путь к файлу

# Включение логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_member = context.bot.get_chat_member(CHANNEL_USERNAME, user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        # Пользователь подписан на канал, отправляем приветствие и файл
        update.message.reply_text(f'Привет, {user.first_name}! Спасибо за подписку.')
        with open(FILE_PATH, 'rb') as f:
            context.bot.send_document(chat_id=update.effective_chat.id, document=InputFile(f))
    else:
        # Пользователь не подписан на канал
        update.message.reply_text(
            f'Привет, {user.first_name}! Пожалуйста, подпишитесь на наш канал ({CHANNEL_USERNAME}), чтобы получить доступ к файлу.')


def main() -> None:
    updater = Updater(BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()