'''
Esterhuizen, J 30285976
# will be followed by explination of my code implementations or remarks about it
#!!! will indicate the pseudocode counterparts given in ITRI615
'''
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

    print("input\tseries\tchar\tcodeTable\toutput")
    breakable_uncompressed = uncompressed
    series = str(breakable_uncompressed.pop(0))                                 #!!! series <= 1st character
    compressed = [] #the output array
    print("\t",series)
    for char in breakable_uncompressed:                                         #!!! while(new input available)

        combo = series+","+char # not memory optimised
        if combo in code_Table.values():                                        #!!! if(series+char is in codetable)
            series = combo                                                      #!!! series = series + char
            print(char,"\t",series,"\t",char)

        else:
            compressed.append(get_Key_From_Value(series, code_Table))           #!!! output code for series
            code_Table[max] = combo                                             #!!! feed series+char in codetable
            max += 1 #move on to next new code
            print(char,"\t",series,"\t",char,"\t",max-1,"=",combo,"\t",get_Key_From_Value(series, code_Table))
            series = char                                                       #!!! series <= char

    if series: #if there is anything left in series
            compressed.append(get_Key_From_Value(series, code_Table))           #!!! output code for series
            print("\t\t\t\t\t",get_Key_From_Value(series, code_Table))
    return compressed #end


def LWZ_Decode(compressed):
    max = 256
    code_Table = {int(i): str(i) for i in range(max)}                           #!!! initial code table: 0-255

    print("newCode\toldCode\tcodetable\t\t\t\t\trough output (proper output on GUI)")
    uncompressed = []
    series = []
    char = ''
    breakable_compressed = compressed
    old_Code = breakable_compressed.pop(0)                                      #!!! old code <= 1st input
    char = code_Table[int(old_Code)]                                            #!!! char <= value for old code
    uncompressed.append(char)                                                   #!!! output value of old code
    print("\t",old_Code,"\t\t\t\t\t\t\t",char)

    for new_Code in breakable_compressed:                                       #!!! while(still input left)
        if int(new_Code) == max:                                                #!!! if newcode not in table

            series.clear()                                                      #\
            series.append(int(old_Code))                                        #!!! series <= series + value of old code**
            series.append(char)                                                 #/

        elif int(new_Code) in code_Table.keys():                                #!!! else
            series.clear()
            series.append(new_Code)                                             #!!! series <= value new code**


        else: #error handling in case compressed data is out of order
            raise ValueError(new_Code," not existing")


        for item in series:
            uncompressed.extend(code_Table[int(item)])                          #!!! output series **values switched here

        arr =[]
        if int(series[0]) > 256:
            arr.append(code_Table[int(item)])
            char = arr[0][0]
        else:
            char = series[0]                                                    #!!! char <= 1st char of series

        char_oldCode_together = []
        char_oldCode_together.append(str(int(old_Code)))
        char_oldCode_together.append(str(char))

        code_Table[max] = char_oldCode_together                                 #!!! add old code value + char by codetable
        max += 1


        print(new_Code,"\t",old_Code,"\t",max-1,"=",char_oldCode_together,"\t\t\t\t",series)
        old_Code = new_Code                                                     #!!! old code <= new code


    fix = strArray_To_intArray(uncompressed)
    returnable = []
    for item in fix: #replaces any code table values above 255 with values of them
        returnable.append(code_Table[int(item)])
    return returnable

#Needed as global variables to function with the GUI in one script with current implementation
input = [1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4]
compressed = []
decompressed = []


#GUI Section
root = tk.Tk()
root.title("LWZ Assignment")
root.geometry('850x260')
root.configure(background='#99500f') #rrggbb - 00 to ff
#tk.Label(root,text = "Application must be restarted upon completion!",background='#99500f',font=(25)).grid(row=4,column=1,padx=5,pady=5)
#tk.Label(root,text = "Input => ",background='#99500f',font=(25)).grid(row=1,column=0,padx=5,pady=5)
tk.Label(root,text = "Joshua Esterhuizen (30285976)\nITRI617 Assignment",justify='left',background='#99500f',font=(6)).grid(row=4,column=0,padx=5,pady=5)


def howTo():
    popUp = tk.Tk()
    tk.Label(popUp,text = "'Show Input' will display the array of values given (which is the example done in class)",font=('Arial',18)).pack()
    tk.Label(popUp,text = "'Reset Input' just recompiles the origional input as the data array is used like a queue",font=('Arial',18)).pack()
    tk.Label(popUp,text = "'Encode' will compress the values and present the new values via the GUI",font=('Arial',18)).pack()
    tk.Label(popUp,text = "'Decode' will decompress the values and present the new values via the GUI - values are correct although in a rough format",font=('Arial',18)).pack()
    tk.Label(popUp,text = "The cmd screen will display the process in a somewhat messy manner",font=('Arial',20)).pack()
    popUp.attributes("-topmost", True)

def showInput():
    global input
    tk.Label(root,text = str(input),justify='left',background='#99500f',font=(25)).grid(row=1,column=1,padx=5,pady=5)


def encode():
    global compressed, input
    compressed = LWZ_Encode(intArray_To_StrArray(input))
    tk.Label(root,text = str(compressed),justify='left',background='#99500f',font=(25)).grid(row=2,column=1,padx=5,pady=5)


def decode():
    global decompressed
    decompressed = LWZ_Decode(intArray_To_StrArray(compressed))
    tk.Label(root,text = str(decompressed),justify='left',background='#99500f',font=(25)).grid(row=3,column=1,padx=5,pady=5)


def resetInput():
    global input
    input = [1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4,1,1,1,2,3,4,4,4]


howToButton = tk.Button(root,bg="#bbffff",command=howTo, text = "How To Use",width = 17,height=2)
howToButton.grid(row=0,column=0,padx=5,pady=5)
displayInputButton = tk.Button(root,bg="teal",command=showInput, text = "Show Iput",width = 17,height=2)
displayInputButton.grid(row=1,column=0,padx=5,pady=5)
resetInputButton = tk.Button(root,bg="teal",command=resetInput, text = "Reset Input",width = 17,height=2)
resetInputButton.grid(row=0,column=1,padx=5,pady=5)
encodeButton = tk.Button(root,bg="teal",command=encode, text = "Encode",width = 17,height=2)
encodeButton.grid(row=2,column=0,padx=5,pady=5)
decodeButton = tk.Button(root,bg="teal",command=decode, text = "Decode",width = 17,height=2)
decodeButton.grid(row=3,column=0,padx=5,pady=5)

root.mainloop()
