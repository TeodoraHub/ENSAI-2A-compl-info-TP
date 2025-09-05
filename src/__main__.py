from business_object.pokemon.attacker_pokemon import Attacker
from business_object.pokemon.defender_pokemon import Defender
from business_object.pokemon.all_rounder_pokemon import AllRounder
from business_object.statistic import Statistic

# Create statistics for the following pokemon
stats_pk1 = Statistic(100, 40, 10, 10, 10, 10)

# Create a pokemon
pk1 = Attacker(name="Pika", stat_current=stats_pk1, type_pk="Attacker")
pk2 = Defender(name="Nidoran", stat_current=stats_pk1, type_pk="Attacker")
pk3 = AllRounder(name="Ptitard", stat_current=stats_pk1, type_pk="Attacker")

# Print the pokemon (call __str__() method)
print(pk1)
print(pk2)
print(pk3)
