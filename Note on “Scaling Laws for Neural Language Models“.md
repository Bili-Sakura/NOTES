# Note on “Scaling Laws for Neural Language Models“

Abstract: We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sampleefficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

## Summary of Power Laws

For easier reference, we provide a summary below of the key trends described throughout the paper.

![\<img alt="" data-attachment-key="2GBAQTDK" width="1531" height="609" src="../attachments/Scaling_Laws _or_Neural_Language_Models/2GBAQTDK.png" ztype="zimage">](./attachments/Scaling_Laws_for_Neural_Language_Models/2GBAQTDK.png)

The empirical fitted values for these trends are:

![\<img alt="" data-attachment-key="V9TQJ9C8" width="1631" height="573" src="../attachments/Scaling_Laws _or_Neural_Language_Models/V9TQJ9C8.png" ztype="zimage">](./attachments/Scaling_Laws_for_Neural_Language_Models/V9TQJ9C8.png)

The optimal parameters for compute efficient training are given by:

![\<img alt="" data-attachment-key="RY35DWBI" width="1641" height="439" src="../attachments/Scaling_Laws _or_Neural_Language_Models/RY35DWBI.png" ztype="zimage">](./attachments/Scaling_Laws_for_Neural_Language_Models/RY35DWBI.png)
