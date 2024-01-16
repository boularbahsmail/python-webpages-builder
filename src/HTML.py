class HTML:
    def __init__(self, TITLE, CONTENT):
        self.__TITLE =  TITLE
        self.__CONTENT = CONTENT

    def getTitle(self):
        return self.__TITLE
    
    def setTitle(self, newTitle):
        self.__TITLE = newTitle

    def getContent(self):
        return self.__CONTENT
    
    def setContent(self, newContent):
        self.__CONTENT = newContent

    Title = property(getTitle, setTitle)
    Content = property(getContent, setContent)

    def __str__(self):
        return f'<!DOCTYPE html><html><head><title>{self.Title}</title></head><body>{self.Content}</body></html>'