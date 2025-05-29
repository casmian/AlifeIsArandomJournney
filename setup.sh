#!/bin/bash

echo "🚀 Configurando entorno para A Life's Random Journey..."

# Verificar prerrequisitos
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no encontrado. Por favor instalar Python 3.8+."
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js no encontrado. Por favor instalar Node.js 18+."
    exit 1
fi

echo "✅ Prerrequisitos verificados"

# Configurar backend Python
echo "📦 Instalando dependencias de Python..."
pip install -r requirements.txt

# Configurar frontend React Native
echo "📦 Instalando dependencias de React Native..."
cd app
npm install

# Crear directorios db si no existen
if [ ! -d "../motor/db" ]; then
    mkdir -p ../motor/db
fi

echo "✅ Entorno configurado correctamente"
echo "🎯 Para iniciar el desarrollo:"
echo "   Backend: python motor/api.py"
echo "   Frontend: cd app && npm start" 