from typing import List, Any


def move(listofobj: List[Any]):
    if not isinstance(listofobj, List):
        raise TypeError
    Ended = listofobj[0]
    brainfuckl = listofobj[1]
    reader = listofobj[2]
    tap = listofobj[3]
    pointer = listofobj[4]
    result = listofobj[5]

    instructor = brainfuckl[reader]
    if (instructor == '>'):
        if (len(tap) == pointer + 1):
            tap = tap + [0]
        pointer = pointer + 1
    elif (instructor == '<'):
        pointer = pointer - 1
    elif (instructor == '+'):
        if (tap[pointer] == 255):
            tap[pointer] = 0
        else:
            tap[pointer] = tap[pointer] + 1
    elif (instructor == '-'):
        if (tap[pointer] == 0):
            tap[pointer] = 255
        else:
            tap[pointer] = tap[pointer] - 1
    elif (instructor == '.'):
        result = result + chr(tap[pointer])
    elif (instructor == '['):
        if (tap[pointer] == 0):
            while (instructor != ']'):
                if (reader == len(brainfuckl) - 1):
                    return [True, brainfuckl, reader, tap, pointer, result]
                reader = reader + 1
                instructor = brainfuckl[reader]
    elif (instructor == ']'):
        if (tap[pointer] != 0):
            while (instructor != '['):
                if (reader == 0):
                    result = "Pointer went over beginning of the tap!(Mismatched parentheses)\n"
                    return [True, brainfuckl, reader, tap, pointer, result]
                reader = reader - 1
                instructor = brainfuckl[reader]
    elif (instructor == ','):
        result = "TODO: Implement the input.\n"
        return [True, brainfuckl, reader, tap, pointer, result]
    else:
        result = "Not a vaild brainfuck code!\n"
        return [True, brainfuckl, reader, tap, pointer, result]

    if (reader == len(brainfuckl) - 1):
        return [True, brainfuckl, reader, tap, pointer, result]
    else:
        reader = reader + 1
        return [False, brainfuckl, reader, tap, pointer, result]


def interpreter(brainfuckstr: str) -> None:
    if not isinstance(brainfuckstr, str):
        raise TypeError
    Ended = False
    brainfuckl = [i for i in brainfuckstr]
    reader = 0
    pointer = 0
    tap = [0]
    result = ""
    while True:
        [Ended, brainfuckl, reader, tap, pointer, result] = move([Ended, brainfuckl, reader, tap, pointer, result])
        if (Ended):
            break
    print(result, end="")


interpreter("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.,")
interpreter("+]+++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++.")
