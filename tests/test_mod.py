import hashlib
import mercantile

import mbtiles


def test_process_tile(data):
    mbtiles.init_worker(str(data.join('RGB.byte.tif')), {
            'driver': 'PNG',
            'dtype': 'uint8',
            'nodata': 0,
            'height': 256,
            'width': 256,
            'count': 3,
            'crs': 'EPSG:3857'})
    tile, contents = mbtiles.process_tile(mercantile.Tile(36, 73, 7))
    assert tile.x == 36
    assert tile.y == 73
    assert tile.z == 7


def test_valid_PNG(data):
    mbtiles.init_worker(str(data.join('RGB.byte.tif')), {
        'driver': 'PNG',
        'dtype': 'uint8',
        'nodata': 0,
        'height': 256,
        'width': 256,
        'count': 3,
        'crs': 'EPSG:3857'})

    contents = mbtiles.process_tile(mercantile.Tile(36, 72, 7))[1]

    # Compare to sha1 of a known valid byte array
    sha1 = hashlib.sha1(contents).hexdigest()
    assert sha1 == '526744d1fbd4a50e2baa484ea022869271c42f47'


def test_valid_JPEG(data):
    mbtiles.init_worker(str(data.join('RGB.byte.tif')), {
        'driver': 'JPEG',
        'dtype': 'uint8',
        'nodata': 0,
        'height': 256,
        'width': 256,
        'count': 3,
        'crs': 'EPSG:3857'})

    contents = mbtiles.process_tile(mercantile.Tile(36, 72, 7))[1]

    # Compare to sha1 of a known valid byte array
    sha1 = hashlib.sha1(contents).hexdigest()
    assert sha1 == '4c9102992d4447e4ce56e84aa88e52d7484f47d1'