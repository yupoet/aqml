" Vim syntax file for AQML (Aurum Quant Markup Language)
" Place in: ~/.vim/syntax/aqml.vim  (Vim)
"       or: ~/.config/nvim/syntax/aqml.vim  (Neovim)
"
" AQML inherits YAML syntax and adds domain-specific highlights.

if exists("b:current_syntax")
  finish
endif

" Load YAML as base
runtime! syntax/yaml.vim
unlet! b:current_syntax

" ── AQML Sections ──────────────────────────────────────────
syn keyword aqmlSection name description version signal_type filters metadata universe rules scoring exit_rules portfolio risk
hi def link aqmlSection Keyword

" ── Rule Types ─────────────────────────────────────────────
syn keyword aqmlRuleType compare compare_all range signal pattern breakout and or not
hi def link aqmlRuleType Type

" ── Indicators ─────────────────────────────────────────────
syn keyword aqmlIndicator ma5 ma10 ma20 ma30 ma60 ma90 ma120 ma125 ma250 ma375 ma500
syn keyword aqmlIndicator ema5 ema10 ema20 ema30 ema60
syn keyword aqmlIndicator macd macd_dif macd_dea macd_signal macd_hist
syn keyword aqmlIndicator rsi6 rsi12 rsi14 rsi24
syn keyword aqmlIndicator kdj_k kdj_d kdj_j
syn keyword aqmlIndicator boll_upper boll_mid boll_middle boll_lower
syn keyword aqmlIndicator atr atr14 atr_percent cci cci14 obv obv_change dmi_plus dmi_minus dmi_pdi dmi_mdi dmi_adx
syn keyword aqmlIndicator sar supertrend supertrend_direction mfi mfi14 wr wr14
syn keyword aqmlIndicator vol_ma5 vol_ma10 vol_ma20 volume_ma5 volume_ma10 volume_ma20 volume_ratio volume_amplify
syn keyword aqmlIndicator close open high low volume amount pe_ttm pe pb ps roe eps total_mv market_cap turnover turnover_rate fi_roe np_yoy revenue_growth
hi def link aqmlIndicator Identifier

" ── Signals ────────────────────────────────────────────────
syn keyword aqmlSignal golden_cross death_cross zero_cross_up zero_cross_down
syn keyword aqmlSignal overbought oversold long_arrangement short_arrangement
syn keyword aqmlSignal squeeze expansion upper_touch lower_touch
hi def link aqmlSignal Constant

" ── Patterns ───────────────────────────────────────────────
syn keyword aqmlPattern hammer engulfing_bull engulfing_bear doji
syn keyword aqmlPattern morning_star evening_star three_white_soldiers three_black_crows
hi def link aqmlPattern Constant

" ── Enums ──────────────────────────────────────────────────
syn keyword aqmlEnum equal_weight score_weighted
syn keyword aqmlEnum daily weekly biweekly monthly
syn keyword aqmlEnum buy sell up down
hi def link aqmlEnum PreProc

" ── Universe Labels ────────────────────────────────────────
syn keyword aqmlUniverse ST STAR BSE ChiNext new_listing
hi def link aqmlUniverse Special

let b:current_syntax = "aqml"
