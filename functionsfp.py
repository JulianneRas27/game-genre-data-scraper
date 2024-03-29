def get_game_category_links(url):
    """
    A function to get all game categories from a page of girlsgogames.com.

        Args: A string url to the all catgories link on girlsgogames.com.

        Output: A list of urls leading to each game category.
    """
    import requests
    from bs4 import BeautifulSoup

    # CREATES A LIST OF ALL LINKS PRESENT
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")

    urls = []
    for link in soup.find_all("a"):
        urls.append(link.get("href"))

    # REMOVES UNNECESSARY LINKS
    del urls[0:204]
    del urls[len(urls) - 11 : len(urls)]

    urls.remove("https://www.girlsgogames.com/games/action")
    urls.remove("https://www.girlsgogames.com/games/adventure")
    urls.remove("https://www.girlsgogames.com/games/animals")
    urls.remove("https://www.girlsgogames.com/games/art-and-creativity")
    urls.remove("https://www.girlsgogames.com/games/beauty-games")
    urls.remove("https://www.girlsgogames.com/games/cooking")
    urls.remove("https://www.girlsgogames.com/games/decoration-games")
    urls.remove("https://www.girlsgogames.com/games/dress_up")
    urls.remove("https://www.girlsgogames.com/games/love-games")
    urls.remove("https://www.girlsgogames.com/games/puzzle")
    urls.remove("https://www.girlsgogames.com/games/simulation")
    urls.remove("https://www.girlsgogames.com/games/skill")
    urls.remove("https://www.girlsgogames.com/games/specials")
    urls.remove("https://www.girlsgogames.com/games/sports")

    return urls


def get_game_links(game_categories):
    """
    A function to get all game urls given a list of category links.

        Args: A list of urls to different game category webpages.

        Output: A string representing the .txt file of the game urls separated by commas.
    """
    import requests
    from bs4 import BeautifulSoup

    each_list_of_games = []
    # LOOPS THROUGH EACH CATEGORY
    for category in game_categories:
        # CREATES A LIST OF ALL LINKS PRESENT
        reqs_g = requests.get(category)
        soup_g = BeautifulSoup(reqs_g.text, "html.parser")

        urls_g = []
        for link_g in soup_g.find_all("a"):
            urls_g.append(link_g.get("href"))

        # REMOVES UNNECESSARY LINKS
        del urls_g[0:206]
        category_name = category[35:]
        link_g = f"https://www.girlsgogames.com/games/{category_name}"
        if link_g in urls_g:
            index_of_second = urls_g.index(
                f"https://www.girlsgogames.com/games/{category_name}"
            )
            to_use = len(urls_g) - index_of_second
            del urls_g[len(urls_g) - to_use : len(urls_g)]
            for game in urls_g:
                each_list_of_games.append(game)
        else:
            continue

    # WRITES THE GAME URLS TO A .TXT FILE
    each_list_of_games = ",".join(each_list_of_games)
    f = open("all_games.txt", "w")
    f.write(each_list_of_games)
    f.close()

    return "all_games.txt"


def get_game_titles(all_game_urls):
    """
    A function to get all game titles given the url to each game from girlsgogames.com.

        Args: A string representing a .txt file of the url to each game separated by commas.

        Output: A string representing a .txt file of all game titles separated by spaces.
    """
    # CREATES A LIST OF ALL THE GAME URLS
    f = open(all_game_urls, "r")
    all_games = f.read()
    f.close()
    all_games = all_games.split(",")

    all_game_titles = []
    cropped_games = []

    for game in all_games:
        if game in cropped_games:
            continue
        else:
            cropped_games.append(game)

    # REFINES EACH URL AND FORMATS THE RESULTING GAME TITLE STRING
    for game in cropped_games:
        all_game_titles.append(game[34 : len(all_games)].replace("-", " "))

    all_game_titles = " ".join(all_game_titles)

    # WRITES THE GAME TITLES TO A .TXT FILE
    g = open("all_game_titles.txt", "w")
    g.write(all_game_titles)
    g.close()

    return "all_game_titles.txt"


def get_game_genres(all_game_urls):
    """
    A function to get all game genres given the url to each game from girlsgogames.com.

        Args: A string representing a .txt file of the url to each game separated by commas.

        Output: A string representing a .txt file of all game genres separated by spaces.
    """
    import requests
    from bs4 import BeautifulSoup

    # CREATES A LIST OF ALL THE GAME URLS
    f = open(all_game_urls, "r")
    all_games = f.read()
    f.close()
    all_games = all_games.split(",")

    each_list_of_genre_urls = []
    for game in all_games:
        # CREATES A LIST OF ALL LINKS PRESENT IN THE CURRENT GAME LINK
        reqs_l = requests.get(game)
        soup_l = BeautifulSoup(reqs_l.text, "html.parser")

        urls_l = []
        for link_l in soup_l.find_all("a"):
            urls_l.append(link_l.get("href"))

        # REMOVES UNNECESSARY LINKS
        pre_link = "https://www.girlsgogames.com/"
        if pre_link in urls_l:
            urls_l.remove("https://www.girlsgogames.com/")
        else:
            continue
        link_l = "https://www.girlsgogames.com/"
        link_l_two = "https://www.girlsgogames.com/disclaimer"
        if link_l in urls_l and link_l_two in urls_l:
            key_index = urls_l.index("https://www.girlsgogames.com/")
            del urls_l[0 : key_index + 2]
            key_index_two = urls_l.index(
                "https://www.girlsgogames.com/disclaimer"
            )
            diff = len(urls_l) - key_index_two
            del urls_l[len(urls_l) - diff : len(urls_l)]
            each_list_of_genre_urls.append(urls_l)
        else:
            continue

    # REFINES EACH URL AND FORMATS THE RESULTING GAME GENRE STRING
    all_game_genres = []
    for list_l in each_list_of_genre_urls:
        for genre_url in list_l:
            all_game_genres.append(
                genre_url[35 : len(all_games)].replace("-", " ")
            )

    all_game_genres = " ".join(all_game_genres)

    # WRITES THE GAME GENRES TO A .TXT FILE
    g = open("all_game_genres.txt", "w")
    g.write(all_game_genres)
    g.close()

    return "all_game_genres.txt"


def other_pages(page_num):
    """
    A function to get all game urls of the boy game genre given the desired page number.

        Args: A int of the desired page number.

        Output: A list of all the game urls on that boy genre page.
    """
    import requests
    from bs4 import BeautifulSoup

    genre = "https://www.girlsgogames.com/games/boy-games?page=" + str(page_num)
    reqs_b = requests.get(genre)
    soup_b = BeautifulSoup(reqs_b.text, "html.parser")
    each_list_of_boy_games = []
    urls_b = []
    for link_b in soup_b.find_all("a"):
        game_link = link_b.get("href")
        urls_b.append(game_link)

    # REMOVE UNNECESSARY LINKS
    del urls_b[0:206]

    index_of_second = urls_b.index(
        f"https://www.girlsgogames.com/games/boy-games"
    )
    to_use = len(urls_b) - index_of_second - 1
    del urls_b[len(urls_b) - to_use : len(urls_b)]
    for game in urls_b:
        each_list_of_boy_games.append(game)
    return each_list_of_boy_games


def get_boy_game_links(
    url_to_use="https://www.girlsgogames.com/games/boy-games",
):
    """
    A function to get all of the game urls from the boy-game genre in girlsgogames.com.

        Args: A string of the url to the boy genre page.

        Output: A string representing a .txt file of all the boy game urls separated by commas.
    """
    import requests
    from bs4 import BeautifulSoup

    genre = url_to_use
    reqs_g = requests.get(genre)
    soup_g = BeautifulSoup(reqs_g.text, "html.parser")
    each_list_of_games = []
    urls_g = []
    for link_g in soup_g.find_all("a"):
        game_link = link_g.get("href")
        urls_g.append(game_link)

    # REMOVE UNNECESSARY LINKS
    del urls_g[0:206]

    index_of_second = urls_g.index(
        f"https://www.girlsgogames.com/games/boy-games"
    )
    to_use = len(urls_g) - index_of_second - 1
    del urls_g[len(urls_g) - to_use : len(urls_g)]
    for game in urls_g:
        each_list_of_games.append(game)

    for i in range(1, 9):
        page_game = other_pages(i)
        for game in page_game:
            each_list_of_games.append(game)

    boy_games = each_list_of_games
    g = open("boy_game_links.txt", "w")
    g.write(",".join(boy_games))
    g.close()
    return "boy_game_links.txt"


def genre_dictionary(genre_list):
    """
    A function to turn a list of game genres into a dictionary where the keys are the genre
    as a string and the values are the number of instances of those genres.

    Args: A list of genres separated by spaces in a .txt file.

    Output: A dictionary variable containing strings and integers.
    """
    # READ THE TEXT FILE DATA
    f = open(genre_list, "r")
    genre_list_string = f.read()
    f.close()

    genre_list_list = genre_list_string.split()
    label_dict = {}
    # COUNT GENRES
    for label in genre_list_list:
        if label in label_dict:
            label_dict[label] = label_dict[label] + 1
        else:
            label_dict[label] = 1

    return label_dict
