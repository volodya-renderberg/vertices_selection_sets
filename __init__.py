#
#
#
#

bl_info = {
    "name": "Vertices selection sets",
    "description": "Creating and using vertex selection sets. In some way analogous to the May selection sets.",
    "author": "Volodya Renderberg",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "View3d tools panel",
    "warning": "", # used for warning icon and text in addons panel
    "category": "Rigging"}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    from . import ui

import bpy


##### REGISTER #####

def register():
    ui.register()

def unregister():
    ui.unregister()

if __name__ == "__main__":
    register()

