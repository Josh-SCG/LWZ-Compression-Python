'''
Esterhuizen, J 30285976
# will be followed by explination of my code implementations or remarks about it
#!!! will indicate the pseudocode counterparts given in ITRI617
'''
import cv2 #used for image handling, installed via pip install opencv
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

    #print("input\tseries\t\tchar\tcodeTable\t\toutput")
    breakable_uncompressed = uncompressed
    series = str(breakable_uncompressed.pop(0))                                 #!!! series <= 1st character
    compressed = [] #the output array
    #print("\t",series)
    for char in breakable_uncompressed:                                         #!!! while(new input available)

        combo = series+","+char # not memory optimised
        if combo in code_Table.values():                                        #!!! if(series+char is in codetable)
            series = combo                                                      #!!! series = series + char
            #print(char,"\t",series,"\t\t",char)

        else:
            compressed.append(get_Key_From_Value(series, code_Table))           #!!! output code for series
            code_Table[max] = combo                                             #!!! feed series+char in codetable
            max += 1 #move on to next new code
            #print(char,"\t",series,"\t\t",char,"\t",max-1,"=",combo,"\t\t",get_Key_From_Value(series, code_Table))
            series = char                                                       #!!! series <= char

    if series: #if there is anything left in series
            compressed.append(get_Key_From_Value(series, code_Table))           #!!! output code for series
            #print("\t\t\t\t\t\t\t\t",get_Key_From_Value(series, code_Table))
    return compressed #end


def LWZ_Decode(compressed):
    max = 256
    code_Table = {int(i): str(i) for i in range(max)}                           #!!! initial code table: 0-255

    #print("newCode\toldCode\tcodetable\t\t\t\t\t\trough output (proper output on GUI)")
    uncompressed = []
    series = []
    char = ''
    breakable_compressed = compressed
    old_Code = breakable_compressed.pop(0)                                      #!!! old code <= 1st input
    char = code_Table[int(old_Code)]                                            #!!! char <= value for old code
    uncompressed.append(char)                                                   #!!! output value of old code
    #print("\t",old_Code,"\t\t\t\t\t\t\t\t",char)

    for new_Code in breakable_compressed:                                       #!!! while(still input left)
        if int(new_Code) == max:                                                #!!! if newcode not in table
            series.clear()                                                      #\
            series.append(int(old_Code))                                        #!!! series <= series + value of old code**
            series.append(char)                                        #/

        elif int(new_Code) in code_Table.keys():                                #!!! else
            series.clear()
            series.append(new_Code)                                             #!!! series <= value new code**


        else: #error handling in case compressed data is out of order
            raise ValueError(new_Code," not existing")


        for item in series:
            if(str(item).isnumeric()):
                uncompressed.append(code_Table[int(item)])                          #!!! output series **values switched here
            else:
                for thing in item:
                    if(str(thing).isnumeric()):
                        uncompressed.append(code_Table[int(thing)])                          #!!! output series **values switched here
                    else:
                        for piece in thing:
                            uncompressed.append(code_Table[int(piece)])

        arr =[]
        if int(series[0]) > 256:
            arr.append(series[0])
            char = arr[0]
        else:
            char = series[0]                                                    #!!! char <= 1st char of series

        char_oldCode_together = []
        char_oldCode_together.append((code_Table[int(old_Code)]))
        char_oldCode_together.append((code_Table[int(char)]))

        code_Table[max] = char_oldCode_together                                 #!!! add old code value + char by codetable
        #print(max,"=",char_oldCode_together)
        max += 1


        #print(new_Code,"\t",old_Code,"\t",max-1,"=",char_oldCode_together,"\t\t\t\t\t",series)
        old_Code = new_Code                                                     #!!! old code <= new code


    #print("\nFull Output",uncompressed)
    return uncompressed


img = (cv2.imread('some.jpg'))
array = (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)).tolist()

compressed_Matrix = []
for item in array:
    compressed = LWZ_Encode(intArray_To_StrArray(item))
    compressed_Matrix.append(compressed)
    print(compressed)

print("\n\nDECOMPRESSED")
decompressed_Matrix = []
for thing in compressed_Matrix:
    decompressed = LWZ_Decode(intArray_To_StrArray(thing))
    decompressed_Matrix.append(decompressed)
    print(decompressed)

#GUI Section
root = tk.Tk()
root.title("LWZ Assignment - IMAGE")
root.geometry('450x150')
root.configure(background='#99500f') #rrggbb - 00 to ff
tk.Label(root,text = "Application must be restarted upon completion!",background='#99500f',font=(25)).grid(row=0,column=0,padx=5,pady=5)
tk.Label(root,text = "All work done via CMD",background='#99500f',font=(30)).grid(row=1,column=0,padx=5,pady=5)
tk.Label(root,text = "Joshua Esterhuizen (30285976)\nITRI617 Assignment-IMAGE",justify='left',background='#99500f',font=(6)).grid(row=2,column=0,padx=5,pady=5)




root.mainloop()
