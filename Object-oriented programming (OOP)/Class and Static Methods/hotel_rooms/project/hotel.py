from typing import List

from project.room import Room


class Hotel:

    def __init__(self, name: str,):
        self.name = name
        self.guests = 0
        self.rooms: List[Room] = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room and not room.is_taken and room.capacity >= people:
            self.guests += people
            room.take_room(people)

    def free_room(self, room_number: int) -> None:
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room and room.is_taken:
            self.guests -= room.guests
            room.free_room()


    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms)}\n"
                f"Taken rooms: {', '.join(taken_rooms)}")
