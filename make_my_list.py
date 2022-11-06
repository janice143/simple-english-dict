#!/bin/python3
# make your own word list from a "mylist.json" file
import json, os

# merged_json = {}
# my_words = []

# 取出我的单词列表
with open(os.path.join("mylist.json"), "r") as input_file:
    contents = input_file.read()
    my_words = json.loads(contents)

# 取出合成的单词库json
with open(os.path.join("processed", "merged.json"), "r") as input_file:
    contents = input_file.read()
    merged_json = json.loads(contents)


# 按照我的单词列表，在合成单词库中查找，并取出
my_words_json = {}
for word in my_words:
    if word.upper() in merged_json:
        data = merged_json[word.upper()]
        meaning = []
        if len(data["MEANINGS"]) > 0:
            if len(data["MEANINGS"][0]) > 1:
                meaning = data["MEANINGS"][0][:2:]
            # else:
            #     print(word)
        else:
            meaning = data["SYNONYMS"]
            # print(word,data)

        my_words_json[word.upper()] = {
            # 选择第一个解释，解释的第一个元素为词性，第二个解释内容，拼接出来
            # 如果没有解释，那么用同义词代替
            # Lst[ Initial : End : IndexJump ]
            "MEANINGS": meaning
        }

# print(my_words_json)

output_file = open(os.path.join("processed", "my_words_list.json"), "w")
output_file.write(json.dumps(my_words_json))

print("Wrote out processed/my_words_list.json")