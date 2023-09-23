import tkinter as tk
from tkinter import filedialog

class MeinGUI:
    def __init__(self, fenster):
        self.fenster = fenster
        fenster.title("Editor")
        fenster.geometry("1200x600")
        fenster.resizable(False, False)

        self.current_file = ""  # Instanzvariable für die aktuelle Datei

        # Create a menu bar
        menubar = tk.Menu(fenster)
        fenster.config(menu=menubar)  # Set the menu bar for the main window

        # Create a File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)  # Add File menu to the menu bar
        filemenu.add_command(label="New", command=self.mneu)
        filemenu.add_command(label="Open", command=self.moeffnen)
        filemenu.add_command(label="Save", command=self.mspeichern)
        filemenu.add_command(label="Save as...", command=self.mspeichern_unter)
        filemenu.add_command(label="Close", command=self.mbeenden)

        # Bearbeiten menu
        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Bearbeiten", menu=editmenu)  # Add File menu to the menu bar
        editmenu.add_command(label="Rückgängig", command=self.mrueckgangig)

        # Bind Ctrl+Z for Undo
        fenster.bind("<Control-z>", self.mrueckgangig)

        # tk.WORD bedeutet, dass der Text im Text-Widget am Ende eines Wortes umgebrochen wird,
        # um sicherzustellen, dass Wörter nicht in der Mitte geteilt werden, wenn sie die rechte
        # Seite des Widgets erreichen.
        self.text_widget = tk.Text(root, wrap=tk.WORD, width=148, height=37)
        self.text_widget.pack()
        self.text_widget.bind("<KeyRelease>", self.text_changed)

        self.undo_stack = [self.text_widget.get("1.0", "end-1c")]

    def mneu(self):
        self.text_widget.delete("1.0", tk.END)
        self.undo_stack.clear()  # Lösche den Rückgängig-Verlauf bei einem neuen Dokument

    def moeffnen(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, content)
                self.current_file = file_path
                self.undo_stack.clear()  # Lösche den Rückgängig-Verlauf beim Öffnen einer Datei

    def mspeichern(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.text_widget.get("1.0", "end"))
        else:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Text Files", "*.txt")])
            if self.current_file:
                with open(self.current_file, 'w') as file:
                    file.write(self.text_widget.get("1.0", "end"))

    def mspeichern_unter(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            content = self.text_widget.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)

    def mbeenden(self):
        root.destroy()

    def mrueckgangig(self, event=None):
        if self.undo_stack:
            last_state = self.undo_stack.pop()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, last_state)

    def text_changed(self, event=None):
        if event and event.keysym in ("Alt_L", "Alt_R", "Control_L", "Control_R", "Shift_L", "Shift_R"):
            return
        current_state = self.text_widget.get("1.0", "end-1c")  # Aktueller Text
        if not self.undo_stack or current_state != self.undo_stack[-1]:
            # Nur speichern, wenn sich der Text geändert hat oder die Liste leer ist
            self.undo_stack.append(current_state)
            # Hier den aktuellen Text sichern, bevor er geändert wird
            self.text_widget.edit_separator()

# Funktion für Strg+Z
def do_undo(event):
    app.mrueckgangig()

if __name__ == "__main__":
    root = tk.Tk()
    app = MeinGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.mbeenden)  # Reagiere auf das Schließen des Fensters
    root.bind_all("<Control-z>", do_undo)  # Strg+Z für Rückgängig
    root.mainloop()
