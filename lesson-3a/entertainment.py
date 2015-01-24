import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()
up = media.Movie("Up",
                 "By tying thousands of balloons to his home, 78-year-old Carl sets out to fulfill his lifelong dream to see the wilds of South America. Russell, a wilderness explorer 70 years younger, inadvertently becomes a stowaway",
                 "http://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "http://www.youtube.com/watch?v=pkqzFUhGPJg")
#print(three_idiots.storyline)
#three_idiots.show_trailer()
dark_knight = media.Movie("The Dark Knight",
                              "When Batman, Gordon and Harvey Dent launch an assault on the mob, they let the clown out of the box, the Joker, bent on turning Gotham on itself and bringing any heroes down to his level",
                              "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "http://www.youtube.com/watch?v=GROmJWb-3wU")
thor = media.Movie("Thor",
                   " The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders",
                   "http://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")
hunger_games = media.Movie("The Hunger Games",
                           " Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, up, dark_knight, thor, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
