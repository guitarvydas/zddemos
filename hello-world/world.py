import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

# define template
def World_install (reg):
    zd.register_component (reg, zd.mkTemplate ("World", None, World_instantiate))

# create an instance of the template
def World_instantiate (reg,owner,name,template_data):
    name_with_id = zd.gensymbol ( "World")
    return zd.make_leaf ( name_with_id, owner, None, World_handler)

# handler for any instance
def World_handler (eh,mev):
    zd.send_string (eh, "", "World", mev)

