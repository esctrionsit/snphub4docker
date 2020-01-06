file_make <- function(status, DIR){
	cat(blue$bgWhite$bold("[ ]") %+% black$bgWhite$bold(" Begining mew file making") %+% "\n")

	tryCatch(
		{
			system(paste(paste("/bin/bash ", DIR, "/setup_scripts/IndexFaGff.sh", sep=""), path_datafolder, path_samtools, name_fasta, path_tabix, name_gff3, sep=" "))

			system(paste(paste("/bin/bash ", DIR, "/setup_scripts/GenomeDatabaseBuild.sh", sep=""), path_datafolder, name_gff3, name_fasta, sep=" "))

			system(paste(paste("/bin/bash ", DIR, "/setup_scripts/AnnoWithSnpEff.sh", sep=""), path_datafolder, path_vcfolder, name_gff3, sep=" "))

			system(paste(paste("/bin/bash ", DIR, "/setup_scripts/MakeGeneIndex.sh", sep=""), path_datafolder, name_gff3, sep=" "))

			system(paste(paste("/bin/bash ", DIR, "/setup_scripts/ClearTmpFiles.sh", sep=""), path_datafolder, sep=" "))
		}, error = function(e) {
			cat(red$bgWhite$bold("[-]") %+% black$bgWhite$bold(" Some things are wrong during file building. Please check the log for more details.") %+% "\n"
				%+% black$bgWhite$bold("    ") %+% black$bgWhite$bold(e) %+% "\n"
				)
			status <- 1
		}
	)
	cat(green$bgWhite$bold("[+]") %+% black$bgWhite$bold(" new file making finished") %+% "\n")
	#return
	status
}