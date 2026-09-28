from calculator.calculations import Calculation


class History:
    def __init__(self):
        self._records: list[Calculation] = []

    def add(self, calculation: Calculation) -> None:
        self._records.append(calculation)

    def all(self) -> list[Calculation]:
        return list(self._records)

    def count(self) -> int:
        return len(self._records)

    def clear(self) -> None:
        self._records.clear()

    def remove(self, index: int) -> Calculation:
        if not (1 <= index <= len(self._records)):
            raise IndexError("History index out of range")
        return self._records.pop(index - 1)