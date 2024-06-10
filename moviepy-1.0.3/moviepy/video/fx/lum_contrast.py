def lum_contrast(clip, lum = 0, contrast=0, contrast_thr=127):
    """ luminosity-contrast correction of a clip """
    
    def fl_image(im):
        im = 1.0*im # float conversion
        corrected = im + lum + contrast*(im-float(contrast_thr))
        corrected[corrected < 0] = 0
        corrected[corrected > 255] = 255
        return corrected.astype('uint8')
    
    return clip.fl_image(fl_image)
