"""
A terminal-based Snake game implemented using the curses library.

This module contains the main game logic for a classic Snake game
where the player controls a snake to eat food, grow, and avoid collisions.
Features include increasing speed, score tracking, and restart options.
"""

import curses
import random
import time


def draw_game(stdscr, snake, food, score):
    """Draw the current game state."""
    stdscr.clear()
    for y, x in snake:
        stdscr.addch(y, x, '█', curses.color_pair(1))
    stdscr.addch(food[0], food[1], '█', curses.color_pair(2))
    stdscr.addstr(0, 0, f'Score: {score}', curses.color_pair(3))
    stdscr.refresh()


def get_direction(next_key, current_direction):
    """Get the new direction based on key press."""
    if next_key == curses.KEY_UP and current_direction != curses.KEY_DOWN:
        return curses.KEY_UP
    if next_key == curses.KEY_DOWN and current_direction != curses.KEY_UP:
        return curses.KEY_DOWN
    if next_key == curses.KEY_LEFT and current_direction != curses.KEY_RIGHT:
        return curses.KEY_LEFT
    if next_key == curses.KEY_RIGHT and current_direction != curses.KEY_LEFT:
        return curses.KEY_RIGHT
    return current_direction


def calculate_head(snake, direction):
    """Calculate the new head position."""
    head = [snake[0][0], snake[0][1]]
    if direction == curses.KEY_UP:
        head[0] -= 1
    elif direction == curses.KEY_DOWN:
        head[0] += 1
    elif direction == curses.KEY_LEFT:
        head[1] -= 1
    elif direction == curses.KEY_RIGHT:
        head[1] += 1
    return head


def check_collision(head, snake, w, h):
    """Check for wall or self collision."""
    if head[0] < 1 or head[0] >= h or head[1] < 1 or head[1] >= w:
        return True
    if head in snake:
        return True
    return False


def generate_food(snake, w, h):
    """Generate a new food position not on the snake."""
    while True:
        nf = [random.randint(1, h - 1), random.randint(1, w - 1)]
        if nf not in snake:
            return nf


def main(stdscr):
    """
    Main function to run the Snake game.

    Initializes the game, handles the game loop, and manages game over.
    Uses curses for terminal display.

    Args:
        stdscr: The curses window object.
    """
    while True:  # Restart loop
        # Initialize curses
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(100)

        # Get screen dimensions
        sh, sw = stdscr.getmaxyx()

        # Check minimum size
        if sh < 10 or sw < 20:
            stdscr.addstr(
                0, 0, "Terminal too small. Resize to at least 20x10.")
            stdscr.refresh()
            stdscr.getch()
            return

        w = sw - 2
        h = sh - 2

        # Colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Score

        # Initial snake position and body
        snake = [
            [h // 2, w // 2],
            [h // 2, w // 2 - 1],
            [h // 2, w // 2 - 2]
        ]

        # Initial food
        food = generate_food(snake, w, h)

        # Initial direction
        direction = curses.KEY_RIGHT

        # Score
        score = 0

        # Delay
        delay = 0.1

        # Game loop
        game_over = False
        while not game_over:
            draw_game(stdscr, snake, food, score)

            # Get next direction
            next_key = stdscr.getch()
            if next_key != -1:
                if next_key == ord('q'):
                    game_over = True
                    continue
                direction = get_direction(next_key, direction)

            # Calculate new head
            head = calculate_head(snake, direction)

            # Check collision
            if check_collision(head, snake, w, h):
                game_over = True
                continue

            # Add new head
            snake.insert(0, head)

            # Check food
            if snake[0] == food:
                score += 1
                delay = max(0.05, delay - 0.01)
                food = generate_food(snake, w, h)
            else:
                # Remove tail
                tail = snake.pop()
                stdscr.addch(tail[0], tail[1], ' ')

            # Delay
            time.sleep(delay)

        # Game over
        stdscr.clear()
        stdscr.addstr(sh // 2, sw // 2 - 5, 'Game Over!', curses.color_pair(3))
        stdscr.addstr(sh // 2 + 1, sw // 2 - 7,
                      f'Final Score: {score}', curses.color_pair(3))
        stdscr.addstr(sh // 2 + 2, sw // 2 - 10,
                      'Press R to restart or Q to quit', curses.color_pair(3))
        stdscr.refresh()

        restart = False
        while True:
            key = stdscr.getch()
            if key == ord('r') or key == ord('R'):
                restart = True
                break
            if key == ord('q') or key == ord('Q'):
                return

        if not restart:
            break


if __name__ == '__main__':
    curses.wrapper(main)
