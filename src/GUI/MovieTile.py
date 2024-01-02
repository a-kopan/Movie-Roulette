#File created for loading Movie class into the result_window.py window. Contains the 'big' and 'small' forms
#'big' form is for when the movie details are shown on the screen
#'small' form is for when the movie is saved as a "tile" on the saved positions tab 
from tkinter import *
from src.Movie import Movie
import requests
from PIL import Image
from io import BytesIO
#Frame which will show the miniature version of saved position
class MovieTile(Frame):
    # Download the poster data using requests, and load it into the variable
    def download_image(master:Frame, url:str):
        if not url: return Image.new(mode='RGB', size=(666,666), color='white')
        response = requests.get(url)
        if not response.status_code==200: return requests.ConnectionError()
        image = Image.open(BytesIO(response.content))
        
        return image
    
    def remove_self_from_queue(self):
        self.self_removal(self)
        
    def __init__(self, master:Frame, data:Movie, remove_from_queue, is_template=False):
        super().__init__()

        if is_template:
            data.genres="Undefined"
        self.self_removal = remove_from_queue
        is_adult:str = "yes" if data.adult else "no"
        self.display_info = f"Title: {data.title}\nGenres: {data.genres}\nYear: {data.release_year}\nScore: {data.vote_average}\nVote Count: {data.vote_count}\n18+: {is_adult}\n"
        
        #'big' part
        self.text:Label = Label(master=master,
                                text= self.display_info,
                                font=("Times New Roman", 30))
        
        self.image:Image = self.download_image(data.poster_path)
        self.saved:bool = False
        
        #'small' part
                
        #Divide this frame onto 2 columns:
        self.columnconfigure(0,weight=5)
        self.columnconfigure(1,weight=1)

        #-A title (button for loading it onto the main screen)
        #Label for the tile
        self.title = Button(master=self, text=data.title)
        self.grid(column=0, sticky="nsew")
        
        #-A remove button (button for removing it from the queue)
        self.remove = Button(master=self, text="Remove", bg='red', fg='white', command=self.remove_self_from_queue)
        self.grid(column=1, sticky="nsew")
