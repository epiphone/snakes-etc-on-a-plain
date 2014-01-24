"""
Everything map-related.
"""

from player import Player
from map_objs import Tile


map1 = """


p
xxxx   xxx
    xxx

"""

map_obj_mapping = {
    'p': Player,
    'x': Tile
}

def parse_map(map_str):
    lines = [part for part in map_str.split('\n') if part]
    max_line_len = len(max(lines, key=len))
    lines = [line + ' '*(max_line_len - len(part)) for line in lines]


