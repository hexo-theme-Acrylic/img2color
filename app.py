#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from api.index import img_to_color


app = Flask(__name__)

@app.route('/')
def index():
  return "This is Marcus's API, /v1/ is public, /v2/ is private."

@app.route('/v1/')
def index_v1():
  return "This is Marcus's public API."

@app.route('/v2/')
def index_v2():
  return "This is Marcus's private API. "

# theme_color
@app.route('/v1/img2color', methods=['POST', 'GET'])
def img2color():
  if request.method == 'GET':
      image_url = request.args.get('img')  # 从查询参数中获取图片链接
  elif request.method == 'POST':
      image_url = request.form.get('img')  # 从请求体中获取图片链接

  if not image_url:
      return "No image URL provided. Please pass the '?img=' parameter when invoking the img", 400

  main_color = img_to_color(image_url)  # 调用颜色提取函数

  return main_color


if __name__ == '__main__':
    app.run()
