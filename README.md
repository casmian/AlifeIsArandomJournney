# 🎮 A Life Is A Random Journey

> Un RPG de texto donde no eliges quién eres. Solo vives lo que te toca.

**Un RPG de texto único e inmersivo**, donde cada partida es una vida diferente, **inspirado en la simulación profunda y la generación de narrativa emergente de Dwarf Fortress**. Con una **interfaz de usuario que evoca el estilo pixelado y nostálgico de Undertale/Deltarune**, optimizada para Android.

## 🎯 **Filosofía del Juego**

*"No eliges quién eres. Solo vives lo que te toca."*

- 🧬 **Generación procedural profunda** de personaje, familia y mundo inicial
- 🌍 **NPCs dinámicos** con historias que se cruzan condicionalmente  
- 🎭 **Arcos de historia** específicos por localización
- ⚡ **Sistemas interconectados** donde todo puede afectar todo
- 📱 **Experiencia offline total** en Android

## 🛠️ **Stack Tecnológico**

- **Framework**: Flutter 3.x + Dart
- **UI**: Widgets nativos + Custom Paint para pixel art
- **Audio**: audioplayers package para música CC0
- **Fuentes**: Google Fonts + custom pixel fonts  
- **Base de datos**: Hive (local NoSQL) + SQLite
- **Compilación**: Flutter build apk/appbundle para Android

## 🎨 **Assets Incluidos**

### 🎵 **Música CC0:**
- **Menu Music**: "The Bard's Tale" por RandomMind
- **Battle Music**: "8-Bit Battle Loop" por Wolfgang_  
- **Battle Theme**: "8 bit battle theme" por celestialghost8

### ✍️ **Fuentes Pixeladas:**
- **Press Start 2P**: Fuente principal retro
- **Determination Mono**: Estilo Undertale/Deltarune

## 🚀 **Comandos de Desarrollo**

```bash
# Crear proyecto Flutter
flutter create . --org com.alifegame

# Ejecutar en desarrollo
flutter run

# Compilar APK
flutter build apk

# Compilar para Google Play Store
flutter build appbundle
```

## 📁 **Estructura del Proyecto**

```
assets/
├── audio/          # 🎵 Música CC0 y efectos
│   ├── menu_music.mp3
│   ├── battle_music.ogg
│   └── battle_theme.wav
└── fonts/          # ✍️ Fuentes pixeladas
    ├── PressStart2P-Regular.ttf
    └── pixel_font.ttf
```

## 🎮 **Estado del Proyecto**

**🔄 En Migración: Python+Kivy → Flutter+Dart**

- ✅ **Assets preservados**: Música CC0 y fuentes pixeladas
- ✅ **Concepto intacto**: Todas las mecánicas de juego planificadas
- 🔄 **Implementación**: Próximo paso - setup inicial Flutter
- 🎯 **Objetivo**: APK confiable para Google Play Store

## 📜 **Licencias**

- **Código**: MIT License
- **Música**: CC0 (ver ATTRIBUTION.txt)
- **Fuentes**: Open Font License

---

*Un proyecto que combina la profundidad narrativa de Dwarf Fortress con la estética nostálgica de Undertale, optimizado para la experiencia móvil moderna.*
