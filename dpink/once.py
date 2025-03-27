import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

# define template
def Once_install (reg):
    zd.register_component (reg, zd.mkTemplate ("Once", None, Once_instantiate))

class Once_counter:
    def __init__ (self):
        self.counter = 0
    
# create an instance of the template
def Once_instantiate (reg,owner,name,template_data):
    name_with_id = zd.gensymbol ("Once")
    return zd.make_leaf ( name_with_id, owner, Once_counter (), Once_handler)

# handler for any instance
def Once_handler (eh,mev):
    inst =  eh.instance_data
    if inst.counter < 1:
        zd.send_string (eh, "", "Why?", mev)
        inst.counter += 1

