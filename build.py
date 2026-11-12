"""Assemble index.html from src/ and stamp a new version.

Usage: python3 build.py
Writes index.html and version.json. Each build gets a new version, so phones
that have the game open see the « Mettre à jour » button.
"""
import json, datetime, pathlib
root = pathlib.Path(__file__).parent
version = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')
head = (root / 'src/head.html').read_text()
game = (root / 'src/game.html').read_text()
update = (root / 'src/update.html').read_text().replace('__VERSION__', version)
(root / 'index.html').write_text(head + game + '\n' + update + '\n</body>\n</html>\n')
(root / 'version.json').write_text(json.dumps({'version': version}) + '\n')
print('version', version)
