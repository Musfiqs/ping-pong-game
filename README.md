# 🏓 Ping Pong Game

A classic ping pong (Pong) game built with Python and Pygame. Experience the nostalgia of one of the first video games ever created!

## 🎮 Features

- **Two-player local multiplayer** gameplay
- **Smooth paddle movement** with responsive controls
- **Realistic ball physics** with wall and paddle bouncing
- **Score tracking** for both players
- **Clean, minimalist design** with classic arcade aesthetics
- **60 FPS gameplay** for smooth animation
- **Visual feedback** with center line and score display

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Musfiqs/ping-pong-game.git
   cd ping-pong-game
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install pygame directly:
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python ping_pong_game.py
   ```

## 🎯 How to Play

### Controls
- **Left Player (Player 1):**
  - `W` - Move paddle up
  - `S` - Move paddle down

- **Right Player (Player 2):**
  - `↑` (Up Arrow) - Move paddle up
  - `↓` (Down Arrow) - Move paddle down

### Gameplay
- Each player controls a paddle on their side of the screen
- The ball bounces off the top and bottom walls
- Players must hit the ball with their paddle to keep it in play
- When a player misses the ball, the opponent scores a point
- The ball resets to the center after each point with a random direction

### Objective
Score points by making the ball pass your opponent's paddle. There's no set winning score - play until you're satisfied with your victory! 🏆

## 🛠️ Technical Details

### Built With
- **Python 3** - Core programming language
- **Pygame 2.5.2** - Game development library for graphics and input handling

### Game Components
- `Paddle` class - Handles paddle movement and rendering
- `Ball` class - Manages ball physics, collision detection, and rendering
- `PingPongGame` class - Main game loop, event handling, and game state management

### Performance
- Runs at 60 FPS for smooth gameplay
- Optimized collision detection
- Efficient rendering with pygame

## 📁 Project Structure

```
ping-pong-game/
│
├── ping_pong_game.py    # Main game file
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🎨 Game Screenshots

The game features:
- Black background with white paddles and ball
- Gray center line dividing the court
- Score display at the top of the screen
- Control instructions at the bottom

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Ideas for Contributions
- Add AI opponent for single-player mode
- Implement power-ups or special effects
- Add sound effects and background music
- Create different difficulty levels
- Add a main menu and settings screen
- Implement online multiplayer

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Future Enhancements

- [ ] AI opponent with adjustable difficulty
- [ ] Sound effects and background music
- [ ] Particle effects for ball collisions
- [ ] Main menu and settings
- [ ] Tournament mode with multiple rounds
- [ ] Custom paddle colors and themes
- [ ] Online multiplayer support

## 🐛 Bug Reports

If you find any bugs or issues, please open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your system information (OS, Python version)

## 🙏 Acknowledgments

- Inspired by the original Pong game by Atari (1972)
- Built with the awesome Pygame library
- Thanks to the Python community for excellent documentation

---

**Enjoy the game!** 🏓✨

*Made with ❤️ by [Musfiqs](https://github.com/Musfiqs)* 