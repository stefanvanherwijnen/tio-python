"""
..
    Copyright: 2017 Twinleaf LLC
    Author: kornack@twinleaf.com
    OriginalDate: November 2017
"""

import tio

class TwinleafDataController(object):
  def __init__(self, dev):
    self._dev = dev
    self.dstream = self._dev._tio.dstream_read_raw

  def dstream_iter(self, number=0):
    if number==0:
      while True:
        yield self._dev._tio.dstream_read_raw(rows = 1, duration=None)
    else:
      for x in range(number):
        yield self._dev._tio.dstream_read_raw(rows = 1, duration=None)

