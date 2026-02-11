---
layout: default
title: 董其实 | Qishi Dong
permalink: /
---

<style>
/* ===== Minimal, clean, publication-style homepage ===== */
:root{
  --fg:#0f172a; --muted:#475569; --bg:#ffffff; --card:#f8fafc; --bd:#e2e8f0;
  --link:#2563eb; --tag:#eef2ff;
}
body{ background:var(--bg); }
a{ color:var(--link); text-decoration:none; }
a:hover{ text-decoration:underline; }
hr{ border:none; border-top:1px solid var(--bd); margin:1.5rem 0; }

.hero{
  display:grid; grid-template-columns: 1.2fr .8fr; gap:1.2rem;
  padding:1.2rem; border:1px solid var(--bd); border-radius:16px; background:var(--card);
}
@media (max-width: 900px){ .hero{ grid-template-columns: 1fr; } }
.h1{ font-size:2.0rem; margin:.1rem 0 .2rem 0; color:var(--fg); }
.subtitle{ margin:.1rem 0; color:var(--muted); font-size:1.05rem; }
.meta{ margin:.6rem 0 0 0; color:var(--muted); }
.btns{ display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.8rem; }
.btn{
  display:inline-block; padding:.45rem .7rem; border:1px solid var(--bd);
  border-radius:999px; background:#fff; color:var(--fg); font-size:.95rem;
}
.tags{ display:flex; flex-wrap:wrap; gap:.45rem; margin-top:.8rem; }
.tag{
  display:inline-block; padding:.25rem .55rem; border-radius:999px;
  background:var(--tag); color:#1e3a8a; border:1px solid #c7d2fe; font-size:.85rem;
}
.avatar{
  width:140px; height:140px; border-radius:18px; object-fit:cover;
  border:1px solid var(--bd); background:#fff;
}
.small{ font-size:.92rem; color:var(--muted); }
.section-title{ margin:1.4rem 0 .6rem 0; font-size:1.35rem; color:var(--fg); }
.kv{ display:grid; grid-template-columns: 110px 1fr; gap:.45rem .8rem; }
.k{ color:var(--muted); }
.v{ color:var(--fg); }
.note{ padding:.75rem 1rem; border-left:4px solid #c7d2fe; background:#f5f7ff; border-radius:10px; }
</style>

<div class="hero">
  <div>
    <div class="h1">董其实 <span class="small">Qishi Dong</span></div>
    <div class="subtitle">深圳技术大学 · 大数据与互联网学院 · 助理教授</div>
    <div class="meta">统计学习 / 生物统计 / 空间组学 / 医疗健康数据建模</div>

    <div class="btns">
      <a class="btn" href="mailto:dongqishi@sztu.edu.cn">Email</a>
      <a class="btn" href="https://github.com/SpatialOmics-pj/dongqishi">GitHub</a>
    </div>

    <div class="tags">
      <span class="tag">Spatial transcriptomics</span>
      <span class="tag">Bayesian / Variational inference</span>
      <span class="tag">Deep probabilistic models</span>
      <span class="tag">Fine-mapping</span>
      <span class="tag">Wearable sensing</span>
    </div>

    <div class="note" style="margin-top:1rem">
      欢迎对 <b>统计建模、生物统计、空间组学</b> 以及 <b>医疗器械/可穿戴算法落地</b> 感兴趣的同学联系我：
      <a href="mailto:dongqishi@sztu.edu.cn">dongqishi@sztu.edu.cn</a>。
    </div>
  </div>

  <div>
    <!-- Upload your photo to: assets/img/avatar.jpg -->
    <img class="avatar" src="/assets/img/avatar.jpg" alt="Qishi Dong" onerror="this.style.display='none'"/>
    <div class="kv" style="margin-top:.9rem">
      <div class="k">地址</div><div class="v">深圳，中国</div>
      <div class="k">研究主题</div><div class="v">空间组学整合、细胞类型解卷积与域识别、可信推断、无创生理信号建模</div>
      <div class="k">合作</div><div class="v">欢迎学术与产业合作（算法研发、数据分析、产品落地）</div>
    </div>
  </div>
</div>

## About

我于 2023 年获香港浸会大学统计学博士学位，现为深圳技术大学大数据与互联网学院助理教授。研究聚焦统计学习、生物统计与医疗健康数据分析，曾在华为诺亚方舟实验室、香港中文大学（深圳）与香港大学从事科研工作。

---

## Research

- **空间组学（Spatial omics）**：多切片/多平台空间转录组整合、细胞类型解卷积、空间域识别与对齐  
- **统计推断（Bayesian & VI）**：变分推断、可校准不确定性、可解释表征学习  
- **遗传统计（Statistical genetics）**：Empirical Bayes 变量选择与遗传 fine-mapping  
- **可穿戴与医疗器械算法**：PPG/ECG 等生理信号建模、个体校准与鲁棒推理  

---

## Publications

> 说明：把论文 PDF 放到仓库里（推荐路径见下），下面的 `[PDF]` 链接会直接生效。

### 2026

1. **FUSION**: Dong, Q.†, Huang, Z.†, Wang, X., Feng, Z., Liu, W., & Huang, B.*  
   *Efficient Latent-Topic Modeling Unifies Cell-Type Deconvolution and Domain Discovery for Multi-Section Spatial Transcriptomics.*  
   Manuscript, 2026. [[PDF](/assets/papers/FUSION.pdf)]

2. Dong, Q.*, Wang, X.*, Guan, X., Liang, L., Ke, X., & Peng, H.  
   *An Empirical Bayes Algorithm for Variable Selection With Applications in Genetic Fine-Mapping.*  
   (In press / 2026). [[PDF](/assets/papers/EmpBVS_clean.pdf)]

### 2025

1. Dong, Q.*, Yang, Y.*, Luo, Z., Shen, H., Shi, X., & Liu, J.*  
   *Robust Spatial Cell-Type Deconvolution with Qualitative Reference for Spatial Transcriptomics.*  
   **Small Methods** 9(5), 2401145 (2025).

### 2023

1. Dong, Q., Zhou, F., Kang, N., Xie, C., Zhang, S., Li, J., Peng, H., & Li, Z.*  
   *DAMix: Exploiting Deep Autoregressive Model Zoo for Improving Lossless Compression Generalization.*  
   **AAAI** (2023).

### 2022

1. Dong, Q., Muhammad, A., Zhou, F., Xie, C., Hu, T., Yang, Y., Bae, S.-H., & Li, Z.*  
   *ZooD: Exploiting Model Zoo for Out-of-Distribution Generalization.*  
   **NeurIPS** (2022).

---

## Patents

- **发明专利申请（已受理）**：申请号 **202511359756.X**，发明创造名称：  
  “一种联合解卷积域识别与对齐的方法、系统、终端及介质”（发文日：2025-09-23）。  
  [[受理通知书 PDF](/assets/patents/202511359756X-专利申请受理通知书.pdf)]

---

## Industry Collaboration

- **森沛科技（深圳）有限公司 × 深圳技术大学**：智能穿戴端 PPG 信号的可校准预测算法优化（2026.02–2026.12）。  
  （可提供数据分析、算法复现/评估、鲁棒性提升与工程化建议。）

---

## Contact

- Email: [dongqishi@sztu.edu.cn](mailto:dongqishi@sztu.edu.cn)
- GitHub: https://github.com/SpatialOmics-pj/dongqishi
