

bl_info = {
    "name": "Low Poly Block v 0.33", 
    "author": "calvindeng",
    "blender": (2, 80, 0),
    "location": "View 3D > Add > Mesh",
    "description": "Add low poly blocks",
    "category": "Add Mesh"
}

if "bpy" in locals():
	import importlib
	importlib.reload(add_mesh_simple_lowpoly_block)
	importlib.reload(add_mesh_complex_lowpoly_block)
else:
	from . import add_mesh_simple_lowpoly_block
	from . import add_mesh_complex_lowpoly_block

import bpy
from bpy.types import Menu
from bpy.utils import register_class, unregister_class
                        
class VIEW3D_MT_mesh_lowpoly_add(Menu):
    # define the low poly block menu
    bl_idname = "VIEW3D_MT_mesh_lowpoly_add"
    bl_label = "Low Poly Block"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("mesh.simple_low_poly_block_add", text="Simple Low Poly")
        layout.operator("mesh.complex_low_poly_block_add", text="Complex Low Poly")

def menu_func(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'
    
    layout.separator()
    layout.menu("VIEW3D_MT_mesh_lowpoly_add", text="Low Poly Block")
   
def customize_menu(self, context):
	bl_label = 'Change'

	obj = context.object
	layout = self.layout

	#print(obj.name)
	if 'simple' in obj.name:
		props = layout.operator("mesh.simple_low_poly_block_add", text = "New Block")
		#props.change = True
		#props.delete = obj.name
		#props.startlocation = obj.location
		#props.dis = obj["dis"]
		#props.x = obj["x"]
		#props.y = obj["y"]
		#props.z = obj["z"]
		layout.separator()

	if 'complex' in obj.name:
		props = layout.operator("mesh.complex_low_poly_block_add", text = "New Block")
		layout.separator()


# register classes 
classes = [
    VIEW3D_MT_mesh_lowpoly_add,
	add_mesh_simple_lowpoly_block.AddLowPolyBlock,
	add_mesh_complex_lowpoly_block.AddLowPolyBlock
]

def register():
	for c in classes:
		register_class(c)
		
	bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
	bpy.types.VIEW3D_MT_object_context_menu.prepend(customize_menu)

def unregister():
	bpy.types.VIEW3D_MT_object_context_menu.remove(customize_menu)
	bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
	
	for c in reversed(classes):
		unregister_class(c)

    
if __name__ == "__main__":
    register()