class IMG:
    def __init__(self, SRC, ALT, WIDTH, HEIGHT, ID="", CLASS=""):
        self.__SOURCE = SRC
        self.__ALT = ALT
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__ID = ID
        self.__CLASS = CLASS

    @property
    def Source(self):
        return self.__SOURCE
    
    @Source.setter
    def Source(self, newSource):
        self.__SOURCE = newSource

    @property
    def Alt(self):
        return self.__ALT
    
    @Alt.setter
    def Alt(self, newAlt):
        self.__ALT = newAlt

    @property
    def Width(self):
        return self.__WIDTH
    
    @Width.setter
    def Width(self, newWidth):
        self.__WIDTH = newWidth

    @property
    def Height(self):
        return self.__HEIGHT
    
    @Height.setter
    def Height(self, newHeight):
        self.__WIDTH = newHeight

    @property
    def Id(self):
        return self.__ID
    
    @Id.setter
    def Id(self, newID):
        self.__ID = newID

    @property
    def Class(self):
        return self.__CLASS
    
    @Class.setter
    def Class(self, newClass):
        self.__CLASS = newClass

    def __str__(self):
        return f'<img src="{self.Source}" alt="{self.Alt}" width="{self.Width}" height="{self.Height}" class="{self.Class}" id="{self.Id}" />'
