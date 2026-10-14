A = "apple orange banana"
words = []
word = ""

for i in A:
    if i == " ":
        words.append(word)
        word = ""
    else:
        word += i
words.append(word)  


print(words[2], words[1], words[0])


B = "   Hello world!   "
print(B)

start = 0
while start < len(B) and B[start] == " ":
    start += 1

end = len(B) - 1
while end >= 0 and B[end] == " ":
    end -= 1

print(B[start : end + 1])
