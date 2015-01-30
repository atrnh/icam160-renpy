#################################################################################
# STYLES for SOCIAL MEDIA SIMULATOR
#
# Filename: game/styles.rpy
# Author: Ashley Trinh
# Date: Dec 2014
# 

init -1 python hide:

    ###################################################
    # DEFAULT STYLE
    # All styles are children of default

    # Body font default
    style.default.font = "fonts/PIXELADE.ttf"
    style.default.size = 13
    style.default.color = "#000"


    # style text is default

    # The following is styling for all the header fonts
    # which other styles will inherit from

    style.header_text = Style(style.default)
    style.header_text.font = "fonts/notalot35.ttf"
    style.header_text.size = 15
    style.header_text.color = "#FFF"

    ###################################################
    # CUSTOM GUI STYLING
    # PARENT STYLES

    style.vbox.xpadding = 0
    style.vbox.ypadding = 0

    # style.drag.

    style.frame.background = Frame("gui/dialog_bg.png", 4, 4, True)
    style.frame.xmargin = 0
    style.frame.bottom_margin = 3 
    style.frame.top_margin = 0
    style.frame.xpadding = 3
    style.frame.ypadding = 7
    style.frame.align = (0.5, 0.5)
    style.frame.xminimum = 100
    style.frame.xmaximum = 400
    style.frame.xfill = True
    # style.frame.yfill = False
    

    style.button.background = Frame("gui/buttons/text_ground.png", 4, 4, True)
    style.button.hover_background = Frame("gui/buttons/text_hover.png", 4, 4, True)
    # Accomodate styling for button hover effect
    style.button.right_margin = 1 
    style.button.bottom_margin = 0
    style.button.xpadding = 5
    style.button.ypadding = 3

    style.button_text = Style(style.header_text)
    style.button_text.color = "#000"
    style.button_text.align = (0.5, 0.5)

    style.large_textbutton = Style(style.button)
    style.large_textbutton.background = Frame("gui/buttons/largetext_ground.png", 6, 6, True)
    style.large_textbutton.hover_background = Frame("gui/buttons/largetext_hover.png", 6, 6, True)

    style.large_textbutton_text = Style(style.button_text)


############# THESE MIGHT BE IMAGEMAPS INSTEAD ##################
    # # Close button for thebookface window
    # style.bf_x_button is x_button:
    #     background "gui/buttons/bfx_ground.png"
    #     hover background "gui/buttons/bfx_hover.png"

    # # Close button for EyeNet
    # style.net_x_button is x_button:
    #     background "gui/buttons/netx_ground.png"
    #     hover background "gui/buttons/netx_hover.png"


    # Title thingies
    style.label.background = Frame("gui/label_bg.png", 4, 4, True)
    style.label.bottom_margin = 0 
    style.label.xpadding = 5
    style.label.ypadding = 6
    style.label.xminimum = 100
    style.label.xmaximum = 400
    style.label.ysize = 20
    style.label.xfill = True 

    style.label_text = Style(style.header_text)
    style.label_text.xalign = 0.0 

    style.label_button = Style(style.button)

    # # "System dialog" boxes
    # style dialog is frame

    # style dialog_text is text:
    #     xalign 0.5

    # style dialog_label is label

    # style tooltip is text:
    #     background Frame("gui/tooltip_bg.png", 1, 1)
    #     # since font can't change it will always be same height 
    #     ymaximum 14 yminimum 14



