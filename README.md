# Vector2KeyFrame - Blender Addon
A Blender addon for importing and applying Vector2 data as animation keyframes for a selected object. 

## Overview
Vector2KeyFrame - Blender Addon is a companion tool for Capture Mouse, a utility that records mouse movement as Vector2() coordinates and stores them in a plain text file. This Blender addon reads that data and converts it into keyframe animation for a selected object.

## Features
- Import Vector2() coordinate data from a plain text file.
- Automatically generate keyframe animation for an object based on the recorded movement.
- Ideal for creating interactive UI animations or using coordinate data for creative motion graphics.
## How It Works
1. Capture Mouse Utility records mouse movements and saves them as (x, y) coordinates stored vertically in a .txt file.
2. This addon imports the file and applies the data as keyframes to the selected object.
3. The object moves in sync with the recorded motion, enabling precise, data-driven animations.
## Installation & Usage
1. Install the addon via Blender’s Preferences > Add-ons > Install.
2. Select an object in the scene.
3. Open the N-panel > Vector2KeyFrames tab.
4. Choose the text file containing the recorded coordinates.
5. Next select a object in the 3D View.
6. Click "Apply Vector2 Key Frames" to generate keyframes.
7. Click the play button in the timeline to preview output.
## Use Cases
- UI animation prototyping in Blender.
- Converting real-world cursor movement into animations.
- Experimenting with data-driven motion graphics.
