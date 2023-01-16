from typing import List, TypedDict

class Match_Follow(TypedDict):
    message_id: int
    match_id: int

class User(TypedDict):
    chat_id: int
    supports_team: int
    following: List[Match_Follow]


