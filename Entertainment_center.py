#importanting appropriate modules to create program 
import media
import Fresh_tomatoes
#Ceating the instance of class "Movie" Named "Toy Story"
toy_story = media.Movie(
    "Toystory",
    "a story of a boy and his toys that come to life",
    "http://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#Ceating the instance of class "Movie" Named "Avatar"
avatar = media.Movie(
    "Avatar",
    "Blue smurfs try not to get blown up",
    "http://vignette3.wikia.nocookie.net/jamescameronsavatar/images/5/5b/3D_Blu-ray_Cover.jpg/revision/latest?cb=20120815202134",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#Ceating the instance of class "Movie" Named "The Prince Of Egypt"
the_prince_of_egypt = media.Movie(
    "The prince of Egypt",
    "Best Movie OF ALL TIME. Das all u need ta know",
    "http://www.gstatic.com/tv/thumb/movieposters/22187/p22187_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=EPzCyBS7mK0")
#Ceating the instance of class "Movie" Named "Star Wars" The Force Awakens"
star_wars_the_force_awakens = media.Movie(
    "Star Wars: The force awakens",
    "lightsabers n stuff",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",
    "https://www.youtube.com/watch?v=sGbxmsDFVnE")
#Ceating the instance of class "Movie" Named "Thor Ragnarok"
thor_ragnarok = media.Movie(
    "Thor Ragnarok",
    "Thor swings his mighty hammer",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcT0wr9U-qhQNc66YqS2KYUYkQROyxgoScYt5kDntcD9C026Vjci",
    "https://www.youtube.com/watch?v=v7MGUNV8MxU")
#Ceating the instance of class "Movie" Named "Justice League"
justice_league = media.Movie(
    "Justice league",
    "Off brand avengers",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcT0F8zz5Cs1fy5kYQhOkwFHc3aiBOtI2pe63myDp3oy5NUoFtsm",
    "https://www.youtube.com/watch?v=3cxixDgHUYw")
#Create a variable that holes all the instances of class Movie that i want to pass to function open_movies_page in module Fresh_tomatoes
movies = [
    avatar,
    toy_story,
    star_wars_the_force_awakens,
    thor_ragnarok,
    justice_league,
    the_prince_of_egypt]
#Pass the Variable Movies into function open_movies_page 
Fresh_tomatoes.open_movies_page(movies)

