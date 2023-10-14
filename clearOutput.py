# import wave
# import struct
# import requests
# import simpleaudio as sa
# import numpy as np
#
# # response = requests.get(
# #     'https://dict.youdao.com/dictvoice',
# #     params={"type": 1, "audio": "English").content
# # 音频数据（假设为bytes类型的音频数据）
# response_audio_data = requests.get('https://dict.youdao.com/dictvoice',
#                                    params={"type": 1, "audio": "meditation"}).content
#
# sample_width = 2  # 16位采样宽度
# sample_rate = 44100  # 采样率
# channels = 1  # 声道数
#
# # 调整音频数据大小
# num_samples = len(response_audio_data) // sample_width
# response_audio_data = response_audio_data[:num_samples * sample_width]
#
# # 解析音频数据
# audio_data = np.frombuffer(response_audio_data, dtype=np.int16)
#
# # 创建WAV文件
# with wave.open("audio.wav", "wb") as wav_file:
#     wav_file.setsampwidth(sample_width)
#     wav_file.setframerate(sample_rate)
#     wav_file.setnchannels(channels)
#
#     # 将音频数据写入WAV文件
#     wav_file.writeframes(audio_data.tobytes())
#
# # 加载MP3音频文件
# wave_obj = sa.WaveObject.from_wave_file("audio.wav")
#
# # 播放音频
# play_obj = wave_obj.play()
#
# # 等待音频播放完毕
# play_obj.wait_done()
import datetime
import time
import pyttsx4


def speak(text):
    engine = pyttsx4.init()
    engine.setProperty('rate', 150)  # 设置语速，可以根据需要进行调整
    engine.setProperty('volume', 1)  # 设置音量，可以根据需要进行调整
    engine.say(text)
    engine.runAndWait()


def get_current_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    return hour, minute


def format_time(hour, minute):
    hour_str = str(hour)
    minute_str = str(minute).zfill(2)  # 补零处理
    return hour_str, minute_str


def speak_time(hour, minute):
    hour_str, minute_str = format_time(hour, minute)
    if hour == 0 and minute == 0:
        speak("现在是午夜整点")
    elif minute == 0:
        speak("现在是{}点整出去走动放松一下眼睛吧".format(hour_str))
    else:
        speak("现在是{}点{}分".format(hour_str, minute_str))


def main():
    while True:
        hour, minute = get_current_time()
        if minute == 0:
            speak_time(hour, minute)
        time.sleep(60)  # 每隔60秒检查一次时间


if __name__ == "__main__":
    main()
