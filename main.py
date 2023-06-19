import bpy

# dependencies
# blender-xray - github.com/PavelBlend/blender-xray
# PyNifly - github.com/BadDogSkyrim/PyNifly/

PATH_TO_OBJECT = r'C:\path\to\stalker.object'
PATH_OUT_NIF = r'C:\path\out\fallout4.nif'

# Импор файла .object
bpy.ops.xray_import.object(files=[{'name': PATH_TO_OBJECT}])

# Выбрать объект в blender
obj = bpy.data.objects[0]
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj

# Экспорт файла .nif
bpy.ops.export_scene.pynifly(filepath=PATH_OUT_NIF, target_game="FO4", chargen_ext="_chargen")
