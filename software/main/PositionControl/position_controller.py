from __future__ import annotations

from enum import Enum, auto
from typing import Optional, Dict

from ..Odometry import Position

from . import SteeringController
from .steering_stages import SteeringStage, CourseEnteringStage, LineFollowingStage, SteeringInplaceStage


class PositionController:
    class Stage(Enum):
        CourseEntering = auto()
        LineFollowing = auto()
        FinalSteering = auto()

    stage_wrappers = {
            Stage.CourseEntering: CourseEnteringStage,
            Stage.LineFollowing: LineFollowingStage,
            Stage.FinalSteering: SteeringInplaceStage
            }

    def __init__(self, controllers: Dict[PositionController.Stage, SteeringController]) -> None:
        self.stages = {k: PositionController.stage_wrappers[k](v)
                       for k, v in controllers.items()}

        self.__current_stage: Optional[PositionController.Stage] = None

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
        return self.__current_stage.value == len(PositionController.Stage)

    def _next_stage(self) -> None:
        if self.current_stage is not None:
            self.current_stage.teardown()

        if self.__current_stage is None \
                or self.current_stage_last:
            self.__current_stage = PositionController.Stage(1)
        else:
            self.__current_stage = PositionController.Stage(self.__current_stage.value + 1)
