from CTkTable import CTkTable
import customtkinter

root = customtkinter.CTk()
value = [["Nombre", "Edad", "Ciudad"], [1, 2, 3], [4, 5, 6]]
table = CTkTable(master=root, row=3, column=3, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)
root.mainloop()
