import bpy
import numpy as np
import json

TEXTS_NAME = 'selected_sets'

def get(name='set1'):
    #get data
    ob = bpy.context.object
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.mode_set(mode = 'EDIT')
    count = len(ob.data.vertices)
    sel = np.zeros(count, dtype=np.bool)
    ob.data.vertices.foreach_get('select', sel)
    #write data
    print(sel)
    write_set(name, sel)
    
def set(name='set1', mode='REPLACE'):
    #read data
    sel = read_set(name)
    print(sel)
    #set data
    ob = bpy.context.object
    if mode=='ADD':
        bpy.ops.object.mode_set(mode = 'OBJECT')
        ob.data.vertices.foreach_set('select', sel)
        bpy.ops.object.mode_set(mode = 'EDIT')
    elif mode=='REPLACE':
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        ob.data.vertices.foreach_set('select', sel)
        bpy.ops.object.mode_set(mode = 'EDIT')


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

#get()
set()

#print(read_set('set1'))