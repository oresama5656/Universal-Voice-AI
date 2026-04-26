# -*- mode: python ; coding: utf-8 -*-
import os

ctk_path = r'C:\Users\PHARMY\AppData\Local\Programs\Python\Python312\Lib\site-packages\customtkinter'
webrtcvad_py = r'C:\Users\PHARMY\AppData\Local\Programs\Python\Python312\Lib\site-packages\webrtcvad.py'
webrtcvad_pyd = r'C:\Users\PHARMY\AppData\Local\Programs\Python\Python312\Lib\site-packages\_webrtcvad.cp312-win_amd64.pyd'

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[(webrtcvad_pyd, '.')],
    datas=[(ctk_path, 'customtkinter'), (webrtcvad_py, '.')],
    hiddenimports=['pystray', 'PIL', 'numpy', 'pygetwindow', 'pywin32'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['webrtcvad'], # フックエラーを避けるために除外
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Universal_Voice_AI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
