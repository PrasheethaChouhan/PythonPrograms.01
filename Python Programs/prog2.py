sentence = input("enter a sentence")
count = 0
wc = 0
for i in sentence:
    if(i==' '):
        wc = wc+1
    else:
        count = count+1
print(wc+1)
print("the number of letters",count)