from PIL import Image
import requests
import io

def img_to_color(image_url):
  response = requests.get(image_url)
  image = Image.open(io.BytesIO(response.content))

  # 调整图像大小，加快颜色提取速度
  image.thumbnail((100, 100))

  # 获取图像中的主题颜色
  main_color = image.getpixel((0, 0))

  # 将颜色转换为十六进制表示形式
  hex_color = '#%02x%02x%02x' % main_color

  return hex_color
