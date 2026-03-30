import customtkinter as tk

class MyCheckboxFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = tk.CTkCheckBox(self, text="Checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10,100), sticky="w")
        self.checkbox_2 = tk.CTkCheckBox(self, text="Checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10,0), sticky="w")
        self.checkbox_3 = tk.CTkCheckBox(self, text="Checkbox 3")
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        self.button = tk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    def button_callback(self):
        print("Button pressed")

app = App()
app.mainloop()