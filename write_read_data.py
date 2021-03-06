import bpy
#from bpy.app.handlers import persistent

import numpy as np
import json

TEXTS_NAME = 'vertices_selection_sets_data'

modes = {
    'EDIT_MESH':'EDIT',
    'PAINT_WEIGHT':'WEIGHT_PAINT',
    }

def create(name='set1'):
    #get data
    ob = bpy.context.object
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.mode_set(mode = 'EDIT')
    count = len(ob.data.vertices)
    sel = np.zeros(count, dtype=np.bool)
    ob.data.vertices.foreach_get('select', sel)
    #write data
    #print(sel)
    write_set(name, sel)

def set_set(mode='REPLACE', name='set1'):
    #read data
    sel = read_set(name)
    #print(sel)
    #set data
    ob = bpy.context.object
    current_mode = bpy.context.mode
    if current_mode in modes:
        current_mode = modes[current_mode]
    #
    if mode=='ADD':
        bpy.ops.object.mode_set(mode = 'OBJECT')
        ob.data.vertices.foreach_set('select', sel)
        #bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = current_mode)
    elif mode=='REPLACE':
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        ob.data.vertices.foreach_set('select', sel)
        #bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = current_mode)
    elif mode=='SUBTR':
        #get current select
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.mode_set(mode = 'EDIT')
        count = len(ob.data.vertices)
        current_select = np.zeros(count, dtype=np.bool)
        ob.data.vertices.foreach_get('select', current_select)
        required = current_select - sel
        # set select
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        ob.data.vertices.foreach_set('select', required)
        #bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = current_mode)


def write_set(name, data):
    if not TEXTS_NAME in bpy.data.texts:
        text = bpy.data.texts.new(TEXTS_NAME)
        data_dict={}
    else:
        text = bpy.data.texts[TEXTS_NAME]
        if text.as_string():
            data_dict = json.loads(text.as_string())
        else:
            data_dict={}
        
    data_dict[name]=data.tolist()
    text.from_string(json.dumps(data_dict, sort_keys=True, indent=4))

def read_set(name):
    if not TEXTS_NAME in bpy.data.texts:
        return(False)
    text = bpy.data.texts[TEXTS_NAME]
    if text.as_string():
        data_dict = json.loads(text.as_string())
        if not name in data_dict:
            return(False)
        else:
            data_list = data_dict[name]
            data=np.asarray(data_list)
            return(data)
    else:
        return(False)

def reload_list_of_sets():
    if not TEXTS_NAME in bpy.data.texts:
        list_of_sets=[]
    else:
        text = bpy.data.texts[TEXTS_NAME]
        if not text.as_string():
            list_of_sets=[]
        else:
            list_of_sets=json.loads(text.as_string()).keys()
    return(list_of_sets)

def delete(name):
    if not TEXTS_NAME in bpy.data.texts:
        return
    else:
        text = bpy.data.texts[TEXTS_NAME]
    if not text.as_string():
        return
    else:
        data_dict = json.loads(text.as_string())
        del data_dict[name]
        text.from_string(json.dumps(data_dict, sort_keys=True, indent=4))
