'''
This file contains the python script that creates movies that evolve
over time. It is a simple script and uses the snipshots as frames,
rather than doing any interpolation.
'''
def makeSingleMovie(initial, final, z, size, text, saveDir, da,
					tag, partplot):

    dxda = (final - initial)/( (1./(1.+z)) - 1.)    # subtract to get position at a=0

	dir = "./"
    width = size['with']
    scale = N.array(size['scale'])
    star_scale_factor = size['star_scale_factor']
    dark_scale_factor = size['dark_scale_factor']
    T_limits = N.array(size['T_limits'])

    if 'pixels' in size.keys() :
        xpixels, ypixels = size['pixels']
    else:
        xpixels, ypixels = 1024, 1024

    if 'use_logh' in size.keys() :
        use_logh = size['use_logh']
    else:
        use_logh = True

    if 'gas_cmap' in size.keys() :
        gas_cmap = size['gas_cmap']

    imageParams = eagle.ImageParams(width, scale, zoom=1., angle=0,
	partplot=partplot, star_scale_factor=star_scale_factor,
	dark_scale_factor=dark_scale_factor, gas_cmap=gas_cmap,
	T_limits=T_limits, use_logh=use_logh)

    plotParams = eagle.PlotParams( xpixels=xpixels, ypixels=ypixels, text=text)

    savedir = ("%s/Webpage/Movies/%s" % (saveDir, tag))
    label = tag


    fileInfo = eagle.FileInfo(dir, 400, label, savedir, snipshot=True)

    eagle.make_movie( fileInfo, imageParams, plotParams, centre=initial,
	dxda=dxda, last_snip=400, delta_angle=da )
