[app]
title = MCQ Test App
package.name = mcqapp
package.domain = org.kivy
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0
orientation = portrait
fullscreen = 0
requirements = python3,kivy,requests
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
# icon.filename = data/icon.png
# presplash.filename = data/splash.png

[buildozer]
log_level = 2
warn_on_root = 0
