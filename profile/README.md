<div align="center">

<img src="https://raw.githubusercontent.com/chetra-quant/.github/main/profile/logo.png" width="120" height="120" alt="chetra-quant"/>

# chetra-quant

**Autonomous quantitative trading research — built to falsify its own ideas before it trusts them.**

<br/>

![Focus](https://img.shields.io/badge/focus-XAUUSD%20%C2%B7%20FX%20%C2%B7%20indices-22D3EE?style=flat-square&labelColor=0A0E17)
![Engine](https://img.shields.io/badge/engine-vectorbt%20%C2%B7%20MT5%20%C2%B7%20MongoDB-34D399?style=flat-square&labelColor=0A0E17)
![Discipline](https://img.shields.io/badge/gate-deflated%20Sharpe%20%C2%B7%20holdout--once-F8FAFC?style=flat-square&labelColor=0A0E17)
![Stage](https://img.shields.io/badge/promotion-paper%20before%20live-22D3EE?style=flat-square&labelColor=0A0E17)

</div>

<br/>

## The factory

A self-improving strategy pipeline where **search is deliberately expensive and evidence is deliberately scarce** — the only way to hunt for edge autonomously without overfitting into fiction.

```mermaid
flowchart LR
    A[Signal] --> B[Backtest]
    B --> C[Causality gate]
    C --> D[Sel-block selection]
    D --> E[Pre-register]
    E --> F["Holdout<br/>(opened once, ever)"]
    F --> G["Spread stress<br/>(1.5x)"]
    G --> H[Correlation gate]
    H --> I["MT5 real-spread replay"]
    I --> J[Paper book]
    J --> K{Human review}
    K -->|approved| L["Live<br/>(human-gated)"]
    K -->|rejected| M["Dead end<br/>(recorded, never re-walked)"]

    Z["Adversary<br/>(label-shuffle, look-ahead probe, spread-double)"]
    Z -. tries to kill .-> C
    Z -. tries to kill .-> F
    Z -. tries to kill .-> I

    classDef live fill:#34D399,stroke:#0A0E17,color:#0A0E17,font-weight:bold;
    classDef dead stroke:#94A3B8,stroke-width:2px,stroke-dasharray: 4 3;
    classDef adversary stroke:#22D3EE,stroke-width:2px,stroke-dasharray: 3 2;
    class L live;
    class M dead;
    class Z adversary;
```

Every gate is a place to say **no**. A hypothesis gets exactly one look at the sealed holdout — enforced at the data layer, not by convention — and the multiple-testing bar rises with every trial the factory has ever run. A separate adversary tries to *kill* each survivor before it reaches the paper book. Live money stays behind a human hand, always.

## Repositories

| Repo | What it is |
|------|-----------|
| **trading-agent** | The factory — gate chain, paper engine, cockpit, self-learning loop |
| **bot-portal** | Customer portal — subscriptions, licensing, crypto pay |
| **claude-brain** | Long-term knowledge: sessions, decisions, dead-ends that stay dead |
| **LLM-trading** · **poly_bot** · **autonomous_bot** | Research tracks & experiments |
| **chetra-trading-dashboard** · **Trading-Journal** · **trading-bot-copy** | Tooling & archive |

## Principles

- **The gate that says _no_ is built before the gate that says _yes_.**
- A dead end is a permanent record — the system never re-walks a road it already proved was a wall.
- No strategy touches real money without an explicit human decision.
- Retail-broker reality is a hard bound: no order book, no tape, no options chain. Edge comes from new *mechanisms*, never more parameter search.

<div align="center">
<br/>
<sub>Research infrastructure · not investment advice.</sub>
</div>
