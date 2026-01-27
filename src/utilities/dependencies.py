import sys
import subprocess
import os

REQUIRED_PACKAGES = [
    'urllib3',
    'iso8601',
    'flask_cors',  # Flask_Cors s'importe comme flask_cors
    'requests',
    'pypresence',
    'valclient',
    'pystray',
    'pyperclip',
    'cursor',
    'psutil',
    'flask',  # Flask s'importe comme flask
    'InquirerPy',
    'PIL',  # Pillow s'importe comme PIL
    'websockets',
]

# Mapping des noms d'import vers les noms de paquets pip
PACKAGE_MAPPING = {
    'flask_cors': 'Flask_Cors',
    'flask': 'Flask',
    'PIL': 'Pillow',
}

def check_dependencies():
    """Vérifie si toutes les dépendances sont installées."""
    missing = []
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            # Utiliser le nom du paquet pip si différent
            pip_name = PACKAGE_MAPPING.get(package, package)
            missing.append(pip_name)
    
    return missing

def install_dependencies():
    """Installe les dépendances manquantes depuis requirements.txt."""
    requirements_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt")
    if not os.path.exists(requirements_path):
        return False
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False

def verify_and_install():
    """Vérifie et installe les dépendances si nécessaire."""
    missing = check_dependencies()
    if missing:
        return False, missing
    return True, []
