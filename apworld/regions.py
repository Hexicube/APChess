from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import APChessWorld

def create_and_connect_regions(world: APChessWorld) -> None:
    world.multiworld.regions += [Region("Game", world.player, world.multiworld)]