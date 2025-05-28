# Script de configuración para A Life's Random Journey - Windows
Write-Host "🚀 Configurando entorno para A Life's Random Journey..." -ForegroundColor Green

# Verificar prerrequisitos
try {
    python --version | Out-Null
    Write-Host "✅ Python encontrado" -ForegroundColor Green
} catch {
    Write-Host "❌ Python 3 no encontrado. Por favor instalar Python 3.8+." -ForegroundColor Red
    exit 1
}

try {
    node --version | Out-Null
    Write-Host "✅ Node.js encontrado" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js no encontrado. Por favor instalar Node.js 18+." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Prerrequisitos verificados" -ForegroundColor Green

# Configurar backend Python
Write-Host "📦 Instalando dependencias de Python..." -ForegroundColor Yellow
pip install -r requirements.txt

# Configurar frontend React Native
Write-Host "📦 Instalando dependencias de React Native..." -ForegroundColor Yellow
Set-Location app
npm install
Set-Location ..

# Crear directorios db si no existen
if (!(Test-Path "motor/db")) {
    New-Item -ItemType Directory -Path "motor/db" -Force
}

Write-Host "✅ Entorno configurado correctamente" -ForegroundColor Green
Write-Host "🎯 Para iniciar el desarrollo:" -ForegroundColor Cyan
Write-Host "   Backend: python motor/api.py" -ForegroundColor White
Write-Host "   Frontend: cd app && npm start" -ForegroundColor White 