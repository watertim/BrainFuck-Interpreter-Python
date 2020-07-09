from typing import List, Any

def move(listofobj: List[Any]):
    if not isinstance(listofobj, List):
        raise TypeError
    if (len(listofobj) != 7):
        raise Exception("List Error")
    #Extract input list
    #ERROR = listofobj[0]
    #Ended = listofobj[1]
    brainfuckl = listofobj[2]
    reader = listofobj[3]
    tap = listofobj[4]
    pointer = listofobj[5]
    result = listofobj[6]

    bypass_list=[' ','\n','\r']
    execution = brainfuckl[reader]
    if (execution == '['):
        if (tap[pointer] == 0):
            bypass = 0
            while (execution != ']' or bypass != -1):
                reader += 1
                execution = brainfuckl[reader]
                if (execution == '['):
                    bypass += 1
                elif (execution == ']'):
                    bypass -= 1
                else: pass

                if (reader == len(brainfuckl) - 1):
                        result = "<SyntaxError> Found mismatched square brackets!\n"
                        return [True, True, brainfuckl, reader, tap, pointer, result]
    elif(execution == ']'):
        if (tap[pointer] != 0):
            bypass = 0
            while (execution != '[' or bypass != -1):
                reader -= 1
                execution = brainfuckl[reader]
                if (execution == ']'):
                    bypass += 1
                elif (execution == '['):
                    bypass -= 1
                else: pass

                if (reader == 0):
                        result = "<SyntaxError> Found mismatched square brackets!\n"
                        return [True, True, brainfuckl, reader, tap, pointer, result]
    elif (execution == '>'):
        if (len(tap) == pointer + 1):
            tap += [0]
        pointer += 1
    elif (execution == '<'):
        pointer -= 1
    elif (execution == '+'):
        if (tap[pointer] == 255):
            tap[pointer] = 0
        else:
            tap[pointer] += 1
    elif (execution == '-'):
        if (tap[pointer] == 0):
            tap[pointer] = 255
        else:
            tap[pointer] -= 1
    elif (execution == '.'):
        result += chr(tap[pointer])
    elif (execution == ','):
        result = "<NotImplementedError> Not implement the input yet!\n"
        return [True, True, brainfuckl, reader, tap, pointer, result]
    elif (execution in bypass_list):#Just bypass
        result = result
    else:
        result = "<SyntaxError> Not a vaild brainfuck code!\n"
        return [True, True, brainfuckl, reader, tap, pointer, result]

    if (reader == len(brainfuckl) - 1):
        return [False, True, brainfuckl, reader, tap, pointer, result]
    else:
        reader += 1
        return [False, False, brainfuckl, reader, tap, pointer, result]


def interpreter(brainfuckstr: str) -> str:
    if not isinstance(brainfuckstr, str):
        raise TypeError
    #print(brainfuckstr)
    ERROR = False
    END = False
    brainfuckl = [i for i in brainfuckstr] #brainfuck code list(a char/a element)
    reader = 0 #pointer for brainfuckl
    tap = [0] #data tap
    pointer = 0 #pointer for tap
    result = "" #output
    while True:
        [ERROR, END, brainfuckl, reader, tap, pointer, result] = move([ERROR, END, brainfuckl, reader, tap, pointer, result])
        if (END):
            break
    return [ERROR, result]

if __name__ == '__main__':
    inp = input()
    print(interpreter(inp))


#interpreter("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.,")
#interpreter("+]+++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++.")
#interpreter(">>----[---->+<]>++.++++++++.++++++++++.>-[----->+<]>.+[--->++<]>+++.>-[--->+<]>-.[---->+++++<]>-.[-->+<]>---.[--->++<]>---.++[->+++<]>.+[-->+<]>+.[--->++<]>---.++[->+++<]>.+++.[--->+<]>----.[-->+<]>-----.[->++<]>+.-[---->+++<]>.--------.>-[--->+<]>.-[----->+<]>-.++++++++.--[----->+++<]>.+++.[--->+<]>-.-[-->+<]>---.++[--->+++++<]>.++++++++++++++.+++[->+++++<]>.[----->+<]>++.>-[----->+<]>.---[->++<]>-.++++++.[--->+<]>+++.+++.[-]")
#interpreter(">+++ [<++++ >-] <-[>>+++ [<+++ >-] < [>>+ >+ >+ [<]<-] >>- - >>++ >++++ >+++ [<]<<-]>>>. >--. >. >. >-. >>+++ [<+++ >-] <- [>>>+++ [<<+++ >>-] <++++ <<-] >+. >. >>+++ [<+++ >-] <[>>+++ [<++++ >-]< [>>+ >+ >+ >+ [<]<-] >>>>+ >- [<]<<-]>>>. >+++. >+. >++. >>+++ [<+++ >-]< [>+++ <-] >+++++. >>+++ [<++++ >-] <-[>>+++ [<++++ >-] <- [>>+ >+ >+ [<] <-] >>>- >>+++ [<] <<-]>>>. >+. >----. >.")