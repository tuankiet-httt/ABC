import tkinter as tk
from views.dichvu_view import DichVuView
from controllers.dichvu_controller import DichVuController

if __name__ == "__main__":
    root = tk.Tk()
    view = DichVuView(root, None)
    controller = DichVuController(view)
    view.controller = controller
    root.mainloop()
