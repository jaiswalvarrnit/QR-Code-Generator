import qrcode
from PIL import Image

# img = qr.make("https://www.linkedin.com/in/varrnit-jaiswal-5963071a0/")
# img.save("My_Linkedin_Profile_QR.png")

# checks the version and checks for any error specify box size and border size
qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4,) 

# give the link
qr.add_data("https://www.linkedin.com/in/varrnit-jaiswal-5963071a0/")
qr.make(fit=True)

# generate qr by specify the colors
img = qr.make_image(fill_color="red", back_color = "blue")

# specify the name you want to save as
img.save("My_Linkedin_Profile_QR.png")
