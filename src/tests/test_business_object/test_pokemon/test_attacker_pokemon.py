from business_object.pokemon.attacker_pokemon import Attacker
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        Alakazam = Attacker(stat_current=Statistic(speed=300, attack=100))

        # WHEN
        multiplier = Alakazam.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 3
