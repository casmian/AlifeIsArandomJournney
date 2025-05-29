# 📱 Guía de Compilación APK - v0.1

## ⚠️ IMPORTANTE: Buildozer en Windows

**Buildozer no funciona nativamente en Windows.** Necesitas una de estas opciones:

### 🐧 Opción 1: WSL (Windows Subsystem for Linux) - RECOMENDADO

```bash
# Instalar WSL en Windows
wsl --install Ubuntu

# Una vez en WSL Ubuntu:
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Instalar Python y Kivy dependencies
pip3 install --upgrade pip
pip3 install buildozer cython

# Clonar el proyecto
git clone https://github.com/casmian/AlifeIsArandomJournney.git
cd AlifeIsArandomJournney/game

# Compilar APK
buildozer android debug
```

### 🐳 Opción 2: Docker

```bash
# Crear Dockerfile
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

RUN pip3 install buildozer cython

WORKDIR /app
COPY . .

CMD ["buildozer", "android", "debug"]
```

### 🌐 Opción 3: GitHub Actions (CI/CD) - AUTOMÁTICO

```yaml
# .github/workflows/build-android.yml
name: Build Android APK

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
        pip install buildozer cython
    
    - name: Build APK
      run: |
        cd game
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: apk-debug
        path: game/bin/*.apk
```

## 📋 Preparativos Completados

### ✅ Archivos Listos para Compilación:
- 🎮 **main.py** - Aplicación principal optimizada para móvil
- 📱 **buildozer.spec** - Configuración Android completa
- 🎨 **assets/** - Fuentes, música, imágenes (12.3 MB total)
- 🖼️ **ui/** - Interfaces .kv optimizadas para táctil

### ✅ Configuración buildozer.spec:
```ini
title = A Life Is A Random Journey
package.name = alifeisarandomjourney
package.domain = org.alifegame
version = 0.1
requirements = python3,kivy,kivymd,sqlite3,sqlalchemy,numpy,plyer
orientation = portrait
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
```

### ✅ Recursos Incluidos:
- 🎵 Música: The Bard's Tale (5.1MB) + batallas (7.1MB)
- ✍️ Fuentes: pixel_font.ttf + PressStart2P-Regular.ttf
- 🖼️ Imágenes: placeholder_scene.png
- 📋 UI: main_menu.kv + game_screen.kv

## 🎯 APK Esperado

### 📦 Características del APK:
- **Nombre**: `alifeisarandomjourney-0.1-debug.apk`
- **Tamaño esperado**: ~15-20 MB
- **Orientación**: Solo vertical (portrait)
- **API mínima**: Android 5.0 (API 21)
- **Arquitecturas**: ARM64 + ARMv7 (compatible con 99% dispositivos)
- **Permisos**: Mínimos (solo almacenamiento interno)

### 🎮 Funcionalidades:
- ✅ Menú principal con animaciones
- ✅ Navegación táctil fluida
- ✅ Audio de alta calidad (música de fondo)
- ✅ Controles de configuración
- ✅ Fuentes pixeladas auténticas
- ✅ Interfaz optimizada 360x640 (escalable)

## 🚀 Próximos Pasos RECOMENDADOS

### Opción A: WSL (Más simple)
1. Instalar WSL Ubuntu en Windows
2. Seguir comandos de la sección WSL
3. Compilar directamente

### Opción B: GitHub Actions (Automático)
1. Hacer push del código a GitHub
2. Crear tag `v0.1`
3. El APK se genera automáticamente
4. Descargar desde Actions

### Opción C: Colaboración
1. Compartir código conmigo para compilar en Linux
2. Te devuelvo el APK compilado
3. Tú haces las pruebas móviles

## 📱 Plan de Testing

### Una vez tengas el APK:
1. **Instalar** en tu dispositivo Android
2. **Probar todas las funciones**:
   - Menú principal (navegación, música)
   - Transición al juego
   - Botones táctiles
   - Audio (volumen, toggle)
   - Configuración
3. **Documentar**:
   - Capturas de pantalla
   - Especificaciones de tu dispositivo
   - Problemas encontrados
   - Sugerencias de mejora

---
**🎯 Objetivo**: APK funcional v0.1 para testing móvil real 