import datetime
import time
import pyttsx4


# 整点提醒休息系统
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
