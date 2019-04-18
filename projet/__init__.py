from .adapter import Adapter
from .strategies import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore, StrategieTournerDroiteAmeliore, StrategieArcGauche, StrategieArcDroit
from .model import RobotVirtuel, Arene, Obstacle, ObstacleCarre, ObstacleRond,ObstacleBalise, lecture, ecriture2
try:
    from .view import View, View3D
except Exception as e:
    print("pyglet pas disponi")
