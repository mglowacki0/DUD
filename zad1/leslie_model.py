import numpy as np

# Dane wejściowe

L = np.array([
    [0,   3,    3,   3],
    [0.2, 0,    0,   0],
    [0,   0.29, 0,   0],
    [0,   0,   0.1,  0]
])

x0 = np.array([1000, 2000, 1500, 500])

# Obliczenia

# Potęga macierzy
L10 = np.linalg.matrix_power(L, 10)

# Rozkład populacji po 10 latach
x10 = L10 @ x0

# Wartości własne (do analizy stabilności)
eigenvalues, eigenvectors = np.linalg.eig(L)

# Promień spektralny
spectral_radius = max(abs(eigenvalues))

# Wyniki

print("Macierz L^10:\n", L10)
print("\nRozkład populacji po 10 latach x10:")
print(x10)

print("\nWartości własne macierzy L:")
print(eigenvalues)

print("\nPromień spektralny:", spectral_radius)

if spectral_radius > 1:
    print("Populacja rośnie.")
elif spectral_radius == 1:
    print("Populacja stabilizuje się.")
else:
    print("Populacja zanika (kurczy się).")
