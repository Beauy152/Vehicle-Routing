def ParseKIF(content):
    arrify = content.replace("(","")
    arrify = arrify.replace(")","")
    arrify = arrify.split(" ")
    # print("arrify:")
    # print(arrify)
    # print(len(arrify))

    if(len(arrify) == 4):
        # print('reformatting')
        sub_arry = [arrify.pop(1)]
        sub_arry.append(arrify.pop(1))
        arrify.insert(1,sub_arry)
    return arrify
    # print(arrify)
    