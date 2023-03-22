from .bloodoath import BloodOath


class Cult:

    all = []

    def __init__(self, name, location, founding_year, slogan, min_age):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        self.min_age = min_age
        Cult.all.append(self)

    @property
    def followers(self):
        return [b.follower for b in BloodOath.all if b.cult == self]

    def recruit_follower(self, follower):
        if follower.age > self.min_age:
            BloodOath('2023-03-22', follower, self)
        else:
            print("You are not old enough")

    @classmethod
    def find_by_name(cls, name):
        for cult in cls.all:
            if cult.name == name:
                return cult
        print("Cult not found")

    @classmethod
    def find_by_location(cls, location):
        for cult in cls.all:
            if cult.location == location:
                return cult
        print("Cult not found")

    @classmethod
    def find_by_founding_year(cls, founding_year):
        for cult in cls.all:
            if cult.founding_year == founding_year:
                return cult
        print("Cult not found")

    @property
    def cult_population(self):
        return len(self.followers)

    @property
    def average_age(self):
        ages = [f.age for f in self.followers]
        return float(sum(ages)/len(ages))

    @property
    def my_followers_mottos(self):
        for f in self.followers:
            print(f"{f.life_motto}")

    @classmethod
    def least_popular(cls):
        lp = cls.all[0]
        for c in cls.all:
            if len(c.followers) < len(lp.followers):
                lp = c
        return lp

    @classmethod
    def most_common_location(cls):
        locations = {c.location for c in cls.all}
        ld = {}
        for l in locations:
            ld[l] = 0
        for c in cls.all:
            for l in ld.keys():
                if c.location == l:
                    ld[l] += 1
        return max(ld, key=ld.get)
