## Experimental Standards for Deep Learning in Natural Language Processing Research

This repository contains supplementary material from [our paper of the same title](https://arxiv.org/abs/2204.06251). Since our paper can only capture the 
state of affairs at the time of publication, the idea here is to keep a more up-to-date version of the resources in the 
appendix here, and invite the community to collaborate in a transparent manner.

We maintain a version of Table 1 in the original paper, giving an overview over useful resources for different stages of
the research process, namely Data, Codebase & Models, Experiments & Analysis, and Publication.

In [CHECKLIST.md](https://github.com/Kaleidophon/experimental-standards-deep-learning-research/blob/main/CHECKLIST.md), 
we distil the actionable points at the end of the core paper sections into a reusable and modifiable checklist to ensure
replicability. 

In [CHANGELOG.md](https://github.com/Kaleidophon/experimental-standards-deep-learning-research/blob/main/CHANGELOG.md),
we transparently document changes to the repository and versioning. The current version is v0.1. 

### :mortar_board: Citing 

If you find the resources helpful or are using the checklist for one of your academic projects, please cite us in the 
following way:

    @article{ulmer2022experimental,
      title={Experimental Standards for Deep Learning in Natural Language Processing Research},
      author={Ulmer, Dennis and Bassignana, Elisa and M{\"u}ller-Eberstein, Max and Varab, Daniel and Zhang, Mike, van der Goot, Rob and Hardmeier, Christian and Plank, Barbara},
      journal={arXiv preprint arXiv:2204.06251},
      year={2022}
    }

In your paper, you could cite our work for instance as follows:

    For our experimental design, we follow many of the guidelines laid out by \citet{ulmer2022experimental}.

### :jigsaw: Contributing

Contributing can come in two forms: Opening an issue to correct mistakes or improve the existing content, or adding new
content by opening pull requests.

When opening an issue, please label the issue accordingly:
* `enhancement-resources` for issues improving or correcting entries in [RESOURCES.md](https://github.com/Kaleidophon/experimental-standards-deep-learning-research/blob/main/RESOURCES.md).
* `enhancement-standards` for issues improving or correcting entries in [CHECKLIST.md](https://github.com/Kaleidophon/experimental-standards-deep-learning-research/blob/main/CHECKLIST.md).
* `duplicate` for indicating duplicate entries.
* `general` for general questions / issues with the repository.

To contribute and add new content, please first check the [CONTRIBUTING.md](https://github.com/Kaleidophon/experimental-standards-deep-learning-research/blob/main/CONTRIBUTING.md)
file and read the contributing guideline before opening a pull request. Use the label 
* `enhancement-resources` for pull requests adding new resources and 
* `enhancement-standards` for pull requests adding new points to the checklist.

The pull request template can be checked under [PULL_REQUEST_TEMPLATE.md](https://github.com/Kaleidophon/experimental-standards-deep-learning-research/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

## Resources 

We split up Table 1 from the paper into section specific resources below.

### :bar_chart: Data

| Name | Description | Link / Reference |
|:----- |:----- |:----- |
| HuggingFace datasets | Hub to store and share (NLP) data set. | [Link](https://huggingface.co/datasets) / [Paper](https://arxiv.org/pdf/2109.02846.pdf) |
| European Language Resources Association | Public institution for language and evaluation resources. | [About](http://www.elra.info/en/about/) / [Link](http://catalogue.elra.info/en-us/) |
| LINDAT/CLARIN | Open access to language resources and other data and services for the support of research in digital humanities and social sciences. | [Link](https://lindat.cz/) [Paper](https://pure.mpg.de/rest/items/item_60744_3/component/file_60745/content) |
| Zenodo | General-purpose open-access repository for research papers, data sets, research software,reports, and any other research related digital artifacts. | [Link](https://zenodo.org/) |

### :computer: Codebase & Model

| Name | Description | Link / Reference |
|:----- |:----- |:----- |
| Anonymous Github | Website to double-anonymize a Github repository. | [Link](https://anonymous.4open.science/) |
| BitBucket | A website and cloud-based service that helps developers store and manage their code, as well as track and control changes to their code. | [Link](https://bitbucket.org/product/) |
| Conda | Open Source package management systemand environment management system. | [Link](https://docs.conda.io/en/latest/) | 
| codecarbon | Python package estimating and tracking carbon emission of various kind of computer programs. | [Link](https://github.com/mlco2/codecarbon) |
| ONNX | Open format built to represent Machine Learning models. | [Link](https://onnx.ai/) |
| Pipenv | Virtual environment for managing Python packages. | [Link](https://pipenv.pypa.io/en/latest/) |
| Virtualenv | Tool to create isolated Python environments. | [Link](https://virtualenv.pypa.io/en/latest/) |

### :microscope: Experiments & Analysis

| Name | Description | Link / Reference |
|:----- |:----- |:----- |
| baycomp | Python implementation of Bayesian tests for the comparison of classifiers. | [Link](https://github.com/janezd/baycomp) / [Paper](https://jmlr.org/papers/volume18/16-305/16-305.pdf) | 
| BayesianTestML | As baycomp, but also including Julia and R implementations. | [Link](https://github.com/BayesianTestsML/tutorial/) / [Paper](https://jmlr.org/papers/volume18/16-305/16-305.pdf) | 
| deep-significance | Python package implementing the ASO test by Dror et al. (2019) and other utilities. | [Link](https://github.com/Kaleidophon/deep-significance) |
| HyBayes | Python package implementing a variety of frequentist and Bayesian significance tests. | [Link](https://github.com/allenai/HyBayes) |
| pingouin | Python package implementing various parametric and non-parametric statistical tests. | [Link](https://github.com/raphaelvallat/pingouin) / [Paper](https://web.archive.org/web/20190429060332id_/https://www.theoj.org/joss-papers/joss.01026/10.21105.joss.01026.pdf) |
| Protocol buffers | Data structure for model predictions | [Link](https://developers.google.com/protocol-buffers/) |
| RankingNLPSystems | Python package to create a fair global ranking of models across multiple tasks (and eval metrics) | [Link](https://github.com/pierrecolombo/rankingnlpsystems) / [Paper](https://arxiv.org/pdf/2202.03799.pdf) | 

### :page_facing_up: Publication

| Name | Description | Link / Reference |
|:----- |:----- |:----- |
| dlpd | Computer science bibliography to find correct versions of papers. | [Link](https://dblp.org/) | 
| impact | Online calculator of carbon emissions based on GPU type | [Link](https://github.com/mlco2/impact) / [Paper](https://arxiv.org/pdf/1910.09700.pdf) |
| Google scholar | Scientific publication search engine. | [Link](https://scholar.google.com/) |
| Semantic Scholar | Scientific publication search engine. | [Link](https://www.semanticscholar.org) |
| rebiber | Python tool to check and normalize the bib entries to the official published versions of the cited papers. | [Link](https://github.com/yuchenlin/rebiber) |
