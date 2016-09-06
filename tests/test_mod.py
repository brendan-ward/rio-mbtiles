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
    assert hashlib.sha1(contents).hexdigest() == '526744d1fbd4a50e2baa484ea022869271c42f47'

    # assert contents[:50] == bytearray(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x02\x00\x00\x00\xd3\x10?1\x00\x00\x00\x06tRNS\x00\x00\x00\x00\x00\x00n\xa6\x07')
    # assert contents[:-10] == ""


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
    assert hashlib.sha1(contents).hexdigest() == '4c9102992d4447e4ce56e84aa88e52d7484f47d1'