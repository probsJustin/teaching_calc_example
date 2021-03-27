import tkinter as tk
from functools import partial
class GUI(tk.Frame):

    buttons_func = dict()
    buttons_num = dict()
    text_fields = dict()
    actions = ""
    actions_split = list()
    counter = 0
    return_value = 0
    first_value = 0
    second_value = 0
    action = ""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text_fields["main"] = tk.Text(self, height=2, width=40)
        self.buttons_func["x"] = tk.Button(self, borderwidth=10, command=partial(self.buttonActions, " x "))
        self.buttons_func["+"] = tk.Button(self, borderwidth=10, command=partial(self.buttonActions, " + "))

        self.buttons_func["-"] = tk.Button(self, borderwidth=10, command=partial(self.buttonActions, " - "))
        self.buttons_func["*"] = tk.Button(self, borderwidth=10, command=partial(self.buttonActions, " * "))
        self.buttons_func["/"] = tk.Button(self, borderwidth=10, command=partial(self.buttonActions, " / "))
        self.buttons_func["clear"] = tk.Button(self, borderwidth=10, command=self.clearScreen)
        self.buttons_func["clear"]["text"] = "clear"
        self.buttons_func["x"]["text"] = "x"
        self.buttons_func["+"]["text"] = "+"
        self.buttons_func["-"]["text"] = "-"
        self.buttons_func["*"]["text"] = "*"
        self.buttons_func["/"]["text"] = "/"
        self.text_fields["main"].grid(row=1,column=1, columnspan=5, padx=20, pady=20)
        self.buttons_func["x"].grid(row=2, column=1, padx=20, pady=20)
        self.buttons_func["+"].grid(row=2, column=2, padx=20, pady=20)
        self.buttons_func["-"].grid(row=2, column=3, padx=20, pady=20)
        self.buttons_func["*"].grid(row=2, column=4, padx=20, pady=20)
        self.buttons_func["/"].grid(row=2, column=5, padx=20, pady=20)
        self.buttons_func["clear"].grid(row=3, column=5, padx=20, pady=20)
        for y in range(0,3):
            for x in range(0,3):
                self.counter = self.counter + 1
                self.buttons_num[self.counter] = tk.Button(self, borderwidth=10, command=partial(self.buttonActions, self.counter))
                self.buttons_num[self.counter]["text"] = self.counter
                self.buttons_num[self.counter].grid(row=y + 3, column=x + 1, padx=20, pady=20)
        self.buttons_num["0"] = tk.Button(self, borderwidth=10)
        self.buttons_num["0"]["text"] = 0
        self.buttons_num["0"].grid(row=3, column=4, padx=20, pady=20)
        self.buttons_num["enter"] = tk.Button(self, borderwidth=10, command=self.buttonEnter)
        self.buttons_num["enter"]["text"] = "enter"
        self.buttons_num["enter"].grid(row=4, column=4, padx=20, pady=20)

    def buttonActions(self, action):
        self.actions = str(action) + self.actions
        self.text_fields["main"].delete("1.0", tk.END)
        self.text_fields["main"].insert("1.0", str(self.actions))
        print(action)

    def buttonEnter(self):
        self.actions_split = self.actions.split(' ')
        try:
            if (len(self.actions_split) == 3):
                print("worked")
                self.first_value = int(self.actions_split[0])
                self.second_value = int(self.actions_split[2])
                self.action = self.actions_split[1]
                if(self.action == "x"):
                    self.return_value = int(self.first_value) * int(self.second_value)
                if(self.action == "-"):
                    self.return_value = int(self.first_value) - int(self.second_value)
                if(self.action == "+"):
                    self.return_value = int(self.first_value) + int(self.second_value)
                if(self.action == "/"):
                    self.return_value = int(self.first_value) / int(self.second_value)
                self.text_fields["main"].delete("1.0", tk.END)
                self.text_fields["main"].insert("1.0", str(self.return_value))

                self.actions = ""
            else:
                self.text_fields["main"].delete("1.0", tk.END)
                self.text_fields["main"].insert("1.0", str("error"))
        except Exception as e:
            print(e)
            self.text_fields["main"].delete("1.0", tk.END)
            self.text_fields["main"].insert("1.0", str("error"))
            self.actions = ""
    def clearScreen(self):
        self.actions = ""
        self.text_fields["main"].delete("1.0", tk.END)
        self.text_fields["main"].insert("1.0", self.actions)














