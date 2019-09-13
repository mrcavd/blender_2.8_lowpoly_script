import bpy, bmesh
from bpy.types import Operator
import random, math
from bpy.props import (IntProperty, BoolProperty, FloatProperty)

default_X = True
default_Y = False
default_Z = False


def add_mesh(dis, x, y, z, i, context):

	#add mesh and create group
	bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, i*2, 0))
	bpy.data.objects["Cube"].name = 'simple_poly'
	obj = context.object
	obj.name = 'simple_poly'
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
	
		if(x == 1):
			while t_mod_x < 0.04 and t_mod_x > -0.04:
				t_mod_x = random.uniform(-dis, dis)
		if(y == 1):
			while t_mod_y < 0.04 and t_mod_y > -0.04:
				t_mod_y = random.uniform(-dis, dis)
		if(z == 1):
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
	
	return obj

	

class AddLowPolyBlock(Operator):
	bl_idname = "mesh.simple_low_poly_block_add"
	bl_label = "Add Simple Low Poly Block"
	bl_description = "Add simple lowploy block to scene"
	bl_option = {'REGISTER', 'UNDO', 'PRESET'}

	dis: FloatProperty(
		name = "Displacement Range",
		description = "Range of how much each vertices shift on respected axis in both positive and negative direction",
		min = 0.09,
		max = 0.50,
		unit = 'LENGTH',
		default = 0.18		
		)

	number_of_blocks: IntProperty(
		name = "Number of Block",
		description = "Number of Block generate at once on Y axis",
		min = 1,
		max = 10,
		default = 1
		)

	x: BoolProperty(
		name = "Enable X Axis Lowpoly Effect",
		description = "Enable vertex dispalcement in X axis",
		default = default_X
		)
	y: BoolProperty(
		name = "Enable Y Axis Lowpoly Effect",
		description = "Enable vertex dispalcement in Y axis",
		default = default_Y
		)
	z: BoolProperty(
		name = "Enable Z Axis Lowpoly Effect",
		description = "Enable vertex dispalcement in Z axis",
		default = default_Z
		)

	#def draw(self, context):
	#	layout = self.layout
	#
	#	box = layout.box()
	#	box.prop(self, 'dis')
	#
	#	box = layout.box()
	#	box.prop(self, 'x')
	#	box.prop(self, 'y')
	#	box.prop(self, 'z')


	def execute(self, context):
		
		for i in range(self.number_of_blocks):
			obj = add_mesh(self.dis, self.x, self.y, self.z, i, context)
		
		#obj["number_of_blocks"] = self.number_of_blocks
		#obj["dis"] = self.dis
		#obj["x"] = self.x
		#obj["y"] = self.y
		#obj["z"] = self.z

		return {'FINISHED'}

	def invoke(self, context, event):
		bpy.context.view_layer.update()

		self.execute(context)

		return {'FINISHED'}