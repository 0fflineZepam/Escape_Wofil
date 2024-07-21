import math

# Ustawienia gry
RES = WIDTH, HEIGHT = 1950, 1000
FPS = 0

# Ustawienia gracza
PLAYER_POS = 1.5, 5  # Pozycja na mini-mapie
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# Ustawienia raycastingu
FOV = math.pi / 3  # Kąt widzenia (60 stopni)
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

# Ustawienia ekranu
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS