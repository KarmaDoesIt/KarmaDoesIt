define y = Character("Creator")
define d = Character("Dumby")

label splashscreen:
image splash = "wut.jpg"
scene black
with Pause(1)

show text "The Programmer's Dilemma..." with dissolve
with Pause(2)

show splash at showface with dissolve
with Pause(2)

scene black with dissolve
with Pause(1)
hide text with dissolve
with Pause(1)

return

transform showface:
    yalign 0.2
    xalign 0.5
init:
    $ a = 0
    $ c = 0
    $ f = 0

label start:


scene bg room:
image bg1 = "bg room1.jpg"
show bg1
image you1 = "You1.png"
show you1 at showface


y "This is you."

y "What is your name?"

python:
 yourname = renpy.input("What is your name?", length=32)

y "Okay, your name is, [yourname]"
y "Well... I don't like your name. So your name will now be Dumby. Little Dumby. Big Dumby. See? It fits you perfectly!"
image you5 = "You5.png"
show you5 at showface
with vpunch
y "Anyway, because we all struggle in life, you will go through the trails of a programming student to see if you'd pass or fail!"
y "Don't be a Dumby though or else, you'll FAIL!"
hide you5
show you1 at showface
y "You got that? Great!"
y "Now, let's begin with your test!"


hide you1 with dissolve

image bg2 = "bg3.jpg"
show bg2
image you2 = "You2.png"

y "Alright Dumb Dumb. Yes I've upgraded your name. Congratulations!"
show you2 at showface

y "Your friends just invited you to hang out! You're about to play the most epic game together. But... OH NO! You got a test tomorrow!"
y "What do you do Dumby?"

menu:
    "Say no and study":
        y "Congrats! You passed the test with a B-!"
        $ a += 1
    "Play but study after":
        y "You get so tired after reviewing a few questions and passed out... You got a C."
        $ c += 1
    "Don't study, You got it!":
        y "Dumby, you didn't 'got it', you got an F on that!"
        $ f += 1
hide you2
hide bg2 with fade
image you3 = "You3.png"
show bg1
y "You get how it works now? It's about time. Because you got two more comin' your way!"
y "Better listen up dumb dumb, cause it only gets harder!"
show you3 at showface with fade
y "You are completing an assignment for class and have become stumped. Nothing seems to be working right and you don't know whats wrong."
y "What do you do?"

menu:
    "Phone a friend":
        y "Two heads are better than one! Good job Dumby! You got a 100, and so did your friend!"
        $ a += 1
    "Google it":
        y "You plagiariser! Irredeemable, TO THE OFFICE! An F for your malpractices."
        $ f += 1
    "Try your best":
        y "You tried...? and that's what counts! You got some points and you got..."
        y "... A C+ on the assignment... good on you?"
        $ c += 1

y "Well, you've done well so far... Though I may be wrong, who knows, I'm just the artist."
y "last test in 3..."
y "2..."
y "1..."
hide bg1
image bg3 = "bg1.jpeg"
image you4 = "You4.png"
show bg3
show you4 at showface
y "{fast}YOU'RE PRESENTING THINK FAST!"

menu:
    "I... what?":
        y "Hmm..."
        $ a += 1
    "I tried my best so here's what I got.":
        y "Hmm..."
        $ c += 1
    "I kinda know what's on there???":
        y "Hmm..."
        $ f += 1
    "What is going on.":
        y "Hmm..."
        $ c += 1
    "Help.":
        y "Hmm..."
        $ f += 1
    "My output is 0.":
        y "Hmm..."
        $ a += 1

hide you4
hide bg3
show bg1
y "well..."
jump ending

label ending:
    if a>c:
        if c>f:
            jump passed
    elif c>a:
        if c>f:
            jump madeit
    elif f>a:
        if f>c:
            jump failed
    else:
        jump failed

label passed:
image passed = "a.jpg"
show passed at showface with fade
y "You... YOU! You passed. You passed so well it brought tears to my eyes."
y "You should go to Harvard! Amazing job, [yourname]."
y "Thank you for playing!"
return

label madeit:
image madeit = "c.png"
show madeit at showface with fade
y "You... made it! Good job. You are exactly like me, so I'll grant you back your name."
y "Good job, [yourname]"
y "Thank you for playing!"
return

label failed:
image failed = "f.jpg"
show failed at showface with fade
y "I expected this... YOU ARE A DUMBY!!! YOU FAILED! Womp womp wooooommmppp!"
y "Thank you for playing!"
return