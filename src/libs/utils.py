def listFuncs(path, display=None):
    toPrint = True if display is None else display
    funcs = [item for item in dir(path) if not item.startswith("__")]
    if toPrint:
        print(funcs)
    return funcs
    
def load_input_lines(file_path, start_at=None, count=None, lineCount=None, label=None):
    with open(file_path) as inp_file:
        data = inp_file.read().splitlines()
        startAt = start_at or 0
        countN = count or 10
        lineMax = lineCount or 120
        count = 0

        if label:
            dash = "=" * 50
            print(f"\n{dash}\nInput Data : {label}\n{dash}\n")
        for index, item in enumerate(data):
            if index >= startAt:
                count = count + 1
                if len(item) > lineMax:
                    print(item[:lineMax], "... {} more.".format(len(item) - lineMax))
                else:
                    print(item)
            if count > countN:
                print(".\n.\n.\n\n{} rows more.".format(len(data) - countN))
                break
        return data
        
def printItem(data, label=None):
    if label:
        dash = "=" * 50
        print(f"\n{dash}\n{label} \n{dash}\n")
    print(data)
        
def printSingleItemList(listData, maxCount=None, label=None):
    printCount = maxCount or 50
    if label:
        dash = "=" * 50
        print(f"\n{dash}\n{label} \n{dash}\n")
    remaining = len(listData) - printCount
    print(listData[:printCount], f"... {remaining} more." if remaining > 0 else "")
    
def printMultiItemList(listData, maxCount=None, label=None):
    printCount = maxCount or 50
    if label:
        dash = "=" * 50
        print(f"\n{dash}\n{label} \n{dash}\n")
    for index, item in enumerate(listData):
        print(item)
        if index > (printCount - 1):
            print(".\n.\n.\n\n{} more items.".format(len(listData) - printCount))
            break
    
def printDict(dictData, maxCount=None):
    printCount = maxCount or 10
    count = 0
    for key in dictData:
        print("{}: {}".format(key, dictData[key]))
        count += 1
        if count > printCount:
            print(".\n.\n.\n\n{} more.".format(len(dictData) - printCount))
            break
            
print([item for item in dir() if not item.startswith("__")])
