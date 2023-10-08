# import sys
#
#
# class Solution:
#     def process(self, nums: list) -> int:
#         res = -sys.maxsize + 1
#         temp = 0
#         for num in nums:
#             temp = max(num, temp + num)
#             res = max(temp, res)
#         return res if res != -sys.maxsize + 1 else 0
#
#
#
#
#
# if __name__ == '__main__':
#     # res = Solution()
#     # math = int(input("数学成绩"))
#     # print(type(math))
#     # English = int(input("英语成绩"))
#     # print(type(math))
#     #
#     # sum_ = math + English
#     # print(sum_)
#     # map_ = {1: 1, 2: 2}
#     # del map_[1]
#     # print(map_)
#     # print(res.process([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#     # a = 1
#     # b = 2
#     def solution(s):
#         # Implement your solution here
#         if len(s) <= 1:
#             return s
#         if s[0] != '?' and s[-1] != '?' and s[0] != s[-1]:
#             return "NO"
#         if s[0] == '?' and s[-1] == '?':
#             for char in 'abcdefghijklmnopqrstuvwxyz':
#                 result = solution(char + s[1:-1] + char)
#                 if result is not None:
#                     return result
#         elif s[0] == '?':
#             return solution(s[-1] + s[1:])
#         elif s[-1] == '?':
#             return solution(s[:-1]+s[0])
#         else:
#             result = solution(s[1:-1])
#             if result is not None:
#                 return s[0] + result + s[-1]
#         return "NO"
#
#     # print(solution("?ab??a"))
#     print(solution("bab??a"))
#
#
#


import ebooklib
from ebooklib import epub
from gtts import gTTS

def epub_to_speech(epub_file, output_file):
    # 打开 EPUB 文件
    book = epub.read_epub(epub_file)

    # 提取文本内容
    texts = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            texts.append(item.get_content().decode())

    # 合并文本内容
    content = ' '.join(texts)

    # 将文本转换为声音
    tts = gTTS(text=content, lang='zh')  # 指定语言，这里使用英语 'en'
    tts.save(output_file)  # 保存为音频文件

# 示例使用
epub_file = '/Users/sarahyang/Downloads/长安的荔枝.epub'  # 替换为你的 EPUB 文件路径
output_file = '/Users/sarahyang/Downloads/长安的荔枝.mp3'  # 替换为输出音频文件路径

epub_to_speech(epub_file, output_file)