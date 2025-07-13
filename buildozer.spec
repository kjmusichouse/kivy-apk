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
requirements = python3,kivy==2.3.0,pyjnius,requests
android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.build_tools = 36.0.0
android.accept_sdk_license = True
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
icon.filename = data/icon.png
# presplash.filename = data/splash.png

[buildozer]
log_level = 2
warn_on_root = 1
