import requests
from os import system
from random import *
from bs4 import BeautifulSoup

def chooseAnime(category):
    animes = category.parent.find_all('span', class_='js-title')
    synopsis = category.parent.find_all('p', class_='preline')
    rating = category.parent.find_all('span', class_='js-score')
    date = category.parent.find_all('div', class_='info')

    rand_num = randrange(0, len(animes)-1)

    chosen_anime = animes[rand_num].text.strip()
    chosen_anime_synopsis = synopsis[rand_num].text.strip()
    chosen_anime_rating = rating[rand_num].text.strip()
    chosen_anime_date = date[rand_num].span.text.strip()
    
    print(f'Anime: {chosen_anime}')
    print(f'Rating: {chosen_anime_rating}')
    print(f'Date: {chosen_anime_date}')
    print(f'Synopsis: {chosen_anime_synopsis}')

    input("Please press any key to continue...")

    #TODO: Find a way to clear screen regardless of OS
    system("clear")

def seasonal_anime():
    url = 'https://myanimelist.net/anime/season'

    print("Loading...")
    response = requests.get(url)
    print("Done!\n\n")

    if response.status_code == 200:
        seed()
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.find_all('div', class_='anime-header')
        while True:
            for i in range(len(categories)):
                print(f'{i+1}. {categories[i].text}')

            print('7. Exit')
            print("\n")
            print("What category do you want?")
            try:
                choice = int(input(" > "))
            except:
                print("Enter a number. ")
                continue
            if choice < 0 or choice > len(categories)+1:
                print("Enter a valid choice.")
                continue
            if choice == 7:
                exit(0)
            chooseAnime(categories[choice-1])

    else:
        print("Bobo, wala ka atang internet.")

def main_menu():
    system("clear")
    ascii_art = '''
 /$$$$$$$$                            /$$$$$$$  /$$ /$$ /$$ /$$   /$$            /$$$$$$            /$$                        
|__  $$__/                           | $$__  $$|__/| $$|__/| $$$ | $$           /$$__  $$          |__/                        
   | $$  /$$$$$$   /$$$$$$   /$$$$$$ | $$  \ $$ /$$| $$ /$$| $$$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$ 
   | $$ |____  $$ /$$__  $$ |____  $$| $$$$$$$/| $$| $$| $$| $$ $$ $$ /$$__  $$| $$$$$$$$| $$__  $$| $$| $$_  $$_  $$ /$$__  $$
   | $$  /$$$$$$$| $$  \ $$  /$$$$$$$| $$____/ | $$| $$| $$| $$  $$$$| $$  \ $$| $$__  $$| $$  \ $$| $$| $$ \ $$ \ $$| $$$$$$$$
   | $$ /$$__  $$| $$  | $$ /$$__  $$| $$      | $$| $$| $$| $$\  $$$| $$  | $$| $$  | $$| $$  | $$| $$| $$ | $$ | $$| $$_____/
   | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      | $$| $$| $$| $$ \  $$|  $$$$$$$| $$  | $$| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$
   |__/ \_______/ \____  $$ \_______/|__/      |__/|__/|__/|__/  \__/ \____  $$|__/  |__/|__/  |__/|__/|__/ |__/ |__/ \_______/
                  /$$  \ $$                                           /$$  \ $$                                                
                 |  $$$$$$/                                          |  $$$$$$/                                                
                  \______/                                            \______/                                                 
         '''
    print(ascii_art)
    print("\n")

if __name__ == '__main__':
    main_menu()
    seasonal_anime()
