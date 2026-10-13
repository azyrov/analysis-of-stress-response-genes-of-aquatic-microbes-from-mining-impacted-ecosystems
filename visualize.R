library(ggplot2)

data <- read.csv("microbial_metrics.csv")

print(head(data))
summary(data)
my_plot <- ggplot(data, aes(x = length, y = gc.content)) +
  geom_point(color = "steelblue", size = 3, alpha = 0.8) +
  labs(title = "GC-Content vs Sequence Length",
       subtitle = "Galamsey Environmental Impact Study",
       x = "Sequence Length (bp)",
       y = "GC-Content (%)") +
  theme_minimal()

print(my_plot)

ggsave("galamsey_gc_plot.png", plot = my_plot, width = 8, height = 6, dpi = 300)