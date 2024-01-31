
import qrcode
from PIL import Image, ImageDraw, ImageFilter
import matplotlib.pyplot as plt

Logo_link = 'logo_ACTEMIUM.png'
 
logo = Image.open(Logo_link)
blur_radius = 0
offset = 4
back_color = Image.new(logo.mode, logo.size, (0,0,0))
offset = blur_radius*0.1 + offset
mask = Image.new("L", logo.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((offset, offset, logo.size[0] - offset, logo.size[1] - offset), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

logo = Image.composite(logo, back_color, mask)

plt.imshow(logo)
logo.save('./lg.png', quality=95)