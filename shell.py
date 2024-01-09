import yeep

print("Yeep Programming Language")
print("Programme Written and Developed by Yipmong Said")
while True:
    text = input("yeep >> ")
    print(text)
    result = yeep.run("<stdin>", text)

    if isinstance(result, list):
        for error in result:
            print(error.as_string())
    else:
        print(result)
