from tkinter import *
from src.Movie import Movie
from result_window_methods import *

# Window which shows filtered movies and such
class ResultWindow(Tk):
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
    
    def __init__(self, movies:list[Movie]):
        super().__init__()

        # Load the movie templates into the queue
        add_templates(movies)
        
        # Background and text color 
        background_color = "#{:02x}{:02x}{:02x}".format(52, 53, 65)
        text_color = "#{:02x}{:02x}{:02x}".format(180, 180, 180)

        # App setup
        self.title = "Results"
        self.geometry("1200x700")
        self.configure(bg=background_color)
    
        # Configure the columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        # Configure the rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)  
        
        self.color_rows_and_columns(False)
        
        # Column 1
        
        #Movie image Frame
        frame_poster = Frame(master=self, bg="red")
        frame_poster.grid(column=0,row=0,sticky="nsew", padx=10, pady=10)
        
        #Button for saving/removing
        button_save_remove = Button(master=self, text="SAVE", bg="lightblue", font=("Times New Roman", 30))
        button_save_remove.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
        
        # Column 2
        
        # Frame for text info
        frame_text_information = Frame(master=self, bg="yellow")
        frame_text_information.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")
        
        # Text info
        
        # Button for drawing again
        button_save_remove = Button(master=self, text="DRAW", bg="green", font=("Times New Roman", 30))
        button_save_remove.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")
        
        # Column 3 
        
        # Frame for label "saved positions"
        frame_top_bar = Frame(master=self, bg="lightblue",height=30)
        frame_top_bar.grid(column=2,row=0,sticky="new", pady=10,padx=(10,0))
        
        # Label "saved positions"
        label_top_bar = Label(master=frame_top_bar, text="saved positions",font=("Times New Roman", 15),bg=frame_top_bar.cget('bg'))
        label_top_bar.pack(anchor=CENTER)

        # Canvas for saved positions
        canvas_saved_movies = Canvas(master=self, bg="green", borderwidth=0, highlightthickness=0)
        canvas_saved_movies.grid(column=2, row=0, sticky="nsew", pady=(frame_top_bar.cget('height')+10,10), padx=(10,0))
        
        # Frame within the canvas
        frame_fill_canvas = Frame(master=canvas_saved_movies, bg="darkgreen")
        frame_fill_canvas.pack()
        
        # Scroll for the saved positions section
        scroll_saved = Scrollbar(canvas_saved_movies, orient="vertical", command=canvas_saved_movies.yview)
        scroll_saved.pack(side="right", fill="y")
        
        # Box for warning about the current movie
        frame_warning = Frame(master=self, bg="red")
        frame_warning.grid(column=2,row=1,sticky="nsew",padx=10)
        
        # Warning about the current movie
        label_warning = Label(master=frame_warning, text="Warning, if you switch to saved movie", font=("Times New Roman", 15), bg=frame_warning.cget('bg'))
        label_warning.pack(anchor=CENTER, fill=BOTH, expand=True)
        
if __name__=="__main__":
    window = ResultWindow([])
    window.mainloop()