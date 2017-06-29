#f = open('war_and_peace.txt')

with open('war_and_peace.txt') as f:

    # loop through each line, printing each
    for lines in f:
        print(lines)

    # We have reached the end of the file so this will do nothing
    print('read line call = ', f.readline())

    # This will bring us back to the beginning of the file
    # It is going to the 0th byte of the file
    f.seek(0)

    # This will now print the first line of the file
    print('read line call2 = ', f.readline())
    
    f.seek(0)
    for lines in f:
        if 'war' in lines:
            print(lines)

    f.seek(0)
    w = open('output.txt', 'w')
    for lines in f:
        if 'war' in lines:
            w.write(lines)
    w.close()
