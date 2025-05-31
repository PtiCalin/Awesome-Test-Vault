# plugin_usage.R
# Visualize VaultOS plugin usage with a simple bar plot

# Mock plugin usage data
plugins <- c("Core", "Template", "Subplugin", "Theme", "Tracker")
usage <- c(15, 10, 7, 5, 3)

# Basic bar plot
barplot(usage,
        names.arg = plugins,
        col = "skyblue",
        main = "VaultOS Plugin Usage",
        xlab = "Plugin Type",
        ylab = "Usage Count")

# Save to file
dev.copy(png, filename="plugin_usage.png")
dev.off()
