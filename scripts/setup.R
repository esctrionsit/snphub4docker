DIR <- dirname(substring(commandArgs(trailingOnly = FALSE)[grep("--file=", commandArgs(trailingOnly = FALSE))], 8))

source(paste(DIR, "/../setup_config.R", sep=""))
source(paste(DIR, "/advanced_config.R", sep=""))
source(paste(DIR, "/setup_scripts/envir_check.R", sep=""))
source(paste(DIR, "/setup_scripts/file_check.R", sep=""))
source(paste(DIR, "/setup_scripts/file_make.R", sep=""))
source(paste(DIR, "/setup_scripts/file_recheck.R", sep=""))

status <- 0

status <- envir_check(status)

if(status != 1){ setup <- file_check(status) }

if(status != 1){ setup <- file_make(status, DIR) }

if(status != 1){ file_recheck() }

if(status != 1){ system(paste("/bin/bash ", DIR, "/setup_scripts/ClearTmpFiles.sh ", path_datafolder, sep=""))}

if(status != 1){
	para <- c("name_vcf_folder", "name_gff3", "name_fasta", "name_metadata", "name_groupdata", "name_sam_location", "name_sysinfo", "name_UIsetting")
	operator <- c("<-", "<-", "<-", "<-", "<-", "<-", "<-", "<-")
	value <- c(paste("\"", name_vcf_folder, "\"", sep=""), paste("\"", name_gff3, "\"", sep=""), paste("\"", name_fasta, "\"", sep=""), paste("\"", name_metadata, "\"", sep=""), paste("\"", name_groupdata, "\"", sep=""), paste("\"", name_sam_location, "\"", sep=""))
	if(!is.na(name_sysinfo)){
		value <- c(value, paste("\"", name_sysinfo, "\"", sep=""))
	}else{
		value <- c(value, "NA")
	}
	if(!is.na(name_UIsetting)){
		value <- c(value, paste("\"", name_UIsetting, "\"", sep=""))
	}else{
		value <- c(value, "NA")
	}
	cdf <- data.frame(para=para, operator=operator, value=value)
	write.table(cdf, paste(path_datafolder, "/", "config.R", sep=""), quote=F, sep=" ", row.names=F, col.names=F)
}