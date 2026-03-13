# AQML Strategy Examples

This directory contains reference strategies demonstrating the current AQML v2 executable profile.

If you want a copy-and-edit starting point rather than a reference specimen, use the template gallery in [`../templates/gallery/`](../templates/gallery/) instead.

All files in this directory are synced to:

- [`../spec/aqml-v2.0.md`](../spec/aqml-v2.0.md)
- [`../spec/schema.json`](../spec/schema.json)
- the current AurumQ parser and evaluator semantics

## Original Examples

| File | Category | Complexity | Description |
|------|----------|------------|-------------|
| [`simple-rsi.aqml`](simple-rsi.aqml) | Momentum | ⭐ Beginner | Single-rule RSI oversold screen |
| [`momentum-breakout.aqml`](momentum-breakout.aqml) | Momentum | ⭐⭐ Intermediate | RSI + MACD + volume confirmation |
| [`mean-reversion.aqml`](mean-reversion.aqml) | Mean Reversion | ⭐⭐ Intermediate | Bollinger Band bounce + fundamentals |
| [`multi-factor-value.aqml`](multi-factor-value.aqml) | Value | ⭐⭐⭐ Advanced | PE/PB/ROE multi-factor with MA trend |
| [`dual-thrust.aqml`](dual-thrust.aqml) | Breakout | ⭐⭐ Intermediate | Classic Dual Thrust range breakout |
| [`kdj-golden-cross.aqml`](kdj-golden-cross.aqml) | Signal | ⭐ Beginner | KDJ golden cross with volume filter |

## Converted from [je-suis-tm/quant-trading](https://github.com/je-suis-tm/quant-trading) (Apache 2.0)

| File | Category | Complexity | Description |
|------|----------|------------|-------------|
| [`awesome-oscillator.aqml`](awesome-oscillator.aqml) | Momentum | ⭐⭐ Intermediate | Awesome Oscillator MA crossover + volume |
| [`bollinger-w-bottom.aqml`](bollinger-w-bottom.aqml) | Mean Reversion | ⭐⭐ Intermediate | Bollinger Bands W-bottom pattern recognition |
| [`heikin-ashi-momentum.aqml`](heikin-ashi-momentum.aqml) | Momentum | ⭐⭐ Intermediate | Heikin-Ashi filtered reversal with engulfing pattern |
| [`macd-crossover.aqml`](macd-crossover.aqml) | Momentum | ⭐ Beginner | Classic MACD golden cross + histogram |
| [`parabolic-sar-trend.aqml`](parabolic-sar-trend.aqml) | Momentum | ⭐⭐ Intermediate | Parabolic SAR trend following with DMI/ADX |
| [`rsi-overbought-oversold.aqml`](rsi-overbought-oversold.aqml) | Mean Reversion | ⭐⭐ Intermediate | RSI 30/70 reversal + fundamental filters |
| [`shooting-star-reversal.aqml`](shooting-star-reversal.aqml) | Mean Reversion | ⭐⭐ Intermediate | Shooting star bearish reversal pattern |

## Converted from [hugo2046/QuantsPlaybook](https://github.com/hugo2046/QuantsPlaybook)

| File | Category | Complexity | Description |
|------|----------|------------|-------------|
| [`ma-channel-breakout.aqml`](ma-channel-breakout.aqml) | Breakout | ⭐⭐ Intermediate | MA crossover + Bollinger channel breakout (申万宏源) |
| [`alligator-timing.aqml`](alligator-timing.aqml) | Momentum | ⭐⭐ Intermediate | Williams Alligator line MA alignment (招商证券) |
| [`ffscore-value.aqml`](ffscore-value.aqml) | Value | ⭐⭐⭐ Advanced | FFScore Piotroski fundamental selection (华泰证券) |
| [`volume-price-resonance.aqml`](volume-price-resonance.aqml) | Momentum | ⭐⭐ Intermediate | Volume-price resonance timing (华创证券) |
| [`icu-ma-timing.aqml`](icu-ma-timing.aqml) | Momentum | ⭐⭐ Intermediate | ICU moving average absolute return timing (中泰证券) |

## ⚠️ Approximation Conversions from [hugo2046/QuantsPlaybook](https://github.com/hugo2046/QuantsPlaybook)

These strategies use **simplified standard-indicator proxies** for models that originally require custom computations (regression, factor decomposition, tick data, macro data). Each file is clearly marked with `metadata.approximation: true` and bilingual approximation notes.

### Factor Strategies (B-因子构建类)

| File | Original Model | Proxy Indicators | Source |
|------|---------------|-------------------|--------|
| [`momentum-factor-ranking.aqml`](momentum-factor-ranking.aqml) | ⚠️ FF3 Momentum Factor | Multi-MA alignment + volume | 华泰证券 |
| [`low-volatility-screen.aqml`](low-volatility-screen.aqml) | ⚠️ Idiosyncratic Volatility | Bollinger squeeze + quality | 华泰证券 |
| [`short-term-reversal.aqml`](short-term-reversal.aqml) | ⚠️ W-Cut Microstructure | RSI6 oversold + Bollinger lower | 开源证券 |
| [`smart-money-flow.aqml`](smart-money-flow.aqml) | ⚠️ Smart Money VWAP 2.0 | MFI + volume surge + OBV | 开源证券 |
| [`chip-concentration.aqml`](chip-concentration.aqml) | ⚠️ Chip Distribution Factor | Bollinger squeeze + low volume | 广发证券 |
| [`turnover-activity.aqml`](turnover-activity.aqml) | ⚠️ Amplitude Hidden Structure | Volume anomaly + CCI + ATR | 东吴证券 |

### Timing Strategies (C-择时类)

| File | Original Model | Proxy Indicators | Source |
|------|---------------|-------------------|--------|
| [`rsrs-support-resistance.aqml`](rsrs-support-resistance.aqml) | ⚠️ RSRS Regression Slope | SAR + DMI + ADX | 光大证券 |
| [`qrs-regime-signal.aqml`](qrs-regime-signal.aqml) | ⚠️ QRS β*R² Signal | EMA crossover + ADX | 中金公司 |
| [`low-latency-trend.aqml`](low-latency-trend.aqml) | ⚠️ LLT/FRAMA/HMA Filters | EMA5/20 crossover + MACD | 国泰君安 |
| [`bull-bear-regime.aqml`](bull-bear-regime.aqml) | ⚠️ CSVC σ/τ Bull-Bear | MA alignment + ADX + volume | 天风证券 |
| [`volatility-regime-timing.aqml`](volatility-regime-timing.aqml) | ⚠️ FF3 Idiosyncratic Vol | Bollinger squeeze + DMI | 国信证券 |
| [`northbound-flow-proxy.aqml`](northbound-flow-proxy.aqml) | ⚠️ Northbound Capital Flow | MFI + volume + EMA trend | 华泰证券 |
| [`time-varying-sharpe.aqml`](time-varying-sharpe.aqml) | ⚠️ Whitelaw Time-Varying Sharpe | RSI range + MA60 + PE | 开源证券 |
| [`herding-effect-proxy.aqml`](herding-effect-proxy.aqml) | ⚠️ CCK Herding (CSAD) | Volume spike + RSI oversold | 开源证券 |

## Strategies Not Converted

The following strategies from the reference repositories were **not converted** because they still fall outside the AQML v2 executable profile even with approximation:

| Strategy | Repo | Reason |
|----------|------|--------|
| Pair Trading | quant-trading | Requires co-integration / spread modeling (multi-asset) |
| Options Straddle | quant-trading | Options derivatives, not equity screening |
| VIX Calculator | quant-trading | Volatility index calculation tool, not a strategy |
| Monte Carlo | quant-trading | Simulation / research project |
| Oil Money | quant-trading | Macro commodity-FX research project |
| London Breakout | quant-trading | Intraday forex-specific, time-zone dependent |
| HHT Model | QuantsPlaybook | Hilbert-Huang Transform + ML classifier |
| Wavelet Analysis | QuantsPlaybook | Signal processing (wavelet decomposition) |
| Trader-Company | QuantsPlaybook | Meta-heuristic ensemble algorithm |
| MLT TSMOM | QuantsPlaybook | Deep multi-task learning model |

## Validating Examples

```bash
# JSON Schema validation
python -c "
import glob, json, yaml, jsonschema
schema = json.load(open('spec/schema.json'))
for f in glob.glob('examples/*.aqml'):
    strategy = yaml.safe_load(open(f))
    jsonschema.validate(strategy, schema)
    print(f'✓ schema {f}')
"
```

```bash
# AurumQ executable-profile validation
.venv/bin/python - <<'PY'
import glob
from pathlib import Path
from aurumq.strategies.service import StrategyService

for f in sorted(glob.glob('examples/*.aqml')):
    StrategyService.validate_aqml(Path(f).read_text(encoding='utf-8'))
    print(f'✓ aurumq {f}')
PY
```

## Contributing

We welcome strategy examples! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines, or use the [Strategy Example issue template](https://github.com/yupoet/aqml/issues/new?template=strategy_example.md).
