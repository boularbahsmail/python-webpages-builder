class HTML:
    def __init__(self, TITLE, CONTENT):
        self.__TITLE =  TITLE
        self.__CONTENT = CONTENT

    @property
    def Title(self):
        return self.__TITLE
    
    @Title.setter
    def Title(self, newTitle):
        self.__TITLE = newTitle

    @property
    def Content(self):
        return self.__CONTENT
    
    @Content.setter
    def Content(self, newContent):
        self.__CONTENT = newContent

    def __str__(self):
        return f'<!DOCTYPE html><html><head><title>{self.Title}</title></head><body>{self.Content}</body></html>'