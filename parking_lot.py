class ParkingLot:
    """
    A class to represent a parking lot with two levels, A and B.
    Each level has the capacity to park 20 vehicles of any size.
    """

    def __init__(self):
        self.capacity_per_level = 20
        self.levels = {"A": {}, "B": {}}

    def assign_parking_spot(self, vehicle_number):
        """
        Assigns a parking spot to a new vehicle.

        Returns:
            dict or str: A dictionary containing the level and parking spot number if a spot is assigned,
                or a string "Parking lot is full" if the parking lot is full.
        """
        level, spot = self.find_empty_spot()
        if level and spot:
            self.levels[level][vehicle_number] = spot
            return {"level": level, "spot": spot}
        else:
            return "Parking lot is full"

    def retrieve_parking_spot(self, vehicle_number):
        """
        Retrieves the parking spot for a particular vehicle.

        Returns:
            dict or str: A dictionary containing the level and parking spot number if the vehicle is found,
                or a string "Vehicle not found" if the vehicle is not in the parking lot.
        """
        for level in self.levels:
            if vehicle_number in self.levels[level]:
                return {"level": level, "spot": self.levels[level][vehicle_number]}
        return "Vehicle not found"

    def find_empty_spot(self):
        """
        Finds an empty parking spot in the parking lot.

        Returns:
            tuple (str, int) or (None, None): A tuple containing the level and parking spot number if a spot is available,
                or (None, None) if the parking lot is full.
        """
        for level in self.levels:
            if len(self.levels[level]) < self.capacity_per_level:
                empty_spot = next(
                    i
                    for i in range(1, self.capacity_per_level + 1)
                    if i not in self.levels[level].values()
                )
                return level, empty_spot
        return None, None
