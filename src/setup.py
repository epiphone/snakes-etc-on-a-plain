from distutils.core import setup
import py2exe

setup(windows=['game.py'],
      options={
        "py2exe": {
            "dist_dir": "../release/win32"
        }
})
