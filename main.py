from src.db_calls import *
from src.GUI.main_window import *


def main():
    # Declare paths and table names to databases
    db_path = "database/Movie_db.db"
    table = "Movies_table"
    # Create the table
    create_table(db=db_path, table_name=table)
    # Clear table, in case that there is already created one
    clear_table(db=db_path, table_name=table)
    # Open the main window
    root = MainWindow(db_name=db_path, table_name=table)
    root.mainloop()


if __name__ == "__main__":
    main()
