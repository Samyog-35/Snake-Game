Snake Game in Python (Pygame)
📌 Project Overview

It is a traditional Snake game developed in Python and Pygame with several types of food, timers, obstacles and skin customization system. The game is based on survival, strategy, and score accruing by gathering various fruits with special effects.

🎮 Gameplay Features:


🍎 Food System
Foods have varying effects:

Apple 🍎 → increases survival time
Berry 🫐→ temporarily pauses the survival timer (the game goes on as usual)
Peach 🍑 → gives temporary speed boost
Grape 🍇 → helps to extend the time of survival, depending on the conditions.


🐍 Snake Mechanics:
Traditional grid-based movement system.
Snake develops when it is eating food.
Collision detection with:
Walls
Itself
Obstacles
💥 Obstacles
Obstacles on the map are randomly generated.
Collision with an obstacle causes game over.
⏳ Survival Timer System
The player has to survive with a countdown timer.
Timer decreases over time
Some foods serve to increase the time of survival.
Game is over when timer runs out.



🎨 Skin System
Press 1–4 to change snake color:
Green 🟢
Red 🔴
Blue 🔵
Gold 🟡



📊 Game Features:
Score system
Random food spawning
Restart system (press R)
Introduction screen and game over screen.



🎮 Controls:
Arrow Keys → Move snake
Enter → Start game
R → Restart game
1–4 → Change snake skin




⚙️ How It Works

The game operates based on a grid in which the snake travels cell after cell with a predefined map. Every game loop processes movement time, collision, food time, and survival time. The types of food alter the gameplay by influencing the score, speed or the time of survival.




🚀 Future Improvements
Combo system (bonus on a series of food collection)
Action (eat, collision, power-ups) sound effects.
Effects of particles during food consumption.
Better animations to provide better visual feel.
High score saving system



🛠️ Built With
Python 🐍
Pygame 🎮

