import functionsfp


def find_outliers(original_dataset, comparison):
    """
    A function to find data in the original dataset that is not represented in the comparison dataset.
    Args: A .txt file representing the first dataset with genres separated by commas, and a comparison
    dataset that is a .txt file with genres separated by commas.
    Output: A dictionary variable of remaining genres
    """
    original_dict = genre_dictionary(original_dataset)
    comparison_dict = genre_dictionary(comparison)
    result = {}
    len_original_dict = 0
    len_comparison_dict = 0
    for genre in original_dict:
        len_original_dict = len_original_dict + original_dict[genre]
    for genre in comparison_dict:
        len_comparison_dict = len_comparison_dict + comparison_dict[genre]

    for genre in original_dict:
        if genre in comparison_dict:
            result[genre] = (original_dict[genre]) / len_original_dict - (
                comparison_dict[genre] / len_comparison_dict
            )
            if result[genre] < 0:
                del result[genre]
        else:
            result[genre] = original_dict[genre] / len_original_dict
    return result


import matplotlib.pyplot as plt

girls_outliers = find_outliers("girls_genres.txt", "boy_genres.txt")
girls_outliers_top = {}

for genre in girls_outliers:
    if girls_outliers[genre] > 0.008:
        girls_outliers_top[genre] = girls_outliers[genre]

print(girls_outliers_top)

boys_outliers = find_outliers("boy_genres.txt", "girls_genres.txt")
boys_outliers_top = {}
for genre in boys_outliers:
    if boys_outliers[genre] > 0.008:
        boys_outliers_top[genre] = boys_outliers[genre]

print(boys_outliers_top)

girl_bargraph_x = list(girls_outliers_top.keys())
girl_bargraph_y = []
for key in girls_outliers_top:
    girl_bargraph_y.append(girls_outliers[key] * 100)

# creating the bar plot
plt.bar(girl_bargraph_x, girl_bargraph_y, color="maroon", width=0.8)

plt.xticks(rotation=80)

plt.xlabel("Game Genre")
plt.ylabel("Genre Instances Across Games in Percent")
plt.title("Girl Game Genres with /n Significant Deviation from the Boy Genres")
plt.show()

# boy_bargraph_x = list(boys_outliers_top.keys())
# boy_bargraph_y = []
# for key in boys_outliers_top:
#     boy_bargraph_y.append(boys_outliers[key]*100)

# # creating the bar plot
# plt.bar(boy_bargraph_x, boy_bargraph_y, color ='maroon',
#     width = 0.8)

# plt.xticks(rotation=80)


import random

f = open("all_game_titles.txt", "r")
game_titles = f.read()
f.close
print(game_titles)

game_titles = game_titles.split()

print(game_titles)

random_titles = []
for _ in range(100):
    random_titles.append(random.choice(game_titles))

random_titles = " ".join(random_titles)

print(random_titles)

g = open("random_game_titles.txt", "w")
g.write(random_titles)
g.close()

f = open("boy_game_file.txt", "r")
game_titles = f.read()
f.close
print(game_titles)

game_titles = game_titles.split()

print(game_titles)

random_titles = []
for _ in range(100):
    random_titles.append(random.choice(game_titles))

random_titles = " ".join(random_titles)

print(random_titles)

g = open("boy_random_game_titles.txt", "w")
g.write(random_titles)
g.close()


def genre_dictionary(genre_list):
    """
    A function to turn a list of game genres into a dictionary where the keys are the genre
    as a string and the values are the number of instances of those genres.
    Args: A list of genres separated by spaces in a .txt file
    Output: A dictionary variable
    """
    f = open(genre_list, "r")
    genre_list_string = f.read()
    f.close()
    genre_list_list = genre_list_string.split(",")
    label_dict = {}
    for label in genre_list_list:
        if label in label_dict:
            label_dict[label] = label_dict[label] + 1
        else:
            label_dict[label] = 1

    return label_dict


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
            all_game_genres.append(genre_url[35 : len(all_games)])

    all_game_genres = ",".join(all_game_genres)

    # WRITES THE GAME GENRES TO A .TXT FILE
    g = open("all_game_genres.txt", "w")
    g.write(all_game_genres)
    g.close()

    return "all_game_genres.txt"


get_game_genres("boy_game_urls.txt")
