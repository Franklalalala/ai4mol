我已经把汇总好的论文与简介整理成一份可下载的 PDF（包含以 abTEM 为核心、与 AI、DFT/基于 DFT 的势能计算以及与实验紧密结合的代表性工作）。
**下载链接（PDF）**：sandbox:/mnt/data/abtem\_papers\_collection.pdf

下面是该汇编中**若干关键结论与主要参考来源**（我在生成 PDF 时检索并核对了下列文献/页面；如果你要把 PDF 里的某篇文章作为论文引用，请优先用原文链接或 DOI）：

* abTEM 本体与设计、DFT（GPAW）集成与示例：Madsen & Susi (2021). ([PMC][1])
* ab-initio 电势 / 将 DFT 电荷密度用于 TEM 模拟的方法（abTEM 的理论基础之一）：Susi et al. (2018/2019). ([arXiv][2], [PubMed][3])
* abTEM 在解释实验中电荷/键合信号的实例（2D MoS₂）：Martis et al. (2023). ([Nature][4])
* 使用 abTEM 模拟 4D-STEM / ptychography 并校准/验证实验重构（复杂/灵敏样品）：Pelz et al. / Peng et al. (2022/2023)。([PMC][5], [Nature][6])
* 以 abTEM 生成大规模合成数据供深度学习训练并转移到实验：Leitherer et al. (npj Computational Materials, 2023)；Boebinger et al. (npj Computational Materials, 2024) 演示了 ML ↔ 实验 闭环的用例。([Nature][7])
* 低剂量 4D-STEM / ptychography 的模拟与实验设计（abTEM 在参数选择与重构可靠性验证中常被使用）：Li et al. (ACS Cent. Sci. 2022)。([美国化学学会出版物][8])
* ML 辅助的 exit-wave / 相位重建与去噪方法，通常以 abTEM 模拟数据作为训练/验证基准（Nielsen / Larsen 等）。([Welcome to DTU Research Database][9])
* AtomAI（把深度学习、仪器接口、第一性原理/模拟工具串接起来的框架）是这一生态系统的代表性工具，常与 abTEM 类模拟配合用于训练/解释。([arXiv][10], [PNNL][11])
* 用于加速多切片/PRISM 模拟、以便把仿真纳入接近实时或大量数据生成流程的工作（对 ML 驱动的实验十分重要）：Robinson et al. (2023)；PRISM 方法参考 Ophus (2017)。([PubMed][12], [arXiv][13])
* 4D-STEM/深度学习的去噪与相位重建等方法，结合 abTEM 合成数据的示范（Sadri 2024, Friedrich 2023 等）。([Nature][14], [Oxford Academic][15])

---

# 关于 PDF 的说明（内容与组织）

* PDF 名称：**abtem\_papers\_collection.pdf**（见上下载链接）
* 内容摘要：每篇论文的题目、作者、发表刊物/年份、链接/DOI（当时可查到者），并附 1 段或多段**摘要 + 重点说明 abTEM 在该工作中如何被使用**（例如：作为合成训练数据、用于 DFT-derived potential 的 multislice / PRISM 仿真、用于设计低剂量实验参数、用于验证/标定重构算法、或在闭环 ML-driven 实验中作为物理前向模型）。
* 收录策略：侧重 **abTEM 的直接引用 / 明确使用** 的工作（并额外列出一些与 abTEM 生态高度相关、且属于 AI + DFT + 实验结合范畴的代表性方法论论文与工具）。我优先收录了在方法学或实验/ML-in-loop 场景中明确将 abTEM 用作仿真基础的论文。

---

# 我在 PDF 中收录的（主要）论文列表（示例 — PDF 内为每篇条目均有更长的简介）

1. Madsen & Susi — *The abTEM code…* (2021). ([PMC][1])
2. T. Susi et al. — *Efficient first principles simulation of electron scattering factors…* (2018/2019). ([arXiv][2])
3. Martis et al. — *Imaging the electron charge density in monolayer MoS₂…* (2023). ([Nature][4])
4. Pelz / Peng et al. — ptychographic atomic electron tomography & MOL growth studies (2022–2023)。([PMC][5], [Nature][6])
5. Leitherer et al. — *Automatic identification of crystal structures and interfaces…* (npj Comput. Mater., 2023)。([Nature][7])
6. Boebinger et al. — *Exploring electron-beam induced modifications…* (npj Comput. Mater., 2024)。([Nature][16])
7. Li et al. — *4D-STEM ptychography for electron-beam-sensitive materials* (ACS Cent. Sci., 2022)。([美国化学学会出版物][8])
8. Peng / Pelz et al. — *Observation of formation and local structures of metal-organic layers* (Nat Commun, 2022)。([Nature][6])
9. Schwartz et al. — *Imaging atomic-scale chemistry from fused multi-modal electron microscopy* (npj Comput. Mater., 2022)。([Nature][17])
10. Robinson et al. — *Towards real-time STEM simulations…* (2023)。([PubMed][12])
11. Machine-learning exit-wave works (DTU / Nielsen / Larsen 等，2022–2023)。([Welcome to DTU Research Database][9])
12. AtomAI (Ziatdinov et al., Nat. Mach. Intell., 2022) — 框架/生态示例。([arXiv][10])
13. Sadri et al. — *Unsupervised deep denoising for 4D-STEM* (npj Comput. Mater., 2024)。([Nature][14])
14. Friedrich et al. — *Phase object reconstruction for 4D-STEM using deep learning* (2023)。([Oxford Academic][15])
15. Ophus — PRISM algorithm（加速大尺度仿真，常与 abTEM 结合）。([arXiv][13])
16. Li et al. — 2025 MOF low-dose ptychography（示例：abTEM 在 4D-STEM 实验设计中的直接使用）。([Nature][18])

（PDF 中给出的每篇简介更长，且将这些文章按“AI + abTEM”、“DFT/ab-initio 潜势 → abTEM”、“实验设计与低剂量成像”、“仿真加速/高吞吐合成数据” 等主题分组，便于快速检索与对照。）

---

# 如果你想我继续做的事（可选，任选其一）

* 把 PDF 再扩展，加入**每篇论文的摘录式关键图表/方法段落**（需要我下载/截图论文 PDF 并摘录 — 我可以把可公开访问的文本摘录到文档中）。
* 把 PDF 按“用途”生成索引（例如：用于 ML 训练 / 用于低剂量实验设计 / 用于 DFT-to-abTEM 电势管线 / 用于实时实验闭环）。
* 将某些论文的*方法节*或*Supplementary*里关于仿真参数（加速电压、探针角度、frozen-phonon 层数、PRISM factor 等）抽出来生成对比表（便于实验人员直接借鉴）。
* 你如果有特定材料 / 技术（例如 zeolite、MOF、2D materials、ptychography、4D-STEM、exit-wave 重建、或某种 ML 任务），我可以在 PDF 的基础上**定制一页快速实施清单**（需要哪些 abTEM 参数、哪些 DFT/GPAW 设置、合成数据的 noise model、以及可复用的 notebook/代码链接）。

直接告诉我你选哪项（或者都要），我就把你需要的内容加入到同一个 PDF 或另存为一个新的文件并立刻给你下载。

---

如果你现在要下载：再次点击（或复制到浏览器）`sandbox:/mnt/data/abtem_papers_collection.pdf` 即可（PDF 已生成）。
需要我把 PDF 转成中文排版版或加入中文注释也可以 — 你更倾向哪种格式？

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10446032/?utm_source=chatgpt.com "The abTEM code: transmission electron microscopy from ..."
[2]: https://arxiv.org/abs/1803.05338?utm_source=chatgpt.com "Efficient first principles simulation of electron scattering factors for transmission electron microscopy"
[3]: https://pubmed.ncbi.nlm.nih.gov/30468946/?utm_source=chatgpt.com "Efficient first principles simulation of electron scattering ..."
[4]: https://www.nature.com/articles/s41467-023-39304-9?utm_source=chatgpt.com "Imaging the electron charge density in monolayer MoS2 at ..."
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10689721/ "
            Solving complex nanostructures with ptychographic atomic electron tomography - PMC
        "
[6]: https://www.nature.com/articles/s41467-022-32330-z?utm_source=chatgpt.com "Observation of formation and local structures of metal ..."
[7]: https://www.nature.com/articles/s41524-023-01133-1 "Automatic identification of crystal structures and interfaces via artificial-intelligence-based electron microscopy | npj Computational Materials"
[8]: https://pubs.acs.org/doi/10.1021/acscentsci.2c01137?utm_source=chatgpt.com "4D-STEM Ptychography for Electron-Beam-Sensitive Materials"
[9]: https://orbit.dtu.dk/en/publications/machine-learning-assisted-exit-wave-reconstruction-for-quantitati?utm_source=chatgpt.com "Machine-Learning Assisted Exit-wave Reconstruction for ..."
[10]: https://arxiv.org/abs/2105.07485?utm_source=chatgpt.com "AtomAI: A Deep Learning Framework for Analysis of Image and Spectroscopy Data in (Scanning) Transmission Electron Microscopy and Beyond"
[11]: https://www.pnnl.gov/people/maxim-ziatdinov?utm_source=chatgpt.com "Maxim Ziatdinov"
[12]: https://pubmed.ncbi.nlm.nih.gov/36800515/?utm_source=chatgpt.com "Towards real-time STEM simulations through targeted ..."
[13]: https://arxiv.org/abs/1702.01904?utm_source=chatgpt.com "A Fast Image Simulation Algorithm for Scanning Transmission Electron Microscopy"
[14]: https://www.nature.com/articles/s41524-024-01428-x "Unsupervised deep denoising for four-dimensional scanning transmission electron microscopy | npj Computational Materials"
[15]: https://academic.oup.com/mam/article/29/1/395/6985579?utm_source=chatgpt.com "Phase Object Reconstruction for 4D-STEM using Deep Learning"
[16]: https://www.nature.com/articles/s41524-024-01448-7 "Exploring electron-beam induced modifications of materials with machine-learning assisted high temporal resolution electron microscopy | npj Computational Materials"
[17]: https://www.nature.com/articles/s41524-021-00692-5?utm_source=chatgpt.com "Imaging atomic-scale chemistry from fused multi-modal ..."
[18]: https://www.nature.com/articles/s41467-025-56215-z?utm_source=chatgpt.com "Atomically resolved imaging of radiation-sensitive metal ..."