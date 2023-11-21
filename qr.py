import qrcode
data = "Hello, world"
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(data)
img = qr.make_image(fill_color = "green", back_color = "#a8187f")
img.save("test.png")