import os
import jikanpy
from sys import exit

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def chooseRandAnime(jikan):
    print("Picking random Anime...")
    try: 
        anime_json = jikan.random(type='anime')
        print("Successfully picked an anime.\n")
        print(f"Title: {anime_json['data']['title']}")
        print(f"Status: {anime_json['data']['status']}")
        print(f"Episodes: {anime_json['data']['episodes']}")
        print(f"Rating: {anime_json['data']['score']}")
        print(f"Synopsis: {anime_json['data']['synopsis']}\n")
        input("Press any key to continue...")
    except Exception as e:
        input(e)
        return

def initJikan():
    try:
        jikan = jikanpy.Jikan()
        print("Successfully initialized JikanPy")
        return jikan
    except Exception as e:
        input(e)
        exit(1)

def mainMenu():
    while True:
        clearScreen()
        print(" TAGA PILI NG ANIME ")
        print("1. Give Random Anime.")
        print("2. Exit.")
        try: 
            choice = int(input("> "))
            match choice:
                case 1:
                    jikan = initJikan();
                    chooseRandAnime(jikan)
                case 2:
                    print("Exiting...")
                    exit(0)
                case _:
                    input("Not in the choices.")
                    clearScreen()

        except ValueError:
            input("Not a valid choice. Try again.")
            clearScreen() 

if __name__ == '__main__':
    mainMenu()

