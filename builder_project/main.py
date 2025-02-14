from builders import TileWorker, Finisher, Painter, Foreman


tile_worker = TileWorker()
finisher = Finisher()
painter = Painter()


foreman = Foreman(tile_worker)
foreman.make_floors()


foreman = Foreman(finisher)
foreman.level_walls()


foreman = Foreman(painter)
foreman.paint_walls()


foreman = Foreman(tile_worker)
foreman.turnkey_work()