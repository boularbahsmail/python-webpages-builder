def generate():
    tagType = input("Tag type (Inline, Bloc) : ")
        
    tagName = input("Tag (name) : ")
    tagID = input("Tag (id) : ")
    tagClass = input("Tag (class) : ")
    attributes = ''

    if (tagType == "Inline" or tagType == "inline" or tagType == "INLINE"):
        attributesLenght = input("Number of attributes : ")

        for i in range(int(attributesLenght)):
            attributeName = input(f"Name of attribute number {i+1} : ")
            attributeValue = input(f"Value of attribute number {i+1} : ")

            attributeFormat = f'{attributeName}="{attributeValue}"'
            attributes += attributeFormat + " "

        Tag = f'<{tagName} {attributes}id="{tagID}" class="{tagClass}" />'
        print(Tag)
        
    elif (tagType == "Bloc" or tagType == "bloc" or tagType == "BLOC"):
        tagContent = input("Tag (content) : ")
        attributesLenght = input("Number of attributes : ")

        for i in range(int(attributesLenght)):
            attributeName = input(f"Name of attribute number {i+1} : ")
            attributeValue = input(f"Value of attribute number {i+1} : ")

            attributeFormat = f'{attributeName}="{attributeValue}"'
            attributes += attributeFormat + " "

        Tag = f'<{tagName} {attributes}id="{tagID}" class="{tagClass}">{tagContent}</{tagName}>'
        print(Tag)

generate()