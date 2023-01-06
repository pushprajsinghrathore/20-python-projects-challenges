import qrcode
from PIL import Image
# PIl is  file fromat to convert qrcode formate
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=5,)
qr.add_data("https://www.linkedin.com/feed/update/urn:li:activity:7016802945086238720/")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save("20 PYTHON PROJECT.png")