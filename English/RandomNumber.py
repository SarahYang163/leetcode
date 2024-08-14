import random
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play


def change_speed(sound, speed=1.0):
    # 通过调整帧速率来改变播放速度
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


# 设置语速倍数，例如 1.0 表示正常速度，2.0 表示二倍速
speed = 1.75  # 你可以将其更改为任何你想要的速度

# 生成并读取10个随机数
for i in range(30):
    # 生成一个随机数
    number = random.randint(11, 99)
    text = f"{i + 1} : {number}"
    print('   ', text, end='')

    # 使用 gTTS 生成语音文件
    tts = gTTS(text=str(number), lang='en')
    filename = f"random_number_{i + 1}.mp3"
    tts.save(filename)

    # 加载生成的音频文件
    sound = AudioSegment.from_file(filename)

    # 调整语音播放速度
    altered_sound = change_speed(sound, speed)

    # 播放调整后的音频
    play(altered_sound)

    # 删除语音文件
    os.remove(filename)
