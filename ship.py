import pygame
import math
from random import randrange, choice
import coord
import base


##########################################################################
##########################################################################
##########################################################################
class Ship(base.BaseClass):

    def __init__(self, **kwargs):
        self.data = {
            "name": "",
            "space": None,
            "hull": None,
            "debug": False,
            "mass": 0.0,
            "acc": 0.0,
            "force": 0,
            "hits": 0,
            "side": "N",
            "agility": math.radians(2.0),
            "speed": 0,
            "radius": 4,
            "mode": "",
            "screen": None,
            "direction": math.radians(randrange(360)),
            "location": coord.Coord(randrange(1000), randrange(1000)),
        }
        self.data.update(kwargs)
        self.components = []

    ######################################################################
    def closest(self, friend=False, enemy=False, neutral=False):
        mindist = 99999999
        minship = None
        for ship in self.space.ships:
            if ship == self:
                continue
            if not neutral and not ship["side"]:
                continue
            if neutral and ship["side"]:
                continue
            if enemy and ship["side"] == self["side"]:
                continue
            if friend and ship["side"] != self["side"]:
                continue
            d = self.distance(ship)
            if d < mindist:
                mindist = d
                minship = ship
        return minship

    ######################################################################
    def closest_neutral(self):
        return self.closest(neutral=True)

    ######################################################################
    def closest_enemy(self):
        return self.closest(enemy=True)

    ######################################################################
    def closest_friend(self):
        return self.closest(friend=True)

    ######################################################################
    def move_towards(self, other):
        """ Move towards the other ship
        """
        distance = self.distance(other)
        newdir = self["location"].angle(other["location"])

        if distance > self["speed"] * 100:
            self["speed"] += self["acc"]
        if distance < self["speed"] * 10:
            self["speed"] -= self["acc"]
        self["speed"] = max(self["speed"], 0.0)
        self["speed"] = min(self["speed"], 100.0)

        if self["debug"]:
            print "Original Direction: %s" % self["direction"]
            print "Target Direction: %s" % newdir
        self.steer_towards(newdir)

        if self["debug"]:
            print "New Direction: %s" % self["direction"]
            print ""

        self.target_ship = other

    ######################################################################
    def steer_towards(self, angle):
        if self["direction"] - angle < self["agility"]:
            self["direction"] += self["agility"]
        elif angle - self["direction"] > self["agility"]:
            self["direction"] -= self["agility"]
        else:
            self["direction"] = angle

    ######################################################################
    def steer(self):
        """ Move towards the target
        This should probably be overwritten by each ship type
        """
        closest = self.closest_enemy()
        if not closest:
            return
        self.move_towards(closest)

    ######################################################################
    def draw(self, screen=None):
        if not screen:
            screen = self["screen"]
        here = self["location"].icoords()
        pygame.draw.circle(screen, self["color"], here, self["radius"], 0)
        vector = self["location"].displace(
            self["speed"] * 20, self["direction"])
        for c in self.components:
            if hasattr(c, 'draw'):
                c.draw(self, screen)

        if self["debug"]:
            font = pygame.font.Font(None, 20)
            txt = "%s @ %s -> %0.2f speed=%0.2f %s" % (
                self, here, self["direction"], self["speed"], self["mode"])
            text = font.render(txt, 1, (255, 255, 255))
            textpos = text.get_rect(centerx=screen.get_width() / 2)
            screen.blit(text, textpos)

            angle = self["location"].angle(self.target_ship["location"])
            dist = self.distance(self.target_ship)
            loc = self.target_ship["location"].icoords()
            txt = "%s @ %s angle=%0.2f distance=%d %s" % (self.target_ship, loc, angle, dist, self.target_ship["mode"])
            text = font.render(txt, 1, (255, 255, 255))
            textpos = text.get_rect(centerx=screen.get_width() / 2, top=20)
            screen.blit(text, textpos)
            pygame.draw.aaline(
                screen, (255, 255, 255), here, self.target_ship["location"].icoords())
        pygame.draw.aaline(screen, (255, 0, 255), here, vector.icoords())

    ######################################################################
    def attack(self):
        enemy = self.closest_enemy()
        if not enemy:
            return
        for c in self.components:
            if 'range' in c:
                if c["rate_cycle"] != c["rate"]:
                    continue
                if self.distance(enemy) < c["range"]:
                    c["rate_cycle"] = 0
                    if randrange(100) < c["accuracy"]:
                        enemy.inflict_damage(randrange(c["damage"]))
                        here = self["location"].icoords()
                        pygame.draw.aaline(
                            self["screen"], (255, 255, 255), here, self.target_ship["location"].icoords())
                        print "Zot %s->%s (Hits: %d, Shield: %d)" % (self["name"], enemy["name"], enemy["hits"], enemy.shields())

    ######################################################################
    def shields(self):
        shield = 0
        shielders = [c for c in self.components if "shield" in c]
        for s in shielders:
            shield += s["shield"]
        return shield

    ######################################################################
    def turn(self):
        for c in self.components:
            if 'rate_cycle' in c:
                c["rate_cycle"] += 1
                c["rate_cycle"] = min(c["rate_cycle"], c["rate"])
            if hasattr(c, 'turn'):
                c.turn()
        self.steer()
        self.move()
        self.attack()

    ######################################################################
    def inflict_damage(self, dmg):
        shielders = [
            c for c in self.components if "shield" in c and c["shield"] > 0]
        if shielders:
            s = choice(shielders)
        else:
            s = None

        if s:
            if s["shield"] > dmg:
                s["shield"] -= dmg
                dmg = 0
            else:
                dmg -= s["shield"]
                s["shield"] = 0

        self["hits"] -= dmg

    ######################################################################
    def distance(self, other):
        if not other:
            return 0
        return self["location"].distance(other["location"])

    ######################################################################
    def move(self):
        self["location"] = self["location"].displace(
            self["speed"], self["direction"])
        self["location"].maxsize(self.space["width"], self.space["height"])

    ######################################################################
    def addComponent(self, c):
        self.components.append(c)

    ######################################################################
    def init(self, **kwargs):
        self.getAcceleration()
        self.data.update(kwargs)
        for c in self.components:
            if 'range' in c:
                c["rate_cycle"] = c["rate"]

    ######################################################################
    def __str__(self):
        details = "H:%d S:%d" % (self["hits"], self.shields())
        return "%s %s (%s)" % (self.__class__.__name__, self["name"], details)

    ######################################################################
    def getMass(self, recalc=False):
        if recalc or not self["mass"]:
            mass = 0
            for c in self.components:
                mass += c["mass"]
            self["mass"] = mass
        return self["mass"]

    ######################################################################
    def getForce(self, recalc=False):
        if recalc or not self["force"]:
            force = 0
            for c in self.components:
                if hasattr(c, 'getForce'):
                    force += c.getForce()
            self["force"] = force
        return self["force"]

    ######################################################################
    def getAcceleration(self, recalc=False):
        if recalc or not self["acc"]:
            acc = float(self.getForce()) / self.getMass()
            self["acc"] = acc
        return self["acc"]

    ######################################################################
    def validate(self):
        space = 0
        power = 0
        maxpower = 0

        if not self.hull:
            return "No hull defined"

        for c in self.components:
            space += c["space"]
            power += c["power"]
            if hasattr(c, 'getPower'):
                maxpower += c.getPower()

        if space > self.hull["maxspace"]:
            return "Ran out of space (%d/%d)" % (space, self.hull.maxspace)

        if power > maxpower:
            return "Ran out of power (%d/%d)" % (power, maxpower)

        return "Validated"

# EOF
