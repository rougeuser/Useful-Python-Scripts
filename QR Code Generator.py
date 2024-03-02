import qrcode

# QR Code Generator: Generates QR code for a given text or URL.
def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data = input("Enter the text or URL: ")
    file_name = input("Enter the output file name (with extension): ")
    generate_qr_code(data, file_name)