from tkinter import *
from game_mechanics import *

class MainApp:
    def main (self):
        global main_window
        main_window = Tk()
        main_window.geometry("720x480")
        main_window.title("Who Wants To Be A Millionaire")
        logo = PhotoImage(file='C:\\Users\\Lenovo V14\\.vscode\\OOP Programs\\quiz_maker_quiz_app_2.0\\quiz_app\\picture.gif')
        main_window.iconphoto(True, logo)
        main_window.config(background="black")
        title = Label(main_window, text="Who Wants To Be A Millionaire", 
              font=("Times New Roman", 40),
              bg="blue")
        title.pack()

        start_button = Button(main_window, text="Start", command=MainApp.game(self))
        start_button.place(x=340, y=300)

        exit_button = Button(main_window, text="Exit", command=exit)
        exit_button.place(x=340, y=330)

        main_window.mainloop()

    def game (self):
        start_game = Game()
        start_game.game()
        quiz_label = Label(main_window, text=f"{quiz}",
                   font=("Times New Roman", 25))
        quiz_label.pack()

        letter_a = Button(main_window, text=f"{choice_a}", command=lambda: select_answer("A"),
                        activebackground="black")
        letter_a.place(x=100, y=200)

        letter_b = Button(main_window, text=f"{choice_b}", command=lambda: select_answer("B"),
                        activebackground="black")
        letter_b.place(x=100, y=300)

        letter_c = Button(main_window, text=f"{choice_c}", command=lambda: select_answer("C"),
                        activebackground="black")
        letter_c.place(x=500, y=200)

        letter_d = Button(main_window, text=f"{choice_d}", command=lambda: select_answer("D"),
                        activebackground="black")
        letter_d.place(x=500, y=300)

        submit_button = Button(main_window, text="Submit", command=submit)
        submit_button.place(x=340,y=340)


main_app = MainApp()

if __name__ == "__main__":
    main_app.main()