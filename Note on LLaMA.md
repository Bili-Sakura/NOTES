# Note on LLaMA

## Highlights

### Scaling Laws

The objective of the scaling laws from Hoffmann et al. (2022) is to determine how to best scale the dataset and model sizes for a particular training compute budget.<span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F14082555%2Fitems%2F8TPGCK9T%22%5D%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/8TPGCK9T">Hoffmann et al., 2022</a></span>)</span> However, this objective disregards the inference budget, which becomes critical when serving a language model at scale. In this context, given a target level of performance, the preferred model is not the fastest to train but the fastest at inference, and although it may be cheaper to train a large model to reach a certain level of performance, a smaller one trained longer will ultimately be cheaper at inference. For instance, although Hoffmann et al. (2022) recommends training a 10B model on 200B tokens, we find that the performance of a 7B model continues to improve even after 1T tokens.

### LLMs Performances on Massive Multitask Language Understanding(MMLU)

The massive multitask language understanding benchmark, or MMLU, introduced by Hendrycks et al. (2020) consists of multiple choice questions covering various domains of knowledge, including humanities, STEM and social sciences. We evaluate our models in the 5-shot setting, using the examples provided by the benchmark, and report results in Table 9. On this benchmark, we observe that the LLaMA-65B is behind both Chinchilla70B and PaLM-540B by a few percent in average, and across most domains. A potential explanation is that we have used a limited amount of books and academic papers in our pre-training data, i.e., ArXiv, Gutenberg and Books3, that sums up to only 177GB, while these models were trained on up to 2TB of books. This large quantity of books used by Gopher, Chinchilla and PaLM may also explain why Gopher outperforms GPT-3 on this benchmark, while it is comparable on other benchmarks. <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F14082555%2Fitems%2F8Y9Y33EK%22%5D%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/8Y9Y33EK">Hendrycks et al., 2021</a></span>)</span>

### Generations from LLaMA-65B

In this section, we show some examples of generations obtained with LLaMA-65B (without instruction finetuning). Prompts are in bold.

![\<img alt="" data-attachment-key="T77PGFJY" width="1843" height="731" src="attachments/LLaMA/T77PGFJY.png" ztype="zimage">](attachments/LLaMA/T77PGFJY.png)

![\<img alt="" data-attachment-key="RB67EZ47" width="1858" height="997" src="attachments/LLaMA/RB67EZ47.png" ztype="zimage">](attachments/LLaMA/RB67EZ47.png)

![\<img alt="" data-attachment-key="WD3BBWBZ" width="1878" height="596" src="attachments/LLaMA/WD3BBWBZ.png" ztype="zimage">](attachments/LLaMA/WD3BBWBZ.png)

![\<img alt="" data-attachment-key="62BGWIH7" width="1854" height="1473" src="attachments/LLaMA/62BGWIH7.png" ztype="zimage">](attachments/LLaMA/62BGWIH7.png)

![\<img alt="" data-attachment-key="SXNPVNED" width="1860" height="894" src="attachments/LLaMA/SXNPVNED.png" ztype="zimage">](attachments/LLaMA/SXNPVNED.png)

![\<img alt="" data-attachment-key="YYUCPUX6" width="1867" height="1661" src="attachments/LLaMA/YYUCPUX6.png" ztype="zimage">](attachments/LLaMA/YYUCPUX6.png)

### Generations from LLaMA-I

![\<img alt="" data-attachment-key="VLN77MZV" width="1856" height="663" src="attachments/LLaMA/VLN77MZV.png" ztype="zimage">](attachments/LLaMA/VLN77MZV.png)

![\<img alt="" data-attachment-key="HXMSQ4BK" width="1871" height="1175" src="attachments/LLaMA/HXMSQ4BK.png" ztype="zimage">](attachments/LLaMA/HXMSQ4BK.png)

![\<img alt="" data-attachment-key="7ZP7L3CW" width="1869" height="675" src="attachments/LLaMA/7ZP7L3CW.png" ztype="zimage">](attachments/LLaMA/7ZP7L3CW.png)

![\<img alt="" data-attachment-key="ARNAS3IG" width="1872" height="2388" src="attachments/LLaMA/ARNAS3IG.png" ztype="zimage">](attachments/LLaMA/ARNAS3IG.png)

![\<img alt="" data-attachment-key="ND42DMXY" width="1878" height="1617" src="attachments/LLaMA/ND42DMXY.png" ztype="zimage">](attachments/LLaMA/ND42DMXY.png)![]()

![\<img alt="" data-attachment-key="RB3PC89U" width="1869" height="1365" src="attachments/LLaMA/RB3PC89U.png" ztype="zimage">](attachments/LLaMA/RB3PC89U.png)

![\<img alt="" data-attachment-key="XWNE4SNR" width="1863" height="1164" src="attachments/LLaMA/XWNE4SNR.png" ztype="zimage">](attachments/LLaMA/XWNE4SNR.png)

![\<img alt="" data-attachment-key="8JCGVB54" width="1908" height="2496" src="attachments/LLaMA/8JCGVB54.png" ztype="zimage">](attachments/LLaMA/8JCGVB54.png)

![\<img alt="" data-attachment-key="CPRH6JJG" width="1926" height="2043" src="attachments/LLaMA/CPRH6JJG.png" ztype="zimage">](attachments/LLaMA/CPRH6JJG.png)

## References

Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., Casas, D. de L., Hendricks, L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E., Millican, K., Driessche, G. van den, Damoc, B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., … Sifre, L. (2022). *Training Compute-Optimal Large Language Models* (arXiv:2203.15556). arXiv. <https://doi.org/10.48550/arXiv.2203.15556>

Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J. (2021). *Measuring Massive Multitask Language Understanding* (arXiv:2009.03300). arXiv. <https://doi.org/10.48550/arXiv.2009.03300>
