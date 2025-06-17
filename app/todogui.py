import tkinter as tk 

class app:
    def __init__(self):
        
            
        self.createdisplay()
        self.update_listbox()

    def createdisplay(self):

        self.fenster = tk.Tk()
        self.fenster.geometry('300x300')
        self.fenster.title('Hausaufgaben')


        self.listbox_zumachen = tk.Listbox(self.fenster, height=10, width=20)
        self.listbox_zumachen.place(x=2, y=54)

        self.add_button = tk.Button(self.fenster, text='Hinzufügen',)
        self.add_button.place(x=130, y=30)

        self.show_button = tk.Button(self.fenster, text='Show more', )
        self.show_button.place(x=2, y=220)

        self.done_button = tk.Button(self.fenster, text='DONE', )
        self.done_button.place(x=130, y=57)

        self.eingabe = tk.Entry(self.fenster)
        self.eingabe.place(x=0, y=32)

        self.close_button = tk.Button(self.fenster, text='Close', command=self.fenster.destroy)
        self.close_button.place(x=258, y=273)

        self.anzeigeoben = tk.Label(self.fenster, text='TODO', font=("times", 18, "bold"))
        self.anzeigeoben.place(x=2, y=0)
    







        self.fenster.mainloop()






























if __name__ == '__main__':
    App = app()