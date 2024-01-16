from src.HTML import HTML
from src.H1 import H1
from src.DIV import DIV
from src.P import P
from src.IMG import IMG
from src.A import A
import webbrowser

if __name__ == "__main__":

    img = IMG("https://avatars.githubusercontent.com/u/57630920?v=4", "My-Avatar", "200px", "200px")
    h1 = H1("Ismail Boularbah", "HTML_TAG_ID", "HTML_TAG_CLASS")
    p = P("TypeScript enthusiast and competitive programmer.", "P_TAG_ID", "P_TAG_CLASS")
    a = A("GitHub Profile", "https://github.com/boularbahsmail", "_blank", "A_TAG_ID", "A_TAG_CLASS")

    div = DIV(f'{img}{h1}{p}{a}', "DIV_TAG_ID", "DIV_TAG_CLASS")

    myWebsiteContent = f'{div}'
    myWebsite = HTML("My Web Page Generated With Python", myWebsiteContent)

    with open("index.html", "w") as index:
        index.write(f'{myWebsite}')
        print("HTML Page Saved Successfully!!")
        # Open index.html file
        webbrowser.open("index.html")
