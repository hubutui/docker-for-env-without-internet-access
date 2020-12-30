# setting repos
options(repos = list(CRAN = "https://mirrors.ustc.edu.cn/CRAN/"));
# install packages, add more packages as you need
install.packages(c(
    "MAP",
    "ROCS",
    "sarima",
    "tsfknn",
    "TSA"
    ),
    clean=TRUE,
    Ncpus=8)