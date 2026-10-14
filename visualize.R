library(ggplot2)

data <- read.csv("microbial_metrics.csv")

print(head(data))
summary(data)

my_plot <- ggplot(data, aes(x = length, y = gc.content, color = group)) +
  geom_point(alpha = 0.4, size = 1) +
  geom_density_2d(alpha = 0.7) +
  labs(title = "GC-Content vs Sequence Length Distribution",
       subtitle = "Real-World Metagenomic Assembly Analysis (Galamsey Ecosystem)",
       x = "Sequence / Contig Length (bp)",
       y = "GC-Content (%)",
       color = "Experimental Group") +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    plot.title = element_text(face = "bold", size = 14),
    axis.title = element.text(face = "bold")
  )

print(my_plot)

ggsave("galamsey_large_scale_plot.png", plot = my_plot, width = 10, height = 6, dpi = 300)