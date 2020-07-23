library(splus2R)
library(ifultools)
library(fractal)
calHurst <- function(S){
    walk <- S
    value = hurstSpec(walk,method="smoothed")
	return(value)
}