# Snake Jungle Edition

Snake Jungle Edition es una versión moderna y temática del clásico juego **Snake**, desarrollado en **Python** con la librería **Pygame**. El jugador controla una serpiente en un entorno de jungla, comiendo ratones para crecer, evitando obstáculos (troncos) y recolectando la mayor puntuación posible.

## Integrantes del grupo
- Erick Antonio Cedeño Loor

## Fecha de entrega
1 de Marzo 2025

## Objetivo del programa
Crear un juego entretenido y educativo que aplique conceptos clave de programación orientada a objetos, manejo de eventos, persistencia de datos, gráficos 2D y sonido utilizando **Pygame**, mientras se mantiene una experiencia jugable y visualmente atractiva con temática de jungla.

## Principales funcionalidades

- **Menú inicial interactivo**  
  - Ingreso de nombre del jugador (con soporte para backspace y límite de caracteres)  
  - Muestra clara de reglas del juego  
  - Presionar ENTER para comenzar

- **Mecánicas del juego**  
  - Control de la serpiente con flechas del teclado (evita giros de 180°)  
  - Comer ratón → +2 puntos, serpiente crece, nueva comida aparece  
  - Velocidad aumenta progresivamente cada 5 comidas  
  - Colisiones con bordes, cuerpo propio y obstáculos → game over  
  - Obstáculos fijos (10 troncos generados aleatoriamente, no se superponen con serpiente inicial)

- **Elementos visuales**  
  - Fondo de jungla (assets/jungle_bg.jpg)  
  - Serpiente con degradado de verde + ojos y boca  
  - Comida (ratón) con orejas y ojos simples  
  - Obstáculos representados como troncos marrones con textura

- **Sonido y música**  
  - Efecto de sonido al comer (eat.wav)  
  - Sonido de game over (game_over.wav)  
  - Música de fondo en loop (opcional: jungle_music.mp3)

- **Sistema de puntuación y récord**  
  - Muestra en tiempo real: Score, Record y Nombre del jugador  
  - Récord persistente guardado en archivo `highscore.txt`  
  - Se actualiza solo si se supera el récord anterior

- **Pantalla de Game Over**  
  - Mensaje “¡CHOCASTE!” con puntaje final  
  - Opciones: **R** para reiniciar, **ESC** para salir

- **Robustez**  
  - Manejo de errores con `try-except` para archivos de imagen y sonido faltantes  
  - No se rompe el juego si faltan assets

## Requisitos para ejecutar

- Python 3.8 o superior  
- Pygame (`pip install pygame`)

```bash
# Instalación recomendada
pip install pygame
Estructura del proyecto
textSNAKE GAME/
├── assets/                  # Imágenes y sonidos
│   ├── jungle_bg.jpg
│   ├── eat.wav
│   ├── game_over.wav
│   └── jungle_music.mp3   (opcional)
├── main.py                  # Archivo principal (flujo del juego)
├── settings.py              # Constantes, colores y configuración
├── snake.py                 # Clase Snake
├── food.py                  # Clase Food
├── obstacles.py             # Clase Obstacles
├── highscore.txt            # Archivo generado automáticamente
└── README.md
