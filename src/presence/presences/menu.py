from .menu_presences import (default,queue,custom_setup)

def presence(rpc,client=None,data=None,content_data=None,config=None):
    state_types = {
        "DEFAULT": default,
        "MATCHMAKING": queue,
        "CUSTOM_GAME_SETUP": custom_setup,
    }
    
    # Vérifier d'abord si on est dans un match personnalisé (salon)
    # Indicateurs possibles : partyState == "CUSTOM_GAME_SETUP", matchMap présent, customGameTeam présent
    is_custom_game = False
    if data:
        if data.get('partyState') == "CUSTOM_GAME_SETUP":
            is_custom_game = True
        elif data.get('matchMap') or data.get('customGameTeam'):
            # Si on a matchMap ou customGameTeam, on est probablement dans un salon personnalisé
            is_custom_game = True
    
    if is_custom_game:
        custom_setup.presence(rpc,client=client,data=data,content_data=content_data,config=config)
        return
    
    # Check if partyState exists and is valid
    if data and 'partyState' in data and data['partyState'] in state_types.keys():
        state_types[data['partyState']].presence(rpc,client=client,data=data,content_data=content_data,config=config)
    elif data and 'queueId' in data and data.get('queueId'):
        # If we have a queueId, check multiple indicators to determine if we're in queue
        queue_entry_time = data.get('queueEntryTime', "0001.01.01-00.00.00")
        matchmaking_state = data.get('matchmakingState', '')
        is_matchmaking = data.get('isMatchmakingGame', False)
        
        # Check if we're in queue using multiple indicators:
        # - queueEntryTime is valid and not default
        # - matchmakingState indicates we're matchmaking
        # - isMatchmakingGame flag is True
        is_in_queue = (
            (queue_entry_time and queue_entry_time != "0001.01.01-00.00.00") or
            matchmaking_state in ['MATCHMAKING', 'QUEUED', 'SEARCHING'] or
            is_matchmaking
        )
        
        if is_in_queue:
            # We're in queue
            queue.presence(rpc,client=client,data=data,content_data=content_data,config=config)
        else:
            # We're in menu but not in queue
            default.presence(rpc,client=client,data=data,content_data=content_data,config=config)
    elif data:
        # Fallback to default menu presence
        default.presence(rpc,client=client,data=data,content_data=content_data,config=config)