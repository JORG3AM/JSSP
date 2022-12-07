# -*- coding: utf-8 -*-
"""MicroGenetic algorithm (one sum).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Vn0kAX1pjIifGMYHuD0BMZDoMLz1H2J
"""

# Libraries
import random
import numpy
import matplotlib.pyplot

# Individual initialization
def createIndividual(n):
  return numpy.random.randint(0, 2, n)

p = createIndividual(10)
print(p)

# Crossover operator
def combine(parentA, parentB, cRate):
  if (random.random() <= cRate):
    cPoint = numpy.random.randint(1, len(parentA))
    #print(cPoint)
    offspringA = numpy.append(parentA[0:cPoint], parentB[cPoint:])
    offspringB = numpy.append(parentB[0:cPoint], parentA[cPoint:])
  else:
    offspringA = numpy.copy(parentA)
    offspringB = numpy.copy(parentB)
  return offspringA, offspringB

p1 = createIndividual(10)
p2 = createIndividual(10)
print(p1)
print(p2)
o1, o2 = combine(p1, p2, 1.0)
print(o1)
print(o2)

# Mutation operator
def mutate(individual, mRate):
  for i in range(len(individual)):
    if (random.random() <= mRate):
      individual[i] = not(individual[i])
  return individual

p1 = createIndividual(10)
print(p1)
mutate(p1, 0.10)
print(p1)

# Evaluation function
def evaluate(individual):
  return sum(individual)

p1 = createIndividual(10)
print(p1)
print(evaluate(p1))

# Tournament selection
def select(population, evaluation, tSize):
  winner = numpy.random.randint(0, len(population))
  for i in range(tSize - 1):
    rival = numpy.random.randint(0, len(population))
    if (evaluation[rival] > evaluation[winner]):
      winner = rival
  return population[winner]

# Genetic algorithm
def geneticAlgorithm(n, pSize, gens, cRate, mRate):
  # Creates the initial population
  population = [None] * pSize
  evaluation = [None] * pSize
  for i in range(pSize):
    population[i] = createIndividual(n)
    evaluation[i] = evaluate(population[i])
  # Keeps a record of the best individual found so far
  index = 0;
  for i in range(1, pSize):
    if (evaluation[i] > evaluation[index]):
      index = i;
  bestIndividual = population[index]
  bestEvaluation = evaluation[index]
  # Keeps the information for plotting the performance of the algorithm
  best = [0] * gens
  avg = [0] * gens
  # Runs the evolutionary process
  for i in range(gens):
    k = 0
    newPopulation = [None] * pSize
    
    newPopulation[index] = population[index]
    # Crossover
    for j in range(pSize // 2):
      parentA = select(population, evaluation, 3)
      parentB = select(population, evaluation, 3)
      offspring1, offspring2 = combine(parentA, parentB, cRate)
      newPopulation[k] = offspring1
      newPopulation[k + 1] = offspring2
      k = k + 2
    population = newPopulation
    # Mutation
    for j in range(pSize):
      population[j] = mutate(population[j], mRate)
      evaluation[j] = evaluate(population[j])
      # Keeps a record of the best individual found so far
      if (evaluation[j] > bestEvaluation):
        bestEvaluation = evaluation[j]
        bestIndividual = population[j]
        index = j
      best[i] = bestEvaluation
      avg[i] = numpy.average(evaluation)
  matplotlib.pyplot.plot(range(gens), best, label = "Best")
  matplotlib.pyplot.plot(range(gens), avg, label = "Average")
  matplotlib.pyplot.legend()
  matplotlib.pyplot.title("GA Run")
  matplotlib.pyplot.show()
  # Returns the best individual found so far
  return bestIndividual, bestEvaluation

# Tests
solution, eval = geneticAlgorithm(100, 8, 100, 1.0, 0.01)
print(solution)
print(eval)