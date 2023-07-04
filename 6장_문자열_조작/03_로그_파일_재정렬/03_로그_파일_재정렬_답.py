def reorder(logs):
    char, num = [], []
    
    for log in logs:
        if log.split()[1].isdigit():
            num.append(log)
        else:
            char.append(log)
            
    char.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return char + num

print(reorder(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))