import numpy as np

# Parámetros
population_size = 10 # Tamaño de la población
gene_range = (0, 10) # Rango de intervalos de los genes, cada gen puede valer de 0 a 10
num_selected = 5 # Tamaño de la genes aptos a seleccionar

# Crear población inicial
population = np.random.uniform(gene_range[0], gene_range[1], population_size)

def fitness_function(x):
    return x ** 2

def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

def mutate(individual, mutation_rate=0.1):
    if np.random.rand() < mutation_rate:
        return individual + np.random.uniform(-1, 1)
    return individual

# Ejecución del algoritmo genético
for generation in range(10):  # Número de generaciones
    fitness = fitness_function(population)
    selected_indices = np.argsort(fitness)[-num_selected:]
    selected_population = population[selected_indices]
    
    new_population = []
    for i in range(num_selected // 2):
        parent1, parent2 = selected_population[2*i], selected_population[2*i + 1]
        child = crossover(parent1, parent2)
        new_population.append(child)
    new_population = np.array(new_population)
    
    mutated_population = np.array([mutate(ind) for ind in new_population])
    population = mutated_population

    print(f"Generación {generation + 1}:")
    print("Población:", population)
    print("Aptitud:", fitness_function(population))
