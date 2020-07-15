#!/usr/bin/env python3
"""

"""

import time
import tldevicesync
import sys
import blessings

def get(d, keys):
    if "." in keys:
        key, rest = keys.split(".", 1)
        return get(d[key], rest)
    else:
        return d[keys]

rpc = [
  ['vector.data.decimation', 'i32', '10'],
  ['accel.data.decimation', 'i32', '1'],
  ['gyro.data.decimation', 'i32', '1'],
  ['bar.data.decimation', 'i32', '1'],
  ['therm.data.decimation', 'i32', '2']
  ]
tio = tldevicesync.DeviceSync(connectionTime=5, rpcs=rpc)

streams = []
streams += [tio.vmr0]
# streams += [tio.vmr0.accel]
streams += [tio.vmr1]
ss = tldevicesync.SyncStream(streams)
    
term = blessings.Terminal()
lastSample = None
fields = ['vector.x', 'vector.y', 'vector.z', 'accel.x', 'accel.y', 'accel.z', 'gyro.x', 'gyro.y', 'gyro.z', 'bar', 'therm']
for row in ss.iter():
  for name, device in row.items():
    sys.stdout.write(f"\r\n{term.clear_eol}{name}")
    for field in fields:
      data = get(device, field)
      sys.stdout.write(f"\r\n {field}: {data or ''}")

  sys.stdout.write(term.clear_eos)
  sys.stdout.write(term.move_up*(len(row)*(len(fields)+1)))
