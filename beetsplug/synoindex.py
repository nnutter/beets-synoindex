"""Updates the Synology (music) index whenever the beets library is changed.

This assumes beets is being run on Synology DiskStation Manager so synoindex is
available.
"""

from subprocess import run

from beets.plugins import BeetsPlugin


class SynoindexPlugin(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.register_listener('item_copied', self.index_item)
        self.register_listener('item_moved', self.index_item)
        self.register_listener('item_linked', self.index_item)
        self.register_listener('item_hardlinked', self.index_item)

    def index_item(self, item, source, destination):
        if str(source).find('/volume1/music/') == 0:
            run(['synoindex', '-R', 'music', '-n', destination, source])
        else:
            run(['synoindex', '-R', 'music', '-a', destination])
