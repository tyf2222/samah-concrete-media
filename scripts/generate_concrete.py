from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import datetime, random
W,H=1600,900
im=Image.new("RGB",(W,H),(12,35,60))
d=ImageDraw.Draw(im)
for y in range(H):
    d.line((0,y,W,y),fill=(int(12+35*y/H),int(35+30*y/H),int(60+30*y/H)))
d.polygon([(0,650),(320,480),(650,650),(950,440),(1600,690),(1600,900),(0,900)],fill=(55,73,85))
d.rectangle((0,720,W,900),fill=(10,25,42))
d.rounded_rectangle((80,100,1510,310),radius=30,fill=(240,244,247))
d.rounded_rectangle((80,750,1510,855),radius=24,fill=(185,30,38))
font="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f=ImageFont.truetype(font,65); f2=ImageFont.truetype(font,74)
d.text((180,160),"READY MIX CONCRETE",font=f,fill=(15,48,80))
d.text((230,760),"07759296259",font=f2,fill="white")
d.text((160,365),"BAGHDAD  |  KARKH + RUSAFA",font=ImageFont.truetype(font,44),fill="white")
d.text((160,425),"Illustrative advertising artwork",font=ImageFont.truetype(font,29),fill=(230,230,230))
Path("images").mkdir(exist_ok=True)
out="images/concrete-"+datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S")+".png"
im.save(out,optimize=True)
print(out)
