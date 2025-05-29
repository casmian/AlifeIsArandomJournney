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

# Configuración de ventana para desarrollo
if platform.system() != 'Android':
    Window.size = (480, 800)  # Simular pantalla de móvil en desarrollo


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
        # Primero intentar con PressStart2P, luego con pixel_font.ttf genérica
        font_paths = [
            'assets/fonts/PressStart2P-Regular.ttf',
            'assets/fonts/pixel_font.ttf'
        ]
        
        font_applied = False
        for pixel_font_path in font_paths:
            if os.path.exists(pixel_font_path):
                print(f"✅ Aplicando fuente pixelada: {pixel_font_path}")
                
                # Aplicar a elementos de texto
                if hasattr(self.ids, 'narrative_text'):
                    self.ids.narrative_text.font_name = pixel_font_path
                
                if hasattr(self.ids, 'option_1'):
                    self.ids.option_1.font_name = pixel_font_path
                    
                if hasattr(self.ids, 'option_2'):
                    self.ids.option_2.font_name = pixel_font_path
                
                font_applied = True
                break
        
        if not font_applied:
            print(f"📝 Usando fuente por defecto (fuente pixelada no encontrada)")


class MainMenuScreen(BoxLayout):
    """Pantalla de menú principal estilo Undertale con animaciones y audio"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Variables para animaciones del menú
        self.menu_animation_time = 0
        self.title_pulse_direction = 1
        self.button_glow_intensity = 0.8
        
        # Aplicar fuente después de la inicialización
        Clock.schedule_once(self.apply_pixel_font_if_available, 0.1)
        
        # Iniciar animaciones del menú
        Clock.schedule_interval(self.update_menu_animations, 0.05)  # 20fps para suavidad
        
        # Animación de entrada del menú
        Clock.schedule_once(self.animate_menu_entrance, 0.2)
    
    def update_menu_animations(self, dt):
        """Actualizar animaciones del menú principal"""
        self.menu_animation_time += dt
        
        # Efecto sutil de "breathing" para el título
        if hasattr(self.ids, 'title_label'):
            pulse = 1.0 + 0.02 * math.sin(self.menu_animation_time * 1.5)
            # La animación del título se maneja visualmente
        
        # Parpadeo sutil del botón destacado
        if hasattr(self.ids, 'start_button'):
            glow = 0.8 + 0.2 * math.sin(self.menu_animation_time * 2.5)
            # El glow se controla a nivel de canvas, aquí registramos el valor
            self.button_glow_intensity = glow
    
    def animate_menu_entrance(self, dt):
        """Animar la entrada del menú principal"""
        # Animación de fade-in para el título
        if hasattr(self.ids, 'title_label'):
            self.ids.title_label.opacity = 0
            anim_title = Animation(opacity=1, duration=1.0)
            anim_title.start(self.ids.title_label)
        
        # Animación staggered para los botones
        def animate_buttons(dt):
            buttons = ['start_button', 'config_button', 'exit_button']
            for i, button_id in enumerate(buttons):
                if hasattr(self.ids, button_id):
                    button = getattr(self.ids, button_id)
                    button.opacity = 0
                    # Retraso progresivo para cada botón
                    anim = Animation(opacity=1, duration=0.6)
                    Clock.schedule_once(lambda dt, btn=button: anim.start(btn), i * 0.2)
        
        Clock.schedule_once(animate_buttons, 0.5)
        
        # Animación para el cuadro de descripción
        if hasattr(self.ids, 'subtitle_label'):
            self.ids.subtitle_label.opacity = 0
            def animate_subtitle(dt):
                anim = Animation(opacity=1, duration=0.8)
                anim.start(self.ids.subtitle_label)
            Clock.schedule_once(animate_subtitle, 1.0)
    
    def apply_pixel_font_if_available(self, dt=None):
        """Aplicar fuente pixelada al menú principal"""
        font_paths = [
            'assets/fonts/PressStart2P-Regular.ttf',
            'assets/fonts/pixel_font.ttf'
        ]
        
        font_applied = False
        for pixel_font_path in font_paths:
            if os.path.exists(pixel_font_path):
                print(f"✅ Aplicando fuente pixelada al menú: {pixel_font_path}")
                
                # Aplicar a elementos del menú
                if hasattr(self.ids, 'title_label'):
                    self.ids.title_label.font_name = pixel_font_path
                
                if hasattr(self.ids, 'subtitle_label'):
                    self.ids.subtitle_label.font_name = pixel_font_path
                
                if hasattr(self.ids, 'start_button'):
                    self.ids.start_button.font_name = pixel_font_path
                
                if hasattr(self.ids, 'config_button'):
                    self.ids.config_button.font_name = pixel_font_path
                    
                if hasattr(self.ids, 'exit_button'):
                    self.ids.exit_button.font_name = pixel_font_path
                
                font_applied = True
                break
        
        if not font_applied:
            print(f"📝 Menú usando fuente por defecto")


class ALifeIsARandomJourneyApp(App):
    """Aplicación principal de A Life Is A Random Journey"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_screen = 'menu'  # Empezar en menú principal
        self.audio_manager = AudioManager()  # Gestor de audio
    
    def build(self):
        """Construir la interfaz de usuario"""
        self.title = 'A Life Is A Random Journey'
        self.icon = 'assets/images/icon.png'  # Se cargará cuando exista
        
        # Cargar archivos .kv
        try:
            Builder.load_file('ui/main_menu.kv')
            print("✅ Archivo de menú principal cargado")
        except Exception as e:
            print(f"⚠️ Error cargando menú principal: {e}")
        
        try:
            Builder.load_file('ui/game_screen.kv')
            print("✅ Archivo de pantalla de juego cargado")
        except Exception as e:
            print(f"⚠️ Error cargando pantalla de juego: {e}")
        
        # Cargar música de fondo
        self.setup_audio()
        
        # Crear y mostrar el menú principal
        main_menu = MainMenuScreen()
        return main_menu
    
    def setup_audio(self):
        """Configurar sistema de audio"""
        # Cargar música de fondo del menú
        menu_music_path = 'assets/audio/menu_music.mp3'
        if self.audio_manager.load_background_music(menu_music_path):
            print("🎵 Sistema de audio configurado")
        else:
            print("📝 Audio en modo silencioso (música no disponible)")
    
    def start_game(self):
        """Iniciar el juego desde el menú principal con animación de transición"""
        print("🎮 Iniciando nueva aventura...")
        
        # Reproducir efecto de sonido de inicio (si existe)
        self.audio_manager.play_sfx('assets/audio/start_game.wav')
        
        # Animación de fade out del menú
        fade_out = Animation(opacity=0, duration=0.5)
        
        def switch_to_game(animation, widget):
            # Cambiar a pantalla de juego
            game_screen = GameScreen()
            self.load_example_scene(game_screen)
            self.root.clear_widgets()
            self.root.add_widget(game_screen)
            
            # Fade in de la nueva pantalla
            game_screen.opacity = 0
            fade_in = Animation(opacity=1, duration=0.5)
            fade_in.start(game_screen)
            
            self.current_screen = 'game'
            
            # Cambiar música (aquí podrías cargar música de juego diferente)
            # self.audio_manager.stop_background_music()
        
        fade_out.bind(on_complete=switch_to_game)
        fade_out.start(self.root)
    
    def show_config(self):
        """Mostrar pantalla de configuración"""
        print("⚙️ Configuración (en desarrollo)")
        
        # Reproducir sonido de menú
        self.audio_manager.play_sfx('assets/audio/menu_select.wav')
        
        # Por ahora solo mostrar controles de audio
        current_volume = int(self.audio_manager.music_volume * 100)
        music_status = "ON" if self.audio_manager.music_enabled else "OFF"
        print(f"🎵 Música: {music_status} (Volumen: {current_volume}%)")
        
        # Toggle música para demostración
        new_status = self.audio_manager.toggle_music()
        print(f"🎵 Música cambiada a: {'ON' if new_status else 'OFF'}")
    
    def exit_game(self):
        """Salir del juego con animación"""
        print("👋 Saliendo del juego...")
        
        # Detener música
        self.audio_manager.stop_background_music()
        
        # Reproducir sonido de salida
        self.audio_manager.play_sfx('assets/audio/exit_game.wav')
        
        # Pequeña animación antes de cerrar
        fade_out = Animation(opacity=0, duration=0.3)
        fade_out.bind(on_complete=lambda anim, widget: self.stop())
        fade_out.start(self.root)
    
    def load_example_scene(self, game_screen):
        """Cargar escena de ejemplo para demostrar la interfaz"""
        
        # Verificar si la imagen existe
        scene_image = 'assets/images/placeholder_scene.png'
        if not os.path.exists(scene_image):
            print(f"⚠️ Imagen no encontrada: {scene_image}")
            scene_image = None
        
        # Texto narrativo de ejemplo
        narrative_text = (
            "* Naciste en una aldea humilde, rodeado de hambre y enfermedades.\n\n"
            "* El aire era pesado, la esperanza escasa.\n\n"
            "* Las casas de adobe se desmoronan lentamente, como los sueños de sus habitantes.\n\n"
            "* Tu familia te mira con ojos cansados. Tu destino está por decidirse.\n\n"
            "* ¿Qué harás con la vida que te ha tocado?"
        )
        
        # Opciones de ejemplo
        options = [
            "Intentar trabajar desde joven para ayudar a la familia",
            "Buscar educación a toda costa, sin importar el sacrificio"
        ]
        
        # Cargar en la interfaz con un pequeño retraso para que se inicialice
        def delayed_setup(dt):
            game_screen.load_scene_data(scene_image, narrative_text, options)
            game_screen.apply_pixel_font_if_available()
        
        Clock.schedule_once(delayed_setup, 0.5)
    
    def on_option_selected(self, option_number, option_text):
        """Manejador cuando se selecciona una opción con animación"""
        print(f"🎯 Opción seleccionada: {option_number}")
        print(f"📝 Texto: {option_text}")
        
        # Reproducir sonido de selección
        self.audio_manager.play_sfx('assets/audio/option_select.wav')
        
        # Animación del botón presionado
        if hasattr(self.root, 'ids'):
            button_id = f'option_{option_number}'
            if hasattr(self.root.ids, button_id):
                button = getattr(self.root.ids, button_id)
                # Pequeña animación de "click"
                anim = Animation(opacity=0.5, duration=0.1) + Animation(opacity=1, duration=0.1)
                anim.start(button)
        
        # Aquí se conectaría con la lógica del juego
        # Por ahora, solo mostrar feedback con efecto typewriter
        if hasattr(self.root, 'ids') and hasattr(self.root.ids, 'narrative_text'):
            feedback_text = (
                f"* Has elegido: {option_text.replace('*', '').strip()}\n\n"
                "* Esta decisión marcará el rumbo de tu vida...\n\n"
                "* [Sistema de juego en desarrollo]\n\n"
                "* Reinicia la aplicación para volver al inicio."
            )
            
            # Usar efecto typewriter para el feedback
            if hasattr(self.root, 'start_typewriter_effect'):
                self.root.start_typewriter_effect(feedback_text)
            else:
                self.root.ids.narrative_text.text = feedback_text
    
    def on_start(self):
        """Llamado cuando la aplicación inicia"""
        print("🎮 A Life Is A Random Journey - Aplicación iniciada")
        print("🎨 Interfaz: Estilo Negro + Animaciones Undertale/Deltarune/Celeste")
        print("🎵 Audio: Sistema de música y efectos implementado")
        print("📱 Modo: Desarrollo local" if platform.system() != 'Android' else "📱 Modo: Android")
        
        # Verificar recursos
        self.check_resources()
        
        # Iniciar música de fondo del menú
        Clock.schedule_once(self.start_menu_music, 1.0)
    
    def start_menu_music(self, dt):
        """Iniciar música del menú con retraso"""
        self.audio_manager.play_background_music()
    
    def check_resources(self):
        """Verificar que los recursos necesarios existen"""
        resources_to_check = [
            ('assets/images/placeholder_scene.png', 'Imagen de escena'),
            ('assets/fonts/PressStart2P-Regular.ttf', 'Fuente Press Start 2P'),
            ('assets/fonts/pixel_font.ttf', 'Fuente pixelada alternativa'),
            ('assets/audio/menu_music.mp3', 'Música del menú'),
            ('ui/main_menu.kv', 'Archivo de menú principal'),
            ('ui/game_screen.kv', 'Archivo de pantalla de juego')
        ]
        
        print("\n📋 Verificando recursos:")
        for resource_path, description in resources_to_check:
            if os.path.exists(resource_path):
                print(f"✅ {description}: {resource_path}")
            else:
                print(f"⚠️ {description}: {resource_path} - NO ENCONTRADO")
        print()
    
    def on_pause(self):
        """Llamado cuando la aplicación se pausa (Android)"""
        # Pausar música en segundo plano
        if self.audio_manager.background_music:
            self.audio_manager.background_music.stop()
        return True
    
    def on_resume(self):
        """Llamado cuando la aplicación se reanuda (Android)"""
        # Reanudar música si estaba activa
        if self.current_screen == 'menu':
            self.audio_manager.play_background_music()


def main():
    """Función principal"""
    print("🚀 Iniciando A Life Is A Random Journey...")
    print("🎯 Versión: 0.1 (Desarrollo)")
    print("🎨 Interfaz: Estilo Negro + Animaciones Undertale/Deltarune/Celeste")
    print("🎮 Menú Principal con Animaciones")
    print("🎵 Sistema de Audio: Música y Efectos")
    print("✨ Efectos: Typewriter, Fade, Breathing, Glow")
    
    try:
        app = ALifeIsARandomJourneyApp()
        app.run()
    except Exception as e:
        print(f"❌ Error al iniciar la aplicación: {e}")
        raise


if __name__ == '__main__':
    main() 