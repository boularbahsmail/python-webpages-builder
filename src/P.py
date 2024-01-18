class P:
    def __init__(self, CONTENT, ID="", CLASS=""):
        self.__CONTENT = CONTENT
        self.__ID = ID
        self.__CLASS = CLASS

    @property
    def Content(self):
        return self.__CONTENT
    
    @Content.setter
    def Content(self, newContent):
        self.__CONTENT = newContent

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
        return f'<p class="{self.Class}" id="{self.Id}">{self.Content}</p>'
