import functionsfp


def test_get_game_category_links():
    """
    Check that the number of category urls matches the number of
    categories manually counted from the site page.
    """
    category = get_game_category_links(
        "https://www.girlsgogames.com/allcategories"
    )
    assert len(category) == 264


def test_get_game_links():
    """
    Check that the string of game urls consists of no spaces.
    """
    games = get_game_links(
        [
            "https://www.girlsgogames.com/games/io-games",
            "https://www.girlsgogames.com/games/2-player",
            "https://www.girlsgogames.com/games/3d-games",
        ]
    )
    assert " " not in games


def test_get_game_links_two():
    """
    Check that the string of game urls consists of commas.
    """
    games_one = get_game_links(
        [
            "https://www.girlsgogames.com/games/io-games",
            "https://www.girlsgogames.com/games/2-player",
            "https://www.girlsgogames.com/games/3d-games",
        ]
    )
    f = open(games_one, "r")
    games = f.read()
    assert games.count(",") > 1


def test_get_game_titles():
    """
    Check that the string of game title urls consists of many spaces.
    """
    games_one = get_game_titles("all_games.txt")
    f = open(games_one, "r")
    games = f.read()
    assert games.count(" ") > 10


def test_get_game_titles_two():
    """
    Check that the string of game title urls consists of no commas.
    """
    games = get_game_titles("all_games.txt")
    assert "," not in games


def test_other_pages():
    """
    Check that the resulting number of game urls matches the amount
    of boys games manually checked on the last page of the boy
    genre section, where the number of games vary from the
    previous pages.
    """
    games = other_pages(2)
    assert len(games) == 37


def test_get_boy_game_links():
    """
    Check that the string of boy game urls consists of many commas.
    """
    games_one = get_boy_game_links()
    f = open(games_one, "r")
    games = f.read()
    assert games.count(",") > 10


def test_get_boy_game_links_two():
    """
    Check that the string of boy game urls consists of no spaces.
    """
    games = get_game_titles("all_games.txt")
    assert " " not in games


def test_genre_dictionary():
    """
    Check that the genre dictionary consists of only positive integers.
    """
    genre_count = genre_dictionary("all_game_genres.txt")
    for _, v in genre_count.items():
        assert v > -1


# TESTING
test_get_game_category_links()
test_get_game_links()
test_get_game_links_two()
test_get_game_titles()
test_get_game_titles_two()
test_other_pages()
test_get_boy_game_links()
test_get_boy_game_links_two()
test_genre_dictionary()
