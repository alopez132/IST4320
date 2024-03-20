def z_presser():
    binholder = 0
    userinput = '0'
    while(userinput != 'z'): # has to be the 'z' key
        print("Type in a number:")
        userinput = input()
        if(userinput.isnumeric()):
            int_input  = int(userinput)
            binholder = binholder + int_input
            print(":::::  What's the right character? ;)  :::::")
            print(binholder)
z_presser()