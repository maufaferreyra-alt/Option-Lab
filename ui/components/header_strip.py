"""Strip horizontal de tickers live al tope de cada page."""
from __future__ import annotations
import streamlit as st

from data.market_provider import get_quotes_batch
from data.tickers import HEADER_STRIP_TICKERS

LABELS = {
    "SPY": "S&P 500",
    "QQQ": "NASDAQ 100",
    "IWM": "RUSSELL 2000",
    "^VIX": "VIX",
    "^TNX": "US 10Y",
    "GLD": "GOLD",
    "BTC-USD": "BTC",
}


def render_header_strip() -> None:
    """Renderea el strip con quotes en vivo. Falla suave: si un quote es None, muestra '—'."""
    quotes = get_quotes_batch(tuple(HEADER_STRIP_TICKERS))
    cells = []
    for sym in HEADER_STRIP_TICKERS:
        q = quotes.get(sym)
        label = LABELS.get(sym, sym)
        if q is None:
            cells.append(
                f'<span class="ticker-cell">'
                f'<span class="symbol">{label}</span>'
                f'<span class="price" style="color:var(--text-muted)">—</span>'
                f'</span>'
            )
            continue
        arrow = "▲" if q.is_up else "▼"
        cls = "pos" if q.is_up else "neg"
        cells.append(
            f'<span class="ticker-cell">'
            f'<span class="symbol">{label}</span>'
            f'<span class="price">{q.price:,.2f}</span>'
            f'<span class="delta {cls}">{arrow} {q.change_pct:+.2f}%</span>'
            f'</span>'
        )
    html = (
        '<div style="background: var(--surface); border: 1px solid var(--border); '
        'border-radius: 6px; padding: 2px 0; margin-bottom: 16px; overflow-x: auto; '
        'white-space: nowrap;">'
        + "".join(cells) + "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)
