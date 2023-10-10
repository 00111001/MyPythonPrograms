import tkinter as tk

class ShoppingPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Planner")

        # Input for plannings
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=0, pady=10, padx=10)

        # Button
        self.add_button = tk.Button(root, text="Hinzufügen", command=self.add_item)
        self.add_button.grid(row=0, column=1, pady=10, padx=10)

        # Listbox
        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, sticky="nsew")

        # Binden der Entf-Taste zum Löschen ausgewählter Elemente
        self.entry.bind('<Return>', self.add_item)
        self.listbox.bind('<Delete>', self.delete_selected)


        # Konfiguriere das Raster, um sich beim Größenändern anzupassen
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def add_item(self,event):
        text = self.entry.get()
        if text:
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def delete_selected(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingPlanner(root)
    root.mainloop()
