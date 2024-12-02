def listFuncs(path):
    return [item for item in dir(path) if not item.startswith("__")]
    
def load_input_lines(file_path, start_at=None, count=None):
    with open(file_path) as inp_file:
        data = inp_file.read().splitlines()
        startAt = start_at or 0
        countN = count or 10
        count = 0
        for index, item in enumerate(data):
            if index >= startAt:
                count = count + 1
                print(item)
            if count > countN:
                print(".\n.\n.\n\n{} rows more.".format(len(data) - countN))
                break
        return data

def printSingleNumList(listData, maxCount=None):
    printCount = maxCount or 50
    print(listData[:printCount], "... {} more.".format(len(listData) - printCount))
    
def printDict(dictData, maxCount=None):
    printCount = maxCount or 10
    count = 0
    for key in dictData:
        print("{}: {}".format(key, dictData[key]))
        count += 1
        if count > printCount:
            print(".\n.\n.\n\n{} more.".format(len(dictData) - printCount))
            break
