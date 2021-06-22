'''
https://pynote.readthedocs.io/en/latest/DataTypes/Touples.html
https://python-reference.readthedocs.io/en/latest/docs/functions/cmp.html

'''

def LWZ_Encode(array):
    char = array[0]
    series = ()????
    for item in array:
        #No need for an actual code table; checking if 0-255 with <256
        if(char+series < 256):
            series += char

        else:
            out.Series
            code_Table.append(series+char)
            series = char

    out.Series

    return encoded_Array

def LWZ_Decode(array):
    code_Table = create_Code_Table()
    new_Code = array[0]

    while(input):
        if(new_Code !in code_Table):
            series = old_Code
            series += old_Code

        else:
            series = new_Code

        out.series
        char = series[0]
        code_Table.append(old_Code+char)
        old_Code = new_Code

    return decoded_Array

'''
import cv2
import numpy as np



#Lists must be in correct order to be picked up
#If Series has multiple numbers - needs to be in a seperate list
def check_For_Sublist(list1, list2):
   l1 = [item for item in list1 if item in list2]
   l2 = [item for item in list2 if item in list1]
   return l1 == l2

def create_Code_Table():
    code_Table = []
    for i in range(0,256):
        code_Table.append(str(i))
    return code_Table


def LWZ_Encode(array):
    code_Table_Size = 256
    #code_Table = {str(int(i)): str(int(i)) for i in range(code_Table_Size)}
    code_Table = create_Code_Table()

    char = []
    result = []
    buffer = []
    for item in array:
        buffer.append(item)
        series = char + buffer
        buffer.clear()
        if check_For_Sublist(series,code_Table):
            char = series
        else:
            result.append(code_Table[char])
            code_Table[series] = code_Table_Size
            code_Table_Size += 1
            char = item

    for value in code_Table.values():
	       print(value)
    if char:
        result.append(code_Table[tuple(char)])

    return result



def LWZ_Decode(encode):

    code_Table_Size = 256
    code_Table = {chr(i): chr(i) for i in range(code_Table_Size)}


    char = result = encode.pop(0)
    for thing in encode:
        if thing in code_Table:
            entry = code_Table[thing]
        elif thing == code_Table_Size:
            entry = char + char[0]
        else:
            raise ValueError('Bad compressed k: %s' % thing)
        result += entry

        code_Table[code_Table_Size] = char + entry[0]
        code_Table_Size += 1

        char = entry
    return result


#img = (cv2.imread('some.jpg'))
#gray = (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)).tolist()

compressed = LWZ_Encode([1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4])
print (compressed)
#decompressed = LWZ_Decode(compressed)
#print (decompressed)

'''
