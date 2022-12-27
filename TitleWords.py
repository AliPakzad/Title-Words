"""
The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship.
This video was captured by one of our heroes who wishes peace


output:
    
2:Persian
3:League
15:Iran
17:Persian
18:League

"""
s = input()

str_array  = s.split()
i = 1
titleWords = []

while i < len(str_array):
    str_array[i]
    word = str_array[i]
    if word.istitle():
        if word[-1] == ".":
            titleWords.append(f"{i+1}:{word[:-1]}")
            i = i + 2
        elif word[-1] == ",":
            titleWords.append(f"{i+1}:{word[:-1]}")
            i = i + 1
        else:
            titleWords.append(f"{i+1}:{word}")
            i = i +1
    else:
        i = i + 1

if len(titleWords) > 0:
    for i in range(len(titleWords)):
        print(titleWords[i])
else:
    print("None")
