#importing the needed modules
import qrcode

#Allowing user to enter the information that needs to be encoded
info = input('Welcome! Enter the Data to be encoded:\n')

#defining and seting the parameters needed to generate qrcode

#for box-size the maximium size is 10
box_size = int(input('Enter the Box size (max 10):\n'))

#for version the maximium value is 15
version = int(input('Enter the version or complexity required (max 15):\n'))

#Defining the function for an instance of qrcode

QR = qrcode.QRCode(version, box_size, border = 5)

#tuning our instance to the data user has provided
QR.add_data(info)

#Encoding the info
QR.make(fit=True)

#turning our encoded info into an image
img=QR.make_image(fill_color='black', back_color='white')

#setting the filename of our qrcode
FileName=input('What name do you want to save the QRCode:\n')

#saving our encoded message
img.save(f'{FileName}.png')

#Message informing user that QRcode has been generated
print('Your Qrcode has been produced. Kindly check your pictures')
