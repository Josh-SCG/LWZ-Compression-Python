'''
# will be followed by explination of my code implementations or remarks about it
#!!! will indicate the pseudocode counterparts given in ITRI615
'''
import cv2 #needed for image to array formatting
import tkinter as tk


#The fact that this function doesn't exist as a part of dictionary methods???
def get_Key_From_Value(val, dict):
    for key, value in dict.items():
         if val == value:
             return key


#Formating functions
def intArray_To_StrArray(arr):
    for j in range(len(arr)):
        arr[j] = str(arr[j])
    return arr

def strArray_To_intArray(arr):
    for j in range(len(arr)):
        arr[j] = int(arr[j])
    return arr


#Compress/Encode Algorithm
def LWZ_Encode(uncompressed):
    #code table is set as a dictionary as to store both the code and 'array' as a part of one data type
    #- i.e. 256: '1,1'

    max = 256 #Current implementation will only function on values 0 - 255
    code_Table = {int(i): str(i) for i in range(max)}                           #!!! initial code table: 0-255

    breakable_uncompressed = uncompressed
    series = str(breakable_uncompressed.pop(0))                                           #!!! series <= 1st character
    compressed = [] #the output array

    for char in breakable_uncompressed:                                                   #!!! while(new input available)

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
    char = ''
    breakable_compressed = compressed
    old_Code = breakable_compressed.pop(0)                                                #!!! old code <= 1st input
    char = (code_Table[int(old_Code)])                                       #!!! char <= value for old code
    uncompressed.append(char)                                                   #!!! output value of old code

    for new_Code in breakable_compressed:                                                 #!!! while(still input left)
        if int(new_Code) == max:                                                #!!! if newcode not in table

            series.clear()                                                      #\
            series.extend((code_Table[int(old_Code)]))                          #!!! series <= series + value of old code
            series.extend(char)                                                 #/

        elif int(new_Code) in code_Table.keys():                                #!!! else
            series.clear()
            series.append(code_Table[int(new_Code)])                            #!!! series <= value old code

        else: #error handling in case compressed data is out of order
            raise ValueError(new_Code," not existing")


        uncompressed.extend(series)                                             #!!! output series
        char = series[0]                                                        #!!! char <= 1st char of series

        char_oldCode_together = []
        char_oldCode_together.extend(code_Table[int(old_Code)])
        char_oldCode_together.extend(char)
        code_Table[max] = char_oldCode_together                                 #!!! add old code value + char by codetable
        max += 1

        old_Code = new_Code                                                     #!!! old code <= new code

    return(uncompressed)



'''
def image_TO_Array():
    cv2_Data = (cv2.imread("some.jpg"))
    array = (cv2.cvtColor(cv2_Data, cv2.COLOR_BGR2GRAY)).tolist()
    return array



array = image_TO_Array()
print(array[0])
compressed_Matrix = []
for item in array:
    compressed = LWZ_Encode(intArray_To_StrArray(item))
    compressed_Matrix.append(compressed)
print(compressed_Matrix[0])

decompressed_Matrix = []
for thing in compressed_Matrix:
    decompressed = LWZ_Decode(intArray_To_StrArray(thing))
    decompressed_Matrix.append(decompressed)
print(decompressed_Matrix[0])
'''

input = [1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4]
compressed = []
decompressed = []



root = tk.Tk()
root.title("LWZ Assignment")
root.geometry('800x230')
root.configure(background='#99500f') #rrggbb - 00 to ff
tk.Label(root,text = "Application must be restarted upon completion!",background='#99500f',font=(25)).grid(row=4,column=1,padx=5,pady=5)
tk.Label(root,text = "Input => ",background='#99500f',font=(25)).grid(row=1,column=0,padx=5,pady=5)
tk.Label(root,text = str(input),background='#99500f',font=(25)).grid(row=1,column=1,padx=5,pady=5)


def howTo():
    popUp = tk.Tk()
    tk.Label(popUp,text = "The original input is shown on the window",font=('Arial',18)).pack()
    tk.Label(popUp,text = "'Encode' will compress the values and present the new values via pop-up",font=('Arial',18)).pack()
    tk.Label(popUp,text = "'Decode' will decompress the values and present the new values via pop-up",font=('Arial',18)).pack()
    tk.Label(popUp,text = "\nThe cmd screen will display the actual process, albeit messy",font=('Arial',18)).pack()
    popUp.attributes("-topmost", True)


def encode():
    global compressed, input
    compressed = LWZ_Encode(intArray_To_StrArray(input))
    tk.Label(root,text = str(compressed),background='#99500f',font=(25)).grid(row=2,column=1,padx=5,pady=5)



def decode():
    global decompressed
    decompressed = LWZ_Decode(intArray_To_StrArray(compressed))
    tk.Label(root,text = str(decompressed),background='#99500f',font=(25)).grid(row=3,column=1,padx=5,pady=5)




howToButton = tk.Button(root,bg="#bbffff",command=howTo, text = "How To Use",width = 17,height=2)
howToButton.grid(row=0,column=0,padx=5,pady=5)
encodeButton = tk.Button(root,bg="teal",command=encode, text = "Encode",width = 17,height=2)
encodeButton.grid(row=2,column=0,padx=5,pady=5)
decodeButton = tk.Button(root,bg="teal",command=decode, text = "Decode",width = 17,height=2)
decodeButton.grid(row=3,column=0,padx=5,pady=5)

root.mainloop()
