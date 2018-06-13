import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar= media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Avatar-Logo-avatar.svg/868px-Avatar-Logo-avatar.svg.png",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pride_and_prejudice = media.Movie("Pride and Prejudice",
"A dangerous flirtation begins between a beautiful young woman and the friend friend of a wealthy bachelor.",
"https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
"https://www.youtube.com/watch?v=1dYv5u6v55Y")

school_of_rock = media.Movie("School of Rock", "Storyline",
"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
"https://www.youtube.com/watch?v=uVeNEbh3A4U")

midnight_in_paris = media.Movie("Midnight in Paris", " Storyline",
"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
"https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story, avatar, pride_and_prejudice, school_of_rock, ratatouille, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
#pride_and_prejudice.show_trailer()
