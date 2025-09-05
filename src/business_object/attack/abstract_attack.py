from abc import ABC, abstractmethod

from business_object.pokemon.abstract_pokemon import AbstractPokemon

import random


class AbstractAttack(ABC):
    def __init__(self, power: int, name: str, description: str) -> None:
        self.power = power
        self.name = name
        self.description = description

    @abstractmethod
    def compute_damage(self, pkm1: AbstractPokemon, pkm2: AbstractPokemon) -> int:
        raise NotImplementedError


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, pkm1: AbstractPokemon, pkm2: AbstractPokemon) -> int:
        return self.power


class AbstractFormulaAttack(ABC):
    @abstractmethod
    def get_attack_stat(self):
        raise NotImplementedError

    @abstractmethod
    def get_defense_stat(self):
        raise NotImplementedError

    def compute_damage(self, pkm1: AbstractPokemon, pkm2: AbstractPokemon) -> int:
        return ((2 * pkm1.level / 5 + 2) * pkm1.power
                * self.get_attack_stat(pkm1) / self.get_defense_stat(pkm2) * 50 + 2) \
            * (random.randrange(85, 100) / 100)


class SpecialFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(self, pkm: AbstractPokemon) -> float:
        raise pkm.sp_atk_current

    def get_defense_stat(self, pkm: AbstractPokemon) -> float:
        raise pkm.sp_def_current


class PhysicalFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(self, pkm: AbstractPokemon) -> float:
        raise pkm.attack_current

    def get_defense_stat(self, pkm: AbstractPokemon) -> float:
        raise pkm.defense_current
