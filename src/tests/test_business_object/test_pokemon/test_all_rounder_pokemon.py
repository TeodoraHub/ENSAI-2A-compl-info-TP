from business_object.pokemon.all_rounder_pokemon import AllRounder
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        Alakazam = AllRounder(stat_current=Statistic(sp_atk=300, sp_def=300))

        # WHEN
        multiplier = Alakazam.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 4
