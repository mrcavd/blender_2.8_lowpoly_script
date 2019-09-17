import bpy, bmesh
from bpy.types import Operator
import random, math
from bpy.props import (IntProperty, BoolProperty, FloatProperty)

def add_mesh(dis, i, context):

	#add mesh and create group
	bpy.ops.mesh.primitive_plane_add(enter_editmode=False, location=(i*2, 0, 0))
	bpy.data.objects["Plane"].name = 'plane_poly'
	obj = context.object
	obj.name = 'plane_poly'
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
		
		while t_mod_z < 0.04 and t_mod_z > -0.04:
			t_mod_z = random.uniform(-dis, dis)
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

class AddLowPolyPlane(Operator):
	bl_idname = "mesh.simple_low_poly_plane_add"
	bl_label = "Add Simple Low Poly Plane"
	bl_description = "Add simple lowploy plane to scene"
	bl_option = {'REGISTER', 'UNDO', 'PRESET'}

	dis: FloatProperty(
		name = "Displacement Range",
		description = "Range of how much each vertices shift on respected axis in both positive and negative direction",
		min = 0.80,
		max = 1.20,
		unit = 'LENGTH',
		default = 1.0		
		)

	number_of_blocks: IntProperty(
		name = "Number of Block",
		description = "Number of Block generate at once on Y axis",
		min = 1,
		max = 10,
		default = 1
		)

	def execute(self, context):
		
		for i in range(self.number_of_blocks):
			obj = add_mesh(self.dis, i, context)

		return {'FINISHED'}
