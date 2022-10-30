from tkinter import *
import tkinter as tk
from tkinter import ttk
import PIL
from PIL import ImageTk, Image
import webbrowser


#Opis planet
FULL_EARTH_DESC = "Jest to druga co do wielkości planeta układu słonecznego. \nZiemia, 3 licząc od Słońca, oraz 5 pod " \
                  "względem wielkości \nplaneta Układu Słonecznego. Pod względem średnicy, masy \noraz gęstości jest " \
                  "to największa planeta skalista \nUkładu Słonecznego. Ziemia jest zamieszkana przez miliony " \
                  "\ngatunków, w tym człowieka. \nCiało Centralne: Słońc \nŚrednia prędkość ruchu: 29,78km/s \nTyp " \
                  "planety: Planeta skalista \nMasa: 5,97x10^24 kg \nPromień: 6371km \nOkres obrotu: 23," \
                  "93 H \nPrzyśpieszenie grawitacyjne: 9,80 m/s^2 \nWiek: 4,54 mld lat \nSatelita naturalny: 1 – " \
                  "Księżyc \nSkład Atmosfery: Azot 78%, Tlen 20%, Argon 0.93%, \nDwutlenek węgla 0,04%, Neon, Hel, " \
                  "Metan, Krypton "

EARTH_FACT = "Ziemia jest chyba najciekawszym obiektem w kosmosie \njaki poznaliśmy. To właśnie tutaj powstało zgodnie " \
             "z naszym obecnym \nstanem wiedzy jedyne życie we wszechświecie. "


FULL_JUPITER_DESC = 'Jowisz to największa planeta Układu Słonecznego. \n Jowisz jest jedną z 4 olbrzymich gazowych ' \
                    'planet krążących wokół naszego Słońca. \n Jego masa równa się 320 masom Ziemi, a jest jedynie 2 ' \
                    'razy większa od niej. \n Ma średnicę 142 984 kilometrów. \n A na naszym niebie jest drugą ' \
                    'najjaśniejszą planetą tuż po Wenus. '

JUPITER_FACT = ""

FULL_NEPTUNE_DESC = 'Neptun jest 8 planetą Układu Słonecznego. \n Zalicza się do planet z gruby gazowych olbrzymów. ' \
                    '\n Jego masa jest aż 17 razy większa od masy Ziemi '

NEPTUNE_FACT = ""

FULL_MARS_DESC = 'Mars jest 4 planetą Układu Słoneczego, nazywany również Czerwoną Planetą \n Swój kolor Mars ' \
                 'zawdzięcza dużej zawartości tlenków żelaza. \n To własnie na ta planeta będzie drugą zaraz po ' \
                 'ziemii na której człowiek postawi swoje stopy. '

MARS_FACT = ""

FULL_SATURN_DESC = 'Jest to druga co do wielkości planeta układu słoneczego. \n Masa Satruna jest około 95 razy ' \
                   'większa niż masa Ziemi. \n Ze względu na gazową strukturę, jego gęstość nie przekracza gęstości ' \
                   'wody. \n Doba na tej planecie trwa bardzo krótko bo zaledwie 10.23 godziny '

SATURN_FACT = ""

FULL_VENUS_DESC = 'Jest to jedna z czterech planet skalistych w Układzie Słonecznym. \n Pod względem masy oraz ' \
                  'wielkości jest bardzo podobna do Ziemi. \n Średnica Wenus jest zaledwie 650 kilometrów mniejsza od ' \
                  'ziemskiej. \n A jej masa jest równa 81.5% masy Ziemi. '

VENUS_FACT = ""

FULL_URANUS_DESC = 'Uran to kolejna z planet należąca do Układu Słonecznego. \n Jej okres obiegu wokół Słońca wynosi ' \
                   '84 lata, a czas obrotu trwa jedynie 17 godzin. \n Jej masa jest 14.5 razy wieksza od masy kuli ' \
                   'ziemskiej. '

URANUS_FACT = ""

FULL_MERCURY_DESC = 'Merkury jest 1 planetą Układu Słonecznego przez \n co jest zauważalna jedynie po zmierzchu. \n ' \
                    'Rok na Merkurym trwa zaledwie 88 dni. \n Co ciekawe Merkury ma płynne jądro. \nTo właśnie 42% ' \
                    'masy planety stanowi płynne żelazo '

MERCURY_FACT = ""

#MAKING AN APP WINDOW
class Root(tk.Tk):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    root = Tk()
    root.title("Kosmiczny katalog")
    root.resizable(False, False)

#HYPERLINK FUNCTION
def callback(url):
    webbrowser.open_new_tab(url)

class Opcje:

    def __init__(self, image_name, full_text, fact_text, wiki_url):
        self.image_name = image_name
        self.full_text = full_text
        self.fact_text = fact_text
        self.wiki_url = wiki_url



ziemia = Opcje("Ziemia.png", FULL_EARTH_DESC, EARTH_FACT, "https://pl.wikipedia.org/wiki/Ziemia")
mars = Opcje("Mars.png", FULL_MARS_DESC, MARS_FACT, "https://pl.wikipedia.org/wiki/Mars")

planets = [ziemia, mars]
print(planets)


def show(event):


    for widget in pierwszy_frame.winfo_children():
        widget.destroy()
    for widget in drugi_frame.winfo_children():
        widget.destroy()
    for widget in trzeci_frame.winfo_children():
        widget.destroy()

    link = tk.Label(trzeci_frame, text="Wikipedia", font=('Helveticabold', 10), bg='#121212', fg='green',
                    cursor="hand2")



    type = clicked.get()

    if type == options_list_planets[2]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(ziemia.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=ziemia.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=ziemia.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(ziemia.wiki_url))
        link.pack()

    if type == options_list_planets[3]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(mars.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=mars.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=mars.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION
        link.pack()
        link.bind("<Button-1>", lambda e: callback(mars.wiki_url))

#FUNCTION FOR PLANET OPTION MENU




#Tło aplikacji
HEIGHT = 700
WIDTH = 900
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = '#1D2022')
canvas.pack()

#Pola wyznaczone dla tekstu
pierwszy_frame = tk.Frame(root, bg='#121212')
pierwszy_frame.place(relx=0.51, rely=0.1, relheight=0.685, relwidth=0.48)

drugi_frame = tk.Frame(root, bg='#121212')
drugi_frame.place(relx=0.01, rely=0.79, relheight=0.2, relwidth=0.50)

trzeci_frame = tk.Frame(root, bg='#121212')
trzeci_frame.place(relx=0.51, rely=0.79, relheight=0.2, relwidth=0.48)

#IMAGE DISPLAY CANVAS
canvas2 = Canvas(root, width=400, height=400, bg='#1D2022', bd=0, highlightthickness=0, relief='ridge')
canvas2.pack()
canvas2.place(relx=0.01, rely=0.1, relheight=0.6, relwidth=0.5)

#Lista planet układu słonecznego
options_list_planets = [
    "Merkury",
    "Wenus",
    "Ziemia",
    "Mars",
    "Jowisz",
    "Saturn",
    "Uran",
    "Neptun"]

#Opcja wyboru
#Rozwijany panel z planetami
clicked = StringVar()
clicked.set(options_list_planets[0])
drop = OptionMenu(root, clicked, *options_list_planets)
drop.place(relx=0.3, rely=0.01, relheight=0.05, relwidth=0.1)


#Przycisk potwierdzenia wyboru z panelu z planetami
button = tk.Button(canvas, text = "Potwierdź")
button.bind('<Button-1>', show)
button.place(relx=0.4, rely=0.01, relheight=0.05, relwidth=0.1)

#Panel domyślny
text_welcome_label1 = "Witaj w kosmicznym katalogu, \n wybierz obiekt z listy po lewej aby otrzymać informacje"
welcome_label1 = tk.Label(pierwszy_frame, text = text_welcome_label1, bg='#121212', fg='white')
welcome_label1.pack()

text_welcome_label2 = "Kosmiczny katalog v1.0 \n aplikacja wciąż jest w trakcie rozwijania, za niedługo pojawią się nowe funkcje"
welcome_label2 = tk.Label(drugi_frame, text = text_welcome_label2, bg='#121212', fg='white')
welcome_label2.pack()


root.mainloop()

