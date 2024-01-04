from tkinter import *
from src.Movie import Movie
from MovieTile import MovieTile
import src.db_calls as dbc
from PIL import ImageTk, Image
# Window which shows filtered movies and such
class ResultWindow(Toplevel):
    
    # Load the choosen 
    # Method for coloring columns/rows (only for checking during development)
    def color_rows_and_columns(self, c):
        if c:
            # frames with color visual for each column
            # column 0
            frame_c_0 = Frame(self, background="grey")
            frame_c_0.grid(column=0, row=0, rowspan=5, sticky="nsew")

            # column 1
            frame_c_1 = Frame(self, background="lightgrey")
            frame_c_1.grid(column=1, row=0, rowspan=5, sticky="nsew")
            
            # column 2
            frame_c_2 = Frame(self, background="lightgrey")
            frame_c_2.grid(column=1, row=0, rowspan=5, sticky="nsew")
        else:
            # frames with colors for each row
            # row 0
            frame_r_0 = Frame(self, background="grey")
            frame_r_0.grid(column=0, row=0, columnspan=3, sticky="nsew")

            # row 1
            frame_r_1 = Frame(self, background="lightgrey")
            frame_r_1.grid(column=0, row=1, columnspan=3, sticky="nsew")

    # On the GUI assemble, load 2 movie templates into a queue
    # One for the space before first movie, second for marking the end of the queue ()
    # Add the first and last movie templates into the queue
    def add_templates(self, movies:list[MovieTile]):
        movie_f = Movie("Start")
        self.first_template = MovieTile(master=self.frame_saved_movies, data=movie_f, result_window=self, is_template=True)
        movie_s = Movie("End")
        self.last_template = MovieTile(master=self.frame_saved_movies, data=movie_s, result_window=self, is_template=True)
        
        movies.insert(0,self.first_template)
        movies.append(self.last_template)
         
    # Remove given tile from the movie queue
    def remove_from_queue(self, tile:MovieTile):
        self.queue.remove(tile)
    
    # Remove given tile from the saved list    
    def remove_from_saved(self, tile=None):
        if not tile:
            tile = self.current
        self.saved.remove(tile)
        tile.saved = False
        
        #Deletes the small version of the tile from the frame
        tile.pack_forget()
    
        #Changes the button
        self.button_save_remove.config(bg='green',
                                        text="SAVE",
                                        command=self.add_to_saved)
        self.refresh_window()
    
    # Add given tile to saved list
    def add_to_saved(self):
        tile = self.current
        #If the tile isn't saved yet
        if not tile in self.saved:
            self.saved.append(tile)
            tile.saved = True
            self.button_save_remove.config(bg='red',
                                           text="REMOVE",
                                           command=self.remove_from_saved)
            #Load the small version of tile into the saved frame
            tile.pack(anchor=N, pady=5, fill=BOTH, expand=True)
            
    # Scale image to the size of the frame that shows it
    def scale_image(self, image:Image):
        new_size = (self.canvas_poster.winfo_width() ,self.canvas_poster.winfo_height())
        image = image.resize(size=new_size)
        return image
    
    # Change the size of image to make it fit into the poster Frame
    def load_image(self, image):
        # Delete previously shown image
        self.canvas_poster.delete('all')
        # Scale the image to good dimensions
        image = self.scale_image(image)
        image = ImageTk.PhotoImage(image=image)
        # Hold the reference to image so it doesn't disappear on the spot
        self.images.append(image)
        self.canvas_poster.create_image(0,0, anchor='nw', image=image)
        
    #Load singular MovieTile's details into the GUI
    def load_tile(self, tile:MovieTile):
        # Load the text details
        self.stringvar_info.set(tile.display_info)
        
        # If image is avaliable, load it
        if tile.image: self.load_image(tile.image)
        
    # Refresh and check if the logic-gui relation
    def refresh_window(self):
        # Change the save button if needed
        if self.current.saved:
            self.button_save_remove.config(bg='red',
                                           text="REMOVE",
                                           command=self.remove_from_saved,
                                           state=ACTIVE)
        else:
            self.button_save_remove.config(bg='green',
                                           text="SAVE",
                                           command=self.add_to_saved,
                                           state=ACTIVE)
        
        #If the current tile is the last one, block the draw button
        if self.current is self.last_template:
            self.button_draw.config(state=DISABLED, bg='grey')
            
        # If the current tile is one of the templates, disable the button
        if self.current is self.last_template or self.current is self.first_template:
            self.button_save_remove.config(state=DISABLED)

    # Draw the next movie and get delete the current one from the queue
    def draw_next(self):
        # Change the current tile
        self.current = self.queue.pop(0)
        # Load current tile
        self.load_tile(self.current)
        # Refresh window
        self.refresh_window()
        
    def __init__(self,movies:list[Movie]):
        #Section for GUI
        super().__init__()
        
        # Background and text color 
        self.background_color = "#{:02x}{:02x}{:02x}".format(52, 53, 65)
        text_color = "#{:02x}{:02x}{:02x}".format(180, 180, 180)

        # App setup
        self.title = "Results"
        self.geometry("1200x700")
        self.configure(bg=self.background_color)
    
        # Configure the columns
        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Configure the rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)  
        
        # Column 1
        
        #Movie poster canvas
        self.canvas_poster = Canvas(self, borderwidth=0, highlightthickness=0, bg=self.background_color)
        self.canvas_poster.grid(column=0, row=0, sticky="nsew", padx=10)
        
        #Movie image Frame
        self.frame_poster = Frame(master=self.canvas_poster)
        self.frame_poster.grid(column=0,row=0,sticky="nsew")
        
        
        #Button for saving/removing
        self.button_save_remove = Button(master=self, text="SAVE", bg="lightblue", font=("Times New Roman", 30), command=self.add_to_saved)
        self.button_save_remove.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
        
        
        # Column 2
        
        # Frame for text info
        self.frame_text_information = Frame(master=self)
        self.frame_text_information.grid(column=1, row=0, padx=10, pady=10, sticky="ns")
        
        # String var that holds current text info displayed
        self.stringvar_info = StringVar()
        
        # Displayed information about a current tile
        self.label_text_info = Label(master=self.frame_text_information,
                                     font=("Times New Roman", 30),
                                     bg=self.background_color,
                                     fg=text_color,
                                     textvariable=self.stringvar_info)
        self.label_text_info.pack(anchor=CENTER, fill=BOTH, expand=True)
        
        # Button for drawing again
        self.button_draw = Button(master=self, text="DRAW", bg="green", font=("Times New Roman", 30), command=self.draw_next)
        self.button_draw.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")
        
        # Column 3 
        
        # Frame for label "saved positions"
        self.frame_top_bar = Frame(master=self, bg="lightblue",height=30)
        self.frame_top_bar.grid(column=2,row=0,sticky="new", pady=10,padx=(10,0))
        
        # Label "saved positions"
        self.label_top_bar = Label(master=self.frame_top_bar, text="saved positions",font=("Times New Roman", 15),bg=self.frame_top_bar.cget('bg'))
        self.label_top_bar.pack(anchor=CENTER)
        
        # Frame with saved movies
        self.frame_saved_movies = Frame(master=self, bg=self.background_color)
        self.frame_saved_movies.grid(column=2, row=0, sticky="nsew", pady=(self.frame_top_bar.cget('height')+10,10), padx=(10,0))
      
        # Box for warning about the current movie
        self.frame_warning = Frame(master=self, bg=self.background_color)
        self.frame_warning.grid(column=2,row=1,sticky="ns")
        
        # Warning about the current movie
        self.label_warning = Label(master=self.frame_warning, text="Warning, if you switch to saved movie,\n the currently chosen one will be lost.", font=("Times New Roman", 15), bg='red')#, bg=self.frame_warning.cget('bg'))
        self.label_warning.pack(anchor=CENTER, fill=X, expand=True)

        # Section for logic
        
        # Main queue for movies (not yet visited)
        #Fill the queue with all filtered MovieTile objects made out of Movie objects
        self.queue:list[MovieTile] = [MovieTile(master=self.frame_saved_movies, data=movie, result_window=self) for movie in movies]
        
        # Keep the reference to each photo so they don't appear as white boxes
        self.images = []
        
        # List for saved MovieTiles
        self.saved = []
        
        # Add first and last templates into the movies section
        self.add_templates(self.queue)
        
        #Currently choosen tile
        self.current:MovieTile = self.queue[0]
        
        # On window appear, load the first template
        self.draw_next()
        
        
if __name__=="__main__":
    
    db_path = r"database\Movie_db.db"
    table_name = "Movies_table"
    temp_requirements = {
    "min_rating":0,
    "max_rating":11,
    "min_production_year":-1,
    "max_production_year":9999,
    "genre_to_get":"Horror"}
    
    movies_from_db = dbc.load_from_db(db_path, table_name, temp_requirements)
    window = ResultWindow(movies=movies_from_db)

    window.mainloop()