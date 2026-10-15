import qrcode

# Ask for personal information
name = input("Enter your name: ")
message = input("Enter a short message: ")
website = input("Enter your favorite website URL: ")

# Create a QR code for the personal message
personal_text = f"My name is {name}. {message}"
personal_qr = qrcode.make(personal_text)
personal_qr.save("personal_qrcode.png")

# Create a QR code for the website
website_qr = qrcode.make(website)
website_qr.save("website_qrcode.png")

# Display confirmation
print("Personal QR code saved as personal_qrcode.png")
print("Website QR code saved as website_qrcode.png")
