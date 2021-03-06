import pytesseract
import time
import telepot
import telepot.exception
from telepot.loop import MessageLoop
from PIL import Image
import cv2


# TelegramBOT

bot = telepot.Bot('1068379297:AAGPrgcBsciI-aGWUbTXfMOFqLO92rOpCYk')
chat = '1068379297'

pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'


def getimg():
    Image.open('imgs/foto.jpg')
    img = cv2.imread("imgs/foto.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    config = "--psm 4"
    try:
        imgtext = pytesseract.image_to_string(adaptive_threshold, lang='por+eng', config=config)
        print(imgtext)
        bot.sendMessage(chat_id, imgtext)
    except telepot.exception.TelegramError:
        bot.sendMessage(chat_id, 'Desculpe, imagem não reconhecida... tente novamente..')


def handle(msg):
    try:
        global photo
        global x
        global chat_id
        chat_id = msg['chat']['id']
        photo = msg['photo'][2]['file_id']
        print('Foto recebida com sucesso... ID: ', photo)
        bot.sendMessage(chat_id, 'Foto recebida com sucesso...\nAnalisando...')
        x = bot.getFile(photo)['file_id']
        bot.download_file(x, 'imgs/foto.jpg')
        time.sleep(2)
        getimg()

    except KeyError:
        chat = 'texto'
        print(chat)


MessageLoop(bot, handle).run_as_thread()

while True:
    pass
    time.sleep(3)

