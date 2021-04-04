f=open("demo.txt")
lines=f.readlines()
sentence = "My name is Pratha"
for i in lines:
    print(i)
words=sentence.split()
print(words)


def greet(name):
    print("Hello" + name + ",How are u")
str1 = input("Enter the name you wish to be greeted")
greet(str1)