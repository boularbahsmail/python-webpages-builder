from src.HTML import HTML
from src.H1 import H1
from src.DIV import DIV
from src.P import P
from src.IMG import IMG
from src.A import A
import webbrowser

if __name__ == "__main__":

    img = IMG("https://avatars.githubusercontent.com/u/57630920?v=4", "My-Avatar", "200px", "200px")
    h1 = H1("Ismail Boularbah")
    p = P("TypeScript enthusiast and competitive programmer.", "about_p", "about_p")
    a = A("GitHub Profile", "https://github.com/boularbahsmail", "_blank", "github_profile_link", "github_profile_link")

    card = DIV(f'{img}{h1}{p}{a}', "card", "card")
    container = DIV(f'{card}', "container", "container")

    myWebsiteContent = f'{container}'
    myWebsite = HTML("My Web Page Generated With Python", myWebsiteContent)

    with open("index.html", "w") as index:
        index.write(f'{myWebsite}')
        print("HTML Page Saved Successfully!!")
        # Open index.html file
        webbrowser.open("index.html")
