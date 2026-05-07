import qrcode 

class QRCodeGenerator:
    def __init__(self, data):
        self.data = data
        # We use qrcode.QRCode here
        self.qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

    def generate(self, filename="qrcode.png"):
        self.qr.add_data(self.data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"QR is successfully generated!!")

my_generator = QRCodeGenerator("https://google.com")
my_generator.generate("google_qr.png")