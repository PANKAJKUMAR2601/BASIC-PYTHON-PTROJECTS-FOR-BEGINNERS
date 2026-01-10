import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=15,            # Controls the complexity/size (1–40)
    box_size=10,           # Size of each block in pixels
    border=5               # White border (default is 4)
)

data = "https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=gfg&matchtype=p&campaignid=20039445781&adgroup=147845288105&gad_source=1&gad_campaignid=20039445781&gbraid=0AAAAAC9yBkDbah8DRupwWeW4wUSVBrjk_&gclid=CjwKCAiA64LLBhBhEiwA-PxguzaxxJ94nlNwuQ4EwKJSgTDlEuj67ovlpKq3FnhPUMj-5kj3Q_Y-ARoCiOYQAvD_BwE"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save("test.png")
