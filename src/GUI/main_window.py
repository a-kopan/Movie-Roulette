from tkinter import *
from tkinter import ttk
from idlelib.tooltip import Hovertip


# Main window to which requirements for movie filtering are provided
class MainWindow(Tk):
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
            frame_c_2 = Frame(self, background="grey")
            frame_c_2.grid(column=2, row=0, rowspan=5, sticky="nsew")
        else:
            # frames with colors for each row
            # row 0
            frame_r_0 = Frame(self, background="grey")
            frame_r_0.grid(column=0, row=0, columnspan=3, sticky="nsew")

            # row 1
            frame_r_1 = Frame(self, background="lightgrey")
            frame_r_1.grid(column=0, row=1, columnspan=3, sticky="nsew")

            # row 0
            frame_r_2 = Frame(self, background="grey")
            frame_r_2.grid(column=0, row=2, columnspan=3, sticky="nsew")

            # row 0
            frame_r_3 = Frame(self, background="lightgrey")
            frame_r_3.grid(column=0, row=3, columnspan=3, sticky="nsew")

            # row 0
            frame_r_4 = Frame(self, background="grey")
            frame_r_4.grid(column=0, row=4, columnspan=3, sticky="nsew")

    def __init__(self):
        # line for setting the background color
        hex_color = "#{:02x}{:02x}{:02x}".format(75, 75, 75)
        hex_color = "#5c6067"
        super().__init__()
        # App setup
        self.title("Movie Roulette")
        self.geometry("1600x700")
        self.resizable(False, False)
        self.configure(bg=hex_color)
        # Column and Row declaration/configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)

        # Adding Widgets

        # 1st row

        # Calling the function for coloring rows/columns
        # self.color_rows_and_columns(False)

        # Movie Roulette title
        label_title = Label(
            self, text="Movie Roulette", font=("Ariel", 30), background=hex_color
        )
        label_title.grid(row=0, column=1, sticky="n", pady=10)

        # --------------------------------------------------------------------#

        # 2nd row
        # Requirements label
        label_requirements = Label(
            self,
            text="Requirements",
            font=("Ariel", 20),
            height=1,
            background=hex_color,
        )
        label_requirements.grid(row=1, column=0, sticky="n", pady=20)

        # About label
        label_about = Label(
            self, text="About", font=("Ariel", 20), background=hex_color
        )
        label_about.grid(row=1, column=2, sticky="n", pady=20)

        # 3rd row
        # Line in the middle
        canvas_line = Canvas(
            self, height=340, width=378, highlightthickness=0, background=hex_color
        )
        x = float(canvas_line.cget("width"))
        canvas_line.create_line(x, 0, x, float(canvas_line.cget("height")), width=2)
        canvas_line.grid(row=2, column=1, sticky="new", pady=6)
        # --------------------------------------------------------------------#

        # 4rd row
        # no API key? label
        label_no_API = Label(
            self,
            text="no API key?",
            font=("Ariel", 10),
            fg="Blue",
            padx=20,
            background=hex_color,
        )
        label_no_API.grid(row=3, sticky="sw", padx=5, pady=5)

        # no API key? label hover
        tooltip_no_KEY = Hovertip(
            label_no_API, "The movie database will be loaded using a local json file."
        )

        # Draw button
        button_draw = Button(
            self, text="DRAW", font=("Ariel", 20), command=(), width=20, height=3
        )
        button_draw.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

        # --------------------------------------------------------------------#

        # 5th row
        # DEMO button
        button_demo = Button(self, text="DEMO", command=(), width=14, height=3)
        button_demo.grid(row=4, column=0, sticky="sw", padx=5, pady=5)

        # Insert API KEY entry
        entry_API_KEY = Entry(self, width=30, font=("Ariel", 20))
        entry_API_KEY.grid(
            row=4,
            column=1,
            sticky="n",
            pady=5,
        )


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
