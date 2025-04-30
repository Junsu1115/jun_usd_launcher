class Type:
    MAP = {
        1: "prop",
        2: "character",
        3: "environment",
        4: "vehicle"
    }

    def __init__(self, type_id):
        self.type_id = type_id

    @property
    def name(self):
        return self.MAP.get(self.type_id)


class Dept:
    MAP = {
        1: "model",
        2: "lookdev",
        3: "rig",
        4: "priviz",
        5: "layout",
        6: "ani",
        7: "light",
        8: "fx"
    }

    def __init__(self, dept_id):
        self.dept_id = dept_id

    @property
    def name(self):
        return self.MAP.get(self.dept_id)


class Lod:
    MAP = {
        1: "hi",
        2: "md",
        3: "lo"
    }

    def __init__(self, lod_id):
        self.lod_id = lod_id

    @property
    def name(self):
        return self.MAP.get(self.lod_id)


class Work:
    MAP = {
        1: "dev",
        2: "pub"
    }

    def __init__(self, work_id):
        self.work_id = work_id

    @property
    def name(self):
        return self.MAP.get(self.work_id)