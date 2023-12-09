import requests
from os import system
from random import *
from bs4 import BeautifulSoup

def chooseAnime(category):
    animes = category.parent.find_all('span', class_='js-title')
    synopsis = category.parent.find_all('p', class_='preline')
    rating = category.parent.find_all('span', class_='js-score')
    rand_num = randrange(0, len(animes)-1)
    chosen_anime = animes[rand_num].text.strip()
    chosen_anime_synopsis = synopsis[rand_num].text.strip()
    chosen_anime_rating = rating[rand_num].text.strip()
    print(f'Anime: {chosen_anime}\nRating: {chosen_anime_rating}\nSynopsis: {chosen_anime_synopsis}')
    input("Please press any key to continue...")
    system("clear")

if __name__ == "__main__":
    system("clear")
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
