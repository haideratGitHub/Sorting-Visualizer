import pygame
import random

# initialize pygame
pygame.init()

# creating window
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# setting title
pygame.display.set_caption("Sorting Visualiser")

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
COLORS = [BLUE, RED, GREEN, WHITE, YELLOW, AQUA, MAGENTA]

font = pygame.font.Font('freesansbold.ttf', 20)


def startSorting(text_color):
    text = font.render("select Algorithm and press Space bar to start sorting ", True, text_color)
    WIN.blit(text, (10, 60))


# this can be increased by increasing the width of WIN
number_of_line = 157
# Random Height of lines
height = []
for i in range(number_of_line):
    # allowing duplicates
    height.append(HEIGHT - (random.randint(1, 500)))
# window running loop
running = True
i = 0  # next line printing iterator
j = 0  # next line's height getting iterator
k = 0  # color changing iterator
BLINK_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(BLINK_EVENT, 750)  # event to change color of "start sorting" text


def drawCircle(algorithm):
    pygame.font.init()
    georgia16 = pygame.font.SysFont('Impact', 16)
    if algorithm == 1:
        # indicates selection sort is selected
        pygame.draw.circle(WIN, AQUA, (20, 20), 7, 7)
        # deselecting
        # insertion sort
        pygame.draw.circle(WIN, BLACK, (20, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 40), 7, 1)
        # bubble sort
        pygame.draw.circle(WIN, BLACK, (140, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 20), 7, 1)
        # quick sort circle
        pygame.draw.circle(WIN, BLACK, (140, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 40), 7, 1)
        # merge sort circle
        pygame.draw.circle(WIN, BLACK, (260, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 20), 7, 1)
        # heap sort circle
        pygame.draw.circle(WIN, BLACK, (260, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 40), 7, 1)
    elif algorithm == 2:
        # indicates insertion sort is selected
        pygame.draw.circle(WIN, AQUA, (20, 40), 7, 7)
        # deselecting
        # selection sort circle
        pygame.draw.circle(WIN, BLACK, (20, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 20), 7, 1)
        # bubble sort circle
        pygame.draw.circle(WIN, BLACK, (140, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 20), 7, 1)
        # quick sort circle
        pygame.draw.circle(WIN, BLACK, (140, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 40), 7, 1)
        # merge sort circle
        pygame.draw.circle(WIN, BLACK, (260, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 20), 7, 1)
        # heap sort circle
        pygame.draw.circle(WIN, BLACK, (260, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 40), 7, 1)
    elif algorithm == 3:
        # indicates bubble sort is selected
        pygame.draw.circle(WIN, AQUA, (140, 20), 7, 7)

        # deselecting
        # selection sort circle
        pygame.draw.circle(WIN, BLACK, (20, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 20), 7, 1)
        # insertion sort circle
        pygame.draw.circle(WIN, BLACK, (20, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 40), 7, 1)
        # quick sort circle
        pygame.draw.circle(WIN, BLACK, (140, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 40), 7, 1)
        # merge sort circle
        pygame.draw.circle(WIN, BLACK, (260, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 20), 7, 1)
        # heap sort circle
        pygame.draw.circle(WIN, BLACK, (260, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 40), 7, 1)
    elif algorithm == 4:
        # indicates quick sort is selected
        pygame.draw.circle(WIN, AQUA, (140, 40), 7, 7)

        # deselecting
        # selection sort circle
        pygame.draw.circle(WIN, BLACK, (20, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 20), 7, 1)
        # insertion sort circle
        pygame.draw.circle(WIN, BLACK, (20, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 40), 7, 1)
        # bubble sort circle
        pygame.draw.circle(WIN, BLACK, (140, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 20), 7, 1)
        # merge sort circle
        pygame.draw.circle(WIN, BLACK, (260, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 20), 7, 1)
        # heap sort circle
        pygame.draw.circle(WIN, BLACK, (260, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 40), 7, 1)
    elif algorithm == 5:
        # indicates merge sort is selected
        pygame.draw.circle(WIN, AQUA, (260, 20), 7, 7)

        # deselecting
        # selection sort circle
        pygame.draw.circle(WIN, BLACK, (20, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 20), 7, 1)
        # insertion sort circle
        pygame.draw.circle(WIN, BLACK, (20, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 40), 7, 1)
        # bubble sort circle
        pygame.draw.circle(WIN, BLACK, (140, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 20), 7, 1)
        # quick sort circle
        pygame.draw.circle(WIN, BLACK, (140, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 40), 7, 1)
        # heap sort circle
        pygame.draw.circle(WIN, BLACK, (260, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 40), 7, 1)
    elif algorithm == 6:
        # indicates heap sort is selected
        pygame.draw.circle(WIN, AQUA, (260, 40), 7, 7)

        # deselecting
        # selection sort circle
        pygame.draw.circle(WIN, BLACK, (20, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 20), 7, 1)
        # insertion sort circle
        pygame.draw.circle(WIN, BLACK, (20, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (20, 40), 7, 1)
        # bubble sort circle
        pygame.draw.circle(WIN, BLACK, (140, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 20), 7, 1)
        # quick sort circle
        pygame.draw.circle(WIN, BLACK, (140, 40), 7, 7)
        pygame.draw.circle(WIN, WHITE, (140, 40), 7, 1)
        # merge sort circle
        pygame.draw.circle(WIN, BLACK, (260, 20), 7, 7)
        pygame.draw.circle(WIN, WHITE, (260, 20), 7, 1)
    else:
        # selection sort
        pygame.draw.circle(WIN, (255, 255, 255), (20, 20), 7, 1)
        text = georgia16.render("selection sort", True, WHITE)
        WIN.blit(text, (30, 10))

        # insertion sort
        pygame.draw.circle(WIN, (255, 255, 255), (20, 40), 7, 1)
        text = georgia16.render("insertion sort", True, WHITE)
        WIN.blit(text, (30, 30))

        # bubble sort
        pygame.draw.circle(WIN, (255, 255, 255), (140, 20), 7, 1)
        text = georgia16.render("bubble sort", True, WHITE)
        WIN.blit(text, (150, 10))

        # quick sort
        pygame.draw.circle(WIN, (255, 255, 255), (140, 40), 7, 1)
        text = georgia16.render("quick sort", True, WHITE)
        WIN.blit(text, (150, 30))

        # merge sort
        pygame.draw.circle(WIN, WHITE, (260, 20), 7, 1)
        text = georgia16.render("merge sort", True, WHITE)
        WIN.blit(text, (270, 10))

        # heap sort
        pygame.draw.circle(WIN, WHITE, (260, 40), 7, 1)
        text = georgia16.render("heap sort", True, WHITE)
        WIN.blit(text, (270, 30))


# this method will check which sort is clicked by mouse
def checkMouseClick():
    global algorithm
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    # check for selection sort coordinate
    if ((20 - 7) < x < (20 + 7)) and ((20 - 7) < y < (20 + 7)):
        algorithm = 1
    # check for insertion sort coordinates
    if ((20 - 7) < x < (20 + 7)) and ((40 - 7) < y < (40 + 7)):
        algorithm = 2
    # check for bubble sort coordinate
    if ((140 - 7) < x < (140 + 7)) and ((20 - 7) < y < (20 + 7)):
        algorithm = 3
    # check quick sort coordinates
    if ((140 - 7) < x < (140 + 7)) and ((40 - 7) < y < (40 + 7)):
        algorithm = 4
    # check for merge sort coordinates
    if ((260 - 7) < x < (260 + 7)) and ((20 - 7) < y < (20 + 7)):
        algorithm = 5
    # check for heap sort coordinates
    if ((260 - 7) < x < (260 + 7)) and ((40 - 7) < y < (40 + 7)):
        algorithm = 6


# algorithm = 1
def selectionSort(height):
    # here we need to sort of height array
    # minimum = YELLOW
    # comparing = MAGENTA
    # sorted part = RED
    size = len(height)
    k = 0
    for i in range(size):
        minimum = height[i]
        pygame.draw.line(WIN, YELLOW, (10 + (i * 5), 600),
                         (10 + (i * 5), height[i]))  # give current minimum yellow color
        pygame.display.update()
        index = 0
        for j in range(i + 1, len(height)):
            pygame.draw.line(WIN, GREEN, (10 + (j * 5), 600),
                             (10 + (j * 5), height[j]))  # give element to be compared magenta color
            pygame.display.update()
            if height[j] > minimum:
                # pygame.draw.line(WIN, BLUE, (10 + (i*5), 600), (10 + (i*5), height[i]))  # restore old minimum color
                pygame.draw.line(WIN, YELLOW, (10 + (j * 5), 600),
                                 (10 + (j * 5), height[j]))  # give yellow to new minimum
                pygame.display.update()
                minimum = height[j]  # update new minimum
                index = j  # update index of new minimum
            pygame.draw.line(WIN, BLUE, (10 + (j * 5), 600), (10 + (j * 5), height[j]))
            pygame.display.update()
        if index is not 0:
            temp = height[i]
            height[i] = minimum
            height[index] = temp
            pygame.draw.line(WIN, BLACK, (10 + (i * 5), 600), (10 + (i * 5), 50))
            pygame.draw.line(WIN, RED, (10 + (i * 5), 600), (10 + (i * 5), height[i]))
            index = 0
            pygame.display.update()
        pygame.draw.line(WIN, BLACK, (10 + (i * 5), 600), (10 + (i * 5), 50))
        pygame.draw.line(WIN, RED, (10 + (i * 5), 600), (10 + (i * 5), height[i]))


# algorithm = 2
def insertionSort(height):
    return 0


# algorithm = 3
def bubbleSort(height):
    return 0


# algorithm = 4
def quickSort(height):
    return 0


# algorithm = 5
def mergeSort(height):
    return 0


# algorithm = 6
def heapSort(height):
    return 0


# print(height)
sorted = False
# 0 for nothing, 1 for selection sort
algorithm = 0
# this loop will draw 157 lines
while running:
    drawCircle(algorithm)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == BLINK_EVENT:
            # startSorting(COLORS[k % 7])
            k += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                startSorting(BLACK)
                if algorithm == 1:
                    selectionSort(height)
                if algorithm == 2:
                    insertionSort(height)
                if algorithm == 3:
                    bubbleSort(height)
                if algorithm == 4:
                    quickSort(height)
                if algorithm == 5:
                    mergeSort(height)
                if algorithm == 6:
                    heapSort(height)
                sorted = True
        if event.type == pygame.MOUSEBUTTONUP:
            checkMouseClick()
    if (10 + i) <= (WIDTH - 10) and sorted == False:
        pygame.draw.line(WIN, BLUE, (10 + i, 600), (10 + i, height[j]))
        j += 1
    i += 5
    pygame.display.update()

# print(height)
