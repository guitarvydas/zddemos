import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

# define template
def FiveTimes_install (reg):
    zd.register_component (reg, zd.mkTemplate ("Five Times", None, FiveTimes_instantiate))

class FiveTimes_counter:
    def __init__ (self):
        self.counter = 0
    
# create an instance of the template
def FiveTimes_instantiate (reg,owner,name,template_data):
    name_with_id = zd.gensymbol ("FiveTimes")
    return zd.make_leaf ( name_with_id, owner, FiveTimes_counter (), FiveTimes_handler)

# handler for any instance
def FiveTimes_handler (eh,mev):
    inst =  eh.instance_data
    if inst.counter < 5:
        zd.send_string (eh, "", "Why?", mev)
        inst.counter += 1

