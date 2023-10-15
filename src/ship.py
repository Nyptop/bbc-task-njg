class Ship:
    VALID_ORIENTATIONS = ['horizontal', 'vertical']

    def __init__(self, length, orientation):
        if orientation not in self.VALID_ORIENTATIONS:
            raise ValueError(
                f"Invalid orientation '{orientation}'. Must be one of {self.VALID_ORIENTATIONS}",
            )

        self.length = length
        self.orientation = orientation
        self.hits = 0

    def is_sunk(self):
        return self.hits >= self.length
