# Hopscotch Game

A Python-based clicking game built with Pygame where players click squares to earn points and unlock upgrades.

## Game Features

### Core Mechanics
- Click squares to earn points
- Score multipliers
- Additive power-ups
- Timer system
- Shop system
- Pause functionality

### Game States
```python
class GameState():
    def __init__(self):
        self.state = 'intro'
```
The game features three main states:
- Intro screen with scrolling background
- Main game with clicking mechanics
- Pause screen with resume option

### Score System
- Basic clicks earn 1 point
- Multiplier upgrades increase points per click
- Additive upgrades give more time
- Shop system for purchasing upgrades

### Timer System
```python
seconds = int((pygame.time.get_ticks() - timer) / 1000)
myTimer = additivenum - seconds
```
- Dynamic timer that counts down
- Can be extended through upgrades
- Pauses during game pause

## Custom Assets

All game assets were created from scratch using digital art tools.

### Visual Elements
1. **Square Assets**
   - Regular square for clicking
   - Special square variations
   - Custom border designs
   ```python
   square = pygame.image.load(r'assets/square.png')
   special_square = pygame.image.load(r'assets/special square.png')
   special_square_max = pygame.image.load(r'assets/special square max.png')
   ```

2. **Cookie Assets**
   - Regular cookie design
   - Special cookie variations
   ```python
   cookie = pygame.image.load(r'assets/cookie.png')
   special_cookie = pygame.image.load(r'assets/special cookie.png')
   special_cookie_max = pygame.image.load(r'assets/special cookie max.png')
   ```

3. **Interface Elements**
   - Custom cursor
   - Shop buttons
   - Play/pause buttons
   ```python
   cursor = pygame.image.load(r'assets/cursor.png')
   pause = pygame.image.load(r'assets/pause.png')
   play = pygame.image.load(r'assets/play.png')
   ```

4. **Background Elements**
   - Main game background
   - Scrolling intro background
   - Border designs
   ```python
   bg = pygame.image.load(r'assets/backround.png')
   bg1 = pygame.image.load(r'assets/bg.png')
   border = pygame.image.load(r'assets/border.png')
   ```

### Custom Fonts
- CompassPro for UI text
- MatchupPro for multiplier display
```python
Compass = pygame.font.Font("assets/CompassPro.ttf", 32)
matchup = pygame.font.Font('assets/MatchupPro.ttf', 32)
```

## Installation and Setup

1. Clone the Repository
```bash
git clone github.com/raghavrat/Hopschotch.git
cd click-game
```

2. Install Required Libraries
```bash
pip install pygame
```

3. Run the Game
```bash
python main.py
```

## Controls

- Left Click: Click squares, buy upgrades
- Mouse Movement: Move cursor
- Any Key: Start game from intro screen
- Click Pause: Pause game
- Click Play: Resume game

## Game Elements

### Shop Items
1. **Additive Upgrade**
   - Increases timer duration
   - Cost increases by 20% each purchase
   ```python
   additivecost = int(additivecost * 1.2)
   additivenum += 1
   ```

2. **Multiplier Upgrade**
   - Increases points per click
   - Cost increases by 20% each purchase
   ```python
   multipliercost = int(multipliercost * 1.2)
   multipliernum += 1
   ```

## Requirements

- Python 3.x
- Pygame library
- Assets folder with all required images and fonts

## Development Notes

### Asset Creation Process
1. All visual assets were created using digital art tools
2. Pixel-perfect designs for consistent look
3. Custom fonts designed for game aesthetics
4. Multiple variations of assets for different states

### Future Plans
- Additional power-ups
- More visual effects
- High score system
- Achievement system
- Sound effects
- Background music

