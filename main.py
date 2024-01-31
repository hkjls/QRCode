import qrcode
from PIL import Image, ImageDraw, ImageFilter

Logo_link = 'logo_ACTEMIUM.png'
logo = Image.open(Logo_link)

# taking base width
basewidth = 300
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
 
# taking url or text
# url = 'https://www.geeksforgeeks.org/'
# url = 'https://mega.nz/folder/Qzdg2IKR#Eb8bCIzZzDxN8X3zeqSlng' # AMZ
# url = 'https://mega.nz/folder/Yj1kiCDQ#Qa5LyYNUEz6YqR77lZFdbg' # ASL
url = 'https://mega.nz/folder/hq1XCKLD#ZzMqthiu6VXZ9os7G_xr8Q' # ADTA
 
# adding URL or text to QRcode
QRcode.add_data(url)
 
# generating QR code
QRcode.make()
 
# taking color name from user
QRcolor = 'Black'
 
# adding color to QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
 
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
 
# save the QR code generated
# QRimg.save('Procedures AMZ V1.5.png')
# QRimg.save('Procedures ASL V2.png')
QRimg.save('test.png')
 
print('QR code generated!')