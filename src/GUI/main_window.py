import src.db_calls as dbc
import src.API.API_request as apir
from src.GUI.result_window import ResultWindow
from src.API.json_to_Movie import responses_to_movies
from tkinter import *
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from src.Movie import *

# Main window to which requirements for movie filtering are provided
class MainWindow(Tk):
    # Colors rows/columns ()
    def color_rows_and_columns(self, c):
        if c:
            # frames with color visual for each column
            # column 0
            frame_c_0 = Frame(self, background="grey")
            frame_c_0.grid(column=0, row=0, rowspan=5, sticky="nsew")

            # column 1
            frame_c_1 = Frame(self, background="lightgrey")
            frame_c_1.grid(column=1, row=0, rowspan=5, sticky="nsew")
        else:
            # frames with colors for each row
            # row 0
            frame_r_0 = Frame(self, background="grey")
            frame_r_0.grid(column=0, row=0, columnspan=3, sticky="nsew")

            # row 1
            frame_r_1 = Frame(self, background="lightgrey")
            frame_r_1.grid(column=0, row=1, columnspan=3, sticky="nsew")

            # row 2
            frame_r_2 = Frame(self, background="grey")
            frame_r_2.grid(column=0, row=2, columnspan=3, sticky="nsew")

            # row 3
            frame_r_3 = Frame(self, background="lightgrey")
            frame_r_3.grid(column=0, row=3, columnspan=3, sticky="nsew")

            # row 4
            frame_r_4 = Frame(self, background="darkgrey")
            frame_r_4.grid(column=0, row=4, columnspan=3, sticky="nsew")

            # row 5
            frame_r_5 = Frame(self, background="lightblue")
            frame_r_5.grid(column=0, row=4, columnspan=3, sticky="nsew")

    # Made for easier implementation of the requirement segments (label and 2 entries)
    # Returns list of StringVars for each entry window
    def set_requirement_segment(
        self,
        master: Tk,
        label_text: str,
        row: int,
        column: int,
        bg_color: str,
        fg_color: str,
    ) -> list[StringVar]:
        # set the label
        label_widget = Label(
            master=master,
            text=label_text,
            font=("Times New Roman", 15),
            bg=bg_color,
            fg=fg_color,
        )
        label_widget.grid(column=column, row=row, sticky="w", padx=10)

        # stringvar for the first entry
        min_stringvar = StringVar()
        # set the first entry
        entry_first = Entry(master=master, width=4, font=("Times New Roman", 10), textvariable=min_stringvar)
        entry_first.insert(0, "0")

        entry_first.grid(column=column, row=row, sticky="w", padx=(500, 0))

        # stringvar for the second entry
        max_stringvar = StringVar()
        # set the second entry
        entry_second = Entry(master=master, width=4, font=("Times New Roman", 10), textvariable=max_stringvar)
        entry_second.insert(0, "9999")

        entry_second.grid(column=column, row=row, sticky="w", padx=(550, 0))
        
        return [min_stringvar, max_stringvar]

    # Adds newlines every n spaces in a string s
    def add_newlines(self, s: str, n: int):
        return "\n".join(s[i:i+n] for i in range(0, len(s), n))
    
    def show_warning(self):
        messagebox.showwarning("Warning", "API key not correct.")
    
    # Get the movies from db that fulfill the requirements
    def get_filtered_movies(self,db,table_name) -> list[Movie]:
        requirements = {
            "min_rating":int(self.min_rating.get()),
            "max_rating":int(self.max_rating.get()),
            "min_production_year":int(self.min_year.get()),
            "max_production_year":int(self.max_year.get()),
            "genre_to_get":self.strvar_curr_category.get()
        } 
        filtered_movies = dbc.load_from_db(db, table_name, requirements=requirements)
        return filtered_movies
    
    # Loads the movies to database using provided API key
    def draw_button_action(self):
        API_KEY = self.entry_API_KEY.get()
        
        #If the API_KEY wasn't provided/is wrong, show a warning message
        if len(API_KEY)<48:
            self.show_warning()
            return
        
        #First, clear the database
        dbc.clear_table(self.db_name, self.table_name)
        
        #Code for movie genre
        current_genre = self.strvar_curr_category.get()
        code = [val for (key,val) in genres.items() if key==current_genre][0]
        
        #Send API request for all movies
        all_movies = apir.send_n_API_requests_with_key(category_code=code, n_of_pages=3, API_KEY=API_KEY)
        
        #Load the movies into the database
        dbc.load_to_db(self.db_name, self.table_name, all_movies)
        
        filtered_movies = self.get_filtered_movies(self.db_name, self.table_name)
        self.pass_to_second_window(filtered_movies)
    
    # Loads the movies to database from local json file
    def demo_button_action(self):
        local_file = open(r'tests\test_json.json',encoding='utf-8')
        all_movies = responses_to_movies(local_file.read())
        dbc.clear_table(self.db_name, self.table_name)
        dbc.load_to_db(self.db_name, self.table_name, all_movies)
        
        filtered_movies = self.get_filtered_movies(self.db_name, self.table_name)
        self.pass_to_second_window(filtered_movies)
    
    # Passes filtered movies to the result window
    def pass_to_second_window(self, filtered_movies):
        # Close the current window
        self.withdraw()
        
        # Open the second window
        result_window = ResultWindow(filtered_movies)
        result_window.mainloop()

    def __init__(self, db_name, table_name):
        super().__init__()
        self.db_name = db_name
        self.table_name = table_name
        # Background and text color 
        background_color = "#{:02x}{:02x}{:02x}".format(52, 53, 65)
        text_color = "#{:02x}{:02x}{:02x}".format(180, 180, 180)
        button_color = "#{:02x}{:02x}{:02x}".format(42, 42, 42)
        # App setup
        self.title("Movie Roulette")
        self.geometry("1200x700")
        self.configure(bg=background_color)

        # Column and Row declaration/configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)

        # Adding Widgets

        # 1st row

        # Calling the function for coloring rows/columns
        #self.color_rows_and_columns(False)

        # Movie Roulette title
        self.label_title = Label(
            self,
            text="Movie Roulette",
            font=("Times New Roman", 30, "bold"),
            background=background_color,
            fg=text_color,
        )
        self.label_title.grid(row=0, column=0, sticky="n", pady=10, columnspan=2)

        # --------------------------------------------------------------------#

        # 2nd row
        # REQUIREMENTS SECTION
        self.label_requirements = Label(
            self,
            text="Requirements",
            font=("Times New Roman", 30),
            background=background_color,
            fg=text_color,
        )
        self.label_requirements.grid(row=1, column=0, sticky="n", pady=20)

        # About label
        self.label_about = Label(
            self,
            text="About",
            font=("Times New Roman", 30),
            background=background_color,
            fg=text_color,
        )
        self.label_about.grid(row=1, column=1, sticky="n", pady=20)

        # --------------------------------------------------------------------#

        # 3rd row

        # Label and 2 windows for movie rating
        self.rating_text = "Min/Max movie rating (leave for all movies)"
        [self.min_rating, self.max_rating] = self.set_requirement_segment(
            master=self,
            label_text=self.rating_text,
            row=2,
            column=0,
            bg_color=background_color,
            fg_color=text_color,
        )

        # Label for text under About
        self.label_about_text = "This application uses an  Advanced Movie Search APi,   created by Akash Joshi. It  loads the movies into the database and    then filters them    based on  the requirements selected. The text-box under the   DRAW button is for the API key insertion."
        self.label_about_text = self.add_newlines(self.label_about_text, 26)

        self.label_under_about = Label(
            text=self.label_about_text,
            font=("Times New Roman", 22),
            width=int((int(self.winfo_width())) / 15),
            background=background_color,
            fg=text_color,
        )

        self.label_under_about.grid(
            row=2, column=1, sticky="nsew", padx=10, rowspan=2, columnspan=2
        )

        # --------------------------------------------------------------------#

        # 4th row
        # Frame for the requirement segment (year and category)
        frame_category = Frame(master=self, bg=background_color)
        frame_category.grid(column=0, row=3, sticky="nsew", pady=10)
        
        frame_category.rowconfigure(0, weight=1)
        frame_category.rowconfigure(1, weight=1)
        
        # Label and 2 windows for movie production year
        self.year_text = "Min/Max movie production year (leave for all movies)"
        [self.min_year, self.max_year] = self.set_requirement_segment(
            master=frame_category,
            label_text= self.year_text,
            row=0,
            column=0,
            bg_color=background_color,
            fg_color=text_color,
        )

        #Label and choice bod for the category of the movie
        self.label_category = Label(frame_category,
                                    text="Category ",
                                    font=("Times New Roman", 15),
                                    bg=background_color,
                                    fg=text_color,
                                    anchor='w')
        self.label_category.grid(row=1,column=0, sticky="nsew", padx=10)
        
        self.strvar_curr_category = StringVar(frame_category)
        self.strvar_curr_category.set(list(genres.keys())[0])
        
        self.optionMenu_category = OptionMenu(frame_category,
                                              self.strvar_curr_category,
                                              *genres.keys(),)
        self.optionMenu_category.grid(row=1, column=0,sticky="e")
        rows, columns = frame_category.grid_size()
        # --------------------------------------------------------------------#
        # 5th row
        # no API key? label
        self.label_no_API = Label(
            self,
            text="no API key?",
            font=("Times New Roman", 10),
            fg="#45b6fe",
            background=background_color,
        )
        self.label_no_API.grid(row=4, sticky="sw", padx=5, pady=5, column=0)

        # no API key? label hover
        tooltip_no_KEY = Hovertip(
            self.label_no_API, "The movie database will be loaded using a local json file."
        )

        # Draw button
        self.button_draw = Button(
            self,
            text="DRAW",
            font=("Times New Roman", 20),
            command= self.draw_button_action,
            width=20,
            height=3,
            bg=button_color,
            fg=text_color,
        )
        self.button_draw.grid(row=4, column=0, sticky="ns", padx=5, pady=5, columnspan=2)

        # --------------------------------------------------------------------#

        # 6th row
        # DEMO button
        self.button_demo = Button(
            self,
            text="DEMO",
            command=self.demo_button_action,
            width=14,
            height=3,
            bg=button_color,
            fg=text_color,
        )
        self.button_demo.grid(row=5, column=0, sticky="sw", padx=5, pady=5)

        # Stringvar for entry for API key
        self.entry_API_strvar = StringVar()
        # Entry for API key
        self.entry_API_KEY = Entry(self, width=30, font=("Times New Roman", 20))
        self.entry_API_KEY.insert(0, "")
        self.entry_API_KEY.grid(row=5, column=0, sticky="n", pady=5, columnspan=2)


if __name__ == "__main__":
    db_path = r"database\Movie_db.db"
    table_name = "Movies_table"
    dbc.clear_table(db_path, table_name)
    window = MainWindow(db_path, table_name)
    window.mainloop()
