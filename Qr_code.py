import sys
sys.path.append(r'C:\Users\niteshparikh\AppData\Local\Programs\Python\Python310\Lib\site-packages')
import qrcode
import image

qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

url_link = 'https://www.youtube.com'

qr.add_data(url_link)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="blue")
img.save("scanner_img.png")