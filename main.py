import os
import json
import asyncio
import jikanpy

def chooseRandAnime(jikan):
    print("Picking random Anime...")
    try: 
        anime_json = jikan.random(type='anime')
        print("Successfully picked an anime.")
        print(anime_json['data']['title'])
    except Exception as e:
        input(e)
        return

def initJikan():
    try:
        jikan = jikanpy.Jikan()
        print("Successfully initialized JikanPy")
        return jikan
    except NetworkError:
        print("There is a problem with your network.")
        exit(1)

async def mainMenu():
    while True:
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
                    os.system('cls' if os.name == 'nt' else 'clear')

        except ValueError:
            input("Not a valid choice. Try again.")
            os.system('cls' if os.name == 'nt' else 'clear')
        

if __name__ == '__main__':
    asyncio.run(mainMenu())

