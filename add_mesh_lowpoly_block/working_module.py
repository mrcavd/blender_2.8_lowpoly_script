import bpy, bmesh
import random, math

def add_mesh(dis, x, y, z):

    #add mesh and create group
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 1))
    obj = bpy.context.object
    me = obj.data
    bpy.ops.object.mode_set(mode='EDIT')
    mesh = bmesh.from_edit_mesh(obj.data)
    
    bpy.ops.mesh.subdivide()
    bpy.ops.mesh.select_all(action = 'DESELECT')
    
    # primed for lowpoly effect      
    for j in mesh.verts:
        j.select = True
        t_mod_x = 0
        t_mod_y = 0
        t_mod_z = 0
    
        if(x == 1):
            while t_mod_x < 0.04 and t_mod_x > -0.04:
                t_mod_x = random.uniform(-dis, dis)
        if(y == 1):
            while t_mod_y < 0.04 and t_mod_y > -0.04:
                t_mod_y = random.uniform(-dis, dis)
        if(z == 1):
            while t_mod_z < 0.04 and t_mod_z > -0.04:
                t_mod_z = random.uniform(-dis, dis)
        bpy.ops.transform.translate(value=(t_mod_x, t_mod_y , t_mod_z*0.5), \
                                    orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), \
                                    orient_matrix_type='GLOBAL', mirror=True, \
                                    use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, \
                                    use_proportional_connected=False, use_proportional_projected=False)
        j.select = False
       
    #finishing touch
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Triangulate")
    
add_mesh(0.18, 1, 1, 1)