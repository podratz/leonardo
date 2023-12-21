import math
from dataclasses import dataclass
from types import NotImplementedType
from typing import Self


@dataclass
class Angle:
    fraction: float = 0

    @classmethod
    @property
    def zero(cls) -> Self:
        return cls(0.0)

    # Factory methods

    @classmethod
    def from_radians(cls, radians: float) -> Self:
        fraction = radians / math.tau
        return cls(fraction)

    @classmethod
    def from_degrees(cls, degrees: float) -> Self:
        fraction = degrees / 360
        return cls(fraction)

    # Properties

    @property
    def fraction_canonic(self) -> float:
        return self.fraction % 1

    @property
    def radians(self) -> float:
        return self.fraction * math.tau

    @property
    def radians_canonic(self) -> float:
        return self.radians % math.tau

    @property
    def degrees(self) -> float:
        return self.fraction * 360

    @property
    def degrees_canonic(self) -> float:
        return self.degrees % 360

    @property
    def complex(self) -> complex:
        real = math.cos(self.radians)
        imag = math.sin(self.radians)
        return complex(real, imag)

    # Arithmetic

    def __add__(self, other: object) -> NotImplementedType | Self:
        if isinstance(other, Angle):
            cls = type(self)
            return cls(self.fraction + other.fraction)
        return NotImplemented

    def __iadd__(self, other: object) -> NotImplementedType | None:
        if isinstance(other, Angle):
            self.fraction += other.fraction
        return NotImplemented

    def __mul__(self, other: object) -> NotImplementedType | Self:
        if isinstance(other, int | float):
            cls = type(self)
            return cls(self.fraction * other)
        return NotImplemented

    def __imul__(self, other: object) -> NotImplementedType | None:
        if isinstance(other, int | float):
            self.fraction *= other
        return NotImplemented

    # Coalescing

    def __str__(self) -> str:
        return f"{self.degrees:.2f}\u00B0"
