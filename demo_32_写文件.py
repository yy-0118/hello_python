with open("D:\\PythonProject1\\data\\水调歌头·明月几时有.txt","w",encoding="utf-8") as f:
    f.write("苏轼《水调歌头·明月几时有》\n我欲乘风归去，\n又恐惊楼玉宇，\n高处不胜寒。")

with open("D:\\PythonProject1\\data\\水调歌头·明月几时有.txt", "a", encoding="utf-8") as f:
    f.write("\n起舞弄清醒，\n何似在人间。")

with open("D:\\PythonProject1\\data\\水调歌头·明月几时有.txt", "r", encoding="utf-8") as f:
    print(f.read())
