import qrcode
from PIL import Image
import pandas as pd
import base64


df = pd.read_excel('Old products list.xlsx')
IcecatID = df.IcecatID.tolist()
for i in range(df.count().IcecatID):
    '''
    1. QRCode Generator with icon for xlsx file
    2. And also converting it to base 64
    3. Writing bytes to file with
    '''
    one_row = df.loc[i].to_list()
    # print(one_row)
    rem = one_row.pop(0)
    # print(rem)
    qr = qrcode.QRCode(
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(str(rem))
    qr.make()
    img_qr_big = qr.make_image().convert('RGB')
    logo = Image.open('image.png')
    pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
    img_qr_big.paste(logo, pos)
    img_qr_big.save(f'images/{str(i)}.png')

    # # Converting image to base64
    # with open(f'images/{str(i)}.png', 'rb') as img_file:
    #     my_string = base64.b64encode(img_file.read())

    # # Creating txt file for base64 data
    # with open(f'images/{str(i)}.txt', 'wb') as text_file:
    #     text_file.write(my_string)
