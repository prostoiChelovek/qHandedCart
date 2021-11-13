from __future__ import annotations

from typing import Optional
from abc import ABC, abstractmethod

from ..Odometry import Position
from ..Path import Line
from ..kinematics import Velocity

from .steering_controller import SteeringController


class SteeringStage(ABC):
    def __init__(self, controller: SteeringController) -> None:
        self._controller = controller

    @abstractmethod
    def set_target(self, target: Position) -> None:
        pass

    @property
    def finished(self) -> bool:
        return self._controller.finished

    def teardown(self) -> None:
        pass

    def update(self) -> None:
        self._controller.update()


class SteeringInplaceStage(SteeringStage):
    def __init__(self, controller: SteeringController) -> None:
        super().__init__(controller)
        
        self.__last_velocity: Optional[Velocity] = None

    def set_target(self, target: Position) -> None:
        vel = self._controller._chassis.velocity
        self.__last_velocity = vel
        vel.linear = 0
        self._controller._chassis.set_velocity(vel)

        target = Position(
                self._controller._odometry.position.translation,
                target.rotation)
        self._controller.set_target(target)

    def teardown(self) -> None:
        if self.__last_velocity is None:
            return

        # TODO: по хорошему, нужно остановится
        self._controller._chassis.set_velocity(self.__last_velocity)


class CourseEnteringStage(SteeringInplaceStage):
    def set_target(self, target: Position) -> None:
        current_pos = self._controller._odometry.position
        line = Line(current_pos.translation, target.translation)

        target = Position(
                target.translation,
                line.angle
                )

        return super().set_target(target)


class LineFollowingStage(SteeringStage):
    def set_target(self, target: Position) -> None:
        self._controller.set_target(target)
