#################################################################################
# SCREENS for SOCIAL MEDIA SIMULATOR
#
# Filename: game/screens.rpy
# Author: Ashley Trinh
# Date: Dec 2014
# 
screen scanline_overlay:
    zorder 50
    add "gui/scanlines.png"
    



#################################################################################
# MAIN MENU

screen main_menu:
    tag menu

    add "gui/main/mm_bg.png"    

    imagebutton auto "gui/main/login_%s.png" xpos 250 ypos 255 action Start()
    imagebutton auto "gui/main/newuser_%s.png" xpos 250 ypos 287 action Start()
    imagebutton auto "gui/main/quit_%s.png" xpos 250 ypos 319 action Quit()



#################################################################################
# SAVE + LOAD
#
# Since they are very similar, both use file_picker screen

screen file_picker():
    modal True

    default current_file = 0
    if current_file != 0:
        frame: # xalign 0 yalign 0:
            add FileScreenshot(current_file) # size(w,h)

    frame:
        style_group "file_picker"
        # viewport id "file_picker":
        #     scrollbars "vertical"
        #     # xmaximum idk
        #     draggable True mousewheel TrueS

        has vbox

        $ rows = 10            

        # Display ten file slots
        for i in range(1, rows + 1):

            button:
                action FileAction(i)
                xfill True

                has hbox

                $ file_name = FileSlotName(i, rows)
                $ file_time = FileTime(i, empty=_("Empty Slot."))
                $ save_name = FileSaveName(i)

                text "[file_name]. [file_time!t]\n[save_name!t]"

                key "save_delete" action FileDelete(i)

screen save():
    modal True

    drag:
        drag_name "save"
        yalign 0.5
        drag_handle (0, 0, 282, 20)

        xalign 0.5

        has vbox

        label "Save"
        use file_picker
        # extra stuff to get back to the main screen

screen load():
    tag menu
    use file_picker
    # extra stuff to get back to the main screen

#################################################################################
# STYLES FOR FILE PICKER

init -2:
    style file_picker_frame is frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is button
    style file_picker_text is button_text



#################################################################################
# INPUT
#
# Displayed when renpy.input() is called

# MAKE INPUT WORK WITH EYENET, USE TO CHECK STRINGS OF APP IDs 
# NOT FINISHED: SYNC WITH SCRIPT.RPY AND MAKE SURE EVERYTHING WORKS HAPPY 

screen input(prompt):

    # if prompt is "eyenet":
    #     modal False
    #     zorder 10
    #     drag:
    #         drag_name "eyenet"
    #         yalign 0.3
    #         xalign 0.5
    #         drag_handle(0, 0, 283, 19)

    #         frame style "eyenet_frame":
    #             fixed:
    #                 input id "eye_input" style "default" xpos 8 ypos 83
    #                 imagebutton auto "gui/screens/eyenet_view_%s.png" xpos 250 ypos 83 focus_mask True action GetInput("input", "eye_input")
    #                 imagebutton auto "gui/screens/eyenet_close_%s.png" xpos 267 ypos 4 focus_mask True action Hide("input")
        
    # else:
        modal True
        #draggable
        drag:
            drag_name "input" 
            xalign 0.5 yalign 0.5
            drag_handle (0, 0, 282, 20)

            has vbox

            label "Query"
            frame id "system":
                vbox:
                    spacing 6
                    text prompt
                    hbox:
                        spacing 3
                        frame style "input_window":
                            input id "input" style "input_window_text"
                        textbutton _("next") action GetInput("input", "input")

#################################################################################
# STYLES FOR INPUT

init -2:
    style input_window:
        background Frame("gui/input_bg.png", 4, 4, True)
        hover_background Frame("gui/input_bg.png", 4, 4, True)
        xpadding 3 ypadding 3
        xsize 357 ysize 13
    
    style input_window_text is default:
        color "#000"
    
    # style eyenet_frame is frame:
    #     background Frame("gui/screens/eyenet_bg.png", 4, 4, True)
    #     xsize 283 ysize 103
    #     xpadding 0 ypadding 0
    #     xmargin 0 ymargin 0
    
    

#################################################################################
# SYSTEM DIALOG 
# 
# For when your computer talks to you. 

screen dialog(label=None,body=None,action=Return()):
    modal True

    # Draggable
    drag id "dialog_drag":
        drag_name "system_dialog"
        xalign 0.5 yalign 0.5
        drag_handle(0, 0, 300, 20)

        has vbox

        label label id "dialog_label" style "dialog_label"
        frame id "dialog_frame" style "dialog_frame":
            has vbox

            text body
            textbutton _("OK") style "ok_button" action action

#################################################################################
# STYLES FOR DIALOG
init -2:
    style ok_button is button:
        xalign 1.0 
    style ok_button_text is button_text

    style dialog_label is label:
        xsize 300
    style dialog_frame is frame:
        xsize 300



#################################################################################
# YES/NO PROMPT
#
# Asks user yes or no question

# Create drag parent object
# drag yesno_drag = Drag(d=Vbox())
# vbox special_box = Vbox(box_label, box_frame, **properties)
# yesno_drag.w = width
# box_label xsize width
# box_frame xsize width

screen yesno_prompt(message, yes_action, no_action):
    modal True
    zorder 10

    # Make screen darker to show that its serious
    # add "yesno_overlay.png"

    # Draggable
    drag id "yesno_drag":
        drag_name "yesno_prompt"
        drag_handle(0, 0, 100, 20)
        xalign 0.5 yalign 0.5

        has vbox

        label "Query" xsize 240
        frame id "system" xsize 240 :
            vbox:
                spacing 5
                xalign 0.5
            
                text _(message)

                hbox:
                    xalign 0.5
                    spacing 40
                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action


#################################################################################
# PREFERENCES
#
# User prefs

screen preferences():
    
    modal True

    # Draggable
    drag:
        drag_name "yesno_prompt"
        yalign 1.0
        drag_handle(0, 0, 200, 20)

        xalign 0.5

        has vbox

        label "Control Panel"
        frame id "system":
            vbox:
                text _("Scanlines")

                hbox:
                    if persistent.scanlines:
                        textbutton _("ON") action SetField(persistent, "scanlines", True) style pref_choice
                        textbutton _("OFF") action SetField(persistent, "scanlines", False)
                    else:
                        textbutton _("ON") action SetField(persistent, "scanlines", True) 
                        textbutton _("OFF") action SetField(persistent, "scanlines", False) style pref_choice

init -2:
    style pref_choice_button is button
    style pref_choice_button_text is button_text:
        color "#000080"

   
#################################################################################
# DESKTOP / MAIN SCREEN
#
# It's going to use a bunch of other screens... or maybe I should use an imagemap?

screen desktop:

    tag desktop

    add "gui/desktop_bg.png"

    imagebutton auto "gui/buttons/quit_%s.png" xpos 5 ypos 5 focus_mask True action Quit()

    imagebutton auto "gui/buttons/save_%s.png" xpos 25 ypos 6 focus_mask True action Show("save")

    imagebutton auto "gui/buttons/pref_%s.png" xpos 44 ypos 5 focus_mask True action Show("preferences")

    imagebutton auto "gui/buttons/trash_%s.png"  xpos 657 ypos 497 action ui.callsinnewcontext("open_trash")


#################################################################################
# ICONS
#

screen eyenet_icon:
    imagebutton auto "gui/buttons/eyenet_%s.png" xpos 651 ypos 340 action Show("bookface")

screen mailbox_icon:
    if new_message_count() > 0:
        imagebutton auto "gui/buttons/mail_%s.png" xpos 661 ypos 423 action Show("mailbox")
        add "gui/buttons/mail_hasnew.png" xpos 661 ypos 423 alpha True
    else:
        imagebutton auto "gui/buttons/mail_%s.png" xpos 661 ypos 423 action Show("mailbox")
        
#################################################################################
# BOOKFACE
#

screen bookface:
    modal False
    zorder 10
    drag:
        drag_name "bookface"
        xalign 0.3 yalign 0.5
        drag_handle (0, 0, 310, 23)

        frame style "bookface_frame":
            fixed:
                imagebutton auto "gui/screens/notifications_%s.png" xpos 17 ypos 146 focus_mask True action Show("notifications")
                imagebutton auto "gui/screens/feed_%s.png" xpos 134 ypos 147 focus_mask True action NullAction()
                imagebutton auto "gui/screens/groups_%s.png" xpos 234 ypos 146 focus_mask True action NullAction()
                imagebutton auto "gui/screens/bookclose_%s.png" xpos 291 ypos 4 focus_mask True action Hide("bookface")

                if new_notifications:
                    add "gui/screens/notifications_hasnew.png" xpos 0 ypos 0 alpha True
                if new_feed:
                    add "gui/screens/newsfeed_hasnew.png" xpos 0 ypos 0 alpha True
                if new_groups:
                    add "gui/screens/groups_hasnew.png" xpos 0 ypos 0 alpha True

screen notifications:
    modal False
    zorder 10
    drag:
        drag_name "notifications"
        xalign 0.2 yalign 0.5
        drag_handle (0, 0, 222, 22)

        frame style "notifications_frame":
            fixed:
                imagebutton auto "gui/screens/bookclose_%s.png" xpos 203 ypos 4 xanchor 0 yanchor 0 focus_mask True action Hide("notifications")                

init -2:

    style bookface_frame is frame:
        background Frame("gui/screens/book_bg.png", 4, 4, True)
        xsize 310 ysize 214
        xmargin 0 ymargin 0 
        xpadding 0 ypadding 0 

    style notifications_frame is frame:
        background Frame("gui/screens/notifications_bg.png", 2, 22)
        xsize 222 yfill False

    style notification_text is default:
        color '#00FF00'

#################################################################################
# MAILBOX
#

init python:
    current_message = None


screen mailbox:
    # default current_message = None
    # $ available_drafts = [i for i in contacts if i.draft_label]    

    modal False

    # Draggable
    drag id "mail_drag":
        drag_name "mail_window"
        xalign 0.5 yalign 0.5
        drag_handle(0, 0, 400, 20)

        has vbox

        label "Mailbox: You have %d new messages!" % (new_message_count())

        frame:
            style_group "mailbox"

            has vbox

            for item in mail:
                if item.view:
                    textbutton ("NEW! \n" + "From: " + item.sender + "\n" + "Subject: " + item.subject) action [item.mark_read, SetVariable("current_message", item), Show("message")] style "large_textbutton"
                else:
                    textbutton (item.sender + item.subject) action [SetVariable("current_message", item), Show("message")] style "large_textbutton"
                    
                            

screen message:
    zorder 10
    drag:
        drag_name "message"
        yalign 1.0
        drag_handle(0, 0, 200, 20)

        xalign 0.5

        has vbox
       

        label "Message"
        frame id "system" style "message_frame":
            use mailbox_commands
            vbox:
                hbox:
                    null height 20
                if current_message is not None:
                    $ sender = current_message.sender
                    $ subject = current_message.subject 
                    $ body = current_message.body
                    frame style "text_frame":
                        has vbox
                        text ("From: [current_message.sender]") 
                        text ("Subject: [current_message.subject]")
                        text body
                        if current_message.subject == "Bookface Dashboard Installer":
                            null height 20
                            textbutton ("Download attachment: dashboard_installer.exe") action Show("eyenet_icon") style "large_textbutton"
                else:
                    hbox:
                        null height 50


init -2:
    $ show_bf = False
    style message_frame is frame:
        ymaximum 300 yfill False
    style text_frame is frame:
        background Frame("gui/buttons/largetext_ground.png", 6, 6, True)


screen mailbox_commands:
    hbox:
        spacing 3
        # if available_drafts:
        #     textbutton "Draft New" action Show("contacts") style "large_textbutton"
        # else:
        #     textbutton "Draft New" action None style "large_textbutton"
        if current_message and current_message.reply_label:
            textbutton "Reply" action current_message.reply style "large_textbutton"
        else:
            textbutton "Reply" action None style "large_textbutton"
        # if current_message:
        #     textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)] style "large_textbutton"
        # else:
        #     textbutton "Delete" action None style "large_textbutton"
        # if new_message_count() > 0:
        #     textbutton "Mark All Read" action mark_all_read style "large_textbutton"
        # else:
        #     textbutton "Mark All Read" action None style "large_textbutton"
        # textbutton "Restore All" action restore_all style "large_textbutton"
        textbutton "Exit" action Hide("message") style "large_textbutton"










