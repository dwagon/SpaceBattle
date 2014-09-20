import component


class TieEngine(component.Engine):

    def __init__(self):
        component.Engine.__init__(self)
        self["space"] = 5
        self["mass"] = 25
        self["force"] = 20

# EOF
