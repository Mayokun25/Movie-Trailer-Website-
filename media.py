#importing webbrowser module so i can open links to the web for pictures and videos 
import webbrowser
#Creating class Movie
class Movie():
#constructor __init__ to pass to define what the instance variables are 
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image 
        self.trailer_youtube_url = trailer_youtube
#defining instance method for show_trailer 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)




        
