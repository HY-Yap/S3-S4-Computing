stat_name_list = ['HP','ATK','DEF','Speed','CRIT Rate','CRIT DMG','Break Effect','Effect RES','Outgoing Healing','Energy Regen Rate','HP%','ATK%','DEF%']

# your code for Task 3
class Stats:
    def __init__(self):
        self._stats = {}
        self.Stats()
        # print(self._stats)
    
    def Stats(self) -> None:
        for itm in stat_name_list:
            self._stats[itm] = None
    
    def get_stats(self) -> dict:
        return self._stats
    
    def read_str(self, stats_str: str) -> dict:
        stats_str = stats_str.split(';')
        for stat in stats_str:
            stat = stat.split(':')
            if stat[0] in self._stats:
                if stat[1] == '' or stat[1] == None:
                    self._stats[stat[0]] = 0
                else:
                    self._stats[stat[0]] = int(stat[1])
    
    def value_list(self) -> list:
        result = []
        for itm in  self._stats:
            result.append(self._stats[itm])
        return result
    
    def __str__(self) -> str:
        result = ''
        for itm in self._stats:
            result += f'{itm}:{self._stats[itm]};'
        return result[:-1]
    
    def __add__(self, other: object) -> object:
        combined = Stats()
        combined.read_str(self.__str__())
        stats_str = other.__str__().split(';')
        for stat in stats_str:
            stat = stat.split(':')
            if stat[0] in combined._stats:
                if stat[1] == '' or stat[1] == None:
                    continue
                else:
                    combined._stats[stat[0]] += int(stat[1])
        return combined


# test for Task 3
def test_stats():
    stats1 = Stats()
    stats1.read_str(
        'HP:1000;ATK:100;DEF:100;Speed:100;CRIT Rate:5;CRIT DMG:50;Break Effect:0;Effect RES:0;Outgoing Healing:0;Energy Regen Rate:0;HP%:0;ATK%:0;DEF%:0')
    print(stats1)

    stats2 = Stats()
    stats2.read_str(
        'HP:1000;ATK:100;DEF:100;Speed:100;CRIT Rate:5;CRIT DMG:50;Break Effect:0;Effect RES:0;Outgoing Healing:0;Energy Regen Rate:0;HP%:0;ATK%:0;DEF%:0')

    stats3 = stats1 + stats2
    print(stats3)


test_stats()
