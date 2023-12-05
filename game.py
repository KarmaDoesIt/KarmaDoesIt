def play (): 
    a = 0
    c = 0
    f = 0
    print ("This is you.")
    yourname = (input("What is your name?\n"))
    print ("\nOkay, your name is,",yourname)
    print ("\nWell... I don't like your name. So your name will now be Dumby. Little Dumby. Big Dumby. See? It fits you perfectly!")

    print ("Anyway, because we all struggle in life, you will go through the trails of a programming student to see if you'd pass or fail!")
    print ("Don't be a Dumby though or else, you'll FAIL!")
    print ("\nYou got that? Great!")
    print ("Now, let's begin with your test!")

    print ("\nAlright Dumb Dumb. Yes I've upgraded your name. Congratulations!")


    print ("\nYour friends just invited you to hang out! You're about to play the most epic game together. But... OH NO! You got a test tomorrow!")
    print ("\nWhat do you do Dumby? (input a number)")
    answer1 = int(input("1.Say no and study\n2.Play but study after\n3.Don't study, You got it!\n"))
    if answer1 == 1:
        a += 1
        print ("Congrats! You passed the test with a B-!")
    elif answer1 == 2:
        print ("You get so tired after reviewing a few questions and passed out... You got a C.")
        c += 1
    elif answer1 == 3:
        print ("Don't study, You got it!")
        f += 1
    else:
        print ("Please print a valid number")
    print ("\nYou get how it works now? It's about time. Because you got two more comin' your way!")
    print ("Better listen up dumb dumb, cause it only gets harder!\nYou are completing an assignment for class and have become stumped. Nothing seems to be working right and you don't know whats wrong.\nWhat do you do?")
    answer2 = int(input("1.Phone a friend\n2.Google it\n3.Try your best\n"))
    if answer2 == 1:
        a += 1
        print ("Two heads are better than one! Good job Dumby! You got a 100, and so did your friend!")
    elif answer2 == 2:
        print ("You plagiariser! Irredeemable, TO THE OFFICE! An F for your malpractices.")
        f += 1
    elif answer2 == 3:
        print ("You tried...? and that's what counts! You got some points and you got...\n... A C+ on the assignment... good on you?")
        c += 1
    else:
        print ("Please print a valid number")
    print ("Well, you've done well so far... Though I may be wrong, who knows, I'm just the artist.\nAlright, last test in 3...\n2...\n1...")
    print ("THINK FAST YOUR PRESENTING:")
    answer3 = int(input("1.I...What?\n2.I tried my best so here's what I got.\n3.I kinda know what's on there???\n4.What is going on.\n5.Help.\n6.My output is 0.\n"))
    if answer3 == 1 or 6:
        a += 1
    elif answer3 == 2 or 4:
        c += 1
    elif answer3 == 3 or 5:
        f += 1
    else:
        print ("Please print a valid number")

    print ("Hmm...\nWell...")

    def passed():
        print ("You... \nYOU! You passed. You passed so well it brought tears to my eyes.\nYou should go to Harvard! Amazing job,", yourname,"\nThank you for playing!")
    def failed():
        print ( "I expected this... YOU ARE A DUMBY!!! YOU FAILED! Womp womp wooooommmppp!\nThank you for playing!")
    def youmadeit():
        print ("You... made it!\nGood job. You are exactly like me, so I'll grant you back your name.\nGood job,",yourname)
        print ("Thank you for playing!")
    if (a>c) and (a>f):
        passed()
    elif (c>a) and (c>f):
        youmadeit()
    elif (f>a) and (f>c):
        failed()
    else:
        failed()