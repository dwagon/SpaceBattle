import component
import random


##########################################################################
##########################################################################
##########################################################################
class Shield(component.Misc):

    def __init__(self):
        component.Misc.__init__(self)
        self["maxshield"] = 100
        self["shield"] = 100
        self["rechargerate"] = 10  # Lower is quicker

    ######################################################################
    def turn(self):
        if self["shield"] < self["maxshield"]:
            if random.randrange(self["rechargerate"]) == 0:
                self["shield"] += 1

# EOF
