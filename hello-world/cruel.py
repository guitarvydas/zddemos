import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

# define template
def Cruel_install (reg):
    zd.register_component (reg, zd.mkTemplate ("Cruel", None, Cruel_instantiate))

# create an instance of the template
def Cruel_instantiate (reg,owner,name,template_data):
    name_with_id = zd.gensymbol ( "Cruel")
    return zd.make_leaf ( name_with_id, owner, None, Cruel_handler)

# handler for any instance
def Cruel_handler (eh,mev):
    zd.send_string (eh, "", "Cruel", mev)

