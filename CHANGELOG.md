## Version 3.3.5 - Bug Fixes and Improvements

### Bug Fixes

- Fixed queue detection: improved queue state detection with multiple indicators (`matchmakingState`, `isMatchmakingGame`, `queueEntryTime`) to adapt to Valorant API changes

- Fixed pregame agent display: presence now correctly displays the selected agent during agent selection phase instead of showing "queue". Pregame state detection is now explicitly verified via `pregame_fetch_player()`

- Fixed account level display: account level is now correctly retrieved via `fetch_account_xp()` and `fetch_player_loadout()` instead of relying solely on presence data. No more "Level 0" display in menus

- Fixed dependency errors: added automatic Python library verification at startup with clear error messages and installation instructions for new users

- Fixed custom game detection: improved detection of custom game lobbies (party rooms) with multiple indicators (`partyState`, `matchMap`, `customGameTeam`)

### Improvements

- Improved state detection logic: explicit pregame state verification before other states to avoid conflicts

- New `fetch_account_level()` method: robust method that tries multiple sources to retrieve account level (presence data, client API with `fetch_account_xp()` and `fetch_player_loadout()`)

- Added account level caching: global cache to avoid repeated API calls for account level retrieval

- Improved error messages: clearer and more informative messages when Python libraries are missing

- Enhanced queue detection: multiple fallback indicators to ensure queue state is properly detected even when `partyState` is not set to "MATCHMAKING"

### Installation

Download valorant-rpc.exe from the assets below and run it

If you encounter missing dependency errors, run:
```
pip install -r requirements.txt
```

---

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

- Created missing __init__.py files in all packages for PyInstaller compatibility

- Configured valorant-rpc.spec with automatic submodule collection, asset inclusion, and collection of pystray/PIL

### Content Updates

- Updated version to 3.3.4 in app_config.py and version.py

- Updated GitHub URLs to the fork krvntzkl/valorant-rpc in version_checker.py and startup.py

- Added support for agents: Harbor, Gekko, Deadlock, Iso, Clove, Vyse, Tejo, Waylay and Veto

- Added support for maps: Abyss and Corrode

### Installation

Download valorant-rpc.exe from the assets below and run it

