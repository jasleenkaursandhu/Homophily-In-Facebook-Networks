# Assessing Homophily in Facebook Friendships

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Analysis](#analysis)
- [Conclusion](#conclusion)
- [Usage](#usage)
- [License](#license)

## Introduction

This project aims to investigate the presence of homophily in Facebook friendships and its sociological implications. Homophily is the tendency of individuals to associate with others who share similar attributes or interests. In this context, we explore whether users on Facebook are more likely to connect with individuals who possess similar characteristics, including interests, education levels, and political affiliations. By examining the presence of homophily, we aim to uncover whether Facebook reflects and potentially reinforces sociological patterns of similarity and connection formation. The project has significant implications for understanding the dynamics of virtual communities and social interactions on online platforms.

## Dataset

The dataset used in this project is the [Ego Facebook Networks](https://snap.stanford.edu/data/ego-Facebook.html) from the Stanford Network Analysis Project (SNAP). The dataset includes information on nodes, edges (friendship connections), and attributes. For specific details on data format and downloading, please refer to the provided link.

## Methodology

### Loading the Facebook Network
We start by loading the Facebook network dataset, consisting of nodes, edges, and attribute features.

### Calculating Common Friends
To measure homophily, we calculate the average number of common friends between connected nodes in the network.

### Community Detection
Louvain community detection is employed to identify communities within the network. We assess homophily by counting matching and non-matching edges based on political affiliation.

### Attribute Analysis
We analyze homophily based on various attributes like location, education, and gender.

## Analysis

The analysis revealed compelling evidence for the presence of homophily in Facebook networks. We consistently observed assortative mixing, community formation, and attribute-based clustering. Users exhibited a clear preference for establishing connections with individuals who share common characteristics, such as location, education, or gender.

## Conclusion

The project concludes that Facebook networks exhibit homophily, emphasizing that users on the platform tend to form connections with individuals who share similar attributes. This observation has implications for understanding the dynamics of online social networks and the reflection of real-world tendencies in forming connections with like-minded individuals.

## Usage

To run the code and perform a similar analysis, follow the steps outlined in the code files provided in this repository.

## License

This project is available under the [MIT License](LICENSE).

---

**Disclaimer:** This project is for research and educational purposes only. Please use the dataset and code responsibly and adhere to the terms of use provided by the dataset source.
