# A Life's Random Journey

> Un RPG de texto donde no eliges quién eres. Solo vives lo que te toca.

## 🧠 Descripción

Este es un **RPG de texto único e inmersivo**, donde cada partida es una vida diferente. No eliges tu nombre, género, clase social ni destino inicial. Solo recibes lo que el mundo decide darte… y decides qué hacer con ello.

## 🛠️ Arquitectura del Proyecto

### Backend (Motor del Juego)
- **Tecnología**: Python
- **Base de Datos**: SQLite (local)
- **Ubicación**: `/motor/`

### Frontend (Aplicación Móvil)
- **Tecnología**: React Native + Expo + TypeScript
- **UI Framework**: React Native Paper + NativeBase
- **Ubicación**: `/app/`

## 📋 Estructura del Proyecto

```
proyecto/
├── motor/                  # Código Python del Backend del Juego
│   ├── data/
│   │   ├── nodes/          # Archivos JSON de nodos narrativos
│   │   ├── npcs/           # Datos de NPCs fijos
│   │   ├── items/          # Datos de objetos
│   │   └── locations/      # Datos de ubicaciones y arcos de historia
│   ├── logic/
│   │   ├── game_generator.py # Generación inicial de personaje y mundo
│   │   ├── story_engine.py   # Gestión de ramificaciones narrativas
│   │   ├── character.py      # Modelo de personaje y atributos
│   │   ├── world_events.py   # Lógica de eventos aleatorios
│   │   ├── npc_manager.py    # Lógica para gestión de NPCs
│   │   ├── location_arcs.py  # Lógica para gestionar arcos de historia
│   │   └── utils.py          # Utilidades diversas
│   ├── db/                 # Base de datos local del juego
│   │   └── game.db         # Archivo de la base de datos SQLite
│   └── api.py              # API interna (comunicación con RN)
│
├── app/                    # Código React Native del Frontend
│   ├── src/
│   │   ├── components/     # Componentes de UI reutilizables
│   │   ├── screens/        # Pantallas principales
│   │   ├── services/       # Interacción con la API de Python
│   │   ├── hooks/          # Custom Hooks de React
│   │   ├── context/        # Contextos globales
│   │   ├── themes/         # Definiciones de estilos y temas
│   │   ├── types/          # Definiciones de TypeScript
│   │   ├── utils/          # Utilidades para cálculo responsivo
│   │   └── App.tsx         # Punto de entrada de la aplicación
│   ├── assets/
│   │   ├── images/         # Sprites e imágenes de UI
│   │   ├── audio/          # Archivos de música y SFX
│   │   └── fonts/          # Fuentes personalizadas
│   ├── app.json            # Configuración de Expo
│   ├── package.json        # Dependencias de React Native
│   └── tsconfig.json       # Configuración de TypeScript
├── README.md
└── requirements.txt        # Dependencias de Python
```

## 🚀 Configuración del Entorno

### Prerrequisitos
- Node.js (v18+)
- Python (3.8+)
- Android Studio (para desarrollo Android)
- Expo CLI

### Instalación

#### Backend (Python)
```bash
# Instalar dependencias de Python
pip install -r requirements.txt
```

#### Frontend (React Native)
```bash
# Ir al directorio de la app
cd app

# Instalar dependencias
npm install

# Iniciar el servidor de desarrollo
npm start
```

## 🎯 Características Únicas

- **Sin elección inicial**: El juego genera automáticamente tu personaje y situación inicial
- **Vida ramificada**: Cada decisión te lleva por un camino distinto
- **NPCs condicionales**: Los personajes que conoces dependen de tu trayectoria de vida
- **Fantasía realista**: Mundo mágico pero con consecuencias reales y permanentes
- **Sistema de tiempo**: Envejeces naturalmente y puedes morir en cualquier momento
- **Finales únicos**: Docenas de finales posibles basados en tus acciones
- **Experiencia offline**: Toda la lógica del juego reside en el dispositivo

## 🎨 Diseño UI

- **Completamente responsivo**: Adaptado para pantallas modernas Android
- **Alta calidad de audio**: Música y efectos de sonido inmersivos
- **Interfaz moderna**: Diseño limpio y elegante con Material Design
- **Accesibilidad**: Cumple con estándares WCAG para contraste y usabilidad

## 📱 Plataformas

- **Android**: Optimizado para dispositivos Android modernos
- **Offline**: Funcionalidad completa sin conexión a internet

---

**Estado del proyecto**: ✅ Entorno configurado - Listo para desarrollo 