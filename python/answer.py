from typing import Optional
from dataclasses import dataclass

@dataclass
class Answer:
    part_one: int
    part_two: Optional[int]

    def __str__(self):
        if self.part_two is None:
            return f'Part one: {self.part_one}'
        return f'Part one: {self.part_one}, Part two: {self.part_two}'

    def __add__(self, other):
        """
        >>> Answer(0, None) + Answer(1, None)
        Answer(part_one=1, part_two=None)
        >>> Answer(123, None) + Answer(0, 123)
        Answer(part_one=123, part_two=123)
        """
        p2 = None
        if self.part_two is not None or other.part_two is not None:
            p2 = (self.part_two or 0) + (other.part_two or 0)

        return Answer(
            part_one=self.part_one + other.part_one,
            part_two=p2
        )

if __name__ == '__main__':
    import doctest
    doctest.testmod()