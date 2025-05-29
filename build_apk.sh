#!/bin/bash
# Script de compilación APK - A Life Is A Random Journey
# Para usar en WSL Ubuntu o Linux

echo "🎮 A Life Is A Random Journey - Compilador APK"
echo "=============================================="

# Verificar si estamos en el directorio correcto
if [ ! -f "game/main.py" ]; then
    echo "❌ Error: Ejecuta este script desde el directorio raíz del proyecto"
    exit 1
fi

echo "📋 Verificando dependencias del sistema..."

# Verificar si buildozer está instalado
if ! command -v buildozer &> /dev/null; then
    echo "⚠️ Buildozer no está instalado. Instalando dependencias..."
    
    # Actualizar paquetes
    sudo apt update
    
    # Instalar dependencias del sistema
    sudo apt install -y \
        git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config \
        zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake \
        libffi-dev libssl-dev libltdl-dev
    
    # Instalar buildozer y cython
    pip3 install --upgrade pip
    pip3 install buildozer cython
    
    echo "✅ Dependencias instaladas"
else
    echo "✅ Buildozer ya está instalado"
fi

echo "🎯 Cambiando al directorio del juego..."
cd game

echo "🏗️ Iniciando compilación APK..."
echo "⏳ Este proceso puede tomar 10-30 minutos en la primera ejecución..."

# Compilar APK
if buildozer android debug; then
    echo ""
    echo "🎉 ¡COMPILACIÓN EXITOSA!"
    echo "📱 APK generado en: game/bin/"
    
    # Mostrar información del APK
    if [ -f "bin/alifeisarandomjourney-0.1-debug.apk" ]; then
        APK_SIZE=$(du -h bin/alifeisarandomjourney-0.1-debug.apk | cut -f1)
        echo "📦 Archivo: alifeisarandomjourney-0.1-debug.apk"
        echo "📏 Tamaño: $APK_SIZE"
        echo ""
        echo "🚀 Para instalar en tu dispositivo Android:"
        echo "   1. Habilita 'Orígenes desconocidos' en Configuración"
        echo "   2. Transfiere el APK a tu dispositivo"
        echo "   3. Abre el archivo APK e instala"
        echo ""
        echo "📋 Para testing, copia el APK a la carpeta tests/v0.1-mobile-test/"
        
        # Copiar APK a carpeta de tests si existe
        if [ -d "../tests/v0.1-mobile-test" ]; then
            cp bin/alifeisarandomjourney-0.1-debug.apk ../tests/v0.1-mobile-test/
            echo "✅ APK copiado a carpeta de tests"
        fi
    fi
else
    echo "❌ Error en la compilación"
    echo "📋 Revisa los errores arriba y verifica:"
    echo "   - Todas las dependencias están instaladas"
    echo "   - El archivo buildozer.spec está configurado correctamente"
    echo "   - Los archivos del proyecto están presentes"
    exit 1
fi

echo ""
echo "🎯 ¡Listo para testing móvil!" 