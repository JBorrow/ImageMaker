mencoder "mf://phase*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=1:nr=2000 -o phase_movie.avi
mencoder "mf://phase*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=2:nr=2000 -o phase_movie.avi

mencoder "mf://bh*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=1:nr=2000 -o bh_movie.avi
mencoder "mf://bh*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=2:nr=2000 -o bh_movie.avi

mencoder "mf://gas*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=1:nr=2000 -o gas_movie.avi
mencoder "mf://gas*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=2:nr=2000 -o gas_movie.avi

mencoder "mf://dark*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=1:nr=2000 -o dark_movie.avi
mencoder "mf://dark*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=2:nr=2000 -o dark_movie.avi

mencoder "mf://hi*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=1:nr=2000 -o hi_movie.avi
mencoder "mf://hi*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=2:nr=2000 -o hi_movie.avi

mencoder "mf://star*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=1:nr=2000 -o star_movie.avi
mencoder "mf://star*.png" -mf fps=24 -ovc x264 -x264encopts bitrate=10000:pass=2:nr=2000 -o star_movie.avi