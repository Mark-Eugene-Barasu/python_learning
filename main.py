import curses
import random
import time


def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Score

    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()
    w = sw - 2
    h = sh - 2

    # Initial snake position and body
    snake = [
        [h // 2, w // 2],
        [h // 2, w // 2 - 1],
        [h // 2, w // 2 - 2]
    ]

    # Initial food
    food = [h // 2, w // 2 + 10]
    stdscr.addch(food[0], food[1], '█', curses.color_pair(2))

    # Initial direction
    direction = curses.KEY_RIGHT

    # Score
    score = 0

    # Game loop
    while True:
        # Draw snake
        for y, x in snake:
            stdscr.addch(y, x, '█', curses.color_pair(1))

        # Draw score
        stdscr.addstr(0, 0, f'Score: {score}', curses.color_pair(3))

        # Refresh screen
        stdscr.refresh()

        # Get next direction
        next_key = stdscr.getch()
        if next_key != -1:
            if next_key == curses.KEY_UP and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP
            elif next_key == curses.KEY_DOWN and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN
            elif next_key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT
            elif next_key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT
            elif next_key == ord('q'):
                break

        # Calculate new head
        head = [snake[0][0], snake[0][1]]
        if direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1

        # Check wall collision
        if head[0] < 1 or head[0] >= h or head[1] < 1 or head[1] >= w:
            break

        # Check self collision
        if head in snake:
            break

        # Add new head
        snake.insert(0, head)

        # Check food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, h - 1),
                    random.randint(1, w - 1)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], '█', curses.color_pair(2))
        else:
            # Remove tail
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        # Delay
        time.sleep(0.1)

    # Game over
    stdscr.addstr(sh // 2, sw // 2 - 5, 'Game Over!', curses.color_pair(3))
    stdscr.addstr(sh // 2 + 1, sw // 2 - 7,
                  f'Final Score: {score}', curses.color_pair(3))
    stdscr.refresh()
    time.sleep(2)


if __name__ == '__main__':
    curses.wrapper(main)
