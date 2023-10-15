# import wave
# import pygame
# import requests
# from pydub import AudioSegment
# import io
# import pyaudio
#
# # 假设你有一个名为response的字节码变量
# response = requests.get(
#     'https://dict.youdao.com/dictvoice?type=0&audio=responsibility responsibility responsibility').content
#
# # 使用 io.BytesIO 将字节码加载为 AudioSegment 对象
# audio = AudioSegment.from_file(io.BytesIO(response), format='wav')
#
# # 导出为 MP3 文件
# output_file = "output.mp3"  # 输出文件名
# audio.export(output_file, format='mp3')
import requests
from bs4 import BeautifulSoup

# 假设响应的HTML内容存储在一个变量中，名为response_html
# response_html = requests.get(
#     "https://fanyi.sogou.com/text?keyword=relative&transfrom=auto&transto=zh-CHS&model=general").content


# 假设 html_content 是包含 HTML 内容的字符串
html_content = requests.get(
    "https://dict.youdao.com/result?word=feedback&lang=en")
# html_content1 = requests.get(
#     "https://fanyi.baidu.com/#en/zh/spend")
# """
# <html>
# <body>
#   <div class="container">
#     <h1 class="title">标题</h1>
#     <p class="content">段落一</p>
#     <p class="content">段落二</p>
#   </div>
# </body>
# </html>
# """

# 创建 BeautifulSoup 对象，指定解析器为 lxml
soup = BeautifulSoup(html_content.text, 'lxml')

# 使用 find_all 方法提取所有具有 class="content" 的元素
# elements = soup.find(class_="word-exp")
# print(elements.text)
context = []
elements = soup.find(class_="basic").find_all(class_="word-exp")
for element in elements:
    context.append(element.text)

elements = soup.find(class_="webPhrase").find_all(class_="mcols-layout")
for element in elements:
    context.append(element.text)
elements = soup.find(class_="blng_sents_part dict-module").find_all(class_="mcols-layout")
for element in elements:
    print(element.text)
# 或者使用 select 方法结合 CSS 选择器提取具有 class="content" 的元素
# elements = soup.select('.content')
# for element in elements:
#     print(element.text)
