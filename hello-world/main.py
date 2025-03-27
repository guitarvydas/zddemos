import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

from hello import Hello_install
from world import World_install
from cruel import Cruel_install
    
[palette, env] = zd.initialize ()
Hello_install (palette)
World_install (palette)
Cruel_install (palette)
zd.start (palette, env)

