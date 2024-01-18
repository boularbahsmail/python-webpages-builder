class A:
    def __init__(self, CONTENT, LINK, TARGET, ID="", CLASS=""):
        self.__CONTENT = CONTENT
        self.__LINK = LINK
        self.__TARGET = TARGET
        self.__ID = ID
        self.__CLASS = CLASS

    @property
    def Content(self):
        return self.__CONTENT
    
    @Content.setter
    def Content(self, newContent):
        self.__CONTENT = newContent

    @property
    def Link(self):
        return self.__LINK
    
    @Link.setter
    def Link(self, newLink):
        self.__LINK = newLink

    @property
    def Target(self):
        return self.__TARGET
    
    @Target.setter
    def Target(self, newTarget):
        self.__TARGET = newTarget

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
        return f'<a href="{self.Link}" target="{self.Target}" class="{self.Class}" id="{self.Id}">{self.Content}</a>'
