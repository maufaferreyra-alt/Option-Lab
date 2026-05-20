"""
Options Lab AR — Landing.

Streamlit auto-genera el sidebar con las páginas en /pages.
"""
from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="Options Lab AR", page_icon="📊", layout="wide")

st.title("📊 Options Lab AR")
st.markdown(
    """
Laboratorio personal de opciones, construido en Python + Streamlit.

### Partes de la app

📚 **Educación** *(disponible)* — Recorrido interactivo basado en Hull, "Options, Futures and Other Derivatives".
Cubre Cap 1, 9, 10, 11 y 18: payoffs, propiedades, put-call parity, estrategias multi-leg, las griegas
y cómo se comportan. Hecho para preparar parcial.

🎲 **Monte Carlo** *(disponible)* — Hull Cap 13. Procesos de Wiener, movimiento Browniano geométrico,
visualización de paths y pricing por simulación con convergencia explícita a Black-Scholes.

🇦🇷 **Mercado AR** *(próximamente)* — Chains reales de BYMA, IV surface, scanner de oportunidades.
Subyacentes líquidos: GGAL, YPF, BMA, PAMP, ALUA, TECO2, BBAR, CRES, METR, COME, EDN, TXAR.

🧠 **AI Scanner** *(próximamente)* — Análisis automatizado de chains AR con LLM
para detectar skew anómalo, calendar spreads atractivos y warnings de liquidez.

---

### Pricing engine

- **Black-Scholes-Merton** analítico con greeks closed-form
- **Binomial** Cox-Ross-Rubinstein y Leisen-Reimer (americanas + europeas)
- **Implied vol** vía Brent's method

Verificación numérica anclada en Hull Ejemplo 14.6:
S=42, K=40, T=0.5, r=0.10, σ=0.20 → Call=4.7594, Put=0.8086.

👈 Abrí **Education** en el sidebar para arrancar.
"""
)

st.divider()
st.caption(
    "Hecho con Python · Streamlit · Plotly · NumPy · SciPy. "
    "Referencia: Hull, J.C. *Options, Futures and Other Derivatives*. "
    "Pricing engine validado contra Ejemplo 14.6."
)
