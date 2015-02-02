#################################################################################
# CUSTOM FUNCTIONS for SOCIAL MEDIA SIMULATOR
#
# Filename: game/functions.rpy
# Author: Ashley Trinh
# Date: Dec 2014
# 

init -2 python:

    #################################################################################
    # Use python's random module because we don't want RenPy to save these 
    # random numbers

    import random
    random.seed()

    import renpy.store as store
    new_list = []
    read_list = []
    trash = []

    #################################################################################
    # Generate tuples of random floats between 0.0 and 1.0 so we can randomly 
    # align things. Returns a Style object with alignment.

    def random_align(yes=False):
        style.random = Style(style.default)

        if not yes:
            style.random.align = (0.5, 0.5)
        else:
            style.random.xalign = random.random()
            style.random.yalign = random.random()

        return style.random

    #################################################################################
    # Custom Action GetInput for button to get input from renpy.input
    
    class GetInput(Action):

        def __init__(self, input_txt, input_id):
            self.input_txt = input_txt
            self.input_id = input_id

        def __call__(self):
            if renpy.get_widget(self.input_txt, self.input_id):
                return str(renpy.get_widget(self.input_txt, self.input_id).content)


    
            


            


            



