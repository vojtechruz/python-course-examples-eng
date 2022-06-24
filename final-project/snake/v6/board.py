import random


class Board:

    def __init__(self, width, height):
        self.snake = [(0, 0), (1, 0), (2, 0)]
        self.direction = (1, 0)
        self.width = width
        self.height = height
        self.food = []
        self.add_food()
        self.add_food()
        self.add_food()
        self.game_over = False

    def move(self):
        if (self.game_over):
            return

        current_x = self.snake[-1][0]
        current_y = self.snake[-1][1]
        new_x = current_x + self.direction[0]
        new_y = current_y + self.direction[1]
        self.snake.append((new_x, new_y))

        if (self.snake[-1] in self.food):
            self.food.remove(self.snake[-1])
            self.add_food()
        else:
            self.snake.pop(0)

        self.check_snake_eats_itself()
        self.check_snake_exits_board()

    def change_direction(self, new_x, new_y):
        old_x, old_y = self.direction
        # Now snake cannot move in the opposite direction than the original
        if (old_x, old_y) != (-new_x, -new_y):
            self.direction = (new_x, new_y)

    def add_food(self):
        for try_number in range(100):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake) and (position not in self.food):
                self.food.append(position)
                return

    def check_snake_eats_itself(self):
        if (self.snake[-1] in self.snake[:-1]):
            self.game_over = True

    def check_snake_exits_board(self):
        x, y = self.snake[-1]
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            self.game_over = True

    def get_image_name(self, index):
        current_x, current_y = self.snake[index]

        if index == 0:
            name_prev = "tail"
        else:
            previous_x, previous_y = self.snake[index - 1]

            if current_x == previous_x and current_y == previous_y - 1:
                name_prev = "top"
            if current_x == previous_x and current_y == previous_y + 1:
                name_prev = "bottom"
            if current_x == previous_x - 1 and current_y == previous_y:
                name_prev = "right"
            if current_x == previous_x + 1 and current_y == previous_y:
                name_prev = "left"

        if index == len(self.snake) - 1:
            name_next = "head"
        else:
            current_x, current_y = self.snake[index]
            next_x, next_y = self.snake[index + 1]

            if current_x == next_x and current_y == next_y - 1:
                name_next = "top"
            if current_x == next_x and current_y == next_y + 1:
                name_next = "bottom"
            if current_x == next_x - 1 and current_y == next_y:
                name_next = "right"
            if current_x == next_x + 1 and current_y == next_y:
                name_next = "left"

        return name_prev + "-" + name_next
