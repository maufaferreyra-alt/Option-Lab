"""CSS premium para Options Lab — Inter + JetBrains Mono + gold accent."""
from __future__ import annotations
import streamlit as st

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #0e1117;
    --surface: #161b22;
    --border: #30363d;
    --text: #e6edf3;
    --text-muted: #8b949e;
    --accent: #d4af37;
    --positive: #3fb950;
    --negative: #f85149;
    --info: #58a6ff;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Números mono en metric values */
[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 28px !important;
    color: var(--text) !important;
}
[data-testid="stMetricLabel"] {
    font-size: 11px !important;
    color: var(--text-muted) !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
[data-testid="stMetricDelta"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
}

/* Cards */
.premium-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 14px 16px;
    margin-bottom: 8px;
    transition: border-color 0.15s ease;
}
.premium-card:hover { border-color: var(--accent); }

/* Header strip ticker */
.ticker-cell {
    display: inline-block;
    padding: 8px 14px;
    border-right: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
}
.ticker-cell:last-child { border-right: none; }
.ticker-cell .symbol { color: var(--text-muted); font-size: 11px; letter-spacing: 0.5px; }
.ticker-cell .price { color: var(--text); font-size: 16px; font-weight: 600; margin-left: 8px; }
.ticker-cell .delta.pos { color: var(--positive); margin-left: 6px; font-size: 12px; }
.ticker-cell .delta.neg { color: var(--negative); margin-left: 6px; font-size: 12px; }

/* Tab styling */
.stTabs [data-baseweb="tab-list"] { gap: 0; border-bottom: 1px solid var(--border); }
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border: none;
    padding: 10px 18px;
    font-size: 13px;
    color: var(--text-muted);
}
.stTabs [aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--surface);
    border-right: 1px solid var(--border);
}

/* Code/mono helpers */
code, .mono {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Hide hamburger en producción */
#MainMenu, footer { visibility: hidden; }
</style>
"""


def inject_premium_css() -> None:
    """Inyecta el CSS custom. Llamar al tope de cada page después de set_page_config."""
    st.markdown(_CSS, unsafe_allow_html=True)
