import matplotlib.pyplot as plt
import numpy as np

# Given values

# Define weight range
weights_A = np.linspace(-0.3, 1.0, 100)

########################
sigma_A = 0.30
sigma_F = 0.20  # Standard deviations of assets A and F
rho = 1  # Correlation between A and F

# Compute portfolio standard deviation
sigma_p = np.sqrt(
    (weights_A * sigma_A) ** 2
    + ((1 - weights_A) * sigma_F) ** 2
    + 2 * weights_A * (1 - weights_A) * rho * sigma_A * sigma_F
)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(weights_A, sigma_p, color="b", label=r"$\rho = 1.0$", linewidth=3, zorder=1)
plt.axvline(0, linestyle="--", color="gray", alpha=0.7)  # Reference line at w_A = 0
plt.axvline(1, linestyle="--", color="gray", alpha=0.7)  # Reference line at w_A = 1


########################

sigma_A = 0.30
sigma_F = 0.20  # Standard deviations of assets A and F
rho = 0.10  # Correlation between A and F

# Compute portfolio standard deviation
sigma_p = np.sqrt(
    (weights_A * sigma_A) ** 2
    + ((1 - weights_A) * sigma_F) ** 2
    + 2 * weights_A * (1 - weights_A) * rho * sigma_A * sigma_F
)

# Plot
plt.plot(weights_A, sigma_p, color="r", label=r"$\rho = 0.10$", linewidth=3, zorder=2)

########################

sigma_A = 0.30
sigma_F = 0.20  # Standard deviations of assets A and F
rho = -1  # Correlation between A and F

# Compute portfolio standard deviation
sigma_p = np.sqrt(
    (weights_A * sigma_A) ** 2
    + ((1 - weights_A) * sigma_F) ** 2
    + 2 * weights_A * (1 - weights_A) * rho * sigma_A * sigma_F
)

# Plot
plt.plot(weights_A, sigma_p, color="gray", label=r"$\rho = -1.0$", linewidth=3, zorder=3)

plt.scatter([0], [sigma_F], color="orange", marker="o", s=200, zorder=3)
plt.scatter([1], [sigma_A], color="blue", marker="o", s=200, zorder=3)

# Adding data labels next to the markers
plt.text(
    0.15, sigma_F + 0.055, "100% in Fund", horizontalalignment="center", fontsize=12, color="black"
)
plt.text(
    0.87, sigma_A + 0.005, "100% in A", horizontalalignment="center", fontsize=12, color="black"
)

# Add arrow from "100% in Fund" label to the orange dot
plt.annotate(
    "",
    xy=(0 + 0.01, sigma_F + 0.01),
    xytext=(0.15, sigma_F + 0.05),
    arrowprops=dict(facecolor="black", edgecolor="black", arrowstyle="->", lw=2),
)


# Adding dashed line at y=0
plt.axhline(y=0, linestyle="--", color="gray", alpha=0.7, linewidth=2)

plt.xlabel("Weight in Asset A", fontsize=14)
plt.ylabel("Portfolio Standard Deviation", fontsize=14)
plt.legend(loc="lower left", bbox_to_anchor=(0.0, 0.1))
# plt.show()
