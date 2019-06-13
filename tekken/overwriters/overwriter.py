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

from abc import ABC, abstractmethod
import struct
import win32.kernel32 as kernel32
import win32.utils.type_limits as type_limits

class Overwriter(ABC):
    def __init__(self, enable, process_memory, value):
        self.enable = enable
        self.process_memory = process_memory
        self.value = value

    @abstractmethod
    def write(self):
        pass

    def update(self):
        if self.enable:
            self.write()

    def _read_address(self, process_handle, address):
        try:
            memory_value = kernel32.read_process_memory(
                process_handle, address, type_limits.get_size(self.value)
            )
            return struct.unpack(
                type_limits.get_struct_format(self.value), memory_value
            )[0]
        except (OSError, struct.error):
            kernel32.close_handle(process_handle)
            raise

    def __repr__(self):
        return 'enable: {}, process_memory: [{}], value: {}'.format(
            self.enable, repr(self.process_memory), self.value
        )
