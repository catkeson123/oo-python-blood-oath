from .bloodoath import BloodOath


class Follower:

    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)

    def join_cult(self, cult):
        if cult.min_age < self.age:
            BloodOath('2023-03-22', self, cult)
        else:
            print('You are not old enough')

    @property
    def cults(self):
        return [b.cult for b in BloodOath.all if b.follower == self]

    @classmethod
    def of_a_certain_age(cls, age):
        return [f for f in cls.all if f.age >= age]

    @property
    def my_cults_slogans(self):
        for c in self.cults:
            print(f"{c.slogan}")

    @classmethod
    def most_active(cls):
        ma = cls.all[0]
        for f in cls.all:
            if len(f.cults) > len(ma.cults):
                ma = f
        return ma

    @property
    def fellow_cult_members(self):
        fcm = []
        for c in self.cults:
            for b in BloodOath.all:
                if c == b.cult and b.follower != self:
                    if b.follower not in fcm:
                        fcm.append(b.follower)
        return fcm
