def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:] #we are slicing the string at a given postion then adding the chracter and then combining it again

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
