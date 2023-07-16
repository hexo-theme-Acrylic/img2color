#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from PIL import Image
import requests
import io
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def img2color():
  if request.method == 'GET':
    image_url = request.args.get('img')  # 从查询参数中获取图片链接
  elif request.method == 'POST':
    image_url = request.form.get('img')  # 从请求体中获取图片链接
  if not image_url:
    return "This is img2color API.Please pass the '?img=' parameter when invoking the img", 200
  response = requests.get(image_url)
  image = Image.open(io.BytesIO(response.content))
  image.thumbnail((100, 100))
  main_color = image.getpixel((0, 0))
  hex_color = '#%02x%02x%02x' % main_color
  return hex_color
if __name__ == '__main__':
    app.run()
