"""
Utility functions.
"""


def distance(p1=(0, 0), p2=(0, 0)):
    """
    Returns the distance between two points.
    """
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5