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
        col.operator("selection_sets.create", text = 'create')
        for item in sorted(self.list_of_sets):
            row = col.row(align = True)
            row.label(item)
            row.operator("selection_sets.set", text = 'add').data='ADD.%s' % item
            row.operator("selection_sets.set", text = 'replace').data='REPLACE.%s' % item
            row.operator("selection_sets.set", text = 'sub').data='SUBTR.%s' % item
            row.operator("selection_sets.delete", text = 'del').name=item
        
class SELECTIONSETS_create(bpy.types.Operator):
    bl_idname = "selection_sets.create"
    bl_label = "create"
    
    name_of_set = bpy.props.StringProperty(name="Name:")

    def execute(self, context):
        wr.create(name=self.name_of_set)
        self.report({'INFO'}, 'create set: %s' % self.name_of_set)
        return{'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class SELECTIONSETS_set(bpy.types.Operator):
    bl_idname = "selection_sets.set"
    bl_label = "set"
    data = bpy.props.StringProperty()

    def execute(self, context):
        tmode = self.data.split('.')[0]
        name = self.data.replace('%s.' % tmode, '')
        wr.set_set(mode=tmode, name=name)
        self.report({'INFO'}, '%s - %s' % (name, tmode))
        return{'FINISHED'}

class SELECTIONSETS_delete(bpy.types.Operator):
    bl_idname = "selection_sets.delete"
    bl_label = "delete"
    name = bpy.props.StringProperty()

    def execute(self, context):
        wr.delete(self.name)
        self.report({'INFO'}, 'set removed : %s' % self.name)
        return{'FINISHED'}

def register():
    bpy.utils.register_class(SELECTIONSETS_panel)
    bpy.utils.register_class(SELECTIONSETS_create)
    bpy.utils.register_class(SELECTIONSETS_set)
    bpy.utils.register_class(SELECTIONSETS_delete)

def unregister():
    bpy.utils.unregister_class(SELECTIONSETS_panel)
    bpy.utils.unregister_class(SELECTIONSETS_create)
    bpy.utils.unregister_class(SELECTIONSETS_set)
    bpy.utils.register_class(SELECTIONSETS_delete)
