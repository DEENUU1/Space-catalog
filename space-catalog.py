from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
import requests
import json
from urllib.request import urlopen
from pprint import pformat
import pandas as pd
from tkcalendar import DateEntry
from bs4 import BeautifulSoup


#PLANET DESCRIPTION
FULL_EARTH_DESC = "Jest to druga co do wielkości planeta układu słonecznego. Ziemia, 3  licząc od \nSłońca, oraz 5 pod " \
                  "względem wielkości \nplaneta Układu Słonecznego. Pod względem średnicy, masy \noraz gęstości jest " \
                  "to największa planeta skalista \nUkładu Słonecznego. Ziemia jest zamieszkana przez miliony " \
                  "\ngatunków, w tym człowieka. \nCiało Centralne: Słońce \nŚrednia prędkość ruchu: 29,78km/s \nTyp " \
                  "planety: Planeta skalista \nMasa: 5,97x10^24 kg \nPromień: 6371km \nOkres obrotu: 23," \
                  "93 H \nPrzyśpieszenie grawitacyjne: 9,80 m/s^2 \nWiek: 4,54 mld lat \nSatelita naturalny: 1 – " \
                  "Księżyc \nSkład Atmosfery: Azot 78%, Tlen 20%, Argon 0.93%, \nDwutlenek węgla 0,04%, Neon, Hel, " \
                  "Metan, Krypton "

EARTH_FACT = "Ziemia jest chyba najciekawszym obiektem w kosmosie \njaki poznaliśmy. To właśnie tutaj powstało zgodnie " \
             "z naszym obecnym \nstanem wiedzy jedyne życie we wszechświecie. "


FULL_JUPITER_DESC = "Jest to piąta w kolejności od Słońca i największa planeta Układu Słoneczegog.\n Masa Jowisza jest " \
                    "nieco mniejsza niż jedna tysięczna masy Słońca.\n Wraz z Saturnem, Uranem i Neptunem tworzą grupę " \
                    "gazowych olbrzymów.\nSkłada się ona w 3/4 z wodoru i 1/4 helu.\nCiało centralne: Słońce " \
                    "\nOkres orbitalny: 11,866d\nTyp planety: gazowy olbrzym\nPromień: 69 911 km " \
                    "\nOkres obrotu: 9,9250 h\nPrzyśpieszenie grawitacyjne: 24,79 m/s^2\nPrędkość ucieczki: 59,5km/s " \
                    "\nSkład atmosfery: wodór: 89,8%, hel: 10,2%, metan: ~0,3%\nPozostałe: amoniak, etan, para wodna"

JUPITER_FACT = "Misje kosmiczne przeprowadzane na Jowiszu:\n1. Program Pioneer: Pioneer 10, Pioneer 11\n2. Program " \
               "Voyager: Voyager 1, Voyager 2\n3. Galileo \n4. Program New Frontiers: New Horizons, Juno "

FULL_NEPTUNE_DESC = "Gazowy olbrzym, najdalsza od Słońca planeta w Układzie Słonecznym, czwarta \npod względem średnicy " \
                    "i trzecia pod względem masy. Neptun jest ponad\n 17 razy masywniejszy od Ziemi i trochę masywniejszy " \
                    "od Urana. Odkryty \nzostał w 1846 jednak jest jedyną planeta układu słonecznego \nktóra została odkryta " \
                    "Za pośrednictwem matematycznych \nobliczeń, a nie na drodze obserwacji nieba. " \
                    "\nCiało centralne: Słońce\nOkres orbitalny: 164,79 lat\nPrędkość ruchu: 5,43 km/s " \
                    "\nTyp planety: gazowy olbrzym\nMasa 1,02413x10^26 kg\nPromień: 24 622 km\n Przyśpieszenie grawitacyjne: 11,15 m/s^2 "\
                    "\nSatelity naturalne: 14\nSkład atmosfery: Wodór: 80%, Hel: 19%, Metan: 1.5%, Pozostałe: HD, etan"
NEPTUNE_FACT = "Misje kosmiczne przeprowadzone na Neptunie:\n1. Program Voyager: Voyager 2"

FULL_MARS_DESC = "Mars to czwarta od Słońca planeta Układu Słonecznego. Krąży \nmiędzy orbitą Ziemi a pasem planetoid" \
                 "dzielącym go od orbity Jowisza. Planeta \nzostała nazwana od imienai rzymskiego boga wojny - Marsa" \
                 "\nCiało centralne: Słońce\nTyp planety: planeta skalista\nMasa: 6.4171x10^23kg\nPromień: 3389.5km" \
                 "\nOkres obrotu: 868.22km/h\nPrzyśpieszenie grawitacyjne: 3.71m/s^2\nSatelity naturalne: 2" \
                 "\nSkład atmosfery: Dwutlenek węgla: 95.32%, Azot: 2.7%, Argon: 1.6%, Tlen: 0.13," \
                 "\nTlenek węgla: 0.07%, Pozostałe: para wodna, tlenek azotu, \nneon, HDO, krypton, ksenon"


MARS_FACT = "Misje kosmiczne przeprowadzane na Marsie:\n1. Program Mariner: Mariner 4, Mariner 6 i 7, Mariner 8, " \
            "Mariner 9\n2. Program Viking: Viking 1, Viking 2\n3. Mars Exploration Rover: Opportunity, Spirit\n4. " \
            "Mars Science Laboratory: Curiosity Rover\n5. Mars Pathfinder: Sojourner, Lądownik Mars " \
            "Pathfinder\n6.Mars Observatory (nieudana)\n7. Mars Climate Orbiter (nieudana)\n8. Mars Polar Lander (" \
            "nieudana)\n9. Mars Global Surveyor\n10. 2001 Mars Odyssey\n11. Mars Reconnaissance Orbiter\n12. " \
            "InSight\n13. Mars Scout Program: Mars Scount 3, Phoenix, Mars Atmospehere and Valatile Evolution\n14. " \
            "Mars 2020: Łazik Preseverance, Dragon Ingenuity\n15. Mars Sample Return Mission "

FULL_SATURN_DESC = 'Jest to druga co do wielkości planeta układu słoneczego. \n Masa Satruna jest około 95 razy ' \
                   'większa niż masa Ziemi. \n Ze względu na gazową strukturę, jego gęstość nie przekracza gęstości ' \
                   'wody. \n Doba na tej planecie trwa bardzo krótko bo zaledwie 10.23 godziny ' \
                   '\nCiało centralne: Słońce\nTyp planety: gazowy olbrzym\nMasa: 5.6834x10^26kg' \
                   '\nPromień: 58 232km\nOkres obrotu: 10.656h\nPrzyśpieszenie grawitacyjne: 10.44m/s^2' \
                   '\nSatelity naturalne: 82 księżyce' \
                   '\nSkład atmosfery: Wodór: 96.3%, Hel: 3.25%, Metan: 0.45%' \
                   '\nPozostałe: amoniak, HD, etan, \nAerozole atmosferyczne: lód, NH3, lód H20'

SATURN_FACT = "Misje kosmiczne przeprowadzone na Saturnie:\n1. Program Pioneer: Pioneer 11\n2. Program Voyager: " \
              "Voyager 1, Voyager 2\n3. Cassini-Huygens\n4. Drogonfly "

FULL_VENUS_DESC = 'Wenus to druga pod względem odległości od Słońca planeta\n Układu Słonecznego. Jest 3 pod względem ' \
                  'jasności ciałem niebieskim\n widocznym na niebue, po Słońcu i Księżycu. Nazwa planety wzięła\n się od ' \
                  'rzymskiej bogini miłości, Wenus.' \
                  'Ciało centralne: Słońce\nObwód orbity: 6.80x10^11m\nOkres orbitalny: 224,701 dni ziemskich' \
                  '\nTyp planety: planeta skalista\nMasa: 4,867x10^24 kg\nPromień równikowy: 6051,8' \
                  '\nPrzyśpieszenie grawitacyjne: 8,87 m/s^2\nPrędkość ucieczki: 10,36km/s' \
                  '\nSkład atmosfery: Dwutlenek węgla: 96.5%, Azot: 3.5%, Pozostałe:\ndwutlenek siarki, argon,para wodna' \
                  'tlenek węgla, hel, neon'

VENUS_FACT = "Misje kosmiczne przeprowadzane na Wenus:\n1. Program Mariner: Mariner 1, Mariner 2, Mariner 5, " \
             "Mariner 10\n2. Program Pioneer: Pioneer 12, Pioneer 13\n 3. Magellan "

FULL_URANUS_DESC = 'Uran to kolejna z planet należąca do Układu Słonecznego. \n Jej okres obiegu wokół Słońca wynosi ' \
                   '84 lata, a czas obrotu trwa jedynie 17 godzin. \n Jej masa jest 14.5 razy wieksza od masy kuli ' \
                   'ziemskiej. '

URANUS_FACT = "Misje kosmiczne przeprowadzone na Uranie:\nProgram Voyager: Voyager 2"

FULL_MERCURY_DESC = 'Najmniejsza i najbliższa Słońca planeta układu Słonecznego. Ukształtowanie \npowierzchni Merkurego ' \
                    'przypomina Księżyc, są na nim liczne kratery uderzeniowe \ni pozbawiony jest on Atmosfery. ' \
                    'Temperatura powierzchni waha się od -173 do 427\n(stopni Celsjusza). Merkury posiada duże żelazne ' \
                    'jądro, generujące pole \nmagnetyczne stukrotnie słabsze od Ziemskiego. Pierwsze udokumentowane ' \
                    '\nobserwacje Merkurego sięgają pierwszego tysiąclecia p.n.e. \nCiało Centralne: Słońce Średnia ' \
                    '\nprędkość ruchu: 47,36 km/s \nTyp planety: Planeta skalista \nMasa: 3,3011x10^23 kg \nPromień: 2439,' \
                    '7 km \nOkres obrotu: 58 dni 15 godzin 26 minut \nPrzyśpieszenie grawitacyjne: 3,7 m/s^2 \nWiek: 4,' \
                    '54 mld lat \nSatelita naturalny: Brak \nSkład Atmosfery: Tlen: 42,0%, Sód: 29,0%, Wodór: 22,0%, ' \
                    '\nHel: 6,0%, Potas: 0,5%  \nArgon, dwutlenek węgla, woda, azot, ksenon, krypton, neon: 0,5% '

MERCURY_FACT = "Misje kosmiczne przeprowadzane na Mercurym:\n1. Mariner 10\n2. MESSENGER"



#OPENING PANDAS


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


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


#FUNCTION FOR PLANET OPTION MENU
class Opcje:

    def __init__(self, image_name, full_text, fact_text, wiki_url):
        self.image_name = image_name
        self.full_text = full_text
        self.fact_text = fact_text
        self.wiki_url = wiki_url


merkury = Opcje("Merkury.png", FULL_MERCURY_DESC, MERCURY_FACT, "https://pl.wikipedia.org/wiki/Merkury")
wenus = Opcje("Wenus.png", FULL_VENUS_DESC, VENUS_FACT, "https://pl.wikipedia.org/wiki/Wenus")
ziemia = Opcje("Ziemia.png", FULL_EARTH_DESC, EARTH_FACT, "https://pl.wikipedia.org/wiki/Ziemia")
mars = Opcje("Mars.png", FULL_MARS_DESC, MARS_FACT, "https://pl.wikipedia.org/wiki/Mars")
jowisz = Opcje("Jowisz.png", FULL_JUPITER_DESC, JUPITER_FACT, "https://pl.wikipedia.org/wiki/Jowisz")
saturn = Opcje("Saturn.png", FULL_SATURN_DESC, SATURN_FACT, "https://pl.wikipedia.org/wiki/Saturn")
uran = Opcje("Uran.png", FULL_URANUS_DESC, URANUS_FACT, "https://pl.wikipedia.org/wiki/Uran")
neptun = Opcje("Neptun.png", FULL_NEPTUNE_DESC, NEPTUNE_FACT, "https://pl.wikipedia.org/wiki/Neptun")


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

    if type == options_list_planets[0]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(merkury.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=merkury.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=merkury.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(merkury.wiki_url))
        link.pack()

    if type == options_list_planets[1]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(wenus.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=wenus.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=wenus.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(wenus.wiki_url))
        link.pack()

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


    if type == options_list_planets[4]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(jowisz.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=jowisz.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=jowisz.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(jowisz.wiki_url))
        link.pack()

    if type == options_list_planets[5]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(saturn.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=saturn.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=saturn.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(saturn.wiki_url))
        link.pack()


    if type == options_list_planets[6]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(uran.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=uran.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=uran.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(uran.wiki_url))
        link.pack()

    if type == options_list_planets[7]:

        # IMAGE DISPLAY
        my_img = ImageTk.PhotoImage(Image.open(neptun.image_name))
        canvas2.create_image(225, 210, image=my_img)
        canvas2.my_img = my_img

        # TEXT LABEL
        # FULL DESCRIPTION
        text_label = tk.Label(pierwszy_frame, text=neptun.full_text, bg='#121212', fg='white')
        text_label.pack()

        # FACTS
        text2_label = tk.Label(drugi_frame, text=neptun.fact_text, bg='#121212', fg='white')
        text2_label.pack()

        # LINKS
        text3_label = tk.Label(trzeci_frame, text="Przydatne linki:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        # HYPERLINK FUNCTION

        link.bind("<Button-1>", lambda e: callback(neptun.wiki_url))
        link.pack()


def showdate():
    label5.config(text=cal.get_date())
    user_date = label5.cget("text")
    return user_date


def showapp(event):

    for widget in pierwszy_frame.winfo_children():
        widget.destroy()
    for widget in drugi_frame.winfo_children():
        widget.destroy()
    for widget in trzeci_frame.winfo_children():
        widget.destroy()

    type = clicked2.get()

    if type == options_list_apps[0]:

        link = tk.Label(trzeci_frame, text="Zdjęcie w pełnej jakości", font=('Helveticabold', 10), bg='#121212',
                        fg='green',
                        cursor="hand2")

        link_2 = tk.Label(trzeci_frame, text="Nasa zdjęcie dnia", font=('Helveticabold', 10), bg='#121212', fg='green',
                          cursor="hand2")

        api_key = 'YOUR_API_KEY'
        URL_APOD = 'https://api.nasa.gov/planetary/apod'

        date = showdate()
        params = {
            'api_key': api_key,
            'date': date,
            'hd': 'True'
        }

        response_image = requests.get(URL_APOD, params=params)

        json_data = json.loads(response_image.text)
        image_url = json_data['hdurl']
        image_descrip = json_data['explanation']
        image_title = json_data['title']

        image_descrip_2 = pformat(image_descrip)
        chars_to_remove = ["(", ")", "'"]
        for char in chars_to_remove:
            image_descrip_2 = image_descrip_2.replace(char, "")

        imageUrl = image_url
        with urlopen(imageUrl) as fd:
            image = Image.open(fd).resize((500, 500))

        my_img = ImageTk.PhotoImage(image)
        canvas2.create_image(225, 210, image=my_img)
        canvas2.nasa_img = my_img

        text_label = tk.Label(pierwszy_frame, text=image_title + "\n\n" + image_descrip_2, bg='#121212', fg='white')
        text_label.pack()

        link.bind("<Button-1>", lambda e: callback(image_url))
        link.pack()
        print(image_url)
        link_2.bind("<Button-1>", lambda e: callback("https://apod.nasa.gov/apod/astropix.html"))
        link_2.pack()

        response = requests.get(image_url)
        if response.status_code:
            fp = open('nasaapodimage.png', 'wb')
            fp.write(response.content)
            fp.close()

    if type == options_list_apps[1]:

        url = "https://astrofaza.pl/nowy-termin-startu-misji-artemis-1/"
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'html.parser')

        tytul = soup.find('h1', class_="entry__heading")
        naglowek = soup.find_all('div', class_="entry__content")
        name = soup.find_all('div', class_="entry__content")

        for t in tytul:
            print(t.get_text(strip=True))
        for x in naglowek:
            xtext = x.find_all("h4")
            for xs in xtext:
                print(xs.get_text(strip=True))
        for div in name:
            innerDivs = div.find_all("p")
            for idiv in innerDivs:
                print(idiv.get_text(strip=True))

        full_text = xs.get_text(strip=True) + idiv.get_text(strip=True)
        print(full_text)

        links = requests.get("https://astrofaza.pl/aktualnosci/")
        soup2 = BeautifulSoup(links.text, 'html.parser')

        link = soup2.find_all('div', class_='news-list__grid')
        for links in link:
            xlinks = links.find_all("a")
            for xd in xlinks:
                # print(xd.get("href"))
                listlinks = []
                listlinks.append(xd.get("href"))
                print(listlinks)

        hyperlinks = tk.Label(trzeci_frame, text="Wikipedia", font=('Helveticabold', 10), bg='#121212', fg='green',
                              cursor="hand2")

        my_img2 = ImageTk.PhotoImage(Image.open("astrofaza.jpg"))
        canvas2.create_image(225, 210, image=my_img2)
        canvas2.my_img = my_img2

        text_label = tk.Label(pierwszy_frame, text=full_text, bg='#121212', fg='white')
        text_label.pack()

        text2_label = tk.Label(drugi_frame, text=t.get_text(strip=True), bg='#121212', fg='white')
        text2_label.pack()

        text3_label = tk.Label(trzeci_frame, text="Najnowsze artykuły:", font=('Arial', 15), bg='#121212', fg='white')
        text3_label.pack()

        hyperlinks.bind("<Button-1>", lambda e: callback(listlinks))
        hyperlinks.pack()


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

options_list_apps = ["Nasa photo of a day", "Astrofaza"]

#CALENDAR
cal = DateEntry(root, width=16, background='magenta3', foreground='white', bd=2)
cal.place(relx=0.5, rely=0.01, relheight=0.05, relwidth=0.1)

label5 = Label(canvas, text="")
label5.place(relx=0.5, rely=0.01, relheight=0.05, relwidth=0.1)


button3 = Button(canvas, text="Wybierz datę", command=showdate)
button3.place(relx=0.6, rely=0.01, relheight=0.05, relwidth=0.1)



#Opcja wyboru
#Rozwijany panel z planetami
clicked = StringVar()
clicked.set(options_list_planets[0])
drop = OptionMenu(root, clicked, *options_list_planets)
drop.place(relx=0, rely=0.01, relheight=0.05, relwidth=0.1)

#Rozwijany panel z innymi funkcjami
clicked2 = StringVar()
clicked2.set(options_list_apps[0])
drop2 = OptionMenu(root, clicked2, *options_list_apps)
drop2.place(relx=0.2, rely=0.01, relheight=0.05, relwidth=0.2)

#Przycisk potwierdzenia wyboru z panelu z planetami
button = tk.Button(canvas, text = "Potwierdź")
button.bind('<Button-1>', show)
button.place(relx=0.1, rely=0.01, relheight=0.05, relwidth=0.1)

#Przycisk potwierdzania wyboru z panelu z innymi funkcjami
button2 = tk.Button(canvas, text = "Potwierdź")
button2.bind('<Button-1>', showapp)
button2.place(relx=0.4, rely=0.01, relheight=0.05, relwidth=0.1)

#Panel domyślny
text_welcome_label1 = "Witaj w kosmicznym katalogu, \n wybierz obiekt z listy po lewej aby otrzymać informacje"
welcome_label1 = tk.Label(pierwszy_frame, text = text_welcome_label1, bg='#121212', fg='white')
welcome_label1.pack()

text_welcome_label2 = "Kosmiczny katalog v2.0 \n aplikacja wciąż jest w trakcie rozwijania, za niedługo pojawią się " \
                      "nowe funkcje \nNowe funckje (v2.0): Zmieniony wygląd, nowy opis dla planet, linki do artykułów "
welcome_label2 = tk.Label(drugi_frame, text = text_welcome_label2, bg='#121212', fg='white')
welcome_label2.pack()


root.mainloop()

