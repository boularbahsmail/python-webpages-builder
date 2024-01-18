class P:
    def __init__(self, CONTENT, ID="", CLASS=""):
        self.__CONTENT = CONTENT
        self.__ID = ID
        self.__CLASS = CLASS

    def getContent(self):
        return self.__CONTENT
    
    def setContent(self, newContent):
        self.__CONTENT = newContent

    def getID(self):
        return self.__ID
    
    def setID(self, newID):
        self.__ID = newID

    def getClass(self):
        return self.__CLASS
    
    def setClass(self, newClass):
        self.__CLASS = newClass

    Content = property(getContent, setContent)
    Id = property(getID, setID)
    Class = property(getClass, setClass)

    def __str__(self):
        return f'<p class="{self.Class}" id="{self.Id}">{self.Content}</p>'
