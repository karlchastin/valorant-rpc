#!/bin/bash

echo "========================================"
echo "Installation des dépendances pour valorant-rpc"
echo "========================================"
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "ERREUR: Python 3 n'est pas installé"
    echo "Veuillez installer Python 3 depuis https://www.python.org/"
    exit 1
fi

echo "Mise à jour de pip..."
python3 -m pip install --upgrade pip

echo ""
echo "Installation des dépendances depuis requirements.txt..."
python3 -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERREUR: L'installation a échoué"
    exit 1
fi

echo ""
echo "========================================"
echo "Installation terminée avec succès!"
echo "========================================"
echo ""
