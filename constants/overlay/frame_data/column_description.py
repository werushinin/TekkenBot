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

"""
"""
from constants.complex_enum import ComplexEnum, ComplexEnumMember

class ColumnsDescription(ComplexEnum):
    INPUT_COMMAND = ComplexEnumMember(0, printable_name='input command')
    MOVE_ID = ComplexEnumMember(1, printable_name='internal move id number')
    MOVE_NAME = ComplexEnumMember(2, printable_name='internal move name')
    ATTACK_TYPE = ComplexEnumMember(3, printable_name='attack type')
    STARTUP_FRAMES = ComplexEnumMember(4, printable_name='startup frames')
    ON_BLOCK_FRAMES = ComplexEnumMember(
        5, printable_name='frame advantage on block'
    )
    ON_HIT_FRAMES = ComplexEnumMember(
        6, printable_name='frame advantage on hit'
    )
    COUNTER_HIT_FRAMES = ComplexEnumMember(
        7, printable_name='frame advantage on counter hit'
    )
    ACTIVE_FRAMES = ComplexEnumMember(
        8, printable_name='active frame connected on/total active frames'
    )
    TRACKING = ComplexEnumMember(
        9, printable_name='how well move tracks during startup'
    )
    TOTAL_FRAMES = ComplexEnumMember(
        10, printable_name='total number of frames in move'
    )
    REACTION_FRAMES = ComplexEnumMember(
        11, printable_name='frames before attacker can act'
    )
    OPPONET_FRAMES = ComplexEnumMember(
        12, printable_name='frames before defender can act'
    )
    NOTES = ComplexEnumMember(13, printable_name='additional move properties')