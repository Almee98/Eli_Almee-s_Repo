from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from panda3d.core import loadPrcFile
import sys
loadPrcFile('conf.prc')

class FloorPlan(ShowBase):
    rotation_speed = 50

    # Okay, this is the updated code.
    def __init__(self):
        super().__init__()
        self.cam.setPos(0, -40, 5)
        self.setBackgroundColor(0, 0, 0, 1)
        self.house = self.loader.loadModel('./floorplan.glb')
        self.house.setH(265)
        self.house.reparentTo(self.render)
        self.accept('q', self.quit_program)

        base.disableMouse()

        self.setup_movement()

        self.mouse_sens = 0.05

        self.taskMgr.add(self.update, "update")

    def update(self, task):
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        if base.win.movePointer(0, base.win.getXSize() // 2, base.win.getYSize() // 2):
            camera.setH(camera.getH() - (x - base.win.getXSize() / 2) * self.mouse_sens)
            camera.setP(camera.getP() - (y - base.win.getYSize() / 2) * self.mouse_sens)
        return task.cont

    def setup_movement(self):
        self.accept("w", self.set_key, ["forward", True])
        self.accept("a", self.set_key, ["left", True])
        self.accept("s", self.set_key, ["backward", True])
        self.accept("d", self.set_key, ["right", True])

        self.accept("w-up", self.set_key, ["forward", False])
        self.accept("a-up", self.set_key, ["left", False])
        self.accept("s-up", self.set_key, ["backward", False])
        self.accept("d-up", self.set_key, ["right", False])

        self.key_map = {"forward": False, "backward": False, "left": False, "right": False}

        self.movement_speed = 5.0

        self.taskMgr.add(self.update_movement, "update_movement")

    def set_key(self, key, value):
        self.key_map[key] = value

    def update_movement(self, task):
        dt = globalClock.get_dt()

        # Calculate movement vector
        move_vec = self.camera.get_quat().get_forward() * (self.key_map["forward"] - self.key_map["backward"]) + \
                   self.camera.get_quat().get_right() * (self.key_map["right"] - self.key_map["left"])

        move_vec.normalize()
        move_vec *= self.movement_speed * dt

        # Update position
        self.camera.set_pos(self.camera.get_pos() + move_vec)

        return task.cont



    def quit_program(self):
        sys.exit(0)


game = FloorPlan()
game.run()