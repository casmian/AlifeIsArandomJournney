# 🎮 A Life Is A Random Journey

> Un RPG de texto donde no eliges quién eres. Solo vives lo que te toca.

## 🧠 Descripción

Este es un **RPG de texto único e inmersivo**, donde cada partida es una vida diferente, **inspirado en la simulación profunda y la generación de narrativa emergente de Dwarf Fortress**. No eliges tu nombre, género, clase social ni destino inicial. Solo recibes lo que el mundo decide darte… y decides qué hacer con ello.

El juego cuenta con una **interfaz de usuario que evoca el estilo pixelado y nostálgico de Undertale/Deltarune**, ejecutándose con fluidez en dispositivos Android y acompañada de **audio de alta calidad** para una inmersión profunda.

## 🛠️ Tecnologías

- **Python** con **Kivy** para la interfaz de usuario
- **SQLite** para persistencia local de datos
- **Buildozer** para compilación Android
- **Pixel Art** estilo retro para gráficos
- **Audio de alta calidad** para inmersión

## 📁 Estructura del Proyecto

```
proyecto/
├── game/                   # Código principal de la aplicación
│   ├── data/              # Datos del juego (JSON)
│   │   ├── nodes/         # Nodos narrativos
│   │   ├── npcs/          # Datos de NPCs
│   │   ├── locations/     # Ubicaciones y arcos
│   │   └── items/         # Objetos del juego
│   ├── assets/            # Recursos multimedia
│   │   ├── images/        # Pixel art (PNG)
│   │   ├── audio/         # Música y efectos (OGG, MP3)
│   │   └── fonts/         # Fuentes pixeladas
│   ├── logic/             # Lógica del juego
│   ├── db/                # Base de datos SQLite
│   ├── ui/                # Interfaz de usuario (Kivy)
│   ├── main.py            # Punto de entrada
│   └── buildozer.spec     # Configuración Android
├── requirements.txt       # Dependencias Python
└── README.md             # Este archivo
```

## 🚀 Instalación y Desarrollo

### Requisitos previos
- Python 3.8+
- Kivy
- Buildozer (para compilación Android)

### Configuración del entorno

```bash
# Instalar dependencias
pip install -r requirements.txt

# Para desarrollo en Android, instalar buildozer
pip install buildozer
```

### Ejecutar en desarrollo

```bash
cd game
python main.py
```

### Compilar para Android

```bash
cd game
buildozer android debug
```

## 🎯 Características Principales

- **Generación de Vida Profunda**: Cada partida genera una historia única
- **NPCs Complejos**: Personajes con historias emergentes
- **Arcos de Localización**: Historias basadas en ubicaciones
- **Sistema de Legado**: Tus acciones afectan futuras partidas
- **Offline Completo**: Toda la lógica reside en el dispositivo
- **Estilo Retro**: UI pixelada inspirada en Undertale/Deltarune

## 📜 Licencia

[Especificar licencia aquí]

## 🤝 Contribución

[Especificar guías de contribución aquí] 