#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Life Is A Random Journey - Aplicación Kivy Principal
Un RPG de texto donde no eliges quién eres. Solo vives lo que te toca.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
import platform
import os
import math
import time
import random

# Configuración de ventana para desarrollo
if platform.system() != 'Android':
    Window.size = (360, 640)  # Tamaño más realista para móvil moderno (9:16)
    Window.minimum_width = 360
    Window.minimum_height = 640


class AudioManager:
    """Gestor de audio para música y efectos de sonido"""
    
    def __init__(self):
        self.background_music = None
        self.music_volume = 0.7
        self.sfx_volume = 0.8
        self.music_enabled = True
        self.sfx_enabled = True
        
    def load_background_music(self, music_file):
        """Cargar música de fondo"""
        if os.path.exists(music_file):
            try:
                self.background_music = SoundLoader.load(music_file)
                if self.background_music:
                    self.background_music.loop = True
                    self.background_music.volume = self.music_volume
                    print(f"🎵 Música cargada: {music_file}")
                    return True
                else:
                    print(f"⚠️ No se pudo cargar la música: {music_file}")
            except Exception as e:
                print(f"❌ Error cargando música: {e}")
        else:
            print(f"📝 Archivo de música no encontrado: {music_file}")
        return False
    
    def load_menu_music(self):
        """Cargar música específica del menú"""
        menu_music_path = "assets/audio/menu_music.mp3"
        return self.load_background_music(menu_music_path)
    
    def play_background_music(self):
        """Reproducir música de fondo"""
        if self.background_music and self.music_enabled:
            if self.background_music.state == 'stop':
                self.background_music.play()
                print("🎵 Música de fondo iniciada")
    
    def stop_background_music(self):
        """Detener música de fondo"""
        if self.background_music:
            self.background_music.stop()
            print("🎵 Música de fondo detenida")
    
    def play_sfx(self, sfx_file):
        """Reproducir efecto de sonido"""
        if self.sfx_enabled and os.path.exists(sfx_file):
            try:
                sound = SoundLoader.load(sfx_file)
                if sound:
                    sound.volume = self.sfx_volume
                    sound.play()
                    return True
            except Exception as e:
                print(f"⚠️ Error reproduciendo SFX: {e}")
        return False
    
    def set_music_volume(self, volume):
        """Establecer volumen de música (0.0 - 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        if self.background_music:
            self.background_music.volume = self.music_volume
    
    def toggle_music(self):
        """Alternar música on/off"""
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            self.play_background_music()
        else:
            self.stop_background_music()
        return self.music_enabled


class GameScreen(BoxLayout):
    """Pantalla principal del juego con interfaz retro y animaciones"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Variables para animaciones
        self.animation_time = 0
        self.text_animation_index = 0
        self.full_text = ""
        self.typewriter_active = False
        
        # Programar animaciones
        Clock.schedule_interval(self.update_animations, 0.1)
    
    def update_animations(self, dt):
        """Actualizar animaciones sutiles estilo Undertale/Deltarune/Celeste"""
        self.animation_time += dt
        
        # Animación de "breathing" para los contenedores de opciones
        if hasattr(self.ids, 'option1_container'):
            # Efecto pulsante sutil para la opción destacada
            pulse = 1.0 + 0.05 * math.sin(self.animation_time * 3)
            # Cambiar ligeramente el color del borde para crear efecto glow
            glow_intensity = 0.8 + 0.2 * math.sin(self.animation_time * 2)
            
            # Actualizar el canvas si es posible (esto es más avanzado)
            # Por ahora, solo registramos la animación
        
        # Continuar animación typewriter si está activa
        if self.typewriter_active and hasattr(self.ids, 'narrative_text'):
            self.update_typewriter_effect()
    
    def start_typewriter_effect(self, text):
        """Iniciar efecto typewriter para el texto narrativo"""
        self.full_text = text
        self.text_animation_index = 0
        self.typewriter_active = True
        
        if hasattr(self.ids, 'narrative_text'):
            self.ids.narrative_text.text = ""
    
    def update_typewriter_effect(self):
        """Actualizar el efecto typewriter"""
        if self.text_animation_index < len(self.full_text):
            # Añadir caracteres gradualmente
            if self.animation_time % 0.03 < 0.03:  # Cada 30ms aprox
                current_text = self.full_text[:self.text_animation_index + 1]
                if hasattr(self.ids, 'narrative_text'):
                    self.ids.narrative_text.text = current_text
                self.text_animation_index += 1
        else:
            self.typewriter_active = False
    
    def load_scene_data(self, scene_image=None, narrative_text=None, options=None):
        """Cargar datos de una nueva escena en la interfaz con animaciones"""
        
        # Actualizar imagen de la escena con fade
        if scene_image and hasattr(self.ids, 'scene_image'):
            # Fade out y fade in sutil
            anim_out = Animation(opacity=0, duration=0.3)
            anim_in = Animation(opacity=1, duration=0.3)
            
            def change_image(animation, widget):
                widget.source = scene_image
            
            anim_out.bind(on_complete=change_image)
            sequence = anim_out + anim_in
            sequence.start(self.ids.scene_image)
        
        # Actualizar texto narrativo con efecto typewriter
        if narrative_text:
            self.start_typewriter_effect(narrative_text)
        
        # Actualizar opciones con animación staggered
        if options:
            if len(options) > 0 and hasattr(self.ids, 'option_1'):
                # Animar entrada de opciones con retraso
                def update_option_1(dt):
                    self.ids.option_1.text = f"* {options[0]}"
                    # Pequeña animación de escala
                    self.ids.option_1.opacity = 0
                    anim = Animation(opacity=1, duration=0.4)
                    anim.start(self.ids.option_1)
                
                Clock.schedule_once(update_option_1, 0.5)
            
            if len(options) > 1 and hasattr(self.ids, 'option_2'):
                def update_option_2(dt):
                    self.ids.option_2.text = f"* {options[1]}"
                    self.ids.option_2.opacity = 0
                    anim = Animation(opacity=1, duration=0.4)
                    anim.start(self.ids.option_2)
                
                Clock.schedule_once(update_option_2, 0.8)
    
    def apply_pixel_font_if_available(self):
        """Aplicar fuente pixelada si está disponible"""
        # Priorizar pixel_font.ttf por defecto
        font_paths = [
            "assets/fonts/pixel_font.ttf",      # Determination Mono (prioridad)
            "assets/fonts/PressStart2P-Regular.ttf"  # Backup
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                print(f"✅ Aplicando fuente pixelada: {font_path}")
                
                # Aplicar a todos los labels del menú
                if hasattr(self, 'ids'):
                    if hasattr(self.ids, 'title_label'):
                        self.ids.title_label.font_name = font_path
                    if hasattr(self.ids, 'subtitle_label'):
                        self.ids.subtitle_label.font_name = font_path
                    if hasattr(self.ids, 'start_button'):
                        self.ids.start_button.font_name = font_path
                    if hasattr(self.ids, 'config_button'):
                        self.ids.config_button.font_name = font_path
                    if hasattr(self.ids, 'exit_button'):
                        self.ids.exit_button.font_name = font_path
                
                self.current_font = font_path
                return True
        
        print("📝 Usando fuente por defecto (fuente pixelada no encontrada)")
        return False


class MainMenuScreen(BoxLayout):
    """Pantalla del menú principal con interfaz retro optimizada para móvil"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Programar aplicación de fuente después de construcción
        Clock.schedule_once(self.apply_pixel_font_if_available, 0.1)
        
        # Variables para animaciones
        self.breathing_direction = 1
        self.fade_alpha = 1.0
        self.glow_intensity = 0.5
        
        # Programar animaciones
        Clock.schedule_interval(self.update_animations, 1/30)  # 30 FPS
    
    def start_new_game(self):
        """Iniciar nueva aventura"""
        print("🎮 Iniciando nueva aventura...")
        # Cambiar a pantalla de juego
        app = App.get_running_app()
        app.switch_to_game()
    
    def open_config(self):
        """Abrir configuración"""
        print("⚙️ Configuración (en desarrollo)")
        # Aquí se implementará la pantalla de configuración
        app = App.get_running_app()
        if hasattr(app.audio_manager, 'music_enabled'):
            current_state = "ON" if app.audio_manager.music_enabled else "OFF"
            volume_percent = int(app.audio_manager.music_volume * 100)
            print(f"🎵 Música: {current_state} (Volumen: {volume_percent}%)")
            
            # Toggle música para demo
            app.audio_manager.toggle_music()
            new_state = "ON" if app.audio_manager.music_enabled else "OFF"
            print(f"🎵 Música cambiada a: {new_state}")
    
    def exit_game(self):
        """Salir del juego"""
        print("👋 Saliendo del juego...")
        app = App.get_running_app()
        app.stop()
    
    def update_animations(self, dt):
        """Actualizar animaciones sutiles"""
        # Breathing animation para el título
        if hasattr(self, 'ids') and hasattr(self.ids, 'title_label'):
            self.breathing_direction *= -1 if random.random() < 0.01 else 1
            
        # Efecto de fade sutil
        self.fade_alpha += (random.random() - 0.5) * 0.02
        self.fade_alpha = max(0.8, min(1.0, self.fade_alpha))
        
        # Glow del botón principal
        self.glow_intensity += (random.random() - 0.5) * 0.05
        self.glow_intensity = max(0.3, min(0.8, self.glow_intensity))

    def apply_pixel_font_if_available(self, dt=None):
        """Aplicar fuente pixelada si está disponible"""
        # Priorizar pixel_font.ttf por defecto
        font_paths = [
            "assets/fonts/pixel_font.ttf",      # Determination Mono (prioridad)
            "assets/fonts/PressStart2P-Regular.ttf"  # Backup
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                print(f"✅ Aplicando fuente pixelada al menú: {font_path}")
                
                # Aplicar a todos los labels del menú
                if hasattr(self, 'ids'):
                    if hasattr(self.ids, 'title_label'):
                        self.ids.title_label.font_name = font_path
                    if hasattr(self.ids, 'subtitle_label'):
                        self.ids.subtitle_label.font_name = font_path
                    if hasattr(self.ids, 'start_button'):
                        self.ids.start_button.font_name = font_path
                    if hasattr(self.ids, 'config_button'):
                        self.ids.config_button.font_name = font_path
                    if hasattr(self.ids, 'exit_button'):
                        self.ids.exit_button.font_name = font_path
                
                self.current_font = font_path
                return True
        
        print("📝 Usando fuente por defecto (fuente pixelada no encontrada)")
        return False


class LifeJourneyApp(App):
    """Aplicación principal optimizada para APK móvil"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.audio_manager = AudioManager()
        self.current_screen = "menu"  # Iniciar en menú
        
    def build(self):
        """Construir la aplicación principal"""
        print("🎮 A Life Is A Random Journey - Aplicación iniciada")
        print("🎨 Interfaz: Estilo Negro + Animaciones Undertale/Deltarune/Celeste")
        print("🎵 Audio: Sistema de música y efectos implementado")
        print("📱 Modo: Desarrollo local")
        
        # Verificar recursos
        self.verify_resources()
        
        # Cargar archivos de interfaz
        try:
            Builder.load_file('ui/main_menu.kv')
            print("✅ Interfaz del menú principal cargada")
        except Exception as e:
            print(f"⚠️ Error cargando menú principal: {e}")
        
        # Crear pantalla principal (menú)
        self.main_menu = MainMenuScreen()
        
        # Cargar pantalla de juego
        try:
            Builder.load_file('ui/game_screen.kv')
            self.game_screen = GameScreen()
            print("✅ Interfaz del juego cargada")
        except Exception as e:
            print(f"⚠️ Error cargando pantalla de juego: {e}")
            self.game_screen = None
        
        # Configurar audio
        self.audio_manager.load_menu_music()
        
        # Iniciar música de fondo
        if self.audio_manager.background_music:
            self.audio_manager.play_background_music()
        
        # Retornar pantalla inicial (menú)
        return self.main_menu
    
    def switch_to_game(self):
        """Cambiar a la pantalla de juego"""
        if self.game_screen:
            print("🎮 Cambiando a pantalla de juego...")
            self.current_screen = "game"
            # Cambiar el widget raíz
            self.root_window.remove_widget(self.root)
            self.root = self.game_screen
            self.root_window.add_widget(self.root)
            # Aplicar fuente al juego también
            if hasattr(self.game_screen, 'apply_pixel_font_if_available'):
                self.game_screen.apply_pixel_font_if_available()
        else:
            print("❌ Pantalla de juego no disponible")
    
    def switch_to_menu(self):
        """Cambiar de vuelta al menú principal"""
        if self.main_menu:
            print("📋 Regresando al menú principal...")
            self.current_screen = "menu"
            self.root_window.remove_widget(self.root)
            self.root = self.main_menu
            self.root_window.add_widget(self.root)
    
    def on_option_selected(self, option_number, option_text):
        """Manejar la selección de opciones en el juego"""
        print(f"🎯 Opción seleccionada: {option_number} - {option_text}")
        
        # Aquí se implementará la lógica del juego
        # Por ahora, solo registramos la selección
        if option_number == 1:
            print("💼 Elegiste trabajar desde joven")
            # Aquí iría la lógica para esa opción
        elif option_number == 2:
            print("📚 Elegiste buscar educación")
            # Aquí iría la lógica para esa opción
        
        # Placeholder: regresamos al menú por ahora
        print("🔄 (Demo) Regresando al menú principal...")
        self.switch_to_menu()
    
    def verify_resources(self):
        """Verificar que todos los recursos están disponibles"""
        print("\n📋 Verificando recursos:")
        
        # Verificar imagen
        image_path = "assets/images/placeholder_scene.png"
        if os.path.exists(image_path):
            print(f"✅ Imagen de escena: {image_path}")
        else:
            print(f"⚠️ Imagen faltante: {image_path}")
        
        # Verificar fuentes (priorizar pixel_font.ttf)
        fonts = [
            ("Determination Mono (principal)", "assets/fonts/pixel_font.ttf"),
            ("Press Start 2P (backup)", "assets/fonts/PressStart2P-Regular.ttf")
        ]
        
        for desc, font_path in fonts:
            if os.path.exists(font_path):
                print(f"✅ {desc}: {font_path}")
            else:
                print(f"⚠️ {desc}: {font_path} - NO ENCONTRADO")
        
        # Verificar música
        music_path = "assets/audio/menu_music.mp3"
        if os.path.exists(music_path):
            print(f"✅ Música del menú: {music_path}")
        else:
            print(f"⚠️ Música faltante: {music_path}")
        
        # Verificar archivos UI
        ui_files = [
            ("ui/main_menu.kv", "Archivo de menú principal"),
            ("ui/game_screen.kv", "Archivo de pantalla de juego")
        ]
        
        for file_path, desc in ui_files:
            if os.path.exists(file_path):
                print(f"✅ {desc}: {file_path}")
            else:
                print(f"⚠️ {desc}: {file_path} - NO ENCONTRADO")
        
        print()  # Línea en blanco para separar


def main():
    """Función principal"""
    print("🚀 Iniciando A Life Is A Random Journey...")
    print("🎯 Versión: 0.1 (Desarrollo)")
    print("🎨 Interfaz: Estilo Negro + Animaciones Undertale/Deltarune/Celeste")
    print("🎮 Menú Principal con Animaciones")
    print("🎵 Sistema de Audio: Música y Efectos")
    print("✨ Efectos: Typewriter, Fade, Breathing, Glow")
    
    try:
        app = LifeJourneyApp()
        app.run()
    except Exception as e:
        print(f"❌ Error al iniciar la aplicación: {e}")
        raise


if __name__ == '__main__':
    main() 