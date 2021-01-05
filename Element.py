class Element:
    def __init__(self, element, level):
            self.e = element
            self.l = level

    def __str__(self):
        return 'Element: ' + self.e + ', Level: ' + str(self.l)
    
    def __call__(self):
        return ('Element: ' + self.e, 'Level: ' + str(self.l))