import pygame
import argparse
from time import sleep

# Parse arguments from command line
parser = argparse.ArgumentParser(description='Countdown')
parser.add_argument('-t', metavar='start_time', required=True,
                    dest='start_time', action='store',
                    help='Dojo start time (in seconds)', type=int)
parser.add_argument('-w', metavar='warning_time', required=True,
                    dest='warning_time', action='store',
                    help='Dojo warning time (in seconds)', type=int)
args = parser.parse_args()
start_time = args.start_time
warning_time = args.warning_time

# Define alert sound
pygame.mixer.init()
alert = pygame.mixer.Sound('beep-01a.wav')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set the height, width and title of the screen
size = [500, 200]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dojo Countdown")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.Font(None, 70)
frame_count = 0
frame_rate = 60

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(WHITE)

    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Tempo: {0:02}:{1:02}".format(minutes, seconds)

    if (minutes * 60) + seconds <= warning_time:
        color = RED
    else:
        color = BLACK

    # Blit to the screen
    text = font.render(output_string, True, color)
    screen.blit(text, [100, 70])
    frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    if minutes == 0 and seconds == 0:
        alert.play()
        sleep(3)
        done = True

# If you forget this line, the program will 'hang' on exit.
pygame.quit()
