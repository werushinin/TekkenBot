#!/usr/bin/env python3

# Copyright (c) 2019, Alchemy Meister
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import enum

class MainMenus(enum.IntEnum):
    NULL = 0
    STORY = 1
    ONLINE = 2
    ARCADE = 3
    TREASURE = 4
    VERSUS = 5
    PRACTICE = 6
    MY_REPLAYS_AND_TIPS = 8
    CHARACTER_CUSTOMIZATION = 9
    PLAYER_CUSTOMIZATION = 10
    GALLERY = 12
    GAME_OPTIONS = 13
    SOUND_OPTIONS = 14
    DISPLAY_SETTINGS = 15
    GRAPHIC_SETTINGS = 16
    CONTROLLER_SETUP = 17
    BUTTON_MAPPING = 18
    COPYRIGHT = 19
    CREDITS = 20
    PLAYER_INFORMATION = 21
    STORE = 22
    ULTIMATE_TEKKEN_BOWL = 28
    EXIT = 30
