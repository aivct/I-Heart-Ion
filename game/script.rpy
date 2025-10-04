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
        if(encoding.words.get(word, False)):
            return word 
        else:
            return hashWord(word)
    
    # Turns a "word" into a ■ symbol
    def hashWord(word):
        return "■"

    def encode(string):
        tokens = tokenize(string)
        tokens = map(encodeWord, tokens)
        return detokenize(tokens)


init python in encoding:
    words = {
        "you": True}

init python in dialogue:
    _constant = True
    stage1_ion = "How are you today?"
    stage1_option1_1 = "Whatever"
    stage1_option1_2 = "Bad"
    stage1_option1_3 = "Good, how are you?"
    stage1_option1_4 = "Purple skies"
    stage1_option1_5 = "Boo Boo"

define ion = Character("Eileen")

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
    $ dialogueIon = f"{encode(dialogue.stage1_ion)}"

    ion "[dialogueIon]"

    $ option1 = f"{encode(dialogue.stage1_option1_1)}"
    $ option2 = f"{encode(dialogue.stage1_option1_2)}"
    $ option3 = f"{encode(dialogue.stage1_option1_3)}"
    $ option4 = f"{encode(dialogue.stage1_option1_4)}"
    $ option5 = f"{encode(dialogue.stage1_option1_5)}"
    
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

    menu:

        "LC: [LC] EC: [EC]"

        "To ask her right away.":

            jump stage1_1

        "To ask her later.":

            jump stage1_1