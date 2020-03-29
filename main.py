from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests #to access the API and get the json data
import re

#function to get URL
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

#Define file extensions to distinguish image from vid/GIF
def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extesion not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

#to send a message/image => need 2 parameters: image URL + recipient's ID (group/user)
#send the message = image
def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1013065538:AAGJNR2MJ4c00rIrXlW8TqrIcIw9CK8qwLw')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
