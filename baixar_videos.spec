# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['baixar_videos.py'],  # Nome do arquivo principal atualizado
    pathex=['.'],  # Caminho atual do script
    binaries=[('ffmpeg_bin/bin/ffmpeg.exe', 'ffmpeg_bin/bin')],  # Inclui o ffmpeg.exe na subpasta bin dentro de ffmpeg_bin
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='baixar_videos',  # Nome do executável atualizado
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
