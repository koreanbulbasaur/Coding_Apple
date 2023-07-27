from PIL import Image
img = Image.open(r'part3\img\photo1.jpg')

# 이미지 크기 조절
# img.resize((300, 500))
# img.save(r'part3\img\resize_photo1.jpg', qulity=100)

# 비율 유지하며 리사이즈하는 법
# img.thumbnail((300, 500))
# img.save(r'part3\img\thum_photo1.jpg')

# 이미지 자르기
# img = img.crop((50, 50, 150, 150))
# img.save(r'part3\img\crop_photo1.jpg')

# 흑백 변환
# img = Image.open(r'part3\img\photo1.jpg').convert('L')
# img.save(r'part3\img\gray_photo1.jpg')

import os
adress = os.getcwd()
files = os.listdir(adress+'\part3\img')
count = 0
for i in files:
    count += 1

print(count)