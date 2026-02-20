# Correctifs modes Escarmouche (Skirmish 2v2) et All Random One Site

### Escarmouche (Skirmish 2v2)

* **Détection du mode** : le mode est maintenant reconnu correctement (queueId `skirmish2v2` envoyé par l’API). La présence affiche « Escarmouche » / « Skirmish » au lieu de « Custom » en menu et en partie.
* **Suivi du score** : le score est lu depuis la racine de la présence, puis en repli depuis `partyPresenceData` et `matchPresenceData`, comme pour les autres champs. En Escarmouche les rounds sont très rapides ; un léger décalage peut rester normal selon l’intervalle de rafraîchissement de la présence.
* **Affichage en partie** : lorsque la carte n’est pas disponible dans les données, l’agent est affiché en grand (grande image) sans erreur.

### All Random One Site (valaram)

* **Constat** : l’API Valorant (match, loadouts, présence) ne fournit pas l’agent du round en cours en All Random One Site. On ne dispose que de l’agent du 1er round.
* **Changement** : pour le mode All Random One Site (`valaram`), on n’affiche plus l’agent. À la place, on affiche le **nom du mode** et l’**icône du mode** (comme au menu) dès que la préférence config est « agent » pour la grande ou la petite image.
* En jeu, au lieu d’un agent figé (faux), la présence affiche par exemple « All Random One Site » avec l’icône du mode. C’est appliqué dès le début de la partie et à chaque refresh.

### Autres correctifs liés

* **Custom setup (salon)** : correction du crash `KeyError: 'MapID'` lorsque la carte est absente ou dans `partyPresenceData` / `matchPresenceData`. Lecture de `matchMap` et `partyOwnerMatchMap` dans les objets imbriqués.
* **fetch_map_data** : utilisation de `MapID` via `.get()` pour éviter toute KeyError si les données sont incomplètes.
