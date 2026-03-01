# AQML Strategy Examples

This directory contains reference strategies demonstrating various AQML patterns.

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

## Strategies Not Converted

The following strategies from the reference repositories were **not converted** because they fall outside AQML v1.0 scope:

| Strategy | Repo | Reason |
|----------|------|--------|
| Pair Trading | quant-trading | Requires co-integration / spread modeling (multi-asset) |
| Options Straddle | quant-trading | Options derivatives, not equity screening |
| VIX Calculator | quant-trading | Volatility index calculation tool, not a strategy |
| Monte Carlo | quant-trading | Simulation / research project |
| Oil Money | quant-trading | Macro commodity-FX research project |
| London Breakout | quant-trading | Intraday forex-specific, time-zone dependent |
| RSRS | QuantsPlaybook | Custom regression slope, not a standard indicator |
| HHT Model | QuantsPlaybook | Hilbert-Huang Transform + ML classifier |
| Wavelet Analysis | QuantsPlaybook | Signal processing (wavelet decomposition) |
| Trader-Company | QuantsPlaybook | Meta-heuristic ensemble algorithm |
| MLT TSMOM | QuantsPlaybook | Deep multi-task learning model |
| Most factor strategies | QuantsPlaybook | Custom factor construction requiring raw tick/order data |

## Validating Examples

```bash
# Python
pip install jsonschema pyyaml
python -c "
import json, yaml, jsonschema, glob
schema = json.load(open('spec/schema.json'))
for f in glob.glob('examples/*.aqml'):
    strategy = yaml.safe_load(open(f))
    jsonschema.validate(strategy, schema)
    print(f'✓ {f}')
"
```

## Contributing

We welcome strategy examples! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines, or use the [Strategy Example issue template](https://github.com/yupoet/aqml/issues/new?template=strategy_example.md).
