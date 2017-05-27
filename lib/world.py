class World(object):
    def __init__(self, max_x, max_y):
        self.world_max_x = max_x
        self.world_max_y = max_y
        self.world_amount_cells = 0
        self.world_cells = {}

        self.gen_world()

    def world_make_cell_name(self, x, y):
        cell_name = '%d/%d' % (x, y)
        return cell_name
    def world_make_cell(self, x, y, is_border):
        name = self.world_make_cell_name(x, y)
        self.world_cells[name] = Cell(name, x, y, is_border)
        print "create Cell: %s border: %s" % (name,is_border)
    def gen_world(self):
        wanted_cells = self.world_max_x * self.world_max_y
        i = 1
        actual_x = 0
        actual_y = 1
        is_border = None
        print "-Begin world gen-"
        while i < wanted_cells or i == wanted_cells:
            if actual_x == self.world_max_x: # Check if it at End of x
                actual_x = 1
                actual_y += 1
                print ''
            else:
                actual_x += 1
            if actual_x == 1 or actual_y == 1 or actual_x == self.world_max_x or actual_y == self.world_max_y: # Check if it is Border
                is_border = True
            else: is_border = False

            i += 1
            self.world_make_cell(actual_x, actual_y, is_border)
        print "-Finish Cell gen-"
class Cell(object):
    def __init__(self, name, x, y, is_border):
        self.name = name

        self.cell_pos_x = x
        self.cell_pos_y = y
        self.cell_is_border = is_border
        self.cell_is_used = False

    def cell_next_round(self):
        foo = None
w = World(4, 4)