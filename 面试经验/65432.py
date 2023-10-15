

import pygame
import requests
response = requests.get('https://dict.youdao.com/dictvoice?type=1&audio=responsibility responsibility').content  # 替换为实际的音频请求地址

# 发送请求
# url = "http://example.com/api/audio"  # 替换为实际的接口 URL
# response = requests.get(url)

# 保存音频文件到临时文件
audio_file = "temp.mp3"  # 临时文件名
with open(audio_file, 'wb') as f:
    f.write(response)

# 初始化 pygame
pygame.init()

# 加载音频文件
pygame.mixer.music.load(audio_file)

# 播放音频
pygame.mixer.music.play()

# 等待音频播放完毕
while pygame.mixer.music.get_busy():
    continue

# 清除临时文件
pygame.mixer.music.stop()
pygame.quit()