# Space Shooter

A fast-paced 2D space shooter built with Python & Pygame. Dodge meteors, blast them out of the sky, and survive as long as you can.

---

## Gameplay

You're a lone spaceship in a field of incoming meteors. Shoot them down before they reach you — one hit and it's over. Your score keeps ticking as long as you're alive, so the longer you last, the better.

---

## Features

- Smooth player movement with diagonal normalization
- Laser shooting with cooldown system
- Randomly spawning, rotating meteors
- Animated explosions on impact
- Pixel-perfect collision detection via masks
- Background music + sound effects
- Live score display

---

## Tech Stack

- **Python 3**
- **Pygame-ce** (sprite groups, masks, custom events, delta-time movement)

---

## 📁 Project Structure

```
space-shooter/
├── Code /
│   ├── main.py
│   ├── settings.py
│   ├── sprites.py
├── audio/
└── images/
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/space-shooter.git
cd space-shooter
```

**2. Install dependencies**
```bash
pip install pygame
```

**3. Run the game**
```bash
python main.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `↑ ↓ ← →` | Move |
| `Space` | Shoot |

---

## Notes

- Make sure all assets (images + audio) are in their correct folders before running (^^)
- The score is time-based — every 100ms alive counts.

---

*Built for fun. Designed to be extended. ( •̀ ω •́ )✧*
