# python3

def read_input():
    str = input()

    if "I" in str:
        p = input()
        t = input()   
    elif "F" in str:
        fileName = "./tests/"+ input()
        file = open(fileName, "r")
        p = file.readline()
        t = file.readline()

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    return (p.rstrip(), t.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    output = []
    pl = len(pattern)
    tl = len(text)
    # this function should find the occurances using Rabin Karp alghoritm 
    for i in range(tl-pl+1):
        if hash(text[i:i+pl]) == hash(pattern):
            if text[i:i+pl] == pattern:
                output.append(i)
    # and return an iterable variable
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    