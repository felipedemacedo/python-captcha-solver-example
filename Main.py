try:
    from PIL import Image
    from PIL import ImageEnhance
except ImportError:
    import Image
import pytesseract # https://pypi.org/project/pytesseract/ | https://github.com/madmaze/pytesseract

black = (0,0,0)
white = (255,255,255)
threshold = (160,160,160)

# Open input image in grayscale mode and get its pixels.
img = Image.open("./in/captcha.svl").convert("LA")

# multiply each pixel by 1.2
out = img.point(lambda i: i * 1.3)

# enh = ImageEnhance.Contrast(out)
# enh.enhance(1.3).show("30% more contrast")

pixels = out.getdata()

newPixels = []
# Compare each pixel 
for pixel in pixels:
    if pixel < threshold:
        newPixels.append(black)
    else:
        newPixels.append(white)

# Create and save new image.
newImg = Image.new("RGB",out.size)
newImg.putdata(newPixels)
newImg.save("./out/newImage.jpg")

pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR/tesseract' # https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows

# Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))
print("-----------------------")
# print(pytesseract.image_to_string(Image.open('captcha (2).svl')))
# https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options
print(pytesseract.image_to_string(Image.open('./out/newImage.jpg'), lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=1234567890 --tessdata-dir="./tessdata"'))
print("-----------------------")