import bpy, bmesh
import random, math
context = bpy.context

'''
set complex poly to 1 in order to get more than 8 tris per face
set it to 0 to get simple repeating 8 tris per face

enable with extra_twist = 1 that introduce extra twist on Y axis to introduce more depth

block equals to the number of block generate at once

dis refers to the displacement range that create the lowpoly effect

x_dis enables  x-axis displacement when set to 1
y_dis ^
z dis ^

'''
complex_poly = 0
extra_twist = 1

block = 2

dis = 0.18
x_dis = 1
y_dis = 0
z_dis = 1
z_modifier = 0.5

for i in range(block):
    #add mesh and create group
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, i*2, 1))
    obj = context.object
    me = obj.data
    vg0 = bpy.ops.object.vertex_group_add()
    #vg0.name = 'deform'
    
    # decide if user wants complex or repeating texture
    if(complex_poly == 0):
        bpy.ops.object.mode_set(mode='EDIT')
        mesh = bmesh.from_edit_mesh(obj.data)
        
        bpy.ops.mesh.subdivide()
        bpy.ops.mesh.select_all(action = 'DESELECT')
        for i in range(0, 8):
            mesh.verts.ensure_lookup_table()
            mesh.verts[i].select = True
        bpy.ops.object.vertex_group_add()
        bpy.ops.object.vertex_group_assign()
        bpy.ops.mesh.select_all(action = 'DESELECT')

        # primed for lowpoly effect      
        for j in mesh.verts:
            j.select = True
            t_mod_x = 0
            t_mod_y = 0
            t_mod_z = 0
            
            if(x_dis == 1):
                while t_mod_x < 0.04 and t_mod_x > -0.04:
                    t_mod_x = random.uniform(-dis, dis)
            if(y_dis == 1):
                while t_mod_y < 0.04 and t_mod_y > -0.04:
                    t_mod_y = random.uniform(-dis, dis)
            if(z_dis == 1):
                while t_mod_z < 0.04 and t_mod_z > -0.04:
                    t_mod_z = random.uniform(-dis, dis) * z_modifier
            
            bpy.ops.transform.translate(value=(t_mod_x, t_mod_y , t_mod_z), \
                                        orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), \
                                        orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, \
                                        use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, \
                                        use_proportional_connected=False, use_proportional_projected=False)
            j.select = False
        
        #finishing touch
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Triangulate")
        
        # introduce extra twist to add more shades
        if(extra_twist == 1):
            bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
            deg = random.randrange(-3, 3)
            rad = math.radians(deg)
            bpy.context.object.modifiers["SimpleDeform"].angle = rad
            bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Y'
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform")

        
        
    elif(complex_poly == 1):
        #subdivide
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.subdivide()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #selecting vertex group
        for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
            g.select = False
        
        for i in range(21,26):
            me.vertices[i].select = True
            
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        
        #subdide again primed for lowpoly effect
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.subdivide()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #decimate and triangulate
        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].ratio = random.uniform(0.25, 0.86)
        bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")
        
        #displace to achieve final effect
        bpy.ops.object.modifier_add(type='DISPLACE')
        bpy.context.object.modifiers["Displace"].vertex_group = "Group"
        bpy.context.object.modifiers["Displace"].mid_level = 0.6
        dis_mod = 0
        while (dis_mod < 0.15 and dis_mod > -0.15):
            dis_mod = random.uniform(-dis*2, dis*2)
        bpy.context.object.modifiers["Displace"].strength = dis_mod
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace")
        
        if(extra_twist == 1):
            bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
            deg = random.randrange(-3, 3)
            rad = math.radians(deg)
            bpy.context.object.modifiers["SimpleDeform"].angle = rad
            bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Y'
    
    

