#################################################################################
# SCRIPT for SOCIAL MEDIA SIMULATOR
#
# Filename: game/script.rpy
# Author: Ashley Trinh
# Date: Dec 2014
# 

image animation = Animation("gui/main/mm_1.png", .5, "gui/main/mm_2.png", .5, "gui/main/mm_3.png", .5, "gui/main/mm_4.png", .5, "gui/main/mm_5.png", .5,"gui/main/mm_6.png", .5,"gui/main/mm_7.png", .5,"gui/main/mm_8.png", .5,"gui/main/mm_9.png", .5,"gui/main/mm_10.png", .5)
image scanlines = Image("gui/scanlines.png", alpha=True)
$ persistent.browser_installed = True
$ current_message = None


# The game starts here.

label splashscreen:
    show image "scanlines" onlayer texture
    show animation 
    $ renpy.pause(5.0)   
    return

label start:
    $ mail = []
    $ mail_queue = [] # for message delay
    $ notifications = []  # for draft feature
    $ available_drafts = []
    $ new_notifications = False # for thebookface
    $ new_feed = False # for thebookface
    $ new_groups = False # for thebookface
    $ open_count = 0 # for thebookface

    $ show_bf = False

    show screen scanline_overlay
    show screen desktop
    call screen dialog("Setup Wizard", "Welcome! The Setup Wizard will now prepare your login profile. Click OK to continue.", Jump("name_prompt"))

label name_prompt:

    python:
        n_input = renpy.input("What is your real name?")
        n_input = n_input.strip()

    if n_input == "":
        $ persistent.n = "Anon"
    else:
        $ persistent.n = n_input
    
    call screen yesno_prompt("Your name is [persistent.n]. Is this correct?", Jump("screenname_prompt"), Jump("name_prompt2"))

label name_prompt2:
    
    python:
        n_input = renpy.input("I'm sorry, can you please enter your real name again?")
        n_input = n_input.strip()

    if n_input == "":
        $ persistent.n = "Anon"
    else:
        $ persistent.n = n_input

    call screen yesno_prompt("Your name is [persistent.n]. Is this correct?", Jump("screenname_prompt"), Jump("name_prompt2"))

label screenname_prompt:
    python:
        s_input = renpy.input("Now, choose a screenname to display to others.")
        s_input = s_input.strip()

    if s_input is "":
        $ persistent.s = "Anon"
    else:
        $ persistent.s = s_input

    call screen yesno_prompt("You want to be known as [persistent.s]?", Jump("setup_complete"), Jump("screenname_prompt2"))

label screenname_prompt2:
    python:
        s_input = renpy.input("I'm sorry, can you please enter your display name again?")
        s_input = s_input.strip()

    if s_input is "":
        $ persistent.s = "Anon"
    else:
        $ persistent.s = s_input
        
    call screen yesno_prompt("You want to be known as [persistent.s]?", Jump("setup_complete"), Jump("screenname_prompt2"))

label setup_complete:
    call screen dialog("System","Congratulations! Your profile has been saved. You may now use your information to log in to your account.")

    $ add_message("Bookface Dashboard Installer", "admin@thebookface.net", "To install thebookface dashboard, download the attachment and run it. \n We hope you enjoy your time with us! \n \n Erica \n System Admin @ thebookface.net")

    show screen mailbox_icon(True)

    $ renpy.pause()

# label eyenet_input:

#     python:
#         eye_input = renpy.input("eyenet")
    
#     if eye_input == "b":

#         if seen_setup: 
#             $ new_notifications = True

#         show screen bookface  

#     else:
#         return

#     $ renpy.pause()

# label reply1_label:
#     $ add_message("Welcome to Ren'Py!", "Eileen", "This is a test message.", delay=True)

#     $ renpy.pause(hard=True)

# label 
    

    

    


# label open_eyenet:
#     show screen eyenet
#     $ renpy.pause()

# label close_eyenet:
#     hide screen eyenet
#     $ renpy.pause()

# label open_mail:

    
#     $ renpy.pause()
