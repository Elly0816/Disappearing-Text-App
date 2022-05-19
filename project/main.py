import tkinter as tk
import time
import threading


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.title("Disappearing Writing App")
        self.geometry("")
        # self.resizable()
        self.minsize(700, 650)
        self.maxsize(700, 650)
        self.create_frame()
        self.create_text()
        self.create_button()

    # Frame holds all items in the window
    def create_frame(self):
        self.frame = tk.Frame(self, bg='gray', height=800, width=1000)
        self.frame.pack_propagate(False)
        self.frame.pack(fill='both', expand=True)

    def create_button(self):
        self.button = tk.Button(self.frame, text="Start",
                                command=self.clicked, height=2,
                                width=8)
        self.button.pack(fill='y', expand=True, anchor="center")

    def create_text(self):
        self.text = tk.Text(self.frame,
                            font=('Times new Roman', 17, 'bold'),
                            relief='groove', state='normal', bg='#ffffff')
        self.text.pack(expand=True, fill='both')
        self.text.bind('<Key>', func=self.pressed)
        self.text.insert('1.0',
                         """Click the start button to start typing text...\nYour text gradually disappears when you stop typing.""")
        self.text['state'] = 'disabled'

    def pressed(self, e):
        self.timer = 0

    def clicked(self):
        self.text['state'] = 'normal'
        self.text.delete('1.0', 'end')
        self.colors = ['#ffffff', '#F2F3F3', '#c0c0c0', '#BDBEBE',
                  '#898989', '#808080', "#545454",
                  '#2b2b2b', '#000001']

        def change_color():
            color = len(self.colors)-1
            while color >= 0 and self.timer <= 20:
                if self.timer == 0:
                    self.timer += 1
                    color = len(self.colors)-1
                    self.text['fg'] = self.colors[color]
                else:
                    self.timer += 1
                    time.sleep(2)
                    self.text['fg'] = self.colors[color]
                    color -= 1
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', "Time's Up! Click Restart to restart...")
            self.text['fg'] = 'black'
            self.text['state'] = 'disabled'
            self.button['text'] = 'Restart'
            self.timer = 0

        return threading.Thread(name="changed font", daemon=True,
                                target=change_color).start()


app = Application()
app.mainloop()
