import pytesseract
import time
import telepot
from telepot.loop import MessageLoop
from PIL import Image

# TelegramBOT

bot = telepot.Bot('1068379297:AAFcBAn9q1hBt25gHguBJ1Ay2-3uJuhZrQ8')
chat = '1068379297'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def getimg():
    img = Image.open('imgs/foto.jpg')
    imgtext = pytesseract.image_to_string(img)
    print(imgtext)
    bot.sendMessage(chat_id, imgtext)



def handle(msg):
    try:
        global photo
        global x
        global chat_id
        chat_id = msg['chat']['id']
        photo = msg['photo'][2]['file_id']
        print('Foto recebida com sucesso... ID: ', photo)
        bot.sendMessage(chat_id, 'Foto recebida, analisando')
        x = bot.getFile(photo)['file_id']
        bot.download_file(x, 'C:\\Projects\\Tesseract\\imgs\\foto.jpg')
        time.sleep(2)
        getimg()

    except KeyError:
        chat = 'texto'
        print(chat)


MessageLoop(bot, handle).run_as_thread()

while True:
    pass
    time.sleep(3)

# text = pytesseract.image_to_string(img)

# print(img)
