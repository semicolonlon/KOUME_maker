from pydub import AudioSegment
from pydub.playback import play
import os

character = (
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん",

    "が", "ぐ", "ご",
    "じ", "ず", "ぜ", "ぞ",
    "だ", "ぢ", "づ", "で", "ど",
    "ば", "び", "ぶ", 

    "ぱ", "ぷ",

    "first_part", "middle_part", "last_part"
)

audio = [None] * len(character)

for i,filename in enumerate(character):
    path = './audio_source/'+ filename + '.mp3'
    if os.path.exists(path):
        audio[i] = AudioSegment.from_file(path)
    else:
        print(path + 'is not exist')

print('小梅太夫メーカー')

script = [character.index('first_part')]

#　上の句のスクリプト提案
first_expression = input('上の句を入力してください : ')
while first_expression:
    if first_expression[0] in character:
        script.append(character.index(first_expression[0]))
    else:
        print('「' + first_expression[0] + '」の音声ファイルがありませんでした。')
    first_expression = first_expression[1:]

script.append(character.index('middle_part'))

# 下の句のスクリプト提案
last_expression = input('下句を入力してください : ')
while last_expression:
    if last_expression[0] in character:
        script.append(character.index(last_expression[0]))
    else:
        print('「' + last_expression[0] + '」の音声ファイルがありませんでした。')
    last_expression = last_expression[1:]

script.append(character.index('last_part'))

total = AudioSegment.empty()

for i in script:
    total += audio[i]

play(total)
