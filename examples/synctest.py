#!/usr/bin/env python3
"""

"""

import time
import tldevicesync
rpc = [['vector.data.decimation', 'i32', '5']]
tio = tldevicesync.DeviceSync(connectionTime=5, rpcs=rpc)

streams = []
streams += [tio.vmr0.vector]
# streams += [tio.vmr0.accel]
streams += [tio.vmr1.accel]
ss = tldevicesync.SyncStream(streams)

for row in ss.iter():
  print(row)
  time.sleep(1)