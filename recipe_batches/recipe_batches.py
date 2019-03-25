#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    results = []
    if recipe.keys() != ingredients.keys():
        return 0
    for x in recipe:
        if ingredients[x] // recipe[x] == 0:
            return 0
        else:
            results.append(ingredients[x] // recipe[x])
    return min(results)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    # # should return 0
    # recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    # ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    # # should return 0
    # recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
    # ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}
    # # should return 1
    # recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
    # ingredients = {'milk': 198, 'butter': 52, 'cheese': 10}
    # # should return 2
    recipe = {'milk': 2, 'sugar': 40, 'butter': 20}
    ingredients = {'milk': 5, 'sugar': 120, 'butter': 500}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
