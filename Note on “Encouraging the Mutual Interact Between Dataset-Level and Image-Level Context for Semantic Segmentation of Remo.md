# Note on “Encouraging the Mutual Interact Between Dataset-Level and Image-Level Context for Semantic Segmentation of Remote Sensing Image“

“Abstract— Recently, semantic segmentation of remote sensing images has witnessed rapid advancement with the adoption of deep neural networks. Contextual cues, referring to the long-range correlation between pixels, are crucial for achieving accurate segmentation results, particularly for objects with less discriminative characteristics in these images. Currently, most studies are centered on incorporating contextual cues by aggregating context information at the dataset level or image level. However, current research often treats contextual cue modeling at the dataset-level and image level as independent procedures, neglecting the intrinsic correlation between these two feature levels. Consequently, the obtained contextual cues are suboptimal. This issue is particularly critical in the semantic segmentation of remote sensing images. To address this, we propose to encourage mutual interaction between dataset-level and image-level contextual cues. Firstly, we propose an interactive dataset–image context aggregation scheme to obtain complementary and consistent multilevel contextual cues. Additionally, we introduce a parallel feature interaction network (PFI-Net) that progressively extracts and fuses features across multiple layers, enabling effective integration of multilevel contexts. Furthermore, we introduce an enhanced shifted window-based cross-attention mechanism to augment model efficiency. Extensive experimental results on the widely used Vaihingen dataset, GaoFen-2 dataset, and instance segmentation in aerial images dataset (iSAID) effectively demonstrate the superiority of our proposed method over the other state-of-the-art methods.”

## Introduction

“Contextual cues typically refer to the long-range correlation between pixels \[20], \[21]. For example, <u>in remote sensing scenes, a boat can often be mistaken for a car due to the similar appearance of objects.</u>”

“However, when considering the contextual cue, such as a scene being described as a “boathouse” near a river, a more accurate prediction can be yielded.”

## Related Work

### Image-level context\[22]

“Deeplab \[23], \[24], \[25], OCRNet \[21], Segmenter \[26], and ISNet \[27]”

## Method

![\<img alt="" data-attachment-key="S2F8HP47" width="2076" height="875" src="  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/S2F8HP47.png" ztype="zimage">](  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/S2F8HP47.png)

![\<img alt="" data-attachment-key="8QYY9ALV" width="2106" height="843" src="  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/8QYY9ALV.png" ztype="zimage">](  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/8QYY9ALV.png)

![\<img alt="" data-attachment-key="UH6REU95" width="2080" height="913" src="  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/UH6REU95.png" ztype="zimage">](  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/UH6REU95.png)

![\<img alt="" data-attachment-key="MP9RA4CF" width="2076" height="1006" src="  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/MP9RA4CF.png" ztype="zimage">](  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/MP9RA4CF.png)

![\<img alt="" data-attachment-key="CNFPAU5J" width="2096" height="1619" src="  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/CNFPAU5J.png" ztype="zimage">](  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/CNFPAU5J.png)

## Results

![\<img alt="" data-attachment-key="T5WQK5VS" width="2120" height="778" src="  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/T5WQK5VS.png" ztype="zimage">](  ./attachments/Encouraging%20the%20Mutual%20Interact%20Between%20Dataset-Level%20and%20Image-Level%20Context%20for%20Semantic%20Segmentation%20of%20Remote%20Sensing%20Image/T5WQK5VS.png)

## References

\[21] Y. Yuan, X. Chen, and J. Wang, “Object-contextual representations for semantic segmentation,” in Computer Vision—ECCV. Glasgow, U.K.: Springer, 2020, pp. 173–190.

\[22] Z. Jin, D. Yu, Z. Yuan, and L. Yu, “MCIBI++: Soft mining contextual information beyond image for semantic segmentation,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 5, pp. 5988–6005, May 2023.

\[23] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille, “DeepLab: Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 40, no. 4, pp. 834–848, Apr. 2018.

\[24] L.-C. Chen, G. Papandreou, F. Schroff, and H. Adam, “Rethinking atrous convolution for semantic image segmentation,” 2017, arXiv:1706.05587.

\[25] L.-C. Chen, Y. Zhu, G. Papandreou, F. Schroff, and H. Adam, “Encoder–decoder with atrous separable convolution for semantic image segmentation,” in Proc. Eur. Conf. Comput. Vis. (ECCV), 2018, pp. 801–818.

\[26] R. Strudel, R. Garcia, I. Laptev, and C. Schmid, “Segmenter: Transformer for semantic segmentation,” in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 7242–7252.

\[27] Z. Jin, B. Liu, Q. Chu, and N. Yu, “ISNet: Integrate image-level and semantic-level context for semantic segmentation,” in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 7169–7178.
