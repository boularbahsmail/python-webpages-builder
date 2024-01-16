class A:
    def __init__(self, CONTENT, LINK, TARGET, ID, CLASS):
        self.__CONTENT = CONTENT
        self.__LINK = LINK
        self.__TARGET = TARGET
        self.__ID = ID
        self.__CLASS = CLASS

    def getContent(self):
        return self.__CONTENT
    
    def setContent(self, newContent):
        self.__CONTENT = newContent

    def getLink(self):
        return self.__LINK
    
    def setLink(self, newLink):
        self.__LINK = newLink

    def getTarget(self):
        return self.__TARGET
    
    def setTarget(self, newTarget):
        self.__TARGET = newTarget

    def getID(self):
        return self.__ID
    
    def setID(self, newID):
        self.__ID = newID

    def getClass(self):
        return self.__CLASS
    
    def setClass(self, newClass):
        self.__CLASS = newClass

    Content = property(getContent, setContent)
    Link = property(getLink, setLink)
    Target = property(getTarget, setTarget)
    Id = property(getID, setID)
    Class = property(getClass, setClass)

    def __str__(self):
        return f'<a href="{self.Link}" target="{self.Target}" class="{self.Class}" id="{self.Id}">{self.Content}</a>'
