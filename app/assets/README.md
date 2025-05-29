# Assets del Proyecto

## 📁 Estructura de Assets

Este directorio contiene todos los recursos multimedia del juego:

### 🎨 Iconos y Branding (Pendientes)
Cuando estén disponibles, agregar estos archivos:

- `icon.png` - Icono principal de la app (1024x1024px)
- `adaptive-icon.png` - Icono adaptativo para Android (1024x1024px)
- `splash.png` - Pantalla de carga (1284x2778px para iPhone 13 Pro Max)

### 🖼️ Imágenes del Juego
- `/images/` - Imágenes de escenas y contextos del juego

### 🎵 Audio
- `/audio/` - Música de fondo y efectos de sonido

### 🔤 Fuentes
- `/fonts/` - Fuentes personalizadas para la UI

## 🛠️ Configuración Actual

**Estado**: Los assets gráficos han sido temporalmente removidos de `app.json` para evitar errores de validación.

**Para reactivar los assets:**
1. Agregar los archivos de imagen correspondientes a este directorio
2. Descomentar las líneas en `app.json`:
   ```json
   {
     "expo": {
       "icon": "./assets/icon.png",
       "splash": {
         "image": "./assets/splash.png"
       },
       "android": {
         "adaptiveIcon": {
           "foregroundImage": "./assets/adaptive-icon.png"
         }
       }
     }
   }
   ```

## 📋 Especificaciones de Assets

### Iconos
- **Formato**: PNG con transparencia
- **Tamaño**: 1024x1024px mínimo
- **Estilo**: Acorde al tema del juego (fantasía oscura/realista)

### Splash Screen
- **Formato**: PNG
- **Tamaño**: Resoluciones múltiples para diferentes dispositivos
- **Contenido**: Logo del juego + fondo temático

### Imágenes del Juego
- **Formato**: WebP (preferido) o PNG
- **Resoluciones**: @2x, @3x, @4x para diferentes densidades
- **Optimización**: Comprimidas para reducir tamaño del APK 