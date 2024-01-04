#File created for loading Movie class into the result_window.py window. Contains the 'big' and 'small' forms
#'big' form is for when the movie details are shown on the screen
#'small' form is for when the movie is saved as a "tile" on the saved positions tab 
import requests
from tkinter import *
from src.Movie import Movie
from PIL import Image
from io import BytesIO
class MovieTile(Frame):
    # Download the poster data using requests, and load it into the variable
    def download_image(master:Frame, url:str):
        if not url: return Image.new(mode='RGB', size=(666,666), color='grey')
        response = requests.get(url)
        if not response.status_code==200: return requests.ConnectionError()
        image = Image.open(BytesIO(response.content))
        
        return image
    
    def remove_self_from_queue(self):
        self.result_window.remove_from_saved(tile=self)
    
    def display_self_in_result(self):
        self.result_window.current = self
        self.result_window.load_tile(self)
        self.result_window.refresh_window()
        
    def __init__(self, master:Frame, data:Movie, result_window=None, is_template=False):
        super().__init__(master=master)

        self.result_window = result_window
        if is_template:
            data.genres="Undefined"
        
        is_adult:str = "yes" if data.adult else "no"
        self.display_info = f"Title: {data.title}\nGenres: {data.genres}\nYear: {data.release_year}\nScore: {data.vote_average}\nVote Count: {data.vote_count}\n18+: {is_adult}\n"
        
        #'big' part
        self.text:Label = Label(master=master,
                                text= self.display_info,
                                font=("Times New Roman", 30))
        
        self.image:Image = self.download_image(data.poster_path)
        self.saved:bool = False
        
        #'small' part
        #Height of both buttons
        height = 5
        # A title (button for loading it onto the main screen)
        #Label for the tile
        self.title = Button(master=self, text=data.title, height=height, bg='grey', command=self.display_self_in_result)
        self.title.pack(side=LEFT, fill=BOTH, expand=True)
        
        # A remove button (button for removing it from the queue)
        self.remove = Button(master=self, text="Remove", height=height, bg='red', fg='white', command=self.remove_self_from_queue,)
        self.remove.pack(side=RIGHT, fill=BOTH)
