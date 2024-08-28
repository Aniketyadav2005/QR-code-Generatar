import qrcode

def generate_qr_code(data, file_name="qr_code.png"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code, higher means bigger code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or less error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Border thickness
    )
    qr.add_data(data)
    qr.make(fit=True)  # Adjusts the size of the QR Code to fit the data
    
    # Create image of the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image
    img.save(file_name)
    print(f"QR Code generated and saved as {file_name}")

if __name__ == "__main__":
    # Example usage
    data_to_encode = input("Enter the data to encode in the QR code: ")
    file_name = input("Enter the file name (with extension) to save the QR code image (default is 'qr_code.png'): ") or "qr_code.png"
    generate_qr_code(data_to_encode, file_name)
