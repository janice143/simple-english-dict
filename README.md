# 一个简易且实用的英语词典

本项目可以生成一个简易的英语词典json格式文件 —— 单词，注释，词性，同义词，反义词。

本项目从nightblade的[simple-english-dictionary](https://github.com/nightblade9/simple-english-dictionary)的代码改造过来。在他的代码里，他编写了两个.py文件：其中一个是用来合并Json文件（合并整个词典）；另外一个是过滤一些单词，生成新的json文件。

本项目最早追溯到[Stack Overflow](https://stackoverflow.com/a/54982015/)的一个问题上。tusharlock10给出了一个解决方案[tusharlock10's dictionary repo](https://github.com/tusharlock10/Dictionary)，单词的压缩文件可以到[Dropbox](https://www.dropbox.com/s/qjdgnf6npiqymgs/data.7z?dl=1)下载。

# 使用

You can consume the data in a variety of formats:

- `data` contains the individual, raw files from tusharlock - they are broken out by letter.
- `processed/merged.json` contains a single JSON file with all the words in it.
- `processed/filtered.json` contains a version with filtered-out words, meanings, synonyms, and antonyms; you can see the list of filtered words in `data/filter_words.txt`
- `processed/my_words_list.json`，包含了一些我想要生成的单词的词典，包含单词，注释；提前准备的单词列表放在`mylist.json`文件中

# Creating your own Filtered List

You will need Python 3.x. Simply update `mylist.json` and run `python3 make_my_list.py`. Consider opening a PR, too!
