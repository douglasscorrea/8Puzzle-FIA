# -*- coding: utf-8 -*-
import constants as c
import time
import shuffle
import bfs
import dfs
import it_dfs
import a_star
import utils




bfs_alg = bfs.BFS(self.shuffler.get_matrix(), self.nmax)
start = time.time()
bfs_alg.BFS_algorithm()
end = time.time()

if end - start < 1:
    print(self.text_time2, "{0:.3f}".format((end - start) * 1000) + "ms")
else:
   print(self.text_time2, "{0:.3f}".format(end - start) + "s")

print(self.text_memory2, "{0:.3f}".format(bfs_alg.get_memory_usage()) + "MB")
