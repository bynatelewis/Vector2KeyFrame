#Vector2 Key Frames
#by Nate Lewis
#2024-2025



bl_info = {
    "name": "Vector2KeyFrames",
    "author": "Nate Lewis",
    "version": (0,3,0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar",
    "description": "A Blender addon for importing and applying plain text Vector2 data as animation keyframes for a selected object.",
    "maintainer": "Nate Lewis",
    "doc_url": "https://github.com/bynatelewis/Vector2KeyFrame",
    "category": "Object",
}

import bpy

# Add-on preferences for saving the file path
class FilePathPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    file_path: bpy.props.StringProperty(
        name="File Path",
        subtype='FILE_PATH',
        default="",
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "file_path")


# Function to read Vector2 data and apply animation
def apply_vector2_animation(file_path):
    vector_data = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                x, y = map(float, line.split(','))
                vector_data.append((x, y))

        obj = bpy.context.object  # Assume an object is selected
        if obj:
            obj.animation_data_create()
            obj.animation_data.action = bpy.data.actions.new(name="Vector2KeyFrames")

            for i, (x, y) in enumerate(vector_data):
                frame_num = i + 1
                obj.location.x = x/100
                obj.location.y = -y/100
                obj.keyframe_insert(data_path="location", frame=frame_num)

        return {'FINISHED'}
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return {'CANCELLED'}


# Operator to apply animation from the file
class OBJECT_OT_apply_vector2_animation(bpy.types.Operator):
    bl_idname = "object.apply_vector2_animation"
    bl_label = "Apply Vector2 Key Frames"
    bl_description = "Reads Vector2 data from a file and applies it as animation"

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        file_path = prefs.file_path

        if not file_path:
            self.report({'WARNING'}, "No file path set in preferences")
            return {'CANCELLED'}

        return apply_vector2_animation(file_path)


# Panel to access the file path setting and run the function
class OBJECT_PT_file_path_panel(bpy.types.Panel):
    bl_label = "Vector2KeyFrames"
    bl_idname = "OBJECT_PT_file_path_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Vector2KeyFrames"

    def draw(self, context):
        layout = self.layout
        prefs = context.preferences.addons[__name__].preferences

        layout.prop(prefs, "file_path")
        layout.operator("object.apply_vector2_animation")


# Register classes
classes = [FilePathPreferences, OBJECT_OT_apply_vector2_animation, OBJECT_PT_file_path_panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
