from .view import View
try:
    from .view3d_en_cour import View3D
except Exception as e:
    print("pyglet pas disponi")
