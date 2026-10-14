library(ggplot2)

data <- read.csv("microbial_metrics.csv")

if (nrow(data) > 5000) {
  data <- data[sample(1:nrow(data), 5000), ]
}

print(head(data))
summary(data)

my_plot <- ggplot(data, aes(x = length, y = gc.content, color = group)) +
  geom_point(alpha = 0.5, size = 1) +
  labs(title = "GC-Content vs Sequence Length Distribution",
       subtitle = "Real-World Metagenomic Assembly Analysis (Galamsey Ecosystem)",
       x = "Sequence / Contig Length (bp)",
       y = "GC-Content (%)",
       color = "Experimental Group") +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    plot.title = element_text(face = "bold", size = 14),
    axis.title = element_text(face = "bold")
  )

print(my_plot)

ggsave("galamsey_large_scale_plot.png", plot = my_plot, width = 10, height = 6, dpi = 300)