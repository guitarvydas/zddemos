import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

from fivetimes import FiveTimes_install

[palette, env] = zd.initialize ()
FiveTimes_install (palette)
zd.start (palette, env)

