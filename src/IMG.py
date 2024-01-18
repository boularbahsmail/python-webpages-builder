class IMG:
    def __init__(self, SRC, ALT, WIDTH, HEIGHT, ID="", CLASS=""):
        self.__SOURCE = SRC
        self.__ALT = ALT
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__ID = ID
        self.__CLASS = CLASS

    def getSource(self):
        return self.__SOURCE
    
    def setSource(self, newSource):
        self.__SOURCE = newSource

    def getAlt(self):
        return self.__ALT
    
    def setAlt(self, newAlt):
        self.__ALT = newAlt

    def getWidth(self):
        return self.__WIDTH
    
    def setWidth(self, newWidth):
        self.__WIDTH = newWidth

    def getHeight(self):
        return self.__HEIGHT
    
    def setHeight(self, newHeight):
        self.__WIDTH = newHeight

    def getID(self):
        return self.__ID
    
    def setID(self, newID):
        self.__ID = newID

    def getClass(self):
        return self.__CLASS
    
    def setClass(self, newClass):
        self.__CLASS = newClass

    Src = property(getSource, setSource)
    Alt = property(getAlt, setAlt)
    Width = property(getWidth, setWidth)
    Height = property(getHeight, setHeight)
    Id = property(getID, setID)
    Class = property(getClass, setClass)

    def __str__(self):
        return f'<img src="{self.Src}" alt="{self.Alt}" width="{self.Width}" height="{self.Height}" class="{self.Class}" id="{self.Id}" />'
