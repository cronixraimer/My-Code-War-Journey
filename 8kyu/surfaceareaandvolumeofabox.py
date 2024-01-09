def get_size(w, h, d):
    surface_area = 2 * d * w + 2 * d * h + 2 * w * h
    volume = w * h * d
    return surface_area, volume

result = get_size(4, 2, 6)
print(result)
#was is unless I googled the formula of surface are and volume
