import math
import pyglet
lib = pyglet

def help() :
    print("defs: help(it), atmin, atmax.")
class list :
    """Min → max or max → min"""
    def atmin(mass: list) :
        DoneMass = []
        while len(mass) > 0 :
            minI = -1
            minVal = 0
            for index in range(len(mass)) :
                if minI < 0 or mass[index] < minVal :
                    minVal = mass[index]
                    minI = index

            DoneMass.append(minVal)
            mass.pop(minI)

        return DoneMass

    def atmin(mass: list) :
        DoneMass = []
        while len(mass) > 0 :
            maxI = -1
            maxVal = 0
            for index in range(len(mass)) :
                if maxI < 0 or mass[index] < maxVal :
                    maxVal = mass[index]
                    maxI = index

            DoneMass.append(maxVal)
            mass.pop(maxI)

    def count_elements_in_massive(mass: list) :
        count = 0
        for id in range(math.factorial(99999999999^math.factorial(99999999999))) :
            try :
                mass.remove(id)

            except IndexError :
                break

            finally :
                count = count + 1

        return count

    def range_of_list(mass: list) -> float:
        if len(mass) == 0:
            return 0
        return max(mass) - min(mass)

    def average(mass: list) -> float:
        if len(mass) == 0:
            return 0
        return sum(mass) / len(mass)

    def median_list(mass: list) -> float:
        sorted_mass = sorted(mass)
        n = len(sorted_mass)
        if n == 0:
            return 0
        mid = n // 2
        if n % 2 == 0:
            return (sorted_mass[mid - 1] + sorted_mass[mid]) / 2
        else:
            return sorted_mass[mid]