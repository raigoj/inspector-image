import argparse
from PIL import Image

def rational_to_float(rational):
    return float(rational[0]) / float(rational[1])

def extract_location(path):
    with open(path, "rb") as src:
        img = Image.open(src)

    exif_data = img._getexif()
    if exif_data is not None:
        for tag, value in exif_data.items():
            # Check if the tag corresponds to GPSInfo (tag number 34853)
            if tag == 34853 and isinstance(value, dict):
                gps_info = value
                latitude_ref = gps_info.get(1)
                latitude = gps_info.get(2)
                longitude_ref = gps_info.get(3)
                longitude = gps_info.get(4)

                if latitude and longitude:
                    
                    lat = float(gps_info[2][0] + gps_info[2][1] / 60 + gps_info[2][2] / 3600)
                    lon = float(gps_info[4][0] + gps_info[4][1] / 60 + gps_info[4][2] / 3600)
                    print(f"Lat: {lat}")
                    print(f"Lon: {lon}")
                    return

    print("Location data not found in the image's EXIF.")
        

def extract_pgp(path):
    with open(path, "rb") as file:
        data = file.read()

    start = b"-----BEGIN PGP PUBLIC KEY BLOCK-----"
    end = b"-----END PGP PUBLIC KEY BLOCK-----"
    start_index = data.find(start)
    end_index = data.find(end)

    if start_index == -1 or end_index == -1:
        print("PGP public key could not be retrieved")
    else:
        pgp_key = data[start_index:end_index + len(end)].decode("utf-8").strip()
        print(pgp_key)


def main():
    parser = argparse.ArgumentParser(description="inspector-image")
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-steg", required=False, type=str, help="Extract PGP key")
    g.add_argument("-map", required=False, type=str, help="Extract location")
    args = parser.parse_args()

    if args.steg:
        extract_pgp(args.steg)
    elif args.map:
        extract_location(args.map)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

