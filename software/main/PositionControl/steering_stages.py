from __future__ import annotations

from enum import Enum, auto
from typing import Optional, Dict
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


class SteeringStages:
    class Stage(Enum):
        CourseEntering = auto()
        LineFollowing = auto()
        FinalSteering = auto()

    stage_wrappers = {
            Stage.CourseEntering: CourseEnteringStage,
            Stage.LineFollowing: LineFollowingStage,
            Stage.FinalSteering: SteeringInplaceStage
            }

    def __init__(self, controllers: Dict[SteeringStages.Stage, SteeringController]) -> None:
        self.stages = {k: SteeringStages.stage_wrappers[k](v)
                       for k, v in controllers.items()}

        self.__current_stage: Optional[SteeringStages.Stage] = None

    def set_target(self, target: Position) -> None:
        self.reset()
        self._next_stage()
        self.current_stage.set_target(target)

    def update(self) -> bool:
        if self.current_stage is None:
            return True

        self.current_stage.update()

        if self.current_stage.finished:
            if self.current_stage_last:
                self.reset()
                return True

            self._next_stage()

        return False

    def reset(self) -> None:
        if self.current_stage == None:
            return

        self.current_stage.teardown()
        self.__current_stage = None

    @property
    def current_stage(self) -> Optional[SteeringStage]:
        if self.__current_stage is None:
            return None
        return self.stages[self.__current_stage]

    @property
    def current_stage_last(self) -> bool:
        if self.__current_stage is None:
            return False
        return self.__current_stage.value == len(SteeringStages.Stage)

    def _next_stage(self) -> None:
        if self.current_stage is not None:
            self.current_stage.teardown()

        if self.__current_stage is None \
                or self.current_stage_last:
            self.__current_stage = SteeringStages.Stage(1)
        else:
            self.__current_stage = SteeringStages.Stage(self.__current_stage.value + 1)
