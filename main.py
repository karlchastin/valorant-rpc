import ctypes,os,traceback

# Vérifier les dépendances AVANT les autres imports
try:
    from src.utilities.dependencies import verify_and_install
    deps_ok, missing_deps = verify_and_install()
    if not deps_ok:
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, 1)
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x40|0x100))
        
        # Essayer d'importer color_print pour les messages, sinon utiliser print
        try:
            from InquirerPy.utils import color_print
            color_print([("Red bold", "Erreur : Bibliothèques Python manquantes")])
            color_print([("Yellow", f"Les bibliothèques suivantes ne sont pas installées : {', '.join(missing_deps)}")])
            color_print([("Cyan", "Pour installer toutes les dépendances, exécutez :")])
            color_print([("White", "pip install -r requirements.txt")])
        except:
            print("Erreur : Bibliothèques Python manquantes")
            print(f"Les bibliothèques suivantes ne sont pas installées : {', '.join(missing_deps)}")
            print("Pour installer toutes les dépendances, exécutez :")
            print("pip install -r requirements.txt")
        
        input("Appuyez sur Entrée pour quitter...")
        os._exit(1)
except ImportError:
    # Si le module de vérification n'existe pas, on continue
    # mais on capturera les erreurs d'import plus tard
    pass

from InquirerPy.utils import color_print
from src.startup import Startup 
from src.utilities.config.app_config import default_config
from src.localization.localization import Localizer

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()

if __name__ == "__main__":
    color_print([("Tomato",f""" _   _____   __   ____  ___  ___   _  ________                
| | / / _ | / /  / __ \\/ _ \\/ _ | / |/ /_  __/__________  ____
| |/ / __ |/ /__/ /_/ / , _/ __ |/    / / / /___/ __/ _ \\/ __/
|___/_/ |_/____/\\____/_/|_/_/ |_/_/|_/ /_/     /_/ / .__/\\__/ 
                                                  /_/ """),("White",f"{default_config['version']}\n")])
    try:
        app = Startup()
    except ModuleNotFoundError as e:
        user32.ShowWindow(hWnd, 1)
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x40|0x100))
        color_print([("Red bold", "Erreur : Bibliothèque Python manquante")])
        color_print([("Yellow", f"La bibliothèque '{e.name}' n'est pas installée.")])
        color_print([("Cyan", "Pour installer toutes les dépendances, exécutez :")])
        color_print([("White", "pip install -r requirements.txt")])
        input(Localizer.get_localized_text("prints","errors","exit") if 'Localizer' in globals() else "Appuyez sur Entrée pour quitter...")
        os._exit(1)
    except:
        user32.ShowWindow(hWnd, 1)
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x40|0x100))
        color_print([("Red bold",Localizer.get_localized_text("prints","errors","error_message"))])
        traceback.print_exc()
        input(Localizer.get_localized_text("prints","errors","exit"))
        os._exit(1)