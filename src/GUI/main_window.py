from tkinter import *
from idlelib.tooltip import Hovertip


# Main window to which requirements for movie filtering are provided
class MainWindow(Tk):
    # function that colors rows/columns ()
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

    # made for easier implementation of the requirement segments (label and 2 entries)
    def set_requirement_segment(
        self,
        root: Tk,
        label_text: str,
        row: int,
        column: int,
        bg_color: str,
        fg_color: str,
    ):
        # set the label
        label_widget = Label(
            master=root,
            text=label_text,
            font=("Times New Roman", 15),
            bg=bg_color,
            fg=fg_color,
        )
        label_widget.grid(column=column, row=row, sticky="w", padx=10)

        # set the first entry
        entry_first = Entry(master=root, width=4, font=("Times New Roman", 10))
        entry_first.insert(0, "0")

        entry_first.grid(column=column, row=row, sticky="w", padx=(500, 0))

        # set the second entry
        entry_second = Entry(master=root, width=4, font=("Times New Roman", 10))
        entry_second.insert(0, "9999")

        entry_second.grid(column=column, row=row, sticky="w", padx=(550, 0))

    # funtion that adds newlines every n spaces in a string s
    def add_newlines(self, s: str, n: int):
        return "\n".join(s[i : i + n] for i in range(0, len(s), n))

    def __init__(self):
        # line for setting the background color
        background_color = "#{:02x}{:02x}{:02x}".format(52, 53, 65)
        text_color = "#{:02x}{:02x}{:02x}".format(180, 180, 180)
        super().__init__()
        # App setup
        self.update_idletasks()
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
        # self.color_rows_and_columns(True)

        # Movie Roulette title
        label_title = Label(
            self,
            text="Movie Roulette",
            font=("Times New Roman", 30, "bold"),
            background=background_color,
            fg=text_color,
        )
        label_title.grid(row=0, column=0, sticky="n", pady=10, columnspan=2)

        # --------------------------------------------------------------------#

        # 2nd row
        # REQUIREMENTS SECTION
        label_requirements = Label(
            self,
            text="Requirements",
            font=("Times New Roman", 30),
            background=background_color,
            fg=text_color,
        )
        label_requirements.grid(row=1, column=0, sticky="n", pady=20)

        # About label
        label_about = Label(
            self,
            text="About",
            font=("Times New Roman", 30),
            background=background_color,
            fg=text_color,
        )
        label_about.grid(row=1, column=1, sticky="n", pady=20)

        # --------------------------------------------------------------------#

        # 3rd row

        # Label and 2 windows for movie rating
        rating_text = "Min/Max movie rating (leave for all movies)"
        self.set_requirement_segment(
            root=self,
            label_text=rating_text,
            row=2,
            column=0,
            bg_color=background_color,
            fg_color=text_color,
        )

        # Label for text under About
        label_about_text = "This application uses an  Advanced Movie Search APi,   created by Akash Joshi. It  loads the movies into the database and    then filters them    based on  the requirements selected."
        label_about_text = self.add_newlines(label_about_text, 26)

        label_under_about = Label(
            text=label_about_text,
            font=("Times New Roman", 22),
            width=int((int(self.winfo_width())) / 15),
            background=background_color,
            fg=text_color,
        )

        label_under_about.grid(
            row=2, column=1, sticky="nsew", padx=10, rowspan=2, columnspan=2
        )

        # --------------------------------------------------------------------#

        # 4th row
        # Label and 2 windows for movie production year
        year_text = "Min/Max movie production year (leave for all movies)"
        self.set_requirement_segment(
            root=self,
            label_text=year_text,
            row=3,
            column=0,
            bg_color=background_color,
            fg_color=text_color,
        )

        # --------------------------------------------------------------------#
        # 5th row
        # no API key? label
        label_no_API = Label(
            self,
            text="no API key?",
            font=("Times New Roman", 10),
            fg="#45b6fe",
            background=background_color,
        )
        label_no_API.grid(row=4, sticky="sw", padx=5, pady=5, column=0)

        # no API key? label hover
        tooltip_no_KEY = Hovertip(
            label_no_API, "The movie database will be loaded using a local json file."
        )

        # Draw button
        button_draw = Button(
            self,
            text="DRAW",
            font=("Times New Roman", 20),
            command=(),
            width=20,
            height=3,
            bg="#{:02x}{:02x}{:02x}".format(42, 42, 42),
            fg=text_color,
        )
        button_draw.grid(row=4, column=0, sticky="ns", padx=5, pady=5, columnspan=2)

        # --------------------------------------------------------------------#

        # 6th row
        # DEMO button
        button_demo = Button(
            self,
            text="DEMO",
            command=(),
            width=14,
            height=3,
            bg="#{:02x}{:02x}{:02x}".format(42, 42, 42),
            fg=text_color,
        )
        button_demo.grid(row=5, column=0, sticky="sw", padx=5, pady=5)

        # Insert API KEY entry
        entry_API_KEY = Entry(self, width=30, font=("Times New Roman", 20))
        entry_API_KEY.insert(0, "           Insert your API key here")
        entry_API_KEY.grid(row=5, column=0, sticky="n", pady=5, columnspan=2)


if __name__ == "__main__":
    window = MainWindow()
    a = window.geometry()
    window.mainloop()
