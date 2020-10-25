from project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stats_count):
        new_name = f"{stats_count} stars Hotel"
        return cls(new_name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number and x.is_taken == False]
        if room:
            room = room[0]
            room.take_room(people)
            if room.is_taken:
                self.guests += people

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number and x.is_taken == True]
        if room:
            room = room[0]
            room.free_room()
            if not room.is_taken:
                self.guests -= room.guests

    def print_status(self):
        free_rooms = [str(x.number) for x in self.rooms if x.is_taken == False]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken == True]
        f_m = ""
        t_r = ""
        if free_rooms:
            f_m = f"Free rooms: {', '.join(free_rooms)}\n"
        if taken_rooms:
            t_r = f"Taken_rooms: {', '.join(taken_rooms)}"
        token = f"Hotel {self.name} has {self.guests} total guests\n" \
                f"{f_m}" \
                f"{t_r}"
        return print(token)

