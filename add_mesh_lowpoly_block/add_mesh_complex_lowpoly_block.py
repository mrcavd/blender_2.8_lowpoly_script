import bpy, bmesh
from bpy.types import Operator
import random, math
from bpy.props import (IntProperty, BoolProperty, FloatProperty)

def add_mesh(dis, extra_twist, i, context):

	#add mesh and create group
	bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, i*2, 0))
	bpy.data.objects["Cube"].name = 'complex_poly'
	obj = context.object
	obj.name = 'complex_poly'
	me = obj.data
	bpy.ops.object.vertex_group_add()

	bpy.ops.object.mode_set(mode='EDIT')
	bpy.ops.mesh.subdivide()
	bpy.ops.mesh.select_all(action = 'DESELECT')
        
	bpy.ops.object.mode_set(mode='OBJECT')
        
	for i in range(20,26):
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
		dis_mod = random.uniform(-dis, dis)
	bpy.context.object.modifiers["Displace"].strength = dis_mod
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace")
        
	if(extra_twist == 1):
		bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
		deg = random.randrange(-3, 3)
		rad = math.radians(deg)
		bpy.context.object.modifiers["SimpleDeform"].angle = rad
		bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Y'

	return obj

class AddLowPolyBlock(Operator):
	bl_idname = "mesh.complex_low_poly_block_add"
	bl_label = "Add Complex Low Poly Block"
	bl_description = "Add complex lowploy block to scene"
	bl_option = {'REGISTER', 'UNDO', 'PRESET'}

	dis: FloatProperty(
		name = "Displacement Range",
		description = "Range of how much each vertices shift on respected axis in both positive and negative direction",
		min = 0.80,
		max = 1.20,
		unit = 'LENGTH',
		default = 1.0		
		)

	twist: BoolProperty(
		name = "Extra twist",
		description = "Extra twist on Y axis",
		default = True
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
			obj = add_mesh(self.dis, self.twist, i, context)

		return {'FINISHED'}