import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

from once import Once_install

[palette, env] = zd.initialize ()
Once_install (palette)
zd.start (palette, env)

