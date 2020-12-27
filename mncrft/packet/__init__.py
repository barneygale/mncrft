import csv
import glob
import os.path
import re


def _load():
    default_protocol_version = 0
    minecraft_versions = {}
    names = {}
    idents = {}
    csv_paths = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        "data",
        "*.csv"))
    for csv_path in glob.glob(csv_paths):
        match = re.match('(\d{4})_(.+)\.csv', os.path.basename(csv_path))
        if not match:
            continue

        protocol_version = int(match.group(1))
        minecraft_version = match.group(2)

        ident = None
        last_section = None
        with open(csv_path) as csv_file:
            reader = csv.reader(csv_file)
            for i, record in enumerate(reader):
                # Skip header
                if i == 0:
                    continue

                # Extract fields
                protocol_mode = record[0]
                direction = record[1]
                name = record[2]

                section = (protocol_mode, direction)
                if section != last_section:
                    ident = 0
                last_section = section

                # Update default protocol version
                default_protocol_version = max(default_protocol_version,
                                               protocol_version)

                # Update minecraft versions
                minecraft_versions[protocol_version] = minecraft_version

                # Update the packet dictionaries
                key = [protocol_version, protocol_mode, direction]
                names[tuple(key + [ident])] = name
                idents[tuple(key + [name])] = ident

                ident += 1

    return (default_protocol_version, minecraft_versions,
            names, idents)

default_protocol_version, minecraft_versions, \
names, idents = _load()
