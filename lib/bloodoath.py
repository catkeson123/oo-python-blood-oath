class BloodOath:

    all = []

    def __init__(self, initiation_date, follower, cult):
        self.initiation_date = initiation_date
        self.follower = follower
        self.cult = cult
        BloodOath.all.append(self)

    @classmethod
    def first_oath(cls):
        return BloodOath.all[0].follower
