install.packages("ggplot2")
library(ggplot2)
if(!require("quanteda")) {install.packages("quanteda"); library("quanteda")}
if(!require("tidyverse")) {install.packages("tidyverse"); library("tidyverse")}
if(!require("scales")) {install.packages("scales"); library("scales")}
if(!require("ggdendro")) {install.packages("ggdendro"); library("ggdendro")}
install.packages("tidytable")
library(tidytable)
install.packages("colorspace")
library(colorspace)
frequencies <- left_join.(Test_Arch, Test_Laien, by = "Wort", head(10), arrange(Anzahl.y), mutate(Wort = factor(Wort, Wort)))
ggplot(Test_Arch_Laien_comb) +
  geom_segment(aes(x=Wort, xend=Wort, y=Anzahl_Arch, yend=Anzahl_Laien), color="grey") +
  geom_point(aes(x=Wort, y=Anzahl_Arch), color = "blue", size = 3 ) +
  geom_point(aes(x=Wort, y=Anzahl_Laien), color = "lightcoral", size = 3 ) +
  ggtitle("Wortfrequenzen im Sprachgebrauch von Architekten und Laien im Vergleich") + 
  xlab("") + ylab("Wortfrequenz") + 
  coord_flip()

