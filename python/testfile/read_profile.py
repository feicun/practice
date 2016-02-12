import pstats
p = pstats.Stats('/tmp/profile_output')
p.sort_stats('cumulative').print_stats(200)
