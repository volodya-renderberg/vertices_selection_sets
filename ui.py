# -*- coding: utf-8 -*-

import bpy

from . import write_read_data as wr

class G(object):
    list_of_sets = []
    
class SELECTIONSETS_panel(bpy.types.Panel):
    bl_idname = "face_rig.tools_panel"
    bl_label = "Selection Sets"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
    layout = 'Selection Sets'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.list_of_sets=wr.reload_list_of_sets()
        layout = self.layout
        layout.label("Selection Sets")
        col = layout.column(align=1)
        for item in self.list_of_sets:
            col.label(item)
        col.operator("selection_sets.create", text = 'create')
        col.operator("selection_sets.set", text = 'add').mode='ADD'
        col.operator("selection_sets.set", text = 'replace').mode='REPLACE'
        
class SELECTIONSETS_create(bpy.types.Operator):
    bl_idname = "selection_sets.create"
    bl_label = "create"

    def execute(self, context):
        wr.create()
        self.report({'INFO'}, 'create set')
        return{'FINISHED'}
    
class SELECTIONSETS_set(bpy.types.Operator):
    bl_idname = "selection_sets.set"
    bl_label = "set"
    mode = bpy.props.StringProperty()

    def execute(self, context):
        wr.set(mode=self.mode)
        self.report({'INFO'}, self.mode)
        return{'FINISHED'}

def register():
    bpy.utils.register_class(SELECTIONSETS_panel)
    bpy.utils.register_class(SELECTIONSETS_create)
    bpy.utils.register_class(SELECTIONSETS_set)

def unregister():
    bpy.utils.unregister_class(SELECTIONSETS_panel)
    bpy.utils.unregister_class(SELECTIONSETS_create)
    bpy.utils.unregister_class(SELECTIONSETS_set)
