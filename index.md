<style>
:root{
  --fg:#0f172a; --muted:#475569; --card:#f8fafc; --bd:#e2e8f0;
  --tag:#eef2ff; --tagbd:#c7d2fe; --tagfg:#1e3a8a;
}

/* Make headings consistent with the page style (override Cayman green) */
h1,h2,h3{ color:var(--fg) !important; font-weight:800; }
h2{ margin-top:1.6rem; }
p{ color:var(--fg); }
hr{ border:none; border-top:1px solid var(--bd); margin:1.5rem 0; }

/* ===== HERO GRID (stable) ===== */
.hero{
  display:grid;
  grid-template-columns: 180px minmax(0, 1.15fr) minmax(0, .85fr);
  gap:16px;
  padding:18px;
  border:1px solid var(--bd);
  border-radius:18px;
  background:var(--card);
  align-items:stretch;
}
.hero > *{ min-width:0; }
.leftcol{ display:flex; flex-direction:column; gap:10px; align-items:flex-start; }
.mid, .right{ min-width:0; }
.right{ align-self:start; }
.right, .right *{ overflow-wrap:anywhere; word-break:break-word; }

/* Responsive */
@media (max-width: 1100px){
  .hero{ grid-template-columns: 180px 1fr; }
  .hero .right{ grid-column: 1 / -1; }
}
@media (max-width: 720px){
  .hero{ grid-template-columns: 1fr; }
}

/* Avatar */
.avatar{
  width:160px; height:160px; border-radius:18px; object-fit:cover;
  border:1px solid var(--bd); background:#fff;
}
.small{ font-size:.92rem; color:var(--muted); }

/* Name block */
.h1{
  font-size:2.05rem;
  font-weight:900;
  margin:2px 0 4px;
  color:var(--fg);
  letter-spacing:.2px;
}
.subtitle{ color:var(--muted); font-size:1.05rem; margin:0 0 6px; }
.meta{ color:var(--muted); margin:6px 0 0; line-height:1.55; }

/* Buttons */
.btns{ display:flex; flex-wrap:wrap; gap:10px; margin-top:12px; }
.btn{
  display:inline-block;
  padding:8px 14px;
  border:1px solid var(--bd);
  border-radius:999px;
  background:#fff;
  color:var(--fg);
  font-size:.95rem;
  font-weight:700;
}
.btn:hover{ text-decoration:none; border-color:#cbd5e1; }

/* Tags */
.tags{ display:flex; flex-wrap:wrap; gap:8px; margin-top:12px; }
.tag{
  display:inline-block;
  padding:6px 10px;
  border-radius:999px;
  background:var(--tag);
  color:var(--tagfg);
  border:1px solid var(--tagbd);
  font-size:.86rem;
  font-weight:650;
}

/* Note */
.note{
  margin-top:14px;
  padding:12px 14px;
  border-left:4px solid var(--tagbd);
  background:#f5f7ff;
  border-radius:12px;
  color:#334155;
  line-height:1.6;
}
.note a{ font-weight:800; }

/* Right panel (icon + content, clean) */
.sidepanel{
  background:#fff;
  border:1px solid var(--bd);
  border-radius:16px;
  padding:10px 12px;
}
.srow{
  display:flex;
  gap:10px;
  padding:10px 6px;
}
.srow + .srow{ border-top:1px solid var(--bd); }
.srow .ico{
  width:26px;
  flex:0 0 26px;
  margin-top:2px;
}
.stext{
  min-width:0;
  color:var(--fg);
  line-height:1.55;
}
.ssub{ color:var(--muted); font-size:.92rem; margin-top:4px; }
.sactions{ margin-top:10px; display:flex; flex-wrap:wrap; gap:8px; }
.mini-btn{
  display:inline-block;
  padding:6px 10px;
  border-radius:999px;
  border:1px solid var(--bd);
  background:#fff;
  color:var(--fg);
  font-size:.9rem;
  font-weight:750;
}
.mini-btn:hover{ text-decoration:none; border-color:#cbd5e1; }

/* Publication cards */
.pubgroup{ margin-top:10px; }
.pubitem{
  display:flex;
  gap:14px;
  padding:14px;
  border:1px solid var(--bd);
  border-radius:16px;
  background:#fff;
  margin:12px 0;
}
@media (max-width: 820px){ .pubitem{ flex-direction:column; } }
.pubimg img{
  width:160px; height:120px; object-fit:cover;
  border:1px solid var(--bd); border-radius:12px; background:#fff;
}
.pubtitle{ font-weight:900; margin:0 0 4px; color:var(--fg); }
.puba{ color:var(--muted); font-size:.94rem; margin:0 0 3px; }
.pubv{ color:#334155; font-size:.95rem; margin:0 0 8px; }
.publinks{ margin-top:8px; font-size:.95rem; }
.publinks a{ margin-right:12px; font-weight:750; }

/* Section lead text */
.sectionlead{ color:var(--muted); margin-top:-4px; line-height:1.7; }
</style>

<!-- ===================== HERO ===================== -->
<div class="hero">

  <!-- Left: photo + ORCID -->
  <div class="leftcol">
    <img class="avatar" src="assets/img/avatar.jpg" alt="Qishi Dong" onerror="this.style.display='none'">
    <div class="small">
      ORCID:
      <a href="https://orcid.org/0009-0005-6994-598X" target="_blank" rel="noopener">0009-0005-6994-598X</a>
    </div>
  </div>

  <!-- Middle: identity -->
  <div class="mid">
    <div class="h1">董其实 <span class="small">| Qishi Dong</span></div>
    <div class="subtitle">深圳技术大学 · 大数据与互联网学院 · 助理教授</div>
    <div class="meta">Statistical learning · Biostatistics · Spatial omics · Deep Learning</div>

    <div class="btns">
      <a class="btn" href="mailto:dongqishi@sztu.edu.cn">Email</a>
      <a class="btn" href="https://scholar.google.com/" target="_blank" rel="noopener">Scholar</a>
      <a class="btn" href="https://github.com/SpatialOmics-pj/dongqishi" target="_blank" rel="noopener">GitHub</a>
      <a class="btn" href="/assets/files/CV.pdf">CV</a>
    </div>

    <div class="tags">
      <span class="tag">Spatial transcriptomics</span>
      <span class="tag">Bayesian inference</span>
      <span class="tag">Variational inference</span>
      <span class="tag">Deep probabilistic models</span>
      <span class="tag">Fine-mapping</span>
    </div>

    <div class="note">
      欢迎对 <b>统计建模、生物统计、空间组学</b> 与 <b>医疗器械/可穿戴算法落地</b> 感兴趣的同学与合作伙伴联系：
      <a href="mailto:dongqishi@sztu.edu.cn">dongqishi@sztu.edu.cn</a>
    </div>
  </div>

  <!-- Right: clean panel -->
  <div class="right">
    <div class="sidepanel">
      <div class="srow">
        <span class="ico">📍</span>
        <div class="stext">
          中国 · 深圳
          <div class="ssub">Shenzhen, China</div>
        </div>
      </div>

      <div class="srow">
        <span class="ico">🔬</span>
        <div class="stext">
          空间组学跨切片整合 · 细胞类型解卷积与空间域识别 · 可校准可信推断 · 无创生理信号（PPG/ECG）建模与个体化校准
        </div>
      </div>

      <div class="srow">
        <span class="ico">🤝</span>
        <div class="stext">
          欢迎学术与产业合作（算法研发、数据分析、产品落地）
          <div class="sactions">
            <a class="mini-btn" href="mailto:dongqishi@sztu.edu.cn?subject=Collaboration%20Inquiry">合作邮件</a>
            <a class="mini-btn" href="https://orcid.org/0009-0005-6994-598X" target="_blank" rel="noopener">ORCID</a>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>


<h2 id="about">About</h2>
<p class="sectionlead">
我于 2023 年获香港浸会大学统计学博士学位，现为深圳技术大学大数据与互联网学院助理教授。
研究聚焦统计学习、生物统计与医疗健康数据分析，曾在华为诺亚方舟实验室、香港中文大学（深圳）与香港大学从事科研工作。
</p>

<hr/>

<h2 id="research">Research</h2>
<ul>
  <li><b>空间组学（Spatial omics）</b>：多切片/多平台空间转录组整合、细胞类型解卷积、空间域识别与对齐</li>
  <li><b>统计推断（Bayesian & VI）</b>：变分推断、可校准不确定性、可解释表征学习</li>
  <li><b>遗传统计（Statistical genetics）</b>：Empirical Bayes 变量选择与遗传 fine-mapping</li>
  <li><b>可穿戴与医疗器械算法</b>：PPG/ECG 等生理信号建模、个体校准与鲁棒推理</li>
</ul>

<hr/>

<h2 id="publications">Publications</h2>


<div class="pubgroup">
  <h3>2026</h3>

  <div class="pubitem">
    <div class="pubimg">
      <img src="/assets/img/pubs/fusion.png" alt="FUSION" onerror="this.style.display='none'">
    </div>
    <div>
      <div class="pubtitle">Efficient Latent-Topic Modeling Unifies Cell-Type Deconvolution and Domain Discovery for Multi-Section Spatial Transcriptomics</div>
      <div class="puba">Dong, Q.†; Huang, Z.†; Wang, X.; Feng, Z.; Liu, W.; Huang, B.*</div>
      <div class="pubv"><b>Manuscript</b>, 2026</div>
      <div class="publinks">
        <a href="/assets/papers/FUSION.pdf">PDF</a>
      </div>
    </div>
  </div>

  <div class="pubitem">
    <div class="pubimg">
      <img src="/assets/img/pubs/empbvs.png" alt="EmpBVS" onerror="this.style.display='none'">
    </div>
    <div>
      <div class="pubtitle">An Empirical Bayes Algorithm for Variable Selection With Applications in Genetic Fine-Mapping</div>
      <div class="puba">Dong, Q.*; Wang, X.*; Guan, X.; Liang, L.; Ke, X.#; Peng, H.</div>
      <div class="pubv"><b>Stat</b>, 2026</div>
      <div class="publinks">
        <a href="/assets/papers/EmpBVS_clean.pdf">PDF</a>
      </div>
    </div>
  </div>

  <h3>2025</h3>

  <div class="pubitem">
    <div class="pubimg">
      <img src="/assets/img/pubs/qrside.png" alt="QR-SIDE" onerror="this.style.display='none'">
    </div>
    <div>
      <div class="pubtitle">Robust Spatial Cell-Type Deconvolution with Qualitative Reference for Spatial Transcriptomics</div>
      <div class="puba">Dong, Q.*; Yang, Y.*; Luo, Z.; Shen, H.; Shi, X.#; Liu, J.#</div>
      <div class="pubv"><b>Small Methods</b> 9(5), 2401145, 2025</div>
      <div class="publinks">
        <a href="#">Paper</a>
      </div>
    </div>
  </div>

  <h3>2023</h3>

  <div class="pubitem">
    <div class="pubimg">
      <img src="/assets/img/pubs/damix.png" alt="DAMix" onerror="this.style.display='none'">
    </div>
    <div>
      <div class="pubtitle">DAMix: Exploiting Deep Autoregressive Model Zoo for Improving Lossless Compression Generalization</div>
      <div class="puba">Dong, Q.; Zhou, F.; Kang, N.; Xie, C.; Zhang, S.; Li, J.; Peng, H.; Li, Z.*</div>
      <div class="pubv"><b>AAAI</b>, 2023</div>
      <div class="publinks">
        <a href="#">Paper</a>
      </div>
    </div>
  </div>

  <h3>2022</h3>

  <div class="pubitem">
    <div class="pubimg">
      <img src="/assets/img/pubs/zood.png" alt="ZooD" onerror="this.style.display='none'">
    </div>
    <div>
      <div class="pubtitle">ZooD: Exploiting Model Zoo for Out-of-Distribution Generalization</div>
      <div class="puba">Dong, Q.; Muhammad, A.; Zhou, F.; Xie, C.; Hu, T.; Yang, Y.; Bae, S.-H.; Li, Z.*</div>
      <div class="pubv"><b>NeurIPS</b>, 2022</div>
      <div class="publinks">
        <a href="#">Paper</a>
      </div>
    </div>
  </div>
</div>

<hr/>

<h2 id="patents">Patents</h2>
<ul>
  <li><b>发明专利申请（已受理）</b>：申请号 <b>202511359756.X</b>，
      “一种联合解卷积域识别与对齐的方法、系统、终端及介质”（发文日：2025-09-23）。
  </li>
</ul>

<hr/>

<h2 id="industry">Industry Collaboration</h2>
<ul>
  <li><b>森沛科技（深圳）有限公司 × 深圳技术大学</b>：智能穿戴端 PPG 信号的可校准预测算法优化（2026.02–2026.12）。</li>
</ul>

<hr/>

<h2 id="contact">Contact</h2>
<ul>
  <li>Email: <a href="mailto:dongqishi@sztu.edu.cn">dongqishi@sztu.edu.cn</a></li>
  <li>ORCID: <a href="https://orcid.org/0009-0005-6994-598X" target="_blank" rel="noopener">0009-0005-6994-598X</a></li>
  <li>GitHub: <a href="https://github.com/SpatialOmics-pj/dongqishi" target="_blank" rel="noopener">SpatialOmics-pj/dongqishi</a></li>
</ul>


