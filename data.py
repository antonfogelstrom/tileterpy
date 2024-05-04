import csv


def save(raw_data, map_size, tile_size):
    file_path = 'data.csv'

    data = []
    for d in raw_data:
        tile_id = d[0][0]
        tile_pos_x = d[1][0] // tile_size
        tile_pos_y = d[1][1] // tile_size
        data.append([tile_id, tile_pos_x, tile_pos_y])

    rows = []
    for y in range(0, map_size[1]):
        columns = []
        for x in range(0, map_size[0]):
            found = False
            for d in data:
                if d[1] == x and d[2] == y:
                    columns.append('{:04d}'.format(d[0]))
                    found = True
            if not found:
                columns.append('9999')
        rows.append(columns)

    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows)


def load():
    file_path = 'data.csv'

    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        data = []
        for row in csv_reader:
            data.append(row)
        return data
