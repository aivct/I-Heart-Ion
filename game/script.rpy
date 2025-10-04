# The script of the game goes in this file.

# The init python statement runs Python at initialization time, before the game loads. 
# Among other things, this can be used to define classes and functions, or to initialize styles, config variables, or persistent data.

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
    
    # Turns a string into an array of tokens
    # TODO we must take care of punctuation at some point argh...
    def tokenize(string):
        return string.split()

    # Turns an array of tokens back into a string
    def detokenize(array):
        return ' '.join(array)

    # Encodes each word based on if we know it or not
    def encodeWord(word):
        if(encoding.words.get(word, ("■", False))[1]):
            return word 
        else:
            return hashWord(word)
    
    # Turns a "word" into a ■ symbol
    def hashWord(word):
        return encoding.words.get(word, ("■", False))[0]

    def encode(string):
        tokens = tokenize(string)
        tokens = map(encodeWord, tokens)
        return detokenize(tokens)

    def unlock(word):
        encoding.update(word, False),

init python in encoding:
    words = {
        "you": ("♚", False)
        ,"you": ("♚", False)}

init python in dialogue:
    _constant = True

define ion = Character("Ion-Chan")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    
    jump stage1_1

    # These display lines of dialogue.

    # This ends the game.

    return

label stage1_1:
    $ dialogueIon = f"{encode("How are you today?")}"

    ion "[dialogueIon]"

    $ option1 = f"{encode("Whatever")}"
    $ option2 = f"{encode("Bad")}"
    $ option3 = f"{encode("Good, how are you?")}"
    $ option4 = f"{encode("Purple skies")}"
    $ option5 = f"{encode("Boo Boo")}"

    # renpy.display_menu([("You are pondering your dialogue choices but you realize you have no idea what she's saying... or what you're saying...",None)
    #    ,("test choice",1)])

    menu:
        "You are pondering your dialogue choices but you realize you have no idea what she's saying... or what you're saying..."

        "[option1]":

            $LC += 4
            $EC += 1
        "[option2]":

            $LC += 4
            $EC += 2
        "[option3]":

            $LC += 5            
            $EC += 5
        "[option4]":

            $LC += 2
            $EC += 3
        "[option5]":

            $LC += 1
            $EC += 3

label s2:
    $ s2_ion1 = f"{encode("What did you do today?")}"
    
    ion "[s2_ion1]" 

    $ s2_op1_1 = f"{encode("Went to the mall")}"
    $ s2_op1_2 = f"{encode("Thought about you")}"
    $ s2_op1_3 = f"{encode("Good, how are you?")}"
    $ s2_op1_4 = f"{encode("Bad")}"
    $ s2_op1_5 = f"{encode("Rejected")}"

    menu: 
        "[s2_op1_1]":
            $LC += 0
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
    $ s2_op2_4 = f"{encode("I love you")}"
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

    $ s2_ion3 = f"{encode("I would really like to hear more later!")}"

    ion "[s2_ion3]" 



label s3:
    $ s3_ion1 = f"{encode("Your shirt is cute")}"
    
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
       
    $ s3_ion2 = f"{encode("Is it your favorite colour?")}"

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

label s4a:
    $ s4a_ion1 = f"{encode("You seem upset today")}"
    
    ion "[s4a_ion1]" 

    $ s4a_op1_1 = f"{encode("Bad day")}"
    $ s4a_op1_2 = f"{encode("No Im not")}"
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

    $ s4a_op2_1 = f"{encode("I dont think so")}"
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

label s4b:
    $ s4b_ion1 = f"{encode("You are nice today")}"
    
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

    $ s4b_op2_1 = f"{encode("I dont think so")}"
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

label s5a:
    $ s5a_ion1 = f"{encode("Did you have food today?")}"

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

label s5b:
    $ s5b_ion1 = f"{encode("Did you have food today?")}"
    
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

label s6a:
    $ s6a_ion1 = f"{encode("I want to ask you something")}"
    
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

label s6b:
    $ s6b_ion1 = f"{encode("I want to ask you something")}"
    
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

label s7a:
    $ s7a_ion1 = f"{encode("You are not pretty")}"
    
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
       
    $ s7a_ion2 = f"{encode("You shouldnt wear that.")}"

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

    $ s7a_ion3 = f"{encode("I just dont like it.")}"

    ion "[s7a_ion3]" 

label s7b:
    $ s7b_ion1 = f"{encode("You look okay today")}"
    
    ion "[s7b_ion1]" 

    $ s7b_op1_1 = f"{encode("Yes, I am")}"
    $ s7b_op1_2 = f"{encode("No, you")}"
    $ s7b_op1_3 = f"{encode("New shirt")}"
    $ s7b_op1_4 = f"{encode("Thank you")}"
    $ s7b_op1_5 = f"{encode("Poo")}"

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

    $ s7b_ion3 = f"{encode("Okay..")}"

    ion "[s7b_ion3]" 

label s8a:
    $ s8a_ion1 = f"{encode("Im really busy tonight")}"
    
    ion "[s8a_ion1]" 

    $ s8a_op1_1 = f"{encode("Thats bad")}"
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

    $ s8a_ion3 = f"{encode("I dont really want to go.")}"

    ion "[s8a_ion3]" 

label s8b:
    $ s8b_ion1 = f"{encode("I might be busy tonight")}"
    
    ion "[s8b_ion1]"

    $ s8b_op1_1 = f"{encode("Thats bad")}"
    $ s8b_op1_2 = f"{encode("Good")}"
    $ s8b_op1_3 = f"{encode("Poo poo")}"
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
            $EC += 3
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

label s9a:
    $ s9a_ion1 = f"{encode("Did you have a question for me?")}"
    
    ion "[s9a_ion1]" 

    $ s9a_op1_1 = f"{encode("Yes please")}"
    $ s9a_op1_2 = f"{encode("Hard no")}"
    $ s9a_op1_3 = f"{encode("Shirt")}"
    $ s9a_op1_4 = f"{encode("I dont like you...")}"
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

    $ s9a_ion3 = f"{encode("Not cool bro.")}"

    ion "[s9a_ion3]" 

label s9b:
    $ s9b_ion1 = f"{encode("Did you have a question for me?")}"
    
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
    $ s9b_op2_4 = f"{encode("Poo shirt with me?")}"
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
            $EC += 1
        "[s9b_op2_5]":
            $LC += 1
            $EC += 1

    $ s9b_ion3 = f"{encode("Umm")}"

    ion "[s9b_ion3]" 

label badend:
    $ ion_badend = f("You will never ride me again.")

    ion "[ion_badend]"


label neutralend:
    $ ion_badend = f("Maybe some other time")

    ion "[ion_badend]"


label goodend:
    $ ion_goodend = f("I would love to go out with you!")

    ion "[ion_goodend]"