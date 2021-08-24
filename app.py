from flask import Flask, request
import requests
from bs4 import BeautifulSoup as bs
import json, base64

app = Flask(__name__)

@app.route('/')
def home():
    a = {
    'Contoh-Penggunaan':{'textmaker': 'api/textmaker?text=halo'}
    }
    return a

@app.route('/api/textmaker', methods=['GET'])
def makerr():
    from lib.textmaker import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'761ea2d5575581057a799d14e9c78e28',
         'image':image_64_encode,
         'name':'TULISIN ARHBOT',
         'expiration': 60
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
            "Results":p
         }
        return js


if __name__ == '__main__':
    app.run()
