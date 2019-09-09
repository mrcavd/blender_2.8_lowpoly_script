import bpy, bmesh
import random, math
from bpy.props import (IntProperty, BoolProperty, FloatProperty)


def add_mesh(self, context):

	#add mesh and create group
	bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 1))
	obj = context.object
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

		# hard coded z_modifier
		# to optimize viewing on YZ plane
		z_modifier = 0.5
	
		if(self.x == 1):
			while t_mod_x < 0.04 and t_mod_x > -0.04:
				t_mod_x = random.uniform(-self.dis, self.dis)
		if(self.y == 1):
			while t_mod_y < 0.04 and t_mod_y > -0.04:
				t_mod_y = random.uniform(-self.dis, self.dis)
		if(self.z == 1):
			while t_mod_z < 0.04 and t_mod_z > -0.04:
				t_mod_z = random.uniform(-self.dis, self.dis)
		bpy.ops.transform.translate(value=(t_mod_x, t_mod_y , t_mod_z*z_modifier), \
									orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), \
									orient_matrix_type='GLOBAL', mirror=True, \
									use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, \
									use_proportional_connected=False, use_proportional_projected=False)
		j.select = False
       
    #finishing touch
	bpy.ops.object.mode_set(mode = 'OBJECT')
	bpy.ops.object.modifier_add(type='TRIANGULATE')
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Triangulate")
	
	#return {'FINISHED'}

	

class AddLowPolyBlock(bpy.types.Operator):
	bl_idname = "mesh.simple_low_poly_block_add"
	bl_label = "Add Simple Low Poly Block"
	bl_description = "Add simple lowploy block to scene"
	bl_option = {'REGISTER', 'UNDO', 'PRESET'}

	dis: FloatProperty(
		name = "Displacement Range",
		description = "Range of how much each vertices shift on respected axis in both "
						"positive and negative direction",
		min = 0.09,
		max = 0.50,
		default = 0.18
	)

	number_of_blocks: IntProperty(
		name = "Number of Block",
		description = "Number of Block generate at once on Y axis",
		min = 1,
		max = 10,
		default = 2
	)
	x: BoolProperty(
		name = "X axis",
		description = "Enable vertex dispalcement in X axis",
		default = True
	)
	y: BoolProperty(
		name = "Y axis",
		description = "Enable vertex dispalcement in Y axis",
		default = False
	)
	z: BoolProperty(
		name = "Z axis",
		description = "Enable vertex dispalcement in Z axis",
		default = False
	)


	def execute(self, context):
		
		add_mesh(self, context)

		return {'FINISHED'}

		
'''
	extra_twist = 1

block = 1

dis = 0.18
x_dis = 1
y_dis = 0
z_dis = 1
z_modifier = 0.5
'''

