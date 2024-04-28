sentence = input("Please enter a sentence : ")

punctuations = "!,.*&%^)'_;?"

new_string = ""

for i in sentence:
    if i not in punctuations:
        new_string +=i

print(new_string)