#习题6.1 编写一个while循环，从字符串的最后一个字符开始，反向逐一处理，直到字符串的第一个字符，一行显示一个字母。

word =input("输入单词：")
print("输入的单词为：",word)
index = len(word) - 1
print("倒序输出为：")
while index >= 0:
    letter = word[index]
    print(letter)
    index = index - 1

#asdfasdfasdfsadf