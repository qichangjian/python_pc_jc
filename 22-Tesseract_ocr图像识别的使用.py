import pytesseract
from PIL import Image

# Tesseract_ocr验证码图像系别技术Demo

# 打开文件的Image
# pytesseract图像识别的

img = Image.open('yzm1.png')
code = pytesseract.image_to_string(img)
print(code)
