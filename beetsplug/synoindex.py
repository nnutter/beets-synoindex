"""Updates the Synology (music) index whenever the beets library is changed.

This assumes beets is being run on Synology DiskStation Manager so synoindex is
available.
"""

from subprocess import run

from beets.plugins import BeetsPlugin


class SynoindexPlugin(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.register_listener('item_moved', self.index_move)

        self.register_listener('item_copied', self.index_copy)
        self.register_listener('item_linked', self.index_copy)
        self.register_listener('item_hardlinked', self.index_copy)

    def index_copy(self, item, source, destination):
        run(['synoindex', '-R', 'music', '-a', destination])

    def index_move(self, item, source, destination):
        run(['synoindex', '-R', 'music', '-n', destination, source])
