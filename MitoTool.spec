# -*- mode: python -*-

block_cipher = None


a = Analysis(['H:\\MitoTool\\10_25\\MitoTool.py'],
             pathex=['H:\\MitoTool\\10_25'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='MitoTool',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='H:\\MitoTool\\src\\root.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MitoTool')
