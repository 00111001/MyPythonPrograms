import tkinter as tk
from tkinter import filedialog

class MeinGUI:
    def __init__(self, fenster):
        fenster.title("Editor")
        fenster.geometry("1200x600")
        fenster.resizable(False, False)

        self.aktuelle_datei = ""  # Instanzvariable für die aktuelle Datei

        # Menüleiste erstellen
        menubar = tk.Menu(fenster)
        fenster.config(menu=menubar)  # Menüleiste für das Hauptfenster festlegen

        # Datei-Menü erstellen
        dateimenü = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=dateimenü)  # Datei-Menü zur Menüleiste hinzufügen
        dateimenü.add_command(label="Neu", command=self.neu)
        dateimenü.add_command(label="Öffnen", command=self.oeffnen)
        dateimenü.add_command(label="Speichern", command=self.speichern)
        dateimenü.add_command(label="Speichern unter...", command=self.speichern_unter)
        dateimenü.add_command(label="Schließen", command=self.beenden)

        # Bearbeiten-Menü
        bearbeitenmenü = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Bearbeiten", menu=bearbeitenmenü)  # Bearbeiten-Menü zur Menüleiste hinzufügen
        bearbeitenmenü.add_command(label="Rückgängig", command=self.rueckgaengig)

        # Strg+Z für Rückgängig binden
        fenster.bind("<Control-z>", self.rueckgaengig)

        # tk.WORD bedeutet, dass der Text im Text-Widget am Ende eines Wortes umgebrochen wird,
        # um sicherzustellen, dass Wörter nicht in der Mitte geteilt werden, wenn sie die rechte
        # Seite des Widgets erreichen.
        self.text_widget = tk.Text(root, wrap=tk.WORD, width=148, height=37)
        self.text_widget.pack()
        self.text_widget.bind("<KeyRelease>", self.text_geaendert)

        self.undo_stack = [self.text_widget.get("1.0", "end-1c")]

    def neu(self):
        self.text_widget.delete("1.0", tk.END)
        self.undo_stack.clear()  # Lösche den Rückgängig-Verlauf bei einem neuen Dokument

    def oeffnen(self):
        dateipfad = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
        if dateipfad:
            with open(dateipfad, "r") as datei:
                inhalt = datei.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, inhalt)
                self.aktuelle_datei = dateipfad
                self.undo_stack.clear()  # Lösche den Rückgängig-Verlauf beim Öffnen einer Datei

    def speichern(self):
        if self.aktuelle_datei:
            with open(self.aktuelle_datei, 'w') as datei:
                datei.write(self.text_widget.get("1.0", "end"))
        else:
            self.aktuelle_datei = filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("Textdateien", "*.txt")])
            if self.aktuelle_datei:
                with open(self.aktuelle_datei, 'w') as datei:
                    datei.write(self.text_widget.get("1.0", "end"))

    def speichern_unter(self):
        dateipfad = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
        if dateipfad:
            inhalt = self.text_widget.get("1.0", tk.END)
            with open(dateipfad, "w") as datei:
                datei.write(inhalt)

    def beenden(self):
        root.destroy()

    def rueckgaengig(self, event=None):
        if self.undo_stack:
            letzter_zustand = self.undo_stack.pop()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, letzter_zustand)

    def text_geaendert(self, event=None):
        if event and event.keysym in ("Alt_L", "Alt_R", "Control_L", "Control_R", "Shift_L", "Shift_R"):
            return
        aktueller_zustand = self.text_widget.get("1.0", "end-1c")  # Aktueller Text
        if not self.undo_stack or aktueller_zustand != self.undo_stack[-1]:
            # Nur speichern, wenn sich der Text geändert hat oder die Liste leer ist
            self.undo_stack.append(aktueller_zustand)
            # Hier den aktuellen Text sichern, bevor er geändert wird
            self.text_widget.edit_separator()

# Funktion für Strg+Z
def rueckgaengig_machen(event):
    app.rueckgaengig()

if __name__ == "__main__":
    root = tk.Tk()
    app = MeinGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.beenden)  # Reagiere auf das Schließen des Fensters
    root.bind_all("<Control-z>", rueckgaengig_machen)  # Strg+Z für Rückgängig
    root.mainloop()
