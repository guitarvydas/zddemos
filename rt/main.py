import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

[palette, env] = zd.initialize ()
zd.start (palette, env)

