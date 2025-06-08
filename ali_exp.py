import tkinter as tk
from tkinter import ttk
from tkinter import font
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def vypocti_level_aliance():
    target = int(entry.get())
    values = text_widget.get("1.0", "end")

    ali_levels = [0, 10, 20, 40, 80, 150, 250, 400, 600, 850, 1_150, 1_500]
    try:
        values_of_exp = [int(x) for x in values.split('\t')] # get the list of values from an user [20, 40, 55, 2]
    except:
        output_label["text"] = 'Špatná forma textu. Nelze zpracovat. Zkus to znovu'

    average_exp = sum(values_of_exp) // len(values_of_exp) # avarege of values of all numbers in the list
    rest_exp = ali_levels[target-1] - average_exp # calculation of rest of value to next level

    output_label["text"] = f'Současná průměrná hodnota expů všech zemí v alianci: {average_exp}k \n K dosažení úrovně {target} zbývá {rest_exp}k expů na jednu zemi,\n což je celkem {rest_exp*len(values_of_exp)}k expů za alianci'
    output_label.configure(background='#c4d8f5')
    # kopírovací tlačítko
    
    copy_button.pack(pady=5)

def zkopiruj_text():
    text = output_label["text"]
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def on_scale_change(value):
    entry_var.set(str(int(float(value))))
    
root = tk.Tk()
root.title("Appka pro výpočet zkušenností aliance")
root.geometry('700x600')
root.configure(bg="#f0f0f0")

# Větší font
big_font = font.Font(family="Helvetica", size=14)

# rámec pro prvky
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# popisek a vstupní pole pro string
label = ttk.Label(frame, text="Vlož označené expy všech zemí najednou ze schránky \n označ, ctrl+C/ctrl+V ==> podobně jako na obrázku: ", justify="center", font=big_font)
label.pack()

image_show = tk.PhotoImage(file=resource_path("ali.png"))
ttk.Label(frame, image=image_show).pack(pady=10)

text_widget = tk.Text(
    frame,
    height=2,
    width=50,
    wrap="word",
    font=big_font,
    padx=10,
    pady=10)

text_widget.pack()

# nastavení kurzoru dovnitř textového pole
text_widget.focus_set()
text_widget.mark_set("insert", "1.0")

# popisek a výběrové pole pro volbu úrovně
label_ali = ttk.Label(frame, text="Vyber cílovou hodnost aliance: ", justify="center", font=big_font)
label_ali.pack(pady=5)


# výběrové pole pro alianční level
entry_var = tk.StringVar(value="1")
entry = ttk.Entry(frame, textvariable=entry_var, font=big_font, width=5, justify="center")
entry.pack(pady=(0, 10))

# Posuvník pod Entry
scale = ttk.Scale(frame, from_=0, to=12, orient="horizontal", command=on_scale_change, length=150)
scale.pack()

# rámec pro výstupní text
output_frame = ttk.Frame(frame)
output_frame.pack(pady=10)


# Výstupní label (zatím prázdný)
output_label = ttk.Label(output_frame, text="", font=big_font, foreground="black", justify="center")
output_label.pack(pady=(10, 0))

copy_button = ttk.Button(output_frame, text="Zkopírovat text", command=zkopiruj_text)

# rámec pro tlačítka
button_frame = ttk.Frame(frame)
button_frame.pack(pady=10)

# Submit tlačítko
submit_button = ttk.Button(button_frame, text="Submit", command=vypocti_level_aliance)
submit_button.pack(side="left", padx=10)

# nulovací tlačítko
submit_clear = ttk.Button(button_frame, text="Vymaž zadávací pole", command=lambda: text_widget.delete("1.0", tk.END))
submit_clear.pack(side="left", padx=10)

# tlačíto pro zavření aplikace
closed_button = ttk.Button(button_frame, text="Ukončit", command=root.destroy)
closed_button.pack(side="left", padx=10)

# Spuštění hlavní smyčky
root.mainloop()