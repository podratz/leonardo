import itertools
from types import NotImplementedType
from typing import Union, cast


class GeometricSequence:
    def __init__(self, common_ratio: float, scale_factor: float = 1.0):
        """Create a geometric sequence from a common ratio and a scale factor."""
        self.common_ratio = common_ratio
        self.scale_factor = scale_factor

    def __getitem__(self, subscript: Union[int, slice]) -> Union[float, list[float]]:
        """Return the element at the given index, or the subsequence bound by the given slice."""
        if isinstance(subscript, int):
            n = subscript

            item = self.scale_factor * (self.common_ratio**n)
            return item

        else:
            if subscript.start is None:
                raise TypeError("sequence requires pre-determined start")
            start = subscript.start

            if subscript.step is not None and subscript.stop is None:
                raise TypeError("sequence with step needs pre-determined stop")
            stop = subscript.stop

            if subscript.step == 0:
                raise ValueError("slice step cannot be zero")
            step = subscript.step or 1

            sequence = [cast(float, self[index]) for index in range(start, stop, step)]
            return sequence

    def __iter__(self):
        """Iterate this infinite geometric sequence."""
        for index in itertools.count():
            yield self[index]

    def __eq__(self, other: object) -> NotImplementedType | bool:
        """Return True if and only if the scale factors and common ratios are equal."""
        if not isinstance(other, GeometricSequence):
            return NotImplemented
        return (
            self.common_ratio == other.common_ratio
            and self.scale_factor == other.scale_factor
        )
