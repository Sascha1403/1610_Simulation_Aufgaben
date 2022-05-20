import matplotlib.pyplot as plt
import numpy as np


def linear_konrenzgenerator(x):
    a = 4
    b = 1
    m = 9
    x1 = (a * x + b) % m
    return x1

def get_pseudo_random_numbers(seed, length):
    pseudo_random_numbers = [seed]
    for i in range(length):
        pseudo_random_numbers.append(linear_konrenzgenerator(pseudo_random_numbers[-1]))
    return pseudo_random_numbers

def get_gaussian_distribution(mu, sigma, number):
    return np.random.normal(mu, sigma, number)

def get_expon_distribution(scale, number):
    return np.random.exponential(scale, number)

def get_uniform_distribution(lower_bound, upper_bound, number):
    return np.random.uniform(lower_bound, upper_bound, number)

def plot_distribution(distribution, name):
    fig, ax = plt.subplots()
    ax.hist(distribution, 15)
    ax.set_title(name, size=25)
    ax.tick_params(labelsize=22)
    ax.set_xlabel('bin range', size=22)
    ax.set_ylabel('frequency', size=22)
    ax.grid()
    plt.show()


if __name__ == '__main__':
    print(get_pseudo_random_numbers(3, 100))
    expon_distribution = get_expon_distribution(0.6, 1000)
    uniform_distribution = get_uniform_distribution(0, 5, 1000)
    gaussian_distribution = get_gaussian_distribution(0.9, 1, 1000)

    plot_distribution(expon_distribution, "Expotentailverteilung")
    plot_distribution(uniform_distribution, "Normalverteilung")
    plot_distribution(gaussian_distribution, "Gaußverteilung")
