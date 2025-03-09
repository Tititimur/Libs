import math

class list :
    def atmin(mass: list) :
        DM = []
        while len(mass) > 0 :
            minI = -1
            minVal = 0
            for index in range(len(mass)) :
                if minI < 0 or mass[index] < minVal :
                    minVal = mass[index]
                    minI = index

            DM.append(minVal)
            mass.pop(minI)

        return DM

    def atmax(mass: list) :
        DM = []
        while len(mass) > 0 :
            maxI = -1
            maxVal = 0
            for index in range(len(mass)) :
                if maxI < 0 or mass[index] < maxVal :
                    maxVal = mass[index]
                    maxI = index

            DM.append(maxVal)
            mass.pop(maxI)

        return DM

    def countElementsInMassive(mass: list) -> int :
        count = 0
        for id in range(float('inf')) :
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

    def averageArifmetic(mass: list) -> float:
        if len(mass) <= 1:
            return 0
        return sum(mass) / len(mass)

    def averageValue(mass: list,sort: bool) -> list:
        if not sort :
            if len(mass) % 2 == 0 :
                return [mass[(len(mass) // 2) - 1], mass[((len(mass) // 2))]]
            else :
                return [mass[(len(mass) // 2)]]
        else :
            SM = list.atmin(mass)
            if len(SM) % 2 == 0 :
                return [SM[(len(SM) // 2) - 1], SM[((len(SM) // 2))]]
            else :
                return [SM[(len(SM) // 2)]]
class operationsWithNumbers :
    def averageArifmetic(mass: list) -> float :
        try :
            return sum(mass) / list.countElementsInMassive(mass)
        except :
            return ZeroDivisionError