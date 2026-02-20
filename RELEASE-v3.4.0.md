# January 2026 (Valorant 12.03+)

## Version 3.4.0 - Presence improvements and new modes

### New features

* **Queue detection**: status now correctly shows "In queue - [mode]" when you start matchmaking. Reads fields from `partyPresenceData` / `matchPresenceData` (queueEntryTime, partyState, etc.)
* **Replay detection**: when watching a replay, presence displays "Watching a replay" (detection via `sessionLoopState` / `partyOwnerSessionLoopState` = REPLAY in menu)
* **In-game detail separator**: in-game detail now uses "•" instead of "//" (e.g. `Competitive • 5 - 3`)
* **Skirmish (2v2) and All Random One Site modes**: support in queue_aliases and locales for mode name display

### Bug fixes

* Fixed queue and replay presence: use of nested API structure (`partyPresenceData`, `matchPresenceData`) for all related fields
* Fixed queue entry time: `queue.py` now reads `queueEntryTime` from `partyPresenceData` for queue start time

### Installation

Download valorant-rpc.exe from the assets below and run it

If you encounter missing dependency errors, run:

```
pip install -r requirements.txt
```
