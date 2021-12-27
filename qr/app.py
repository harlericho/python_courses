import qrcode
# social page path
imgCode = qrcode.make('http://www.whatsapp.com')
imgCode.save('wht.png')