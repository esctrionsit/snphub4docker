FROM centos:centos7

LABEL maintainer="Wang Wenxi<wangwenxi20@gmail.com>"

##########################################################
# yum

RUN yum -y update

RUN yum -y install epel-release

RUN yum -y update

RUN yum -y install R

RUN yum -y install libjpeg-turbo-devel

RUN yum -y install openssl-devel

RUN yum -y install libcurl-devel

RUN yum -y install -y geos-devel

RUN yum -y install udunits2-devel

RUN yum -y install postgresql-devel

RUN yum -y install libsqlite3x-devel.x86_64

RUN yum -y install wget

RUN yum -y install curl

RUN yum -y install bzip2

RUN yum -y install ncurses-devel

WORKDIR /

RUN mkdir tmpdownloads

##########################################################
# bin

# SAMtools

WORKDIR /tmpdownloads/

RUN wget -c https://github.com/samtools/samtools/releases/download/1.4/samtools-1.4.tar.bz2

RUN ls

RUN tar jxvf samtools-1.4.tar.bz2

WORKDIR /tmpdownloads/samtools-1.4

RUN ./configure --prefix=/tmpdownloads/samtools-1.4

RUN make && make install

RUN cp ./bin/samtools /usr/local/bin/

RUN echo 'export PATH="/tmpdownloads/samtools-1.4/bin:$PATH" ' >>~/.bashrc

RUN source ~/.bashrc

# BCFtools

WORKDIR /tmpdownloads/

RUN wget -c https://github.com/samtools/bcftools/releases/download/1.8/bcftools-1.8.tar.bz2

RUN tar jxvf bcftools-1.8.tar.bz2

WORKDIR /tmpdownloads/bcftools-1.8

RUN ./configure --prefix=/tmpdownloads/bcftools-1.8

RUN make && make install

RUN cp ./bcftools /usr/local/bin/

RUN echo 'export PATH="/tmpdownloads/samtools-1.4/bin:$PATH" ' >>~/.bashrc

RUN source ~/.bashrc

# tabix

WORKDIR /tmpdownloads/

RUN wget -c https://github.com/samtools/htslib/releases/download/1.6/htslib-1.6.tar.bz2

RUN tar jxvf htslib-1.6.tar.bz2

WORKDIR /tmpdownloads/htslib-1.6

RUN ./configure --prefix=/tmpdownloads/htslib-1.6

RUN make && make install

RUN cp ./bin/tabix /usr/local/bin/

RUN echo 'export PATH="/tmpdownloads/htslib-1.6/bin:$PATH" ' >>~/.bashrc

RUN source ~/.bashrc

# seqkit

WORKDIR /tmpdownloads/

RUN wget -c https://github.com/shenwei356/seqkit/releases/download/v0.11.0/seqkit_linux_amd64.tar.gz

RUN tar -zxvf seqkit_linux_amd64.tar.gz

RUN cp seqkit /usr/local/bin/

# PROJ

WORKDIR /tmpdownloads/

RUN wget https://download.osgeo.org/proj/proj-6.2.1.tar.gz

RUN tar -zxvf proj-6.2.1.tar.gz

RUN wget https://download.osgeo.org/proj/proj-datumgrid-1.8.zip

RUN unzip -o proj-datumgrid-1.8.zip -d proj-6.2.1/data/

WORKDIR /tmpdownloads/proj-6.2.1

RUN ./configure && make && make install

ENV PKG_CONFIG_PATH=/tmpdownloads/proj-6.2.1

# GEOS

WORKDIR /tmpdownloads/

RUN wget http://download.osgeo.org/geos/geos-3.6.2.tar.bz2

RUN tar -xjf geos-3.6.2.tar.bz2

WORKDIR /tmpdownloads/geos-3.6.2

RUN ./configure && make && make install

RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/libgeos-x86_64.conf

RUN ldconfig

# GDAL

WORKDIR /tmpdownloads/

RUN wget http://download.osgeo.org/gdal/3.0.2/gdal302.zip

RUN unzip gdal302.zip

WORKDIR /tmpdownloads/gdal-3.0.2

RUN ./configure && make && make install

RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/libgdal-x86_64.conf

RUN ldconfig

##########################################################
# R packages

RUN R -e "install.packages('shiny', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('ggplot2', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('ggmap', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('crayon', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('rjson', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('udunits2', configure.args='--with-udunits2-include=/usr/include/udunits2/', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('RPostgreSQL', dependencies=TRUE, repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('ape', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('adegenet', repos='https://cran.rstudio.com/')"

# RUN R -e "install.packages('pegas', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/pegas/pegas_0.11.tar.gz', repos=NULL, type='source')"

# RUN R -e "install.packages('vcfR', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('memuse', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('pinfsc50', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('vegan', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/vcfR/vcfR_1.9.0.tar.gz', repos=NULL, type='source')"

RUN R -e "install.packages('DT', repos='https://cran.rstudio.com/')"

RUN R -e "install.packages('maps', repos='https://cran.rstudio.com/')"

##########################################################
# Clone SnpHub

WORKDIR /

RUN yum -y install git

RUN git clone https://github.com/esctrionsit/snphub

RUN git clone https://github.com/esctrionsit/snphub4docker

RUN cp /snphub4docker/run_snphub /

RUN /bin/bash -c 'chmod +x /run_snphub'

##########################################################
# To save spaces

WORKDIR /

RUN rm -rf tmpdownloads
