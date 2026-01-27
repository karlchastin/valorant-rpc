# Guide complet : Fork et Release GitHub

Ce document récapitule toutes les étapes nécessaires pour forker un projet, mettre à jour le code, et créer une release sur GitHub.

## Contexte

- Repo original : `colinhartigan/valorant-rpc` (version 3.2.3)
- Fork : `krvntzkl/valorant-rpc`
- Nouvelle version : 3.3.4

## Étape 1 : Forker le projet

1. Aller sur le repo original : https://github.com/colinhartigan/valorant-rpc
2. Cliquer sur "Fork" en haut à droite
3. Choisir ton compte GitHub (`krvntzkl`)
4. Le fork est créé : https://github.com/krvntzkl/valorant-rpc

## Étape 2 : Cloner le fork localement

```powershell
git clone https://github.com/krvntzkl/valorant-rpc.git
cd valorant-rpc
```

## Étape 3 : Modifier le code

- Faire toutes tes modifications dans l'IDE
- Tester que tout fonctionne
- Compiler l'exe si nécessaire (dans `dist/valorant-rpc.exe`)

## Étape 4 : Configurer Git (une seule fois)

```powershell
git config --global user.name "krvntzkl"
git config --global user.email "krvntzkl@users.noreply.github.com"
```

## Étape 5 : Créer un Personal Access Token GitHub

1. Aller sur : https://github.com/settings/tokens
2. Cliquer sur "Generate new token" → "Generate new token (classic)"
3. Donner un nom (ex: "Upload Script")
4. Choisir une durée (90 jours recommandé)
5. **Cocher la permission "repo"** (toutes les permissions)
6. Cliquer sur "Generate token"
7. **COPIER le token immédiatement** (il ne sera plus visible après)

## Étape 6 : Mettre à jour le code sur GitHub

### Option A : Utiliser le script automatique

```powershell
.\update-and-release-FIXED.ps1
```

Le script va :
- Ajouter tous les fichiers
- Créer un commit
- **Force push** vers GitHub (écrase l'ancien code)
- Créer le tag v3.3.4
- Te donner les instructions pour la release

### Option B : Méthode manuelle

```powershell
# Ajouter tous les fichiers
git add -A

# Créer un commit
git commit -m "Update to version 3.3.4 - Bug fixes and improvements"

# Force push (écrase l'ancien code du fork)
git push -f origin main
```

**Important** : Utilise `git push -f` (force) pour écraser l'ancien code du fork avec ta version.

## Étape 7 : Changer la branche par défaut sur GitHub

Si GitHub affiche toujours l'ancien code (branche `v3` au lieu de `main`) :

1. Aller sur : https://github.com/krvntzkl/valorant-rpc/settings
2. Dans la section "Default branch", cliquer sur le bouton de changement
3. Sélectionner `main` comme branche par défaut
4. Cliquer sur "Update" puis confirmer "I understand, update the default branch"

Ou aller directement sur : https://github.com/krvntzkl/valorant-rpc/tree/main

## Étape 8 : Créer le tag

```powershell
# Créer le tag annoté
git tag -a v3.3.4 -m "Release version 3.3.4"

# Push le tag vers GitHub
git push origin v3.3.4
```

## Étape 9 : Créer la release avec l'exe

### Option A : Utiliser le script automatique (recommandé)

```powershell
.\create-release-now.ps1
```

Le script va :
- Vérifier que le tag existe
- Demander ton Personal Access Token
- Créer la release via l'API GitHub avec titre et description
- Uploader l'exe comme asset

### Option B : Via GitHub CLI

Si tu as GitHub CLI installé :

```powershell
gh release create v3.3.4 dist\valorant-rpc.exe --title "v3.3.4" --notes-file release-notes.md
```

### Option C : Méthode manuelle

1. Aller sur : https://github.com/krvntzkl/valorant-rpc/releases/new
2. Sélectionner le tag : `v3.3.4`
3. Titre : `v3.3.4`
4. Description : Copier-coller les notes de release (voir ci-dessous)
5. Uploadez le fichier : `dist\valorant-rpc.exe`
6. Cliquer sur "Publish release"

## Notes de release pour v3.3.4

```
## Version 3.3.4 - Bug Fixes and Improvements

### Bug Fixes
- Fixed KeyError 'sessionLoopState': added checks to handle the absence of this key in presence data
- Fixed KeyError 'partyAccessibility': replaced direct accesses with .get() and default values in build_party_state()
- Fixed AttributeError 'systray': added hasattr() checks before calling systray.exit() in startup.py
- Fixed small_text error: ensured small_text is at least 2 characters long before sending to Discord
- Fixed SyntaxWarning: corrected invalid escape sequences in the ASCII art in main.py
- Fixed session loops: Game_Session and Range_Session no longer depend on sessionLoopState and now directly verify the game's state
- Fixed indentation errors in startup.py and presence.py

### Improvements
- Improved menu/in-game detection: coregame_fetch_player() is now checked to detect the in-game state before assuming the menu
- Improved build.bat with error handling, informative messages, and use of the .spec file
- Immediate presence update: ingame.presence() now updates presence instantly with basic information before the detailed loop
- KeyError protection: use of .get() with default values across all presence functions (default, queue, away, custom_setup)
- Added default values: added defaults for partyAccessibility, partySize, maxPartySize, accountLevel, partyId, etc.
- Created missing init.py files in all packages for PyInstaller compatibility
- Configured valorant-rpc.spec with automatic submodule collection, asset inclusion, and collection of pystray/PIL

### Content Updates
- Updated version to 3.3.4 in app_config.py and version.py
- Updated GitHub URLs to the fork krvntzkl/valorant-rpc in version_checker.py and startup.py
- Added support for agents: Harbour, Gekko, Deadlock, Iso, Clove, Vyse, Tejo, Waylay and Veto
- Added support for maps: Abyss and Corrode

### Installation
Download `valorant-rpc.exe` from the assets below and run it.
```

## Problèmes courants et solutions

### Le code ne se met pas à jour sur GitHub

**Cause** : GitHub affiche une autre branche par défaut (ex: `v3`)

**Solution** :
1. Vérifier que tu as bien pushé sur `main` : `git push -f origin main`
2. Changer la branche par défaut dans les settings du repo
3. Ou aller directement sur : https://github.com/krvntzkl/valorant-rpc/tree/main

### La release n'a pas l'exe

**Cause** : Seul le tag a été créé, pas la vraie release

**Solution** : Utiliser le script `create-release-now.ps1` qui crée la release via l'API avec l'exe

### Erreur d'authentification lors du push

**Cause** : Token incorrect ou expiré

**Solution** :
1. Vérifier que le token a la permission `repo`
2. Créer un nouveau token si nécessaire
3. Utiliser le token comme mot de passe (pas ton mot de passe GitHub)

### Les fichiers .ps1 apparaissent dans le repo

**Cause** : Ils ont été commités avant d'être ajoutés au `.gitignore`

**Solution** :
```powershell
# Retirer du tracking
git rm --cached *.ps1

# Ajouter le .gitignore modifié
git add .gitignore

# Commit
git commit -m "Remove PowerShell scripts from tracking"

# Push
git push origin main
```

Le `.gitignore` contient déjà `*.ps1`, donc ils ne seront plus trackés à l'avenir.

## Checklist finale

- [ ] Fork créé sur GitHub
- [ ] Code modifié localement
- [ ] Git configuré (user.name et user.email)
- [ ] Personal Access Token créé avec permission `repo`
- [ ] Code pushé sur GitHub (force push si nécessaire)
- [ ] Branche par défaut changée vers `main` si nécessaire
- [ ] Tag v3.3.4 créé et pushé
- [ ] Release créée avec titre, description et exe
- [ ] Vérification que tout est correct sur GitHub

## Scripts disponibles

- `update-and-release.ps1` : Version simple (push normal)
- `update-and-release-FIXED.ps1` : Version avec force push (recommandé pour fork)
- `create-release-now.ps1` : Crée la release avec l'exe via l'API GitHub

**Note** : Les scripts `.ps1` sont ignorés par Git (dans `.gitignore`), donc ils ne seront pas uploadés sur GitHub.

