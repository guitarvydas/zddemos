import sys
sys.path.insert(0, '../zd')
import kernel0d as zd

# define template
def Hello_install (reg):
    zd.register_component (reg, zd.mkTemplate ("Hello", None, Hello_instantiate))

# create an instance of the template
def Hello_instantiate (reg,owner,name,template_data):
    name_with_id = zd.gensymbol ( "Hello")
    return zd.make_leaf ( name_with_id, owner, None, Hello_handler)

# handler for any instance
def Hello_handler (eh,mev):
    zd.send_string (eh, "", "Hello", mev)

