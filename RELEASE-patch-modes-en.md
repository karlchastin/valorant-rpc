# Patch notes – Skirmish & All Random One Site fixes

### Skirmish (2v2 Escarmouche)

* **Mode detection**: Mode is now correctly detected (API sends queueId `skirmish2v2`). Presence shows "Skirmish" / "Escarmouche" instead of "Custom" in menu and in-game.
* **Score tracking**: Score is read from presence root, then from `partyPresenceData` and `matchPresenceData` as fallback. In Skirmish, rounds are very fast; a slight score delay may remain depending on presence refresh interval.
* **In-game display**: When map data is missing, agent is shown as large image without errors.

### All Random One Site (valaram)

* **Issue**: Valorant API (match, loadouts, presence) does not provide the current round’s agent in All Random One Site; only the first round’s agent is available.
* **Change**: For All Random One Site (`valaram`), we no longer show the agent. Instead we show the **mode name** and **mode icon** (as in menu) whenever the user’s config preference is "agent" for large or small image.
* In-game, instead of a stuck (wrong) agent, presence shows e.g. "All Random One Site" with the mode icon. Applied from match start and on every refresh.

### Related fixes

* **Custom setup (party room)**: Fixed `KeyError: 'MapID'` when map was missing or only in `partyPresenceData` / `matchPresenceData`. Map is now read from `matchMap` and `partyOwnerMatchMap` in nested objects.
* **fetch_map_data**: Uses `.get("MapID", "")` to avoid KeyError when data is incomplete.
