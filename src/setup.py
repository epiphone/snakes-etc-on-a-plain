from distutils.core import setup
import py2exe

setup(windows=['game.py'],
      data_files = [('', ['map0.txt', 'map1.txt', 'map2.txt', 'map3.txt', 'map4.txt', 'map5.txt', 'map6.txt'])],
      name="snakes-etc-on-a-plain",
      options={
        "py2exe": {
            "dist_dir": "../release/win32",
            "optimize": 2,
            "bundle_files": 2
        }
})
