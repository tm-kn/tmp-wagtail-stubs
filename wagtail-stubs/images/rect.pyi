from typing import Any

class Vector:
    x: Any = ...
    y: Any = ...
    def __init__(self, x: Any, y: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, key: Any): ...
    def __eq__(self, other: Any) -> Any: ...

class Rect:
    left: Any = ...
    top: Any = ...
    right: Any = ...
    bottom: Any = ...
    def __init__(self, left: Any, top: Any, right: Any, bottom: Any) -> None: ...
    size: Any = ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    centroid: Any = ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def centroid_x(self): ...
    @property
    def centroid_y(self): ...
    def as_tuple(self): ...
    def clone(self): ...
    def round(self): ...
    def move_to_clamp(self, other: Any): ...
    def move_to_cover(self, other: Any): ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, key: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    @classmethod
    def from_point(cls, x: Any, y: Any, width: Any, height: Any): ...
