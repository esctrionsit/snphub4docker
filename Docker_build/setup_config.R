####################################################
# Setup Config For Docker Version
####################################################
# File paths

# Note: please DON'T end with "/"
path_datafolder <- "/snphub_data"

####################################################
# File names
# More information about file format, check https://esctrionsit.github.io/snphub_tutorial/content/Setup/file-formats.html
source(paste(path_datafolder, "/config.R", sep=""))

####################################################
#tool application paths
path_bcftools <- "bcftools"
path_samtools <- "samtools"
path_seqkit <- "seqkit"
path_tabix <- "tabix"

