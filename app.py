"""Options Lab — landing / market dashboard."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from ui.styling import inject_premium_css
from ui.components.header_strip import render_header_strip
from data.tickers import UNIVERSE

st.set_page_config(
    page_title="Options Lab",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
inject_premium_css()
render_header_strip()

# Hero
st.markdown(
    '<div style="display:flex;justify-content:space-between;align-items:baseline;">'
    '<h1 style="margin:0;font-weight:600;letter-spacing:-0.5px;">Options Lab</h1>'
    '<span style="color:var(--text-muted);font-size:13px;">'
    'Hull-driven · real-time chains · personal use</span>'
    '</div>',
    unsafe_allow_html=True,
)
st.markdown('<hr style="border-color:var(--border);margin:12px 0 24px;">', unsafe_allow_html=True)

# Quick stats
c1, c2, c3, c4 = st.columns(4)
c1.metric("Universo de tickers", len(UNIVERSE))
c2.metric("Modelos de pricing", "4", help="BS · Binomial CRR · Leisen-Reimer · Monte Carlo")
c3.metric("Greeks closed-form", "5", help="Δ Γ ν Θ ρ")
c4.metric("Estrategias", "11", help="Spreads, straddles, butterflies, condors, collars")

# Categorías
st.markdown("### Universo cubierto")
by_cat: dict[str, list] = {}
for t in UNIVERSE:
    by_cat.setdefault(t.category, []).append(t)

cols = st.columns(len(by_cat))
for col, (cat, tickers) in zip(cols, by_cat.items()):
    with col:
        sample = ", ".join(t.symbol for t in tickers[:5])
        suffix = " ..." if len(tickers) > 5 else ""
        st.markdown(
            f'<div class="premium-card">'
            f'<div style="color:var(--text-muted);font-size:11px;text-transform:uppercase;letter-spacing:0.5px;">{cat}</div>'
            f'<div style="font-family:JetBrains Mono;color:var(--accent);font-size:18px;font-weight:600;margin-top:4px;">'
            f'{len(tickers)} tickers</div>'
            f'<div style="font-family:JetBrains Mono;color:var(--text-muted);font-size:11px;margin-top:6px;">'
            f'{sample}{suffix}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

st.markdown("### Navegación")
nav1, nav2, nav3 = st.columns(3)
nav1.markdown(
    '<div class="premium-card">'
    '<div style="font-weight:600;font-size:16px;">📚 Education</div>'
    '<div style="color:var(--text-muted);font-size:13px;margin-top:4px;">'
    'Hull Cap 1, 9, 10, 11, 18 — parcial prep con widgets interactivos.</div></div>',
    unsafe_allow_html=True,
)
nav2.markdown(
    '<div class="premium-card">'
    '<div style="font-weight:600;font-size:16px;">📈 Market Lab</div>'
    '<div style="color:var(--text-muted);font-size:13px;margin-top:4px;">'
    'Chain real de yfinance · greeks calculadas con engine · strategy builder sobre quotes reales.'
    '</div></div>',
    unsafe_allow_html=True,
)
nav3.markdown(
    '<div class="premium-card">'
    '<div style="font-weight:600;font-size:16px;">🎲 Monte Carlo</div>'
    '<div style="color:var(--text-muted);font-size:13px;margin-top:4px;">'
    'Hull Cap 13 — Wiener processes, paths GBM, pricing por simulación.</div></div>',
    unsafe_allow_html=True,
)

st.caption("Data: yfinance (delay ~15 min). Cache: prices 60s · chains 5min · rate 1h.")
