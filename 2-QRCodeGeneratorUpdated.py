import qrcode

# Prompt user to enter data to be encoded
while True:
    info = input('Welcome! Enter the Data to be encoded:\n')
    if info:
        break
    else:
        print('Invalid input. Please enter a non-empty string.')

# Prompt user to enter box size, version, and error correction level
while True:
    try:
        box_size = int(input('Enter the Box size (max 10): '))
        version = int(input('Enter the version or complexity required (max 15): '))
        error_correction = int(input('Enter the error correction level (0-3): '))
        if 1 <= box_size <= 10 and 1 <= version <= 15 and 0 <= error_correction <= 3:
            break
        else:
            print('Invalid input. Please enter values within the specified range.')
    except ValueError:
        print('Invalid input. Please enter integer values.')

# Create QR code instance
qr = qrcode.QRCode(version, error_correction=error_correction, box_size=box_size, border=5)

# Add data to QR code instance
qr.add_data(info)

# Generate QR code image
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

# Prompt user to enter filename
while True:
    filename = input('Enter the filename to save the QR code as (without extension): ')
    if filename:
        break
    else:
        print('Invalid input. Please enter a non-empty string.')

# Save QR code image to file
try:
    img.save(f'{filename}.png')
    print(f'QR code saved as {filename}.png')
except IOError:
    print('Error: Failed to save QR code to file.')
