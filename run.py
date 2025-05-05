# run.py

import sys
import gestor.menu as menu
import gestor.ui as ui

def main():
    
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    else:
        app = ui.MainWindow()
        app.mainloop()