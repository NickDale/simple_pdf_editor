import tkinter as tk

from files import FileUtil


class UI:

    def __init__(self):
        self.file_util = FileUtil()

    def create_ui(self):

        window = tk.Tk()
        window.title("Simple Pdf Editor")
        window.rowconfigure(0, minsize=800, weight=1)
        window.columnconfigure(1, minsize=800, weight=1)

        txt_edit = tk.Text(window)
        buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(buttons, text="Open", command=lambda: self.file_util.open_file(window, txt_edit))
        btn_save_pdf = tk.Button(buttons, text="Save As...", command=lambda: self.file_util.save_as(txt_edit))
        clear_btn = tk.Button(buttons, text="Clear all", command=lambda: self.file_util.clear_all(txt_edit))
        merge_btn = tk.Button(buttons, text="Merge pdf", command=lambda: self.file_util.merge_pdf(txt_edit))
        label = tk.Label(buttons)

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        merge_btn.grid(row=1, column=0, sticky="ew", padx=5)
        label.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        btn_save_pdf.grid(row=3, column=0, sticky="ew", padx=5)
        clear_btn.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        buttons.grid(row=0, column=0, sticky="ns")
        txt_edit.grid(row=0, column=1, sticky="nsew")

        window.mainloop()
