""" Game fix for The Legend of Heroes: Trails in the Sky
"""
#pylint: disable=C0103

from protonfixes import util


def main():
    """ Install directshow and xvid for videos
    """

    util.protontricks("directshow")
    util.protontricks("lav_filters")

    # Allows SoraVoice mod to be injected
    util.winedll_override('dinput8', 'n,b')
    util.winedll_override('dsound', 'n,b')
