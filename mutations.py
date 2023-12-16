def mutate_string(string, position, character):
    stripped = string[:position] + character + string[position+1:]        
    return stripped

