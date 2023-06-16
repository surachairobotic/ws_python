import random
import time, os

class Person:
    WAITING = 0
    IN_ELEVATOR = 1
    DONE = 2

    def __init__(self, from_floor, to_floor):
        self.from_floor = from_floor
        self.to_floor = to_floor
        self.status = Person.WAITING

class Building:
    def __init__(self):
        self.total_floors = 15
        self.elevator_floor = 1
        random.seed(time.time())
        self.all_people = [Person(1, self.rand_floor()) for x in range(15)] + \
            [Person(self.rand_floor(), 1) for x in range(15)]
        random.shuffle(self.all_people)

        self.people = self.all_people[0:5]
        self.score = 0

        #print("x1")
        #print([x for x in range(self.total_floors + 2, 0, -1)])
        #for floor_number in range(self.total_floors + 2, 0, -1):
        #    print("x")
        #print("x2222222222222222222222222222222222222222")

        self.draw()
        #print("x3")

    def rand_floor(self):
        return int(random.random()*self.total_floors)+1

    def start_elevator(self, controller):
        while len([p for p in self.people if p.status != Person.DONE]):
            if len([p for p in self.people if p.status == Person.WAITING]) < 5 and \
                len(self.people) < len(self.all_people) - 1:
                self.people.append(self.all_people[len(self.people)])
            controller(self)
        self.draw()

    def goto_floor(self, floor):
        if floor == self.elevator_floor:
            return

        direction = 1
        if floor < self.elevator_floor:
            direction = -1

        while floor != self.elevator_floor:
            self.elevator_floor += direction
            self.draw()

        for person in self.people:
            # Drop off on this floor
            if person.status == Person.IN_ELEVATOR and \
                person.to_floor is self.elevator_floor:
                person.status = Person.DONE

            # Pickup anyone on this floor
            if person.status == Person.WAITING and \
                person.from_floor == self.elevator_floor:
                person.status = Person.IN_ELEVATOR

        self.draw()

    def lift_character(self):
        return (
            '\u0030\u20E3', '\u0031\u20E3', '\u0032\u20E3', '\u0033\u20E3',
            '\u0034\u20E3', '\u0035\u20E3', '\u0036\u20E3', '\u0037\u20E3',
        )[len([p for p in self.people if p.status == Person.IN_ELEVATOR])]

    def draw(self):
        #print(('\033[13A\nScore: %d\n' % self.score))
        os.system('cls')
        print(('Score: %d\n' % self.score))
        for floor_number in range(self.total_floors, 0, -1):
            elevator = '  '
            if self.elevator_floor == floor_number:
                elevator = self.lift_character() + ' '
            is_waiting = '  '
            if len([p for p in self.people if p.status == Person.WAITING and \
                p.from_floor == floor_number]):
                is_waiting = '\U0001F464 '
            is_done = ''
            for person in self.people:
                if person.status == Person.DONE and \
                    person.to_floor == floor_number:
                    is_done += '\U0001F464 '
            print(('%02s %s %s %s' % (floor_number, is_waiting, elevator, is_done)))

        self.score += 1
        time.sleep(0.025)

def elevator(building):
    for person in building.people:
        if person.status == Person.WAITING and \
            person.from_floor != building.elevator_floor:
            building.goto_floor(person.from_floor)
            return

        if person.status == Person.IN_ELEVATOR:
            building.goto_floor(person.to_floor)
            return

building = Building()
building.start_elevator(elevator)
