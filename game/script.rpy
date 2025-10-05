# The script of the game goes in this file.

# The init python statement runs Python at initialization time, before the game loads. 
# Among other things, this can be used to define classes and functions, or to initialize styles, config variables, or persistent data.

# TODO: Transcript Variable + Display
# TODO: Graphix and Backgrounds
# TODO: Sound

default LC = 0
default EC = 0

# For scripting tmps

default dialogueIon = None
default option1 = None
default option2 = None
default option3 = None
default option4 = None 
default option5 = None

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import string
    from random import randint
    translator = str.maketrans('', '', string.punctuation)

    # Turns a string into an array of tokens
    # TODO we must take care of punctuation at some point argh...; it temporarily works for now by ignoring punctuations but that is no longterm solution.
    def tokenize(text):
        return text.translate(translator).lower().split()

    # Turns an array of tokens back into a string
    def detokenize(array):
        return ' '.join(array)

    # Encodes each word based on if we know it or not
    def encodeWord(word):
        if(encoding.words.get(word, ("??", False, False))[1]):
            return word 
        else:
            return hashWord(word)
    
    # Turns a "word" into a ■ symbol,
    def hashWord(word):
        return encoding.words.get(word, ("??", False, False))[0]

    def encode(string):
        tokens = tokenize(string)
        tokens = map(encodeWord, tokens)
        return detokenize(tokens)

    def unlock(stage, newLC):
        if newLC > 6:
            if stage == 1:
                
                encoding.words.update({"you": ("▢", True, True)})
                encoding.words.update({"your": ("▢", True, True)})
            elif stage == 2:
                
                encoding.words.update({"today": ("▣", True, True)})
                encoding.words.update({"day": ("▣", True, True)})
                encoding.words.update({"tonight": ("▣", True, True)})

                encoding.words.update({"more": ("✵", True, True)})
                encoding.words.update({"really": ("✵", True, True)})
                encoding.words.update({"better": ("✵", True, True)})
            elif stage == 3:
                
                encoding.words.update({"i": ("♠", True, True)})
                encoding.words.update({"my": ("♠", True, True)})
                encoding.words.update({"me": ("♠", True, True)})
                encoding.words.update({"who": ("♠", True, True)})

                encoding.words.update({"hard": ("⮝", True, True)})
            elif stage == 4:
                
                encoding.words.update({"yes": ("⬢", True, True)})

                encoding.words.update({"no": ("♥", True, True)})
                encoding.words.update({"not": ("♥", True, True)})
                encoding.words.update({"none": ("♥", True, True)})
                encoding.words.update({"never": ("♥", True, True)})

            elif stage == 5:
                
                encoding.words.update({"good": ("▬", True, True)})
                encoding.words.update({"favourite": ("▬", True, True)})
                encoding.words.update({"cool": ("▬", True, True)})
                encoding.words.update({"awesome": ("▬", True, True)})

                encoding.words.update({"bad": ("¤", True, True)})
                encoding.words.update({"suck": ("¤", True, True)})

            elif stage == 6:
                
                encoding.words.update({"like": ("✪", True, True)})

                encoding.words.update({"food": ("♜", True, True)})
            
            elif stage == 7:
                
                encoding.words.update({"pretty": ("➽", True, True)})

                encoding.words.update({"please": ("♛", True, True)})

            elif stage == 8:
                
                encoding.words.update({"want": ("◢", True, True)})

                encoding.words.update({"ride": ("Ѫ", True, True)})

        
        for i in range(int(4*newLC/5)):
            toUnlock = list(encoding.words.keys())[randint(0, len(encoding.words)-1)]
            if (not encoding.words[toUnlock][2]) and (not encoding.words[toUnlock][1]):
                encoding.words.update({toUnlock: (encoding.words[toUnlock][0], True, False)})
            else:
                i-= 1


init python in encoding:
    words = {
        "how": ("■", False, False),
        "are": ("Ҧ", False, False),
        "were": ("Ҧ", False, False),
        "you": ("▢", False, True),
        "your": ("▢", False, True),
        "today": ("▣", False, True),
        "day": ("▣", False, True),
        "tonight": ("▣", False, True),
        "whatever": ("▤", False, False),
        "maybe": ("▤", False, False),
        "okay": ("▤", False, False),
        "um": ("▤", False, False),
        "bad": ("¤", False, True),
        "suck": ("¤", False, True),
        "good": ("▬", False, True),
        "nice": ("▬", False, True),
        "favourite": ("▬", False, True),
        "cool": ("▬", False, True),
        "awesome": ("▬", False, True),
        "purple": ("¢", False, False),
        "skies": ("#", False, False),
        "shirt": ("#", False, False),
        "boo": ("*", False, False),
        "glad": ("▰", False, False),
        "to": ("▱", False, False),
        "hear": ("▲", False, False),
        "this": ("△", False, False),
        "that": ("△", False, False),
        "thank": ("◆", False, False),
        "and": ("◇", False, False),
        "what": ("◈", False, False),
        "poo": ("◉", False, False),
        "police": ("◊", False, False),
        "i": ("♠", False, True),
        "my": ("♠", False, True),
        "me": ("♠", False, True),
        "who": ("♠", False, True),
        "have": ("♣", False, False),
        "go": ("◎", False, False),
        "went": ("◎", False, False),
        "now": ("●", False, False),
        "did": ("◐", False, False),
        "do": ("◐", False, False),
        "handling": ("◐", False, False),
        "the": ("◑", False, False),
        "market": ("&", False, False),
        "thought": ("◓", False, False),
        "think": ("◓", False, False),
        "guess": ("◓", False, False),
        "know": ("◓", False, False),
        "about": ("◘", False, False),
        "rejected": ("◙", False, False),
        "is": ("Ʃ", False, False),
        "was": ("Ʃ", False, False),
        "be": ("Ʃ", False, False),
        "am": ("Ʃ", False, False),
        "with": ("◩", False, False),
        "anyone": ("◨", False, False),
        "friends": ("◭", False, False),
        "friend": ("◭", False, False),
        "not": ("♥", False, True), 
        "none": ("♥", False, True), 
        "no": ("♥", False, True), 
        "never": ("♥", False, True), 
        "a": ("♦", False, False),
        "date": ("✚", False, False),
        "of": ("✜", False, False),
        "business": ("✠", False, False),
        "like": ("✪", False, True),
        "want": ("◢", False, True),
        "more": ("✵", False, True),
        "really": ("✵", False, True),
        "better": ("✵", False, True),
        "later": ("❤", False, False),
        "pretty": ("➽", False, True),
        "it": ("⦿", False, False),
        "got": ("⧒", False, False),
        "colour": ("⧪", False, False),
        "yes": ("⬢", False, True),
        "hard": ("⮝", False, True),
        "seem": ("⯂", False, False),
        "look": ("⯂", False, False),
        "upset": ("⨂", False, False),
        "always": ("❖", False, False),
        "so": ("♚", False, False),
        "well": ("♚", False, False),
        "please": ("♛", False, True),
        "food": ("♜", False, True),
        "in": ("♝", False, False),
        "mood": ("♞", False, False),
        "for": ("♟", False, False),
        "all": ("⏏", False, False),
        "should": ("ᛓ", False, False),
        "would": ("ᛓ", False, False),
        "next": ("ᛒ", False, False),
        "time": ("ᛥ", False, False),
        "sometime": ("ᛥ", False, False),
        "ask": ("ᛃ", False, False),
        "somethings": ("ᚙ", False, False),
        "something": ("ᚙ", False, False),
        "thing": ("ᚙ", False, False),
        "anything": ("ᚙ", False, False),
        "answer": ("£", False, False),
        "new": ("§", False, False),
        "wear": ("©", False, False),
        "dress": ("©", False, False),
        "little": ("@", False, False),
        "party": ("Ѣ", False, False),
        "ride": ("Ѫ", False, True),
        "question": ("ф", False, False),
        "help": ("ϴ", False, False),
        "busy": ("Ω", False, False),
        "Bus-chan": ("¶", False, False),
        "else": ("±", False, False),
        "stop": ("ȹ", False, False),
        "why": ("ɐ", False, False),

    }


init python in dialogue:
    _constant = True

define ion = Character("Ion-chan")

transform size_normal:
    ysize 1000
    fit "contain"

transform size_close:
    ysize 1200
    fit "contain"

transform size_far:
    ysize 800
    fit "contain"

transform scenes:
    zoom 0.5
    fit "contain"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    "It's been a long day and a longer term."

    "School, parents, friends, stress."

    "It's getting to be too much."

    "The only truly bright spot to look forward to was the Grand GDC Party."

    "It's the BIGGEST and BESTEST night of the term (according to the posters)."

    "The only problem?"

    "It's the afternoon of the party, and you still have no date."

    "You just spent the past six hours at the Kitchener market trying to convince your classmate to go with you."

    "You got turned down cold."

    "You only have one hope left."

    "The one who has been there for you in every hour of need."

    "The one who always makes sure you get where you need to be."

    "The one who makes you feel truly seen."

    "The one who will stop by regularly with lights and horns blaring to cheer you up."
    
    jump stage1_1

    # These display lines of dialogue.

    # This ends the game.

    return 

label stage1_1:

    scene station_kitchenermarket

    show ion wave at center, size_close

    "Ion-chan"

    $ s1_ion1 = f"{encode("How are you today?")}"

    ion "[s1_ion1]"

    hide ion wave
    show ion smiling at center, size_close

    "The problem is, you can never quite understand what she's saying."

    "Because Ion-Chan only speaks Locomotish, not English."

    "Most of the time, you would be willing to just nod along with what she says."

    "But now, you are out of options."

    "You MUST find a way to convince her to go to the party with you."

    "Maybe you can use context clues to guess?"

    $ tempLC = LC

    $ s1_op1_1 = f"{encode("Whatever")}"
    $ s1_op1_2 = f"{encode("Bad")}"
    $ s1_op1_3 = f"{encode("Good, how are you?")}"
    $ s1_op1_4 = f"{encode("Purple skies")}"
    $ s1_op1_5 = f"{encode("Boo Boo")}"

    # renpy.display_menu([("You are pondering your dialogue choices but you realize you have no idea what she's saying... or what you're saying...",None)
    #    ,("test choice",1)])

    menu:
        #"You are pondering your dialogue choices but you realize you have no idea what she's saying... or what you're saying..."

        "[s1_op1_1]":

            $LC += 4
            $EC += 1
        "[s1_op1_2]":

            $LC += 4
            $EC += 2
        "[s1_op1_3]":

            $LC += 5            
            $EC += 5
        "[s1_op1_4]":

            $LC += 2
            $EC += 3
        "[s1_op1_5]":

            $LC += 1
            $EC += 3

    "Did that go well?"

    "Hard to say."

    "Maybe if you keep trying to talk to her, you can figure out some words."

    "You have 9 stops before reaching UW."

    "And then you will meet your fate."

    $ s1_ion2 = f"{encode("Glad to hear that")}"

    ion "[s1_ion2]"

    $ s1_op1_1 = f"{encode("Thank you")}"
    $ s1_op1_2 = f"{encode("And you?")}"
    $ s1_op1_3 = f"{encode("Hear what?")}"
    $ s1_op1_4 = f"{encode("Poo Poo")}"
    $ s1_op1_5 = f"{encode("Police")}"

    # renpy.display_menu([("You are pondering your dialogue choices but you realize you have no idea what she's saying... or what you're saying...",None)
    #    ,("test choice",1)])

    menu:
        #"You are pondering your dialogue choices but you realize you have no idea what she's saying... or what you're saying..."

        "[s1_op1_1]":

            $LC += 4
            $EC += 1
        "[s1_op1_2]":

            $LC += 4
            $EC += 2
        "[s1_op1_3]":

            $LC += 5            
            $EC += 5
        "[s1_op1_4]":

            $LC += 2
            $EC += 3
        "[s1_op1_5]":

            $LC += 1
            $EC += 3

    $ s2_ion3 = f"{encode("I have to go now")}"
    
    ion "[s2_ion3]"


    "If you guess correct words, you may get some new ones revealed."

    if LC-tempLC > 6:
        "You unlocked ▢ (you/your)!"

    $ dummy = unlock(1, LC-tempLC)

    hide ion smiling

    scene black with fade

label s2:

    scene station_frederick with fade

    "8 stations left. Here we go."

    show ion smiling at center, size_close

    $ s2_ion1 = f"{encode("What did you do today?")}"
    
    $ tempLC = LC

    ion "[s2_ion1]" 

    $ s2_op1_1 = f"{encode("Went to the market")}"
    $ s2_op1_2 = f"{encode("Thought about you")}"
    $ s2_op1_3 = f"{encode("Good, how are you?")}"
    $ s2_op1_4 = f"{encode("Bad")}"
    $ s2_op1_5 = f"{encode("Rejected")}"

    menu: 
        "[s2_op1_1]":
            $LC += 5
            $EC += 4
        "[s2_op1_2]":
            $LC += 5
            $EC += 2
        "[s2_op1_3]":
            $LC += 2
            $EC += 5
        "[s2_op1_4]":
            $LC += 3
            $EC += 2
        "[s2_op1_5]":
            $LC += 3
            $EC += 1

    $ s2_ion2 = f"{encode("Were you with anyone?")}"

    ion "[s2_ion2]" 

    $ s2_op2_1 = f"{encode("My friends")}"
    $ s2_op2_2 = f"{encode("Not a date")}"
    $ s2_op2_3 = f"{encode("None of your business")}"
    $ s2_op2_4 = f"{encode("I like you")}"
    $ s2_op2_5 = f"{encode("Boo Boo")}"

    menu: 
        "[s2_op2_1]":
            $LC += 5
            $EC += 4
        "[s2_op2_2]":
            $LC += 4
            $EC += 2
        "[s2_op2_3]":
            $LC += 4
            $EC += 1
        "[s2_op2_4]":
            $LC += 2
            $EC += 3
        "[s2_op2_5]":
            $LC += 1
            $EC += 3

    $ s2_ion3 = f"{encode("I really want to hear more later")}"

    ion "[s2_ion3]" 

    if LC-tempLC > 6:
        "You unlocked ▣ (today/day/tonight) and ✵ (more/really/better)!"

    $ dummy = unlock(2, LC-tempLC)

    hide ion smiling

    scene black with fade

label s3:

    scene station_kitchenercityhall with fade

    "7 stations left. How many words can you unlock?."

    show ion smiling at center, size_close

    $ s3_ion1 = f"{encode("Your shirt is pretty")}"
    
    $ tempLC = LC

    ion "[s3_ion1]"

    $ s3_op1_1 = f"{encode("Thank you")}"
    $ s3_op1_2 = f"{encode("No it is not")}"
    $ s3_op1_3 = f"{encode("Shirt")}"
    $ s3_op1_4 = f"{encode("You poo")}"
    $ s3_op1_5 = f"{encode("I got it today")}"

    menu: 
        "[s3_op1_1]":
            $LC += 5
            $EC += 5
        "[s3_op1_2]":
            $LC += 5
            $EC += 2
        "[s3_op1_3]":
            $LC += 2
            $EC += 3
        "[s3_op1_4]":
            $LC += 1
            $EC += 1
        "[s3_op1_5]":
            $LC += 4
            $EC += 2
       
    $ s3_ion2 = f"{encode("Is it your favourite colour?")}"

    ion "[s3_ion2]" 

    $ s3_op2_1 = f"{encode("Yes")}"
    $ s3_op2_2 = f"{encode("I like you more")}"
    $ s3_op2_3 = f"{encode("You suck")}"
    $ s3_op2_4 = f"{encode("I poo you")}"
    $ s3_op2_5 = f"{encode("Today was hard")}"

    menu: 
        "[s3_op2_1]":
            $LC += 5
            $EC += 4
        "[s3_op2_2]":
            $LC += 4
            $EC += 5
        "[s3_op2_3]":
            $LC += 3
            $EC += 1
        "[s3_op2_4]":
            $LC += 1
            $EC += 1
        "[s3_op2_5]":
            $LC += 3
            $EC += 3

    $ s3_ion3 = f"{encode("This is hard")}"

    ion "[s3_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ♠ (I/my/me/who) and ⮝ (hard)!"

    $ dummy = unlock(3, LC-tempLC)

    if EC > 18:
        jump s4b
    else:
        jump s4a

label s4a:

    $ tempLC = LC

    scene station_central with fade

    "6 stations left. Pay attention to which symbols are repeated."

    show ion smiling at center, size_close

    $ s4a_ion1 = f"{encode("You seem upset today")}"
    
    ion "[s4a_ion1]" 

    $ s4a_op1_1 = f"{encode("Bad day")}"
    $ s4a_op1_2 = f"{encode("No I am not")}"
    $ s4a_op1_3 = f"{encode("Purple shirt")}"
    $ s4a_op1_4 = f"{encode("I like you")}"
    $ s4a_op1_5 = f"{encode("I was rejected")}"

    menu: 
        "[s4a_op1_1]":
            $LC += 4
            $EC += 4
        "[s4a_op1_2]":
            $LC += 5
            $EC += 1
        "[s4a_op1_3]":
            $LC += 1
            $EC += 2
        "[s4a_op1_4]":
            $LC += 3
            $EC += 1
        "[s4a_op1_5]":
            $LC += 4
            $EC += 5
       
    $ s4a_ion2 = f"{encode("Are you always like this?")}"

    ion "[s4a_ion2]" 

    $ s4a_op2_1 = f"{encode("I do not think so")}"
    $ s4a_op2_2 = f"{encode("Yes please")}"
    $ s4a_op2_3 = f"{encode("Poo poo")}"
    $ s4a_op2_4 = f"{encode("I suck")}"
    $ s4a_op2_5 = f"{encode("More today")}"

    menu: 
        "[s4a_op2_1]":
            $LC += 5
            $EC += 4
        "[s4a_op2_2]":
            $LC += 2
            $EC += 2
        "[s4a_op2_3]":
            $LC += 1
            $EC += 1
        "[s4a_op2_4]":
            $LC += 4
            $EC += 3
        "[s4a_op2_5]":
            $LC += 4
            $EC += 5

    $ s4a_ion3 = f"{encode("Cool.")}"

    ion "[s4a_ion3]"

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ⬢ (yes) and ♥ (no/not/none/never)!"

    $ dummy = unlock(4, LC-tempLC)

    if EC > 24:
        jump s5b
    else:
        jump s5a

label s4b:
    scene station_central with fade

    "6 stations left. Pay attention to which symbols are repeated."

    show ion smiling at center, size_close

    $ s4b_ion1 = f"{encode("You are nice today")}"

    $ tempLC = LC
    
    ion "[s4b_ion1]" 

    $ s4b_op1_1 = f"{encode("Good day")}"
    $ s4b_op1_2 = f"{encode("No I am not")}"
    $ s4b_op1_3 = f"{encode("Purple shirt")}"
    $ s4b_op1_4 = f"{encode("I like you")}"
    $ s4b_op1_5 = f"{encode("Yes I am")}"

    menu: 
        "[s4b_op1_1]":
            $LC += 4
            $EC += 4
        "[s4b_op1_2]":
            $LC += 5
            $EC += 2
        "[s4b_op1_3]":
            $LC += 1
            $EC += 2
        "[s4b_op1_4]":
            $LC += 3
            $EC += 5
        "[s4b_op1_5]":
            $LC += 4
            $EC += 3
       
    $ s4b_ion2 = f"{encode("Are you always like this?")}"

    ion "[s4b_ion2]" 

    $ s4b_op2_1 = f"{encode("I do not think so")}"
    $ s4b_op2_2 = f"{encode("Yes please")}"
    $ s4b_op2_3 = f"{encode("Poo poo")}"
    $ s4b_op2_4 = f"{encode("I suck")}"
    $ s4b_op2_5 = f"{encode("More today")}"

    menu: 
        "[s4b_op2_1]":
            $LC += 5
            $EC += 4
        "[s4b_op2_2]":
            $LC += 2
            $EC += 3
        "[s4b_op2_3]":
            $LC += 1
            $EC += 1
        "[s4b_op2_4]":
            $LC += 4
            $EC += 2
        "[s4b_op2_5]":
            $LC += 4
            $EC += 3

    $ s4b_ion3 = f"{encode("Cool.")}"

    ion "[s4b_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ⬢ (yes) and ♥ (no/not/none/never)!"

    $ dummy = unlock(4, LC-tempLC)

    if EC > 24:
        jump s5b
    else:
        jump s5a

label s5a:

    scene station_grh with fade

    "5 stations left. Ion-Chan's expressions can give clues."

    show ion smiling at center, size_close

    $ s5a_ion1 = f"{encode("Did you have food today?")}"

    $ tempLC = LC

    ion "[s5a_ion1]" 

    $ s5a_op1_1 = f"{encode("Yes")}"
    $ s5a_op1_2 = f"{encode("No")}"
    $ s5a_op1_3 = f"{encode("Poo me")}"
    $ s5a_op1_4 = f"{encode("I good you")}"
    $ s5a_op1_5 = f"{encode("Like you")}"

    menu: 
        "[s5a_op1_1]":
            $LC += 5
            $EC += 3
        "[s5a_op1_2]":
            $LC += 5
            $EC += 4
        "[s5a_op1_3]":
            $LC += 1
            $EC += 1
        "[s5a_op1_4]":
            $LC += 1
            $EC += 2
        "[s5a_op1_5]":
            $LC += 2
            $EC += 4
       
    $ s5a_ion2 = f"{encode("Is that why you are in a bad mood?")}"

    ion "[s5a_ion2]" 

    $ s5a_op2_1 = f"{encode("Yes")}"
    $ s5a_op2_2 = f"{encode("No")}"
    $ s5a_op2_3 = f"{encode("Food is good")}"
    $ s5a_op2_4 = f"{encode("Poo for all")}"
    $ s5a_op2_5 = f"{encode("Sorry")}"

    menu: 
        "[s5a_op2_1]":
            $LC += 5
            $EC += 4
        "[s5a_op2_2]":
            $LC += 5
            $EC += 2
        "[s5a_op2_3]":
            $LC += 2
            $EC += 4
        "[s5a_op2_4]":
            $LC += 1
            $EC += 1
        "[s5a_op2_5]":
            $LC += 4
            $EC += 5

    $ s5a_ion3 = f"{encode("Maybe you should have food next time.")}"

    ion "[s5a_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ▬ (good/favourite/cool/awesome) and ¤ (bad/suck)!"

    $ dummy = unlock(5, LC-tempLC)

    if EC > 30:
        jump s6b
    else:
        jump s6a

label s5b:

    scene station_grh with fade

    "5 stations left. Ion-Chan's expressions can give clues."

    show ion smiling at center, size_close

    $ s5b_ion1 = f"{encode("Did you have food today?")}"

    $ tempLC = LC
    
    ion "[s5b_ion1]" 

    $ s5b_op1_1 = f"{encode("Yes")}"
    $ s5b_op1_2 = f"{encode("No")}"
    $ s5b_op1_3 = f"{encode("Poo me")}"
    $ s5b_op1_4 = f"{encode("I good you")}"
    $ s5b_op1_5 = f"{encode("Like you")}"

    menu: 
        "[s5b_op1_1]":
            $LC += 5
            $EC += 4
        "[s5b_op1_2]":
            $LC += 5
            $EC += 2
        "[s5b_op1_3]":
            $LC += 1
            $EC += 1
        "[s5b_op1_4]":
            $LC += 1
            $EC += 3
        "[s5b_op1_5]":
            $LC += 2
            $EC += 5
       
    $ s5b_ion2 = f"{encode("Was it your favourite?")}"

    ion "[s5b_ion2]" 

    $ s5b_op2_1 = f"{encode("Yes")}"
    $ s5b_op2_2 = f"{encode("No")}"
    $ s5b_op2_3 = f"{encode("Food is good")}"
    $ s5b_op2_4 = f"{encode("Poo for all")}"
    $ s5b_op2_5 = f"{encode("You are nice")}"

    menu: 
        "[s5b_op2_1]":
            $LC += 5
            $EC += 4
        "[s5b_op2_2]":
            $LC += 5
            $EC += 4
        "[s5b_op2_3]":
            $LC += 3
            $EC += 3
        "[s5b_op2_4]":
            $LC += 1
            $EC += 2
        "[s5b_op2_5]":
            $LC += 2
            $EC += 5

    $ s5b_ion3 = f"{encode("It would be good to have food sometime.")}"

    ion "[s5b_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ▬ (good/favourite/cool/awesome) and ¤ (bad/suck)!"

    $ dummy = unlock(5, LC-tempLC)

    if EC > 30:
        jump s6b
    else:
        jump s6a

label s6a:

    scene station_allen with fade

    "4 stations left. How do you think this going?."

    show ion smiling at center, size_close

    $ s6a_ion1 = f"{encode("I want to ask you something")}"

    $ tempLC = LC
    
    ion "[s6a_ion1]" 

    $ s6a_op1_1 = f"{encode("Yes")}"
    $ s6a_op1_2 = f"{encode("No")}"
    $ s6a_op1_3 = f"{encode("You are good")}"
    $ s6a_op1_4 = f"{encode("You poo")}"
    $ s6a_op1_5 = f"{encode("I want food")}"

    menu: 
        "[s6a_op1_1]":
            $LC += 4
            $EC += 4
        "[s6a_op1_2]":
            $LC += 4
            $EC += 2
        "[s6a_op1_3]":
            $LC += 5
            $EC += 4
        "[s6a_op1_4]":
            $LC += 1
            $EC += 1
        "[s6a_op1_5]":
            $LC += 3
            $EC += 2
       
    $ s6a_ion2 = f"{encode("Do you not like me?")}"

    ion "[s6a_ion2]" 

    $ s6a_op2_1 = f"{encode("Yes")}"
    $ s6a_op2_2 = f"{encode("No")}"
    $ s6a_op2_3 = f"{encode("I like poo")}"
    $ s6a_op2_4 = f"{encode("You like me")}"
    $ s6a_op2_5 = f"{encode("You are bad")}"

    menu: 
        "[s6a_op2_1]":
            $LC += 5
            $EC += 1
        "[s6a_op2_2]":
            $LC += 5
            $EC += 4
        "[s6a_op2_3]":
            $LC += 3
            $EC += 2
        "[s6a_op2_4]":
            $LC += 3
            $EC += 2
        "[s6a_op2_5]":
            $LC += 4
            $EC += 1

    $ s6a_ion3 = f"{encode("I guess that is my answer...")}"

    ion "[s6a_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ✪ (like) and ♜ (food)!"

    $ dummy = unlock(6, LC-tempLC)

    if EC > 44:
        jump s7c
    elif EC > 28:
        jump s7b
    else:
        jump s7a

label s6b:

    scene station_allen with fade

    "4 stations left. How do you think this going?."

    show ion smiling at center, size_close

    $ s6b_ion1 = f"{encode("I want to ask you something")}"

    $ tempLC = LC
    
    ion "[s6b_ion1]" 

    $ s6b_op1_1 = f"{encode("Yes")}"
    $ s6b_op1_2 = f"{encode("No")}"
    $ s6b_op1_3 = f"{encode("You are good")}"
    $ s6b_op1_4 = f"{encode("You poo")}"
    $ s6b_op1_5 = f"{encode("I want food")}"

    menu: 
        "[s6b_op1_1]":
            $LC += 4
            $EC += 4
        "[s6b_op1_2]":
            $LC += 4
            $EC += 1
        "[s6b_op1_3]":
            $LC += 5
            $EC += 5
        "[s6b_op1_4]":
            $LC += 1
            $EC += 1
        "[s6b_op1_5]":
            $LC += 3
            $EC += 2
       
    $ s6b_ion2 = f"{encode("Do you like me?")}"

    ion "[s6b_ion2]" 

    $ s6b_op2_1 = f"{encode("Yes")}"
    $ s6b_op2_2 = f"{encode("No")}"
    $ s6b_op2_3 = f"{encode("I like poo")}"
    $ s6b_op2_4 = f"{encode("You like me?")}"
    $ s6b_op2_5 = f"{encode("You are good")}"

    menu: 
        "[s6b_op2_1]":
            $LC += 5
            $EC += 4
        "[s6b_op2_2]":
            $LC += 5
            $EC += 1
        "[s6b_op2_3]":
            $LC += 3
            $EC += 1
        "[s6b_op2_4]":
            $LC += 3
            $EC += 2
        "[s6b_op2_5]":
            $LC += 4
            $EC += 5

    $ s6b_ion3 = f"{encode("I guess thats my answer...")}"

    ion "[s6b_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ✪ (like) and ♜ (food)!"

    $ dummy = unlock(6, LC-tempLC)

    if EC > 44:
        jump s7c
    elif EC > 28:
        jump s7b
    else:
        jump s7a

label s7a:

    scene station_waterloopublicsquare2 with fade

    "3 stations left. Some important words get permanently locked if you don't get them."

    show ion smiling at center, size_close

    $ s7a_ion1 = f"{encode("You are not pretty")}"

    $ tempLC = LC
    
    ion "[s7a_ion1]" 

    $ s7a_op1_1 = f"{encode("Yes I am")}"
    $ s7a_op1_2 = f"{encode("No, you")}"
    $ s7a_op1_3 = f"{encode("New shirt")}"
    $ s7a_op1_4 = f"{encode("Thank you")}"
    $ s7a_op1_5 = f"{encode("Poo")}"

    menu: 
        "[s7a_op1_1]":
            $LC += 4
            $EC += 2
        "[s7a_op1_2]":
            $LC += 2
            $EC += 1
        "[s7a_op1_3]":
            $LC += 3
            $EC += 4
        "[s7a_op1_4]":
            $LC += 4
            $EC += 3
        "[s7a_op1_5]":
            $LC += 1
            $EC += 3
       
    $ s7a_ion2 = f"{encode("You should not wear that.")}"

    ion "[s7a_ion2]" 

    $ s7a_op2_1 = f"{encode("Yes, I should")}"
    $ s7a_op2_2 = f"{encode("No, it is not")}"
    $ s7a_op2_3 = f"{encode("Like like")}"
    $ s7a_op2_4 = f"{encode("Please")}"
    $ s7a_op2_5 = f"{encode("A little")}"

    menu: 
        "[s7a_op2_1]":
            $LC += 5
            $EC += 2
        "[s7a_op2_2]":
            $LC += 2
            $EC += 2
        "[s7a_op2_3]":
            $LC += 1
            $EC += 3
        "[s7a_op2_4]":
            $LC += 3
            $EC += 4
        "[s7a_op2_5]":
            $LC += 2
            $EC += 2

    $ s7a_ion3 = f"{encode("I do not like it.")}"

    ion "[s7a_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ➽ (pretty) and ♛ (please)!"

    $ dummy = unlock(7, LC-tempLC)

    if EC > 50:
        jump s8c
    elif EC > 34:
        jump s8b
    else:
        jump s8a

label s7b:

    scene station_waterloopublicsquare2 with fade

    "3 stations left. Some important words get permanently locked if you don't get them."

    show ion smiling at center, size_close

    $ s7b_ion1 = f"{encode("You look okay today")}"

    $ tempLC = LC
    
    ion "[s7b_ion1]" 

    $ s7b_op1_1 = f"{encode("Yes, I am")}"
    $ s7b_op1_2 = f"{encode("No, you")}"
    $ s7b_op1_3 = f"{encode("New shirt")}"
    $ s7b_op1_4 = f"{encode("Thank you")}"
    $ s7b_op1_5 = f"{encode("Purple")}"

    menu: 
        "[s7b_op1_1]":
            $LC += 4
            $EC += 3
        "[s7b_op1_2]":
            $LC += 2
            $EC += 3
        "[s7b_op1_3]":
            $LC += 4
            $EC += 4
        "[s7b_op1_4]":
            $LC += 5
            $EC += 4
        "[s7b_op1_5]":
            $LC += 1
            $EC += 2
       
    $ s7b_ion2 = f"{encode("I think you should dress better")}"

    ion "[s7b_ion2]" 

    $ s7b_op2_1 = f"{encode("Yes, I should")}"
    $ s7b_op2_2 = f"{encode("No, it is not")}"
    $ s7b_op2_3 = f"{encode("Like like")}"
    $ s7b_op2_4 = f"{encode("Please")}"
    $ s7b_op2_5 = f"{encode("A little")}"

    menu: 
        "[s7b_op2_1]":
            $LC += 5
            $EC += 3
        "[s7b_op2_2]":
            $LC += 2
            $EC += 2
        "[s7b_op2_3]":
            $LC += 1
            $EC += 3
        "[s7b_op2_4]":
            $LC += 3
            $EC += 3
        "[s7b_op2_5]":
            $LC += 3
            $EC += 4

    $ s7b_ion3 = f"{encode("Okay...")}"

    ion "[s7b_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ➽ (pretty) and ♛ (please)!"

    $ dummy = unlock(7, LC-tempLC)

    if EC > 50:
        jump s8c
    elif EC > 34:
        jump s8b
    else:
        jump s8a

label s7c:

    scene station_waterloopublicsquare2 with fade

    "3 stations left. Some important words get permanently locked if you don't get them."

    show ion smiling at center, size_close

    $ s7c_ion1 = f"{encode("You look pretty today")}"

    $ tempLC = LC
    
    ion "[s7c_ion1]" 

    $ s7c_op1_1 = f"{encode("Yes, I am")}"
    $ s7c_op1_2 = f"{encode("No, you")}"
    $ s7c_op1_3 = f"{encode("New shirt")}"
    $ s7c_op1_4 = f"{encode("Thank you")}"
    $ s7c_op1_5 = f"{encode("Shirt")}"

    menu: 
        "[s7c_op1_1]":
            $LC += 4
            $EC += 3
        "[s7c_op1_2]":
            $LC += 4
            $EC += 5
        "[s7c_op1_3]":
            $LC += 3
            $EC += 4
        "[s7c_op1_4]":
            $LC += 5
            $EC += 5
        "[s7c_op1_5]":
            $LC += 1
            $EC += 3
       
    $ s7c_ion2 = f"{encode("Is it for me?")}"

    ion "[s7c_ion2]" 

    $ s7c_op2_1 = f"{encode("Yes, I am")}"
    $ s7c_op2_2 = f"{encode("No, it is not")}"
    $ s7c_op2_3 = f"{encode("Like like")}"
    $ s7c_op2_4 = f"{encode("Please")}"
    $ s7c_op2_5 = f"{encode("A little")}"

    menu: 
        "[s7c_op2_1]":
            $LC += 2
            $EC += 5
        "[s7c_op2_2]":
            $LC += 5
            $EC += 2
        "[s7c_op2_3]":
            $LC += 1
            $EC += 3
        "[s7c_op2_4]":
            $LC += 3
            $EC += 1
        "[s7c_op2_5]":
            $LC += 4
            $EC += 4

    $ s7c_ion3 = f"{encode("I like it")}"

    ion "[s7c_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 7:
        "You unlocked ➽ (pretty) and ♛ (please)!"

    $ dummy = unlock(1, LC-tempLC)

    if EC > 50:
        jump s8c
    elif EC > 34:
        jump s8b
    else:
        jump s8a

label s8a:

    scene station_waterloolaurierpark with fade

    "2 stations left. How Ion-Chan feels is very important now."

    show ion smiling at center, size_close

    $ s8a_ion1 = f"{encode("I am really busy tonight")}"

    $ tempLC = LC
    
    ion "[s8a_ion1]" 

    $ s8a_op1_1 = f"{encode("That is bad")}"
    $ s8a_op1_2 = f"{encode("Good")}"
    $ s8a_op1_3 = f"{encode("Poo poo")}"
    $ s8a_op1_4 = f"{encode("No")}"
    $ s8a_op1_5 = f"{encode("I like you")}"

    menu: 
        "[s8a_op1_1]":
            $LC += 5
            $EC += 4
        "[s8a_op1_2]":
            $LC += 5
            $EC += 1
        "[s8a_op1_3]":
            $LC += 3
            $EC += 3
        "[s8a_op1_4]":
            $LC += 2
            $EC += 1
        "[s8a_op1_5]":
            $LC += 1
            $EC += 3
       
    $ s8a_ion2 = f"{encode("You know, the party?")}"

    ion "[s8a_ion2]" 

    $ s8a_op2_1 = f"{encode("Party?")}"
    $ s8a_op2_2 = f"{encode("Yes")}"
    $ s8a_op2_3 = f"{encode("I want you")}"
    $ s8a_op2_4 = f"{encode("Ride you friend")}"
    $ s8a_op2_5 = f"{encode("I know")}"

    menu: 
        "[s8a_op2_1]":
            $LC += 5
            $EC += 2
        "[s8a_op2_2]":
            $LC += 4
            $EC += 4
        "[s8a_op2_3]":
            $LC += 2
            $EC += 2
        "[s8a_op2_4]":
            $LC += 1
            $EC += 1
        "[s8a_op2_5]":
            $LC += 5
            $EC += 4

    $ s8a_ion3 = f"{encode("I do not want to go.")}"

    ion "[s8a_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ◢ (want) and Ѫ (ride)!"

    $ dummy = unlock(8, LC-tempLC)

    if EC > 56:
        jump s9c
    elif EC > 40:
        jump s9b
    else:
        jump s9a

label s8b:

    scene station_waterloolaurierpark with fade

    "2 stations left. How Ion-Chan feels is very important now."

    show ion smiling at center, size_close

    $ s8b_ion1 = f"{encode("I might be busy tonight")}"

    $ tempLC = LC
    
    ion "[s8b_ion1]"

    $ s8b_op1_1 = f"{encode("That is bad")}"
    $ s8b_op1_2 = f"{encode("Good")}"
    $ s8b_op1_3 = f"{encode("Purple poo")}"
    $ s8b_op1_4 = f"{encode("No")}"
    $ s8b_op1_5 = f"{encode("I like you")}"

    menu: 
        "[s8b_op1_1]":
            $LC += 5
            $EC += 4
        "[s8b_op1_2]":
            $LC += 5
            $EC += 1
        "[s8b_op1_3]":
            $LC += 3
            $EC += 2
        "[s8b_op1_4]":
            $LC += 2
            $EC += 1
        "[s8b_op1_5]":
            $LC += 1
            $EC += 4
       
    $ s8b_ion2 = f"{encode("You know, the party.")}"

    ion "[s8b_ion2]" 

    $ s8b_op2_1 = f"{encode("Party?")}"
    $ s8b_op2_2 = f"{encode("Yes")}"
    $ s8b_op2_3 = f"{encode("I want you")}"
    $ s8b_op2_4 = f"{encode("Ride you friend")}"
    $ s8b_op2_5 = f"{encode("I know")}"

    menu: 
        "[s8b_op2_1]":
            $LC += 4
            $EC += 2
        "[s8b_op2_2]":
            $LC += 5
            $EC += 4
        "[s8b_op2_3]":
            $LC += 2
            $EC += 3
        "[s8b_op2_4]":
            $LC += 1
            $EC += 3
        "[s8b_op2_5]":
            $LC += 5
            $EC += 4

    $ s8b_ion3 = f"{encode("Who would want to go?")}"

    ion "[s8b_ion3]" 

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ◢ (want) and Ѫ (ride)!"

    $ dummy = unlock(8, LC-tempLC)

    if EC > 56:
        jump s9c
    elif EC > 40:
        jump s9b
    else:
        jump s9a

label s8c:

    scene station_waterloolaurierpark with fade

    "2 stations left. How Ion-Chan feels is very important now."

    show ion smiling at center, size_close

    $ s8c_ion1 = f"{encode("I am not doing anything tonight")}"

    $ tempLC = LC
    
    ion "[s8c_ion1]"

    $ s8c_op1_1 = f"{encode("That is good")}"
    $ s8c_op1_2 = f"{encode("Bad")}"
    $ s8c_op1_3 = f"{encode("Purple shirt")}"
    $ s8c_op1_4 = f"{encode("Yes")}"
    $ s8c_op1_5 = f"{encode("I like you")}"

    menu: 
        "[s8c_op1_1]":
            $LC += 5
            $EC += 4
        "[s8c_op1_2]":
            $LC += 5
            $EC += 1
        "[s8c_op1_3]":
            $LC += 3
            $EC += 3
        "[s8c_op1_4]":
            $LC += 2
            $EC += 4
        "[s8c_op1_5]":
            $LC += 1
            $EC += 5
       
    $ s8c_ion2 = f"{encode("Bus-chan is handling the party")}"

    ion "[s8c_ion2]" 

    $ s8c_op2_1 = f"{encode("Party?")}"
    $ s8c_op2_2 = f"{encode("Yes")}"
    $ s8c_op2_3 = f"{encode("I want you")}"
    $ s8c_op2_4 = f"{encode("Ride you friend")}"
    $ s8c_op2_5 = f"{encode("I know")}"

    menu: 
        "[s8c_op2_1]":
            $LC += 4
            $EC += 2
        "[s8c_op2_2]":
            $LC += 5
            $EC += 5
        "[s8c_op2_3]":
            $LC += 2
            $EC += 4
        "[s8c_op2_4]":
            $LC += 2
            $EC += 4
        "[s8c_op2_5]":
            $LC += 4
            $EC += 4

    $ s8c_ion3 = f"{encode("I would want to go")}"

    ion "[s8c_ion3]"

    hide ion smiling

    scene black with fade

    if LC-tempLC > 6:
        "You unlocked ◢ (want) and Ѫ (ride)!"

    $ dummy = unlock(8, LC-tempLC)

    if EC > 56:
        jump s9c
    elif EC > 40:
        jump s9b
    else:
        jump s9a

label s9a:

    scene station_uw with fade

    "Last station. This is your chance."

    show ion smiling at center, size_close

    $ s9a_ion1 = f"{encode("Your stop now. Anything else?")}"
    
    ion "[s9a_ion1]" 

    $ s9a_op1_1 = f"{encode("Yes please")}"
    $ s9a_op1_2 = f"{encode("Hard no")}"
    $ s9a_op1_3 = f"{encode("Shirt")}"
    $ s9a_op1_4 = f"{encode("I do not like you...")}"
    $ s9a_op1_5 = f"{encode("Whatever")}"

    menu: 
        "[s9a_op1_1]":
            $LC += 5
            $EC += 4
        "[s9a_op1_2]":
            $LC += 4
            $EC += 1
        "[s9a_op1_3]":
            $LC += 1
            $EC += 2
        "[s9a_op1_4]":
            $LC += 2
            $EC += 1
        "[s9a_op1_5]":
            $LC += 3
            $EC += 3
       
    $ s9a_ion2 = f"{encode("Well...")}"

    ion "[s9a_ion2]" 

    $ s9a_op2_1 = f"{encode("Want to have food with me?")}"
    $ s9a_op2_2 = f"{encode("You are pretty")}"
    $ s9a_op2_3 = f"{encode("Please ride me?")}"
    $ s9a_op2_4 = f"{encode("Poo shirt with me?")}"
    $ s9a_op2_5 = f"{encode("Help")}"

    menu: 
        "[s9a_op2_1]":
            $LC += 5
            $EC += 2
        "[s9a_op2_2]":
            $LC += 3
            $EC += 4
        "[s9a_op2_3]":
            $LC += 5
            $EC += 1
        "[s9a_op2_4]":
            $LC += 2
            $EC += 1
        "[s9a_op2_5]":
            $LC += 1
            $EC += 2

    $ s9a_ion3 = f"{encode("Not cool")}"

    ion "[s9a_ion3]" 

    if EC > 62:
        jump goodend
    elif EC > 46:
        jump neutralend
    else:
        jump badend

label s9b:
    scene station_uw with fade

    "Last station. This is your chance."

    show ion smiling at center, size_close

    $ s9b_ion1 = f"{encode("Your stop now. Anything else?")}"
    
    ion "[s9b_ion1]" 

    $ s9b_op1_1 = f"{encode("Yes please")}"
    $ s9b_op1_2 = f"{encode("Hard no")}"
    $ s9b_op1_3 = f"{encode("Shirt")}"
    $ s9b_op1_4 = f"{encode("I like you")}"
    $ s9b_op1_5 = f"{encode("Whatever")}"

    menu: 
        "[s9b_op1_1]":
            $LC += 5
            $EC += 5
        "[s9b_op1_2]":
            $LC += 4
            $EC += 1
        "[s9b_op1_3]":
            $LC += 1
            $EC += 2
        "[s9b_op1_4]":
            $LC += 2
            $EC += 3
        "[s9b_op1_5]":
            $LC += 3
            $EC += 3
       
    $ s9b_ion2 = f"{encode("Well?")}"

    ion "[s9b_ion2]"

    $ s9b_op2_1 = f"{encode("Want to have food with me?")}"
    $ s9b_op2_2 = f"{encode("You are pretty")}"
    $ s9b_op2_3 = f"{encode("Please ride me?")}"
    $ s9b_op2_4 = f"{encode("Purple shirt with me?")}"
    $ s9b_op2_5 = f"{encode("Help")}"

    menu: 
        "[s9b_op2_1]":
            $LC += 5
            $EC += 4
        "[s9b_op2_2]":
            $LC += 3
            $EC += 5
        "[s9b_op2_3]":
            $LC += 5
            $EC += 3
        "[s9b_op2_4]":
            $LC += 2
            $EC += 2
        "[s9b_op2_5]":
            $LC += 1
            $EC += 1

    $ s9b_ion3 = f"{encode("Um")}"

    ion "[s9b_ion3]" 

    if EC > 62:
        jump goodend
    elif EC > 46:
        jump neutralend
    else:
        jump badend

label s9c:

    scene station_uw with fade

    "Last station. This is your chance."

    show ion smiling at center, size_close

    $ s9c_ion1 = f"{encode("Your stop now. Anything to ask me?")}"
    
    ion "[s9c_ion1]" 

    $ s9c_op1_1 = f"{encode("Yes please")}"
    $ s9c_op1_2 = f"{encode("Hard no")}"
    $ s9c_op1_3 = f"{encode("Shirt")}"
    $ s9c_op1_4 = f"{encode("I like you")}"
    $ s9c_op1_5 = f"{encode("Whatever")}"

    menu: 
        "[s9c_op1_1]":
            $LC += 5
            $EC += 5
        "[s9c_op1_2]":
            $LC += 4
            $EC += 1
        "[s9c_op1_3]":
            $LC += 1
            $EC += 2
        "[s9c_op1_4]":
            $LC += 2
            $EC += 5
        "[s9c_op1_5]":
            $LC += 3
            $EC += 4
    
    hide ion smiling 
    show ion concerned at center, size_close

    $ s9c_ion2 = f"{encode("Well?")}"

    ion "[s9c_ion2]"

    $ s9c_op2_1 = f"{encode("Want to have food with me?")}"
    $ s9c_op2_2 = f"{encode("You are pretty")}"
    $ s9c_op2_3 = f"{encode("Please ride me?")}"
    $ s9c_op2_4 = f"{encode("Purple shirt with me?")}"
    $ s9c_op2_5 = f"{encode("Help")}"

    menu: 
        "[s9c_op2_1]":
            $LC += 5
            $EC += 5
        "[s9c_op2_2]":
            $LC += 3
            $EC += 5
        "[s9c_op2_3]":
            $LC += 5
            $EC += 4
        "[s9c_op2_4]":
            $LC += 2
            $EC += 2
        "[s9c_op2_5]":
            $LC += 1
            $EC += 1
    
    hide ion concerned
    show ion happy at center, size_close

    $ s9c_ion3 = f"{encode("Awesome!")}"

    ion "[s9c_ion3]"

    if EC > 62:
        jump goodend
    elif EC > 46:
        jump neutralend
    else:
        jump badend

label badend:
    $ ion_badend = "You will never ride me again."

    scene black with fade

    ion "[ion_badend]"

    "Oops."

    "There goes my self-esteem."

    return 0

label neutralend:
    $ ion_badend = "Maybe some other time."

    scene black with fade

    ion "[ion_badend]"

    "That... probably could have gone better."

    "If only there was a way to do the afternoon all over again."

    return 0

label goodend:
    $ ion_goodend = "I would love to go out with you!"

    ion "[ion_goodend]"

    hide ion smiling

    scene endcard with fade

    "And now you can live happily ever after."

    "You and Ion-Chan will be happy for the rest of your days."

    return 0