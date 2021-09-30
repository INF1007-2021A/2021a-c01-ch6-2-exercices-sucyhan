#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.colors
from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    my_dict = dict()
    for index, value in enumerate(some_list):
        my_dict[value]= index
#    dictionnaire = []
#    for x in some_list:
#        dictionnaire[x] = some_list.index(x)
#    return dictionnaire
#    dictionnaire = dict()
#    for e in some_list:
#        dictionnaire[e] = dictionnaire.get (e, some_list.index(e))
    return my_dict


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
#    some_list = []
#    for color in colors:
#        some_list.append((cnames[color]))

    return [(color, cnames[color]) for color in colors]


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350

    return [i for i in range(10000) if i < 15 or i > 350]


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    mse_dict = {}
    for key_model_name, value in model_dict.items():
        print(key_model_name)
        print(value)
        error_sum = 0
        for point in value:
          error_sum +=  (point[0] - point[1]) ** 2

        mse_dict[key_model_name] = error_sum/len(value)
    return mse_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
