#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#HelperFunctions.py

def ParseKIF(content):
    arrify = content.replace("(","")
    arrify = arrify.replace(")","")
    arrify = arrify.split(" ")

    if(len(arrify) == 4):
        sub_arry = [arrify.pop(1)]
        sub_arry.append(arrify.pop(1))
        arrify.insert(1,sub_arry)
    return arrify
    