[app]

# (str) Title of your application
title = A Life Is A Random Journey

# (str) Package name
package.name = alifeisarandomjourney

# (str) Package domain (needed for android/ios packaging)
package.domain = org.alifegame

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ogg,wav,mp3,ttf,otf,json,db

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests,bin,venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"]([^'"]*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,pillow

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/assets/images/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/assets/images/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use (optional). This is the API version the NDK ships with.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Python Service
# use that parameter to set custom Java class instead of PythonService
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so they can be imported and used from python using pyjnius.
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.include_exts'.
# 1) android.add_assets = source_dir/asset_name
# 2) android.add_assets = source_dir/asset_name:dest_asset_name
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
# The option may be used in three ways, the value may contain one or zero ':'
# Some examples:
# 1) A file to place in the default resource category:
#    android.add_resources = my_icons/all-inclusive.png:drawable
# 2) A directory, here 'my_icons', containing resources to place in the default resource category:
#    android.add_resources = my_icons:drawable
# 3) A directory, here 'my_icons', containing resources to place in a specific resource category 'mipmap':
#    android.add_resources = my_icons:mipmap
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
android.enable_androidx = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# You can build multiple archs by separating with comma: armeabi-v7a,arm64-v8a
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = key:value,key2:value2
# android.manifest_placeholders =

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# 'aab' is the format required for uploading the app to Google Play.
# 'apk' is a more universal format, but has a larger file size.
# 'aar' is only used if the goal is to publish the app on a Maven repository.
# (str) default: 'aab'
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# 'apk' is more universal, but has a larger file size.
# 'aar' is only used if the goal is to publish the app on a Maven repository.
# (str) default: 'apk'
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    Profile definitions
#    -----------------------------------------------------------------------------

#    Buildozer can use a profiles.ini file to know which options to use depending on the current profile.
#    If no profile.ini file is found, buildozer will create a default one with:
#        [profile:dev]
#        [profile:prod]
#
#    You can extend/override values loaded from profile.ini with this spec file.
#    For that, you need to set a profile and add the option key in the section [profile:SELECTED_PROFILE].
#    If a key appears in both profile.ini and buildozer.spec, the value from buildozer.spec will be used.

#    Example:
#        We have a profile.ini with:
#            [profile:dev]
#            mode = debug
#            android.logcat_filters = *:E
#
#            [profile:prod]
#            mode = release
#            android.logcat_filters = *:W
#
#        And in buildozer.spec we would have:
#            ...
#            [profile:dev]
#            mode = release
#
#        Then, if we call buildozer with: buildozer --profile dev android debug
#        The specs loaded would be:
#            mode = release (from buildozer.spec, overriding profile.ini)
#            android.logcat_filters = *:E (from profile.ini)

[profile:dev]
mode = debug

[profile:prod]
mode = release 