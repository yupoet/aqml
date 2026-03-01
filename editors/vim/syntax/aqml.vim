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
syn keyword aqmlSection aqml name description version metadata universe rules scoring exit_rules portfolio risk
hi def link aqmlSection Keyword

" ── Rule Types ─────────────────────────────────────────────
syn keyword aqmlRuleType compare range signal pattern breakout
hi def link aqmlRuleType Type

" ── Indicators ─────────────────────────────────────────────
syn keyword aqmlIndicator ma5 ma10 ma20 ma60 ma120 ma250
syn keyword aqmlIndicator ema5 ema10 ema20 ema60
syn keyword aqmlIndicator macd macd_dif macd_dea macd_hist
syn keyword aqmlIndicator rsi6 rsi14
syn keyword aqmlIndicator kdj_k kdj_d kdj_j
syn keyword aqmlIndicator boll_upper boll_mid boll_lower
syn keyword aqmlIndicator atr14 cci14 obv dmi_plus dmi_minus dmi_adx
syn keyword aqmlIndicator sar supertrend mfi14 wr14
syn keyword aqmlIndicator volume_ma5 volume_ma10 volume_ma20
syn keyword aqmlIndicator close open high low volume pe_ttm pb roe total_mv
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
syn keyword aqmlEnum weighted equal threshold
syn keyword aqmlEnum equal_weight score_weighted market_cap_weighted kelly risk_parity
syn keyword aqmlEnum daily weekly biweekly monthly
syn keyword aqmlEnum above below
hi def link aqmlEnum PreProc

" ── Universe Labels ────────────────────────────────────────
syn keyword aqmlUniverse ST STAR BSE ChiNext new_listing
hi def link aqmlUniverse Special

let b:current_syntax = "aqml"
