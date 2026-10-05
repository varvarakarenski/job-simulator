# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default player_name = "Alex"
define p = Character("[player_name]")

default not_fit = False
default picked_languages = False
default picked_systems = False
default evil_points = 0 
default worked_in_HR = False

screen choice_timer(time_limit, timeout_label):
    timer time_limit action Jump(timeout_label)

    bar: 
        xalign 0.5
        yalign 0.1
        xmaximum 400
        value AnimatedValue(0.0, time_limit, delay=time_limit, old_value=time_limit)

default answered1 = False 
default answered2 = False
default answered3 = False    
# Game starts here

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    e "Hello! Ready for your interview?"

    menu:
        "Yes.":
            pass  
        "No.":
            jump what_am_i_doing_here

    e "Now, let me take a look at your resume."

    e "What was your name again?"

    $ player_name = renpy.input("What is your name?", length=50).strip()

    e "Great. I'm Eileen. I'll be your interviewer today."

    e "..."

    e "Here you are. You're interviewing for the role of \"Destruction Intern,\" correct?"

    menu:
        "That's right.":
            pass
        "Not quite.":
            jump what_am_i_doing_here

    e "Let's see. \"Experience\" ... Line cook ... Dog Walker ... "

    e "Wow - you interned for our rival, Evil Inc. !"

    e "Seeing as our interests are pretty similar. I'd like to ask you a few questions."

    e "What was your primary role at Evil, Inc.?"

    menu: 
        "I was a janitor.":
            $ not_fit = True
            jump no_job
        "I was an engineer.":
            $ evil_points += 10
            pass
        "I was a developer.":
            $ evil_points += 5
            pass
        "I worked in HR.":
            $ worked_in_HR = True
            $ evil_points += 25
            pass


    e "Wonderful. "

    e "What kind of projects did you work on?"

    menu: 
        "I designed weapons and defense technologies.":
            $ evil_points += 5
            jump skills
        "I stole candy from babies.":
            $ evil_points += 10
            jump skills
        "I was a field agent in the tying-peoples-shoelaces-together division.":
            $ evil_points += 5
            jump skills
        "I scheduled a lot of meetings that could have been emails.":
            $ evil_points += 10
            jump skills
        "I programmed change detection algorithms to monitor climate change from space.":
            $ not_fit: True
            jump no_job

label skills:
    e "And what skills did you apply to this project?"

label skills_loop:
    if picked_languages or picked_systems:
        e "Anything else?"

    menu:

        "Python, Ada, and C++. " if not picked_languages:
            $ picked_languages = True
            jump skills_loop

        "Evil systems engineering and evil computer-aided design." if not picked_systems:
            $ picked_systems = True 
            jump skills_loop

        "Empathy and compassion.":
            $ not_fit = True
            jump no_job

        "That's all." if picked_languages or picked_systems:
            pass

    e "Excellent. Let's move on to the next part of the interview."
    jump speed_round

label speed_round:
    e "SPEED ROUND!"
    jump timed_questions

label timed_questions:
    show screen choice_timer(time_limit=5.0, timeout_label="intrview_timeout")
    $ math_answer = renpy.input("What is pi/2 radians in degrees?").strip()
    
    if math_answer == "90":
        hide screen choice_timer 
        $ answered1 = True
        pass

    show screen choice_timer(time_limit=5.0, timeout_label="interview_timeout")
    $ gravity_answer = renpy.input("What is the acceleration of gravity on earth in m/s^2?").strip()
    
    if gravity_answer == "9.8":
        hide screen choice_timer
        $ answered2 = True
        pass

    show screen choice_timer(time_limit=5.0, timeout_label="interview_timeout")
    $ moon_answer = renpy.input("What is the radius of Earth's Moon, to the nearest kilometer?").strip()
    if moon_answer == "1737":
        hide screen choice_timer
        $ answered3 = True
        pass

    e "Excellent. You're in stellar shape as a candidate."
    jump scenarios

label scenarios:
    e "I'd like to give you a few situations and see what you'd do."

    e "Scenario 1: You're walking down the street and witness a woman's purse being stolen. What do you do?"
    menu:
        "Run after the thief.":
            $ not_fit = True
            jump no_job
        "Break out into song to motivate passers by to help recover the purse.":
            e "...Sure."
            $ evil_points += 15
            pass
        "Walk up to the woman and ask for her watch too.":
            $ evil_points += 10
            pass
    
    e "Nice. Scenario 2: Someone at your birthday party is allergic to the cake you ordered for everyone. What's your plan?"
    menu:
        "Have them sit and watch everyone else eat cake.":
            $ evil_points += 5
            pass
        "Reluctantly drive to the store and buy some cupcakes.":
            $ not_fit = True
            jump no_job
        "Throw the cake away and yell at them for it being \"their fault\"":
            e "Wow. These are seriously evil intentions."
            $ evil_points += 20
            pass

    e "Last one - Scenario 3. Your mega expensive super-yacht is sinking, and you must choose who to save."
    menu:
        "The captain.":
            $ not_fit = True
            jump no_job
        "My sister's handsome boyfriend.":
            $ not_fit = True
            jump no_job
        "The $500,000 in cash I had onboard \"just in case.\"":
            $ evil_points += 10
            pass
        "Save nothing and swim away myself.":
            $ evil_points += 15
            e "A truly badass and unreasonably selfish decision. Admirable."
            pass


# Bad consequences

label interview_timeout:
    e "You're hesitating... uncertainty is a terrible trait in this office."
    $ not_fit = True
    jump no_job

label what_am_i_doing_here:
    e "Then, why exactly are you here?"

    menu:
        "For funsies.":
            pass
        "Dunno.":
            pass

    e "..."
    jump no_job

label no_job: 
    if not_fit:
        e "..."
        e "I don't think you're the best fit for our industry."
        e "We try to priotitize candidates who are ultimately and indubitably morally corrupt."
        e "Let's end it here."
        
    "You didn't get the job. Better luck next time."
    return

# Good consequences

label got_the_job:
    e "Well, [player_name], I've got to give it to you."
    e "This has been a great interview, and accoring to our state of the art monitoring systems, you scored [evil_points] evil points!"
    if worked_in_HR:
        e "And if I recall corretly - you worked in HR. That's a pretty big evil indicator."
        pass
    e "You should be proud."
    e "If you'll accept the offer..."
    e "Welcome to Obliterate Corp. !"

    return