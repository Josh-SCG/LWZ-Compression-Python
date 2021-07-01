'''
# will be followed by explination of my code implementations or remarks about it
#!!! will indicate the pseudocode counterparts given in ITRI615
'''

import cv2 #needed for image to array formatting

#The fact that this function doesn't exist as a part of dictionary methods???
def get_Key_From_Value(val, dict):
    for key, value in dict.items():
         if val == value:
             return key

#Compress/Encode Algorithm
def LWZ_Encode(uncompressed):
    #code table is set as a dictionary as to store both the code and 'array' as a part of one data type
    #- i.e. 256: '1,1'

    max = 256 #Current implementation will only function on values 0 - 255
    code_Table = {int(i): str(i) for i in range(max)}                           #!!! initial code table: 0-255


    series = str(uncompressed.pop(0))                                           #!!! series <= 1st character
    compressed = [] #the output array

    for char in uncompressed:                                                   #!!! while(new input available)

        combo = series+","+char # not memory optimised
        if combo in code_Table.values():                                        #!!! if(series+char is in codetable)
            series = combo                                                      #!!! series = series + char

        else:
            compressed.append(get_Key_From_Value(series, code_Table))           #!!! output code for series
            code_Table[max] = combo                                             #!!! feed series+char in codetable
            max += 1 #move on to next new code
            series = char                                                       #!!! series <= char

    if series: #if there is anything left in series
            compressed.append(get_Key_From_Value(series, code_Table))           #!!! output code for series

    return compressed #end

def LWZ_Decode(compressed):
    max = 256
    code_Table = {int(i): str(i) for i in range(max)}                           #!!! initial code table: 0-255

    uncompressed = []
    series = []

    old_Code = compressed.pop(0)                                                #!!! old code <= 1st input
    uncompressed.append(int(old_Code))                                          #!!! output value of old code

    for new_Code in compressed:
        if int(new_Code) in code_Table.keys():
            temp = code_Table[int(old_Code)]
            series.append(temp[:])

        elif int(new_Code) == max:
            series.clear()
            series.append(old_Code)
            series.append(old_Code)
        else:
            raise ValueError('Bad compressed k: %s' % new_Code)

        uncompressed.append(series[:])
        code_Table[max] = old_Code +","+ series[0]
        max += 1
        old_Code = new_Code



    print(code_Table)
    return uncompressed

def intArray_to_strArray(array):
    for item in array:
        for j in range(len(item)):
            item[j] = str(item[j])
    return array

img = (cv2.imread('some.jpg'))
gray = (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)).tolist()

#array = intArray_to_strArray(gray)

def int_str(arr):
    for j in range(len(arr)):
        arr[j] = str(arr[j])
    return arr



arr = [1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4]
arr2 = int_str(arr)
test = LWZ_Encode(arr2)
print(test)
test2 = LWZ_Decode(int_str(test))
print(test2)

'''
compressed_Matrix = []
for item in array:
    compressed = LWZ_Encode(item)
    compressed_Matrix.append(compressed)
print(compressed_Matrix)

decompressed_Matrix = []
for thing in compressed_Matrix:
    decompressed = LWZ_Decode(thing)
    decompressed_Matrix.append(decompressed)
print(decompressed_Matrix)
'''
