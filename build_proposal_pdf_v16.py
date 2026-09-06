import os
from playwright.sync_api import sync_playwright

S = "/tmp/claude-0/-home-user/2ca1d236-9107-50cb-86bc-b6464e28a04f/scratchpad"

with open(f"{S}/seal_b64.txt") as f:
    seal = f.read().strip()
with open(f"{S}/chrome_b64.txt") as f:
    chrome = f.read().strip()

seal_uri   = f"data:image/png;base64,{seal}"
chrome_uri = f"data:image/png;base64,{chrome}"

def fmt(n, plus=False):
    if n == 0: return "₪0"
    if n < 0: return f"-₪{abs(int(n)):,}"
    if plus and n > 0: return f"+₪{int(n):,}"
    return f"₪{int(n):,}"

# ── קבועים ────────────────────────────────────────────────────────────────────
AOV           = 380
EXT_MONTHLY   = 715     # Shopify ×3
FIXED_OPS     = 1200    # הוצאות הפעלה קבועות
RS_PCT        = 0.08    # 8% RS מהכנסות ברוטו
GM_90         = 0.90    # מרווח גולמי Intermax (בקירוב)
EFFECTIVE_MARGIN = GM_90 - RS_PCT  # 0.82 — מרווח אחרי RS

RETAINER_PER_CHANNEL = 10000
CHANNEL_DISCOUNT_PCT = 20
CHANNEL_DISCOUNTED   = int(RETAINER_PER_CHANNEL * (1 - CHANNEL_DISCOUNT_PCT / 100))  # 8000

# מחירי קריאטיב מוסכמים
STATIC_PRICE = 130    # ₪115-150 טווח מוסכם עם הלקוח
VIDEO_PRICE  = 1760   # ₪1,760 — עשוי לעלות עם מורכבות הפקה (נספג על-ידי LGG)

mgmt_fees = {
    0:20000,
    1:8000,2:8000,3:8000,4:8000,5:8000,6:8000,
    7:16000,8:16000,
    9:24000,10:24000,11:24000,12:24000,
}

# ── נתוני מדיה והכנסות (v16 — שמרני → אגרסיבי → מינוף מהיר יותר) ─────────
# (שלב, מדיה, ROAS, תקציב_כולל, הזמנות_חדשות, חוזרות, הכנסות_חוזרות, הכנסה_כוללת, RS, _)
B = {
    0: ("הקמה",   0,     None, 20000,   0,   0,    0,      0,     0,  0),
    1: ("למידה", 11220,  1.0,  20000,  30,   0,    0,  11220,   898,  0),
    2: ("השקה",   9460,  1.5,  20000,  35,   2,  760,  14190,  1135,  0),
    3: ("צמיחה",  9200,  2.0,  20000,  44,   4, 1520,  18400,  1472,  0),
    4: ("מינוף", 11440,  2.5,  24000,  60,  15, 5700,  28600,  2288,  0),
    5: ("שיא",   14180,  2.8,  27000,  80,  24, 9120,  39704,  3176,  0),
    6: ("מיטוב", 19180,  3.2,  32000, 120,  42,15960,  61376,  4910,  0),
}
B_ext = {
    7:  ("גוגל",   24740, 3.3, 47580, 160,  57, 21660,  81642,  6531, 0),
    8:  ("גוגל+",  28000, 3.1, 50840, 170,  58, 22040,  86800,  6944, 0),
    9:  ("TikTok", 35000, 3.2, 67600, 220,  75, 28500, 112000,  8960, 0),
    10: ("TikTok+",40000, 3.0, 72600, 240,  76, 28880, 120000,  9600, 0),
    11: ("Scale",  45000, 3.3, 79620, 300,  91, 34580, 148500, 11880, 0),
    12: ("Max",    50000, 3.5, 84620, 360, 101, 38380, 175000, 14000, 0),
}

# תרחיש שמרני
C = {
    0: ("הקמה",  0,    None, 20000,   0,  0,    0,     0,    0, 0),
    1: ("למידה", 8000, 0.8,  20000,  21,  0,    0,  6400,  512, 0),
    2: ("השקה",  8000, 1.2,  20000,  26,  1,  380,  9980,  798, 0),
    3: ("צמיחה", 8000, 1.6,  20000,  34,  3, 1140, 14100, 1128, 0),
    4: ("מינוף", 9000, 2.0,  24000,  47, 10, 3800, 21660, 1733, 0),
    5: ("שיא",  10000, 2.3,  27000,  58, 16, 6080, 28080, 2246, 0),
    6: ("מיטוב",12000, 2.7,  32000,  81, 28,10640, 41420, 3314, 0),
}

# תרחיש אגרסיבי
A = {
    0: ("הקמה",   0,    None, 20000,   0,  0,    0,     0,    0, 0),
    1: ("למידה", 14000, 1.3,  20000,  37,  0,    0, 18200, 1456, 0),
    2: ("השקה",  12000, 2.0,  20000,  48,  3, 1140, 25140, 2011, 0),
    3: ("צמיחה", 11000, 2.8,  20000,  61,  8, 3040, 34280, 2742, 0),
    4: ("מינוף", 14000, 3.2,  24000,  90, 22, 8360, 50820, 4066, 0),
    5: ("שיא",   18000, 3.5,  27000, 126, 36,13680, 81720, 6538, 0),
    6: ("מיטוב", 24000, 4.0,  32000, 192, 63,23940,126960,10157, 0),
}

# ── תכנית קריאטיב (v16 — מחיר מוסכם: ₪130 סטטי | ₪1,760 וידאו) ────────────
creative_plan = {
    # (סטטי, וידאו, עלות_כוללת) — פחות וידאו בחודשים הראשונים לשמירת תקציב
    1:  ( 6, 0,   780),   # 6×130
    2:  ( 6, 1,  2540),   # 6×130 + 1×1760
    3:  ( 8, 1,  2800),   # 8×130 + 1×1760
    4:  ( 8, 2,  4560),   # 8×130 + 2×1760
    5:  (10, 2,  4820),   # 10×130 + 2×1760
    6:  (10, 2,  4820),
    7:  (12, 3,  6840),   # 12×130 + 3×1760
    8:  (12, 3,  6840),
    9:  (12, 4,  8600),   # 12×130 + 4×1760
    10: (12, 4,  8600),
    11: (14, 5, 10620),   # 14×130 + 5×1760
    12: (14, 5, 10620),
}

CPM_M = {1:65,2:65,3:55,4:55,5:50,6:50,7:48,8:48,9:52,10:50,11:48,12:45}
CTR_M = {1:.020,2:.025,3:.025,4:.030,5:.030,6:.030,7:.030,8:.030,9:.028,10:.030,11:.032,12:.035}

# ── חישוב חודשי (v16 — הלקוח מחשב רווח נקי לפי מרווח הגולמי שלו ~90%) ──────
def compute_month(m):
    if m == 0:
        ti = 20000 + EXT_MONTHLY
        be_t = round((ti + FIXED_OPS) / EFFECTIVE_MARGIN)
        return {'phase':'הקמה','ad_spend':0,'cpm':None,'reach':0,'ctr':None,'visitors':0,
                'cvr':None,'nc':0,'rc':0,'total_orders':0,'ad_rev':0,'rrev':0,'total_rev':0,
                'roas':None,'lgg_fee':20000,'media':0,'creative':0,'ext':EXT_MONTHLY,
                'total_invest':ti,'rs':0,'be_threshold':be_t,'profitable':False}
    d = B[m] if m <= 6 else B_ext[m]
    ph,ads,roas,_,nc,rc,rrev,rev,rs,_ = d
    cr = creative_plan[m][2] if m in creative_plan else 0
    cpm = CPM_M.get(m); ctr = CTR_M.get(m)
    reach = round(ads/cpm*1000) if cpm and ads>0 else 0
    visitors = round(reach*ctr) if ctr and reach>0 else 0
    cvr = round(nc/visitors*100,1) if visitors>0 else 0
    tot_ord = nc+rc
    lgg = mgmt_fees[m]
    total_invest = lgg + ads + cr + EXT_MONTHLY
    # נקודת איזון ב-90% מרווח גולמי: הכנסה × 0.82 ≥ total_invest + FIXED_OPS
    be_t = round((total_invest + FIXED_OPS) / EFFECTIVE_MARGIN)
    profitable = (rev * EFFECTIVE_MARGIN) >= (total_invest + FIXED_OPS)
    return {'phase':ph,'ad_spend':ads,'cpm':cpm,'reach':reach,'ctr':ctr,
            'visitors':visitors,'cvr':cvr,'nc':nc,'rc':rc,'total_orders':tot_ord,
            'ad_rev':nc*AOV,'rrev':rrev,'total_rev':rev,'roas':roas,
            'lgg_fee':lgg,'media':ads,'creative':cr,'ext':EXT_MONTHLY,
            'total_invest':round(total_invest),'rs':rs,
            'be_threshold':be_t,'profitable':profitable}

MD = {m: compute_month(m) for m in range(13)}
first_profitable = next((m for m in range(1, 13) if MD[m]['profitable']), None)


# ── טבלת תרחישים M1-M6 (v16 — ללא עמודת נטו, עם בדיקת נקודת איזון 90%) ────
def scenario_rows():
    labels = {1:"M1",2:"M2",3:"M3",4:"M4",5:"M5",6:"M6"}
    rows = ""
    for m in range(1,7):
        lgg = mgmt_fees[m]
        ads = B[m][1]
        cr  = creative_plan[m][2]
        base_costs = lgg + ads + cr + EXT_MONTHLY + FIXED_OPS
        be_t = round(base_costs / EFFECTIVE_MARGIN)

        _,_,_,_,cnc,crc,_,crev,crs,_ = C[m]
        _,_,_,_,bnc,brc,_,brev,brs,_ = B[m]
        _,_,_,_,anc,arc,_,arev,ars,_ = A[m]

        c_above = crev >= be_t
        b_above = brev >= be_t
        a_above = arev >= be_t

        check = lambda ok: ('<span style="color:#1a7a4a;font-weight:900">✓</span>'
                            if ok else '<span style="color:#c41414;font-weight:900">✗</span>')

        hl = ' style="background:#f0eaf9"' if (b_above and m>=4) else (' style="background:#e8f5ee"' if b_above else "")
        rows += f'<tr{hl}>'
        rows += f'<td>{labels[m]}</td>'
        rows += f'<td style="color:#7a5a10;font-weight:700">{fmt(be_t)}</td>'
        rows += f'<td style="background:#f0f0f0;width:2mm"></td>'
        rows += f'<td>{fmt(crev)}</td><td style="text-align:center;font-size:11px">{check(c_above)}</td>'
        rows += f'<td style="background:#f0f0f0;width:2mm"></td>'
        rows += f'<td>{fmt(brev)}</td><td style="text-align:center;font-size:11px">{check(b_above)}</td>'
        rows += f'<td style="background:#f0f0f0;width:2mm"></td>'
        rows += f'<td>{fmt(arev)}</td><td style="text-align:center;font-size:11px">{check(a_above)}</td>'
        rows += f'</tr>'

    c_tot = sum(C[m][7] for m in range(1,7))
    b_tot = sum(B[m][7] for m in range(1,7))
    a_tot = sum(A[m][7] for m in range(1,7))
    rows += f'<tr style="background:#1a1a2e;color:#fff;font-weight:800">'
    rows += f'<td>H1 סה"כ</td><td style="color:#e8cc80">—</td>'
    rows += f'<td style="background:#333"></td>'
    rows += f'<td style="color:#aadcc0">{fmt(c_tot)}</td><td style="color:#555">—</td>'
    rows += f'<td style="background:#333"></td>'
    rows += f'<td style="color:#aadcc0">{fmt(b_tot)}</td><td style="color:#555">—</td>'
    rows += f'<td style="background:#333"></td>'
    rows += f'<td style="color:#aadcc0">{fmt(a_tot)}</td><td style="color:#555">—</td>'
    rows += f'</tr>'
    return rows

sc_rows = scenario_rows()

# ── טבלת תחזית שנתית (v16 — ללא CM ו-נטו, עם עמודת נקודת איזון 90%) ────────
def drive_table_transposed():
    D = MD
    CAM=("#ede7f9","#5b1fa8"); CON=("#dce6f7","#1a3fa8"); REV=("#d8f0e5","#1a7a4a")
    EXP=("#fde8e8","#8b1a1a"); RS_=("#ede7f9","#5b1fa8"); BEQ=("#fdf3d8","#7a5a10")
    cols = [
        ("מדיה",CAM,lambda m:fmt(D[m]['ad_spend']) if D[m]['ad_spend']>0 else "—"),
        ("CPM",CAM,lambda m:f"₪{D[m]['cpm']}" if D[m]['cpm'] else "—"),
        ("חשיפות",CAM,lambda m:f"{D[m]['reach']//1000}K" if D[m]['reach']>0 else "—"),
        ("CTR",CAM,lambda m:f"{round(D[m]['ctr']*100,1)}%" if D[m]['ctr'] else "—"),
        ("מבקרים",CAM,lambda m:f"{round(D[m]['visitors']/1000,1)}K" if D[m]['visitors']>0 else "—"),
        ("CVR",CON,lambda m:f"{D[m]['cvr']}%" if D[m]['cvr'] else "—"),
        ("הז׳ חדשות",CON,lambda m:str(D[m]['nc']) if D[m]['nc']>0 else "—"),
        ("חוזרים",CON,lambda m:str(D[m]['rc']) if D[m]['rc']>0 else "—"),
        ("הזמ׳ כולל",CON,lambda m:str(D[m]['total_orders']) if D[m]['total_orders']>0 else "—"),
        ("הכנ׳ מד׳",REV,lambda m:fmt(D[m]['ad_rev']) if D[m]['ad_rev']>0 else "—"),
        ("הכנ׳ חז׳",REV,lambda m:fmt(D[m]['rrev']) if D[m]['rrev']>0 else "—"),
        ("הכנסה כוללת",REV,lambda m:fmt(D[m]['total_rev']) if D[m]['total_rev']>0 else "—"),
        ("ROAS",REV,lambda m:f"{D[m]['roas']}×" if D[m]['roas'] else "—"),
        ("LGG שכ׳׳ט",EXP,lambda m:fmt(D[m]['lgg_fee'])),
        ("קריאטיב",EXP,lambda m:fmt(D[m]['creative']) if D[m]['creative']>0 else "—"),
        ("הוצ׳ נוספות",EXP,lambda m:fmt(D[m]['ext'])),
        ("סה׳׳כ השקעה",EXP,lambda m:fmt(D[m]['total_invest'])),
        ("RS 8%",RS_,lambda m:fmt(D[m]['rs']) if D[m]['rs']>0 else "—"),
        ("נ.א. 90%",BEQ,lambda m:fmt(D[m]['be_threshold']) if m>0 else "—"),
    ]
    sec1 = '<th colspan="2" style="background:#1a1a2e;color:#fff;font-size:6px;padding:1mm 0.5mm;text-align:center">חודש / KPI</th>'
    for label,span,token in [("קמפיין",5,CAM),("המרה",4,CON),("הכנסות",4,REV),("הוצאות",4,EXP),("RS",1,RS_),("נ.א. 90%",1,BEQ)]:
        sec1 += f'<th colspan="{span}" style="background:{token[0]};color:{token[1]};font-size:6.5px;font-weight:800;text-align:center;padding:1mm">{label}</th>'
    sec2 = '<th style="background:#1a1a2e;color:#fff;font-size:6px;padding:0.8mm;width:9mm">חודש</th>'
    sec2 += '<th style="background:#1a1a2e;color:#fff;font-size:6px;padding:0.8mm;width:13mm">שלב</th>'
    for lbl,token,_ in cols:
        sec2 += f'<th style="background:{token[0]};color:{token[1]};font-size:5.5px;padding:0.7mm 0.4mm;text-align:center;white-space:nowrap;width:12mm">{lbl}</th>'
    rows_html = ""
    for m in range(13):
        profitable=D[m]['profitable']; invest=D[m]['total_invest']
        over_budget=invest>20000
        if m==0: rbg="background:#f5f5f5"
        elif profitable: rbg="background:#f0f7f2"
        elif m%2==0: rbg="background:#fafaf9"
        else: rbg=""
        m_color="#5b1fa8" if m==0 else ("#1a7a4a" if profitable else "#c41414")
        m_cell=f'<td style="font-size:7px;font-weight:900;color:{m_color};padding:0.9mm;text-align:center;border-right:2px solid #eee">M{m}</td>'
        phase_cell=f'<td style="font-size:6.5px;color:#555;padding:0.7mm 0.5mm;white-space:nowrap">{D[m]["phase"]}</td>'
        data_cells=""
        for lbl,token,fn in cols:
            v=fn(m)
            if lbl in("מדיה","LGG שכ׳׳ט","קריאטיב","הוצ׳ נוספות"): vc="color:#8b2222" if v!="—" else "color:#ccc"
            elif lbl=="סה׳׳כ השקעה":
                vc="color:#8b2222;font-weight:800" if v!="—" else "color:#ccc"
                if over_budget and m>0: vc="color:#c41414;font-weight:900"
            elif lbl in("הכנ׳ מד׳","הכנ׳ חז׳","הכנסה כוללת"): vc="color:#1a7a4a;font-weight:700" if v!="—" else "color:#ccc"
            elif lbl=="ROAS": vc="color:#7a5a10;font-weight:700" if v!="—" else "color:#ccc"
            elif lbl=="RS 8%": vc="color:#5b1fa8;font-weight:700" if v!="—" else "color:#ccc"
            elif lbl=="נ.א. 90%":
                if m==0: vc="color:#ccc"
                elif profitable: vc="color:#1a7a4a;font-weight:700"
                else: vc="color:#c49a2a;font-weight:700"
            else: vc="color:#444"
            data_cells += f'<td style="font-size:6.5px;{vc};padding:0.7mm 0.4mm;text-align:center;white-space:nowrap">{v}</td>'
        rows_html += f'<tr style="{rbg};border-bottom:1px solid #eee">{m_cell}{phase_cell}{data_cells}</tr>'

    tots={k:sum(D[m][k] for m in range(13)) for k in ['ad_spend','total_rev','lgg_fee','creative','ext','total_invest','rs']}
    ft=f'<td colspan="2" style="background:#1a1a2e;color:#fff;font-size:6.5px;font-weight:800;padding:1mm">סיכום M0-M12</td>'
    ft+=f'<td style="background:#1a1a2e;color:#e0d0f5;font-size:6px">{fmt(tots["ad_spend"])}</td>'
    ft+=f'<td colspan="4" style="background:#1a1a2e;color:#555;font-size:6px;text-align:center">—</td>'
    ft+=f'<td colspan="3" style="background:#1a1a2e;color:#555;font-size:6px;text-align:center">—</td>'
    ft+=f'<td colspan="2" style="background:#1a1a2e;color:#555">—</td>'
    ft+=f'<td style="background:#1a1a2e;color:#aadcc0;font-weight:800;font-size:6.5px">{fmt(tots["total_rev"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#555">—</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-size:6px">{fmt(tots["lgg_fee"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-size:6px">{fmt(tots["creative"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-size:6px">{fmt(tots["ext"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-weight:800;font-size:6.5px">{fmt(tots["total_invest"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#d6c6f0;font-weight:800;font-size:6.5px">{fmt(tots["rs"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#e8cc80;font-size:6.5px">—</td>'
    note=(f'נקודת איזון 90% מרווח גולמי: הכנסות > (LGG + מדיה + קריאטיב + Ext + הוצ׳) ÷ 0.82 | '
          f'🟢 = מעל נקודת האיזון | 🔴 = מתחת לנקודת האיזון | RS 8% מחוץ ל-₪20K')
    return f"""<div style="overflow-x:hidden">
<table style="width:263mm;border-collapse:collapse;font-variant-numeric:tabular-nums;direction:rtl;font-family:inherit;table-layout:fixed">
  <colgroup><col style="width:9mm"><col style="width:13mm">{"".join(['<col style="width:12mm">']*19)}</colgroup>
  <thead>
    <tr style="border-bottom:1px solid #ddd">{sec1}</tr>
    <tr style="border-bottom:2px solid #ccc">{sec2}</tr>
  </thead>
  <tbody>{rows_html}</tbody>
  <tfoot><tr>{ft}</tr></tfoot>
</table></div>
<div style="margin-top:1.5mm;font-size:5.8px;color:#888;border-top:1px solid #eee;padding-top:1mm">{note}</div>"""

drive_tbl = drive_table_transposed()

# ── שורות טבלת השקעה בדף 10 ────────────────────────────────────────────────
_inv_rows = "".join([
    f'<tr{"" if not MD[m]["profitable"] else " class=hl"}>'
    f'<td>M{m}</td>'
    f'<td style="font-size:7.5px">{"הקמה" if m==0 else "Meta" if m<=6 else "Meta+Google" if m<=8 else "Meta+Google+TikTok"}</td>'
    f'<td class="pur">{fmt(mgmt_fees[m])}</td>'
    f'<td>{"—" if m==0 else fmt(B[m][1] if m<=6 else B_ext[m][1])}</td>'
    f'<td>{"—" if m==0 else fmt(creative_plan[m][2])}</td>'
    f'<td style="font-weight:800;color:#8b2222">{fmt(MD[m]["total_invest"])}</td>'
    f'<td style="font-weight:800;color:#1a7a4a">{fmt(MD[m]["total_rev"]) if MD[m]["total_rev"]>0 else "—"}</td>'
    f'<td style="font-size:10px;text-align:center">{"✓" if MD[m]["profitable"] else ("—" if m==0 else "✗")}</td>'
    f'</tr>'
    for m in range(13)
])


# ── CSS + עמוד שער (עמוד 1) ───────────────────────────────────────────────────
html_parts = []
html_parts.append(f"""<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="UTF-8">
<title>Intermax × LGG — הצעה אסטרטגית 2026</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800;900&display=swap">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --p:#5b1fa8;--p2:#7b3fcf;--pp:#f0eaf9;--pm:#d6c6f0;
  --g:#1a7a4a;--gp:#e8f5ee;--gm:#aadcc0;
  --b:#1a3fa8;--bp:#eaeff9;--bm:#b0c0e8;
  --au:#c49a2a;--ap:#fdf6e3;--am:#e8cc80;
  --r:#c41414;--rp:#ffeaea;
  --ink:#111;--is:#444;--im:#777;--rule:#ddd;--off:#fafaf9;
  --f:'Heebo',Arial,sans-serif;
}}
html,body{{background:#e5e5e5;font-family:var(--f);color:var(--ink);print-color-adjust:exact;-webkit-print-color-adjust:exact}}
.page{{width:297mm;min-height:210mm;background:#fff;margin:8mm auto;padding:10mm 12mm 8mm;position:relative;page-break-after:always;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,.18)}}
@media print{{html,body{{background:#fff}}.page{{margin:0;box-shadow:none;page-break-after:always}}}}
.ph{{display:flex;justify-content:space-between;align-items:center;margin:-10mm -12mm 4.5mm;padding:2.5mm 12mm;background:var(--p)}}
.ph img{{height:7.5mm;object-fit:contain;filter:brightness(0) invert(1)}}
.ph .wm{{font-size:8.5px;font-weight:800;letter-spacing:.12em;color:#fff;text-transform:uppercase}}
.ph .ey{{font-size:7px;letter-spacing:.14em;color:rgba(255,255,255,.65);text-transform:uppercase}}
.cover{{padding:0;display:flex;flex-direction:column;min-height:210mm}}
.ctop{{height:14mm;background:linear-gradient(135deg,var(--p) 60%,var(--p2));display:flex;align-items:center;justify-content:space-between;padding:0 13mm}}
.ctop span{{font-size:7.5px;letter-spacing:.18em;color:rgba(255,255,255,.75);text-transform:uppercase}}
.cbody{{flex:1;padding:8mm 13mm 5mm;display:flex;flex-direction:column}}
.clrow{{display:flex;align-items:center;justify-content:space-between;margin-bottom:5mm}}
.ct{{font-size:30px;font-weight:900;line-height:1.08;color:var(--ink);margin-bottom:2mm}}
.ct span{{color:var(--p)}}
.cs{{font-size:11.5px;font-weight:300;color:var(--is);margin-bottom:5mm}}
.cmg{{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm;border-top:1px solid var(--rule);padding-top:3mm}}
.cmg label{{font-size:7px;letter-spacing:.1em;color:var(--im);text-transform:uppercase;display:block;margin-bottom:1px}}
.cmg span{{font-size:10px;font-weight:700}}
.cbot{{height:6mm;background:var(--p);display:flex;align-items:center;padding:0 13mm;justify-content:space-between}}
.cbot span{{font-size:7px;color:rgba(255,255,255,.7);letter-spacing:.08em}}
.stag{{font-size:8px;letter-spacing:.2em;color:var(--p);text-transform:uppercase;margin-bottom:1mm;font-weight:700}}
.stit{{font-size:19px;font-weight:900;color:var(--ink);margin-bottom:2.5mm;line-height:1.2}}
h2{{font-size:11.5px;font-weight:800;color:var(--ink);margin:2.5mm 0 1.5mm;border-right:3px solid var(--p);padding-right:2mm}}
p{{font-size:10.5px;line-height:1.6;color:var(--is);margin-bottom:1.5mm}}
ul{{padding-right:4mm;font-size:10px;line-height:1.7;color:var(--is)}}
li{{margin-bottom:0.4mm}}
strong{{color:var(--ink)}}
.c2{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.c3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3.5mm}}
.c4{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.kpi{{background:var(--pp);border:1px solid var(--pm);border-right:3px solid var(--p);border-radius:4px;padding:2.5mm 3mm}}
.kpi.gn{{background:var(--gp);border-color:var(--gm);border-right-color:var(--g)}}
.kpi.go{{background:var(--ap);border-color:var(--am);border-right-color:var(--au)}}
.kpi.bl{{background:var(--bp);border-color:var(--bm);border-right-color:var(--b)}}
.kpi.rd{{background:var(--rp);border-color:#f0b0b0;border-right-color:var(--r)}}
.kpi .kl{{font-size:6.5px;letter-spacing:.1em;color:var(--p);text-transform:uppercase;margin-bottom:0.5mm;font-weight:700}}
.kpi.gn .kl{{color:var(--g)}}.kpi.go .kl{{color:#7a5a10}}.kpi.bl .kl{{color:var(--b)}}.kpi.rd .kl{{color:var(--r)}}
.kpi .kv{{font-size:20px;font-weight:900;color:var(--ink);line-height:1;font-variant-numeric:tabular-nums}}
.kpi .kv.sm{{font-size:14px}}
.kpi .ks{{font-size:7px;color:var(--im);margin-top:0.5mm}}
table{{width:100%;border-collapse:collapse;font-size:9px;font-variant-numeric:tabular-nums;direction:rtl}}
thead th{{background:var(--p);color:#fff;padding:1.8mm 1.5mm;font-weight:700;font-size:8px;white-space:nowrap;text-align:right}}
thead th.gc{{background:var(--g)}}thead th.ga{{background:#7a5a10}}thead th.gb{{background:var(--b)}}
tbody tr{{border-bottom:1px solid var(--rule)}}
tbody tr:nth-child(even){{background:var(--off)}}
tbody tr.hl{{background:var(--pp)!important;font-weight:700}}
tbody tr.m0{{background:#f5f5f5;color:#888;font-style:italic}}
td{{padding:1.2mm 1.5mm;text-align:right;color:var(--is);white-space:nowrap}}
td:first-child{{font-weight:600;color:var(--ink)}}
td.pos{{color:var(--g);font-weight:700}}td.neg{{color:var(--r);font-weight:700}}td.pur{{color:var(--p);font-weight:700}}
tfoot td{{background:var(--p);color:#fff;font-weight:800;padding:2mm;font-size:7.5px}}
.box{{border:1px solid var(--pm);background:var(--pp);border-right:4px solid var(--p);border-radius:4px;padding:2.5mm 3mm;margin:1mm 0;font-size:8.5px;line-height:1.65}}
.box.gn{{background:var(--gp);border-color:var(--gm);border-right-color:var(--g)}}
.box.go{{background:var(--ap);border-color:var(--am);border-right-color:var(--au)}}
.box.re{{background:var(--rp);border-color:#f0b0b0;border-right-color:var(--r)}}
.box.bl{{background:var(--bp);border-color:var(--bm);border-right-color:var(--b)}}
.box.dk{{background:#1a1a2e;border-color:#3a3a5e;border-right-color:var(--p);color:#ccc}}
.box.dk strong{{color:#fff}}
.cf{{display:inline-block;padding:1px 4px;border-radius:3px;font-size:6.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;vertical-align:middle;margin-left:1mm}}
.cf.h{{background:#d8f0e5;color:#1a7a4a}}.cf.m{{background:#fdf3d8;color:#7a5a10}}.cf.l{{background:#fde8e8;color:#8b1a1a}}
.timeline-row{{display:flex;gap:0;margin-bottom:2.5mm}}
.tl-month{{min-width:16mm;font-size:7px;font-weight:800;color:var(--p);padding-top:1mm}}
.tl-dot{{width:3mm;display:flex;flex-direction:column;align-items:center}}
.tl-dot .d{{width:3mm;height:3mm;border-radius:50%;background:var(--p);flex-shrink:0}}
.tl-dot .l{{width:1px;flex:1;background:var(--rule);margin-top:0.5mm}}
.tl-content{{flex:1;background:var(--pp);border-radius:3px;padding:2mm 3mm;margin-right:2mm;font-size:8px;line-height:1.5}}
</style>
</head>
<body>

<!-- עמוד 1: שער -->
<div class="page cover" style="padding:0">
  <div class="ctop">
    <span>CONFIDENTIAL — INTERMAX GROUP × LOS GARDIOS GROUP — D2C E-COMMERCE STRATEGY 2026</span>
    <span>ספטמבר 2026</span>
  </div>
  <div class="cbody">
    <div class="clrow">
      <img src="{chrome_uri}" class="cr" alt="LGG" style="height:22mm;object-fit:contain">
      <img src="{seal_uri}" alt="Seal" style="height:20mm;object-fit:contain">
    </div>
    <div class="ct">הצעה אסטרטגית<br><span>D2C E-Commerce</span></div>
    <div class="cs">Ed Hardy Israel · Umbro Israel · Intermax Group Hub — ניהול מלא של 3 חנויות Shopify</div>
    <div class="cmg">
      <div><label>תקציב חודשי</label><span>₪20,000</span></div>
      <div><label>RS ל-LGG</label><span>8%</span></div>
      <div><label>ריטיינר / ערוץ</label><span>₪{CHANNEL_DISCOUNTED:,}</span></div>
      <div><label>ציר סבלנות</label><span>5 חודשים</span></div>
      <div><label>AOV ממוצע</label><span>₪{AOV}</span></div>
      <div><label>מרווח גולמי</label><span>~90%</span></div>
    </div>
    <div style="margin-top:4mm;display:grid;grid-template-columns:repeat(3,1fr);gap:3mm">
      <div style="background:#f5f0fc;border:1px solid #d6c6f0;border-radius:5px;padding:3mm 4mm;text-align:center">
        <div style="font-size:8px;letter-spacing:.1em;color:#5b1fa8;font-weight:800;text-transform:uppercase;margin-bottom:1mm">Ed Hardy Israel</div>
        <div style="font-size:9px;color:#444">Y2K Revival · Tattoo Culture · Tel Aviv Nightlife</div>
      </div>
      <div style="background:#eaf0fc;border:1px solid #b0c0e8;border-radius:5px;padding:3mm 4mm;text-align:center">
        <div style="font-size:8px;letter-spacing:.1em;color:#1a3fa8;font-weight:800;text-transform:uppercase;margin-bottom:1mm">Umbro Israel</div>
        <div style="font-size:9px;color:#444">Sports Authority · Padel · Football Kits</div>
      </div>
      <div style="background:#fdf6e3;border:1px solid #e8cc80;border-radius:5px;padding:3mm 4mm;text-align:center">
        <div style="font-size:8px;letter-spacing:.1em;color:#c49a2a;font-weight:800;text-transform:uppercase;margin-bottom:1mm">Intermax Hub</div>
        <div style="font-size:9px;color:#444">Multi-Brand · Fast Simon AI · Loyalty</div>
      </div>
    </div>
  </div>
  <div class="cbot">
    <span>Los Gardios Group | ח.פ. 516819257 | losgardios.com</span>
    <span>LGG-IMX-2026 | v16 | מסמך סודי</span>
  </div>
</div>
""")


# ── עמוד 2: אסטרטגיה עסקית ─────────────────────────────────────────────────
html_parts.append(f"""
<!-- עמוד 2: אסטרטגיה עסקית -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">01 — אסטרטגיה עסקית</span><span class="ey">Business Strategy</span></div>
  <div class="stag">01 — BUSINESS STRATEGY</div>
  <div class="stit">הזדמנות השוק — ישראל D2C ביגוד ואופנה</div>
  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi gn"><div class="kl">שוק אופנה ישראל</div><div class="kv sm">₪6.3B</div><div class="ks"><span class="cf h">HIGH</span> 3.4% לשנה · 18 מיליון קניות</div></div>
    <div class="kpi go"><div class="kl">AOV ישראלי D2C</div><div class="kv sm">$190</div><div class="ks"><span class="cf h">HIGH</span> מהגבוה בעולם — ₪380 ספורט</div></div>
    <div class="kpi bl"><div class="kl">מגרשי פאדל</div><div class="kv sm">130+</div><div class="ks"><span class="cf m">MED</span> 36 בבנייה · חלון כניסה</div></div>
  </div>
  <div class="c2">
    <div>
      <h2>ניתוח תחרות — פערים בשוק</h2>
      <table style="margin-top:1.5mm;font-size:8px">
        <thead><tr><th>קטגוריה</th><th>המצב הקיים</th><th>ההזדמנות</th></tr></thead>
        <tbody>
          <tr><td>Tattoo Streetwear D2C</td><td>ייבוא אפור, ASOS</td><td class="pos"><strong>D2C ישראלי, עברית, ₪250-500</strong></td></tr>
          <tr><td>ביגוד פאדל ייעודי</td><td>חנויות ספורט כלליות</td><td class="pos"><strong>מותג פאדל ישראלי ראשון</strong></td></tr>
          <tr><td>קיטים מועדוני חובבים</td><td>B2B אופליין בלבד</td><td class="pos"><strong>D2C + B2B באותה חנות</strong></td></tr>
          <tr><td>פלטפורמת D2C מאוחדת</td><td>Zara, ASOS מחו"ל</td><td class="pos"><strong>Hub ישראלי רב-מותגי</strong></td></tr>
        </tbody>
      </table>
      <div class="box gn" style="margin-top:2mm;font-size:8px">
        <span class="cf h">HIGH</span> <strong>ממצא מרכזי:</strong> אין D2C ישראלי שמחזיק tattoo streetwear ₪200-400. פער מובנה בשוק. ריצה — הספורט הצומח הכי מהיר בישראל — ורק Umbro עם ה-DNA הנכון.
      </div>
      <h2 style="margin-top:2mm">מדוע עכשיו?</h2>
      <ul style="font-size:8.5px">
        <li><strong>iOS 17 פרטיות:</strong> מי שיש לו Pixel ונתונים ינצח. כניסה עכשיו = יתרון מצטבר</li>
        <li><strong>עלות CPC עולה:</strong> כל שנה יקר יותר — כניסה ראשונה = חיסכון לעתיד</li>
        <li><strong>Shopify ישראל:</strong> Bit + עברית + Klaviyo RTL = תשתית מלאה</li>
      </ul>
    </div>
    <div>
      <h2>ארכיטקטורת 3 חנויות</h2>
      <div style="display:grid;gap:2mm;margin-top:1.5mm">
        <div class="box" style="font-size:8px">
          <strong style="color:var(--p)">Ed Hardy Israel</strong> — tattoo-flash, אחרי צבא 18-28, תל אביב / מרכז<br>
          AOV ₪387 | ROAS M6: 3.2× | פתיחה: M1 | <span class="cf h">HIGH</span> Y2K revival פעיל
        </div>
        <div class="box bl" style="font-size:8px">
          <strong style="color:var(--b)">Umbro Israel</strong> — ספורט, ריצה + פאדל + כדורגל, גיל 25-45<br>
          AOV ₪380 | עסקאות קיטים B2B | <span class="cf m">MED</span> 130+ מגרשי פאדל פעילים
        </div>
        <div class="box go" style="font-size:8px">
          <strong style="color:var(--au)">Intermax Hub</strong> — nine72.com / intermax.co.il · רב-מותגי<br>
          Fast Simon AI · נאמנות רב-מותגית · קונה Ed Hardy → המלצה Umbro
        </div>
      </div>
      <div class="box re" style="margin-top:2mm;font-size:8px">
        <span class="cf l">RISK</span> <strong>מתחילים מאפס.</strong> אין היסטוריית Pixel, רשימת אימייל, או ROAS benchmark ישראלי. חודשים M1-M3 הם שלב למידה — ציר סבלנות 5 חודשים הכרחי.
      </div>
      <h2 style="margin-top:2mm">תשתית טכנולוגית</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm">
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>PayPlus / Cardcom</strong><br>Shopify Payments לא ב-IL<br><span class="cf h">HIGH</span> Bit + תשלומים</div>
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>Fast Simon</strong><br>חיפוש AI + סינון + UX<br><span class="cf m">MED</span> שיפור CVR בין 15-25%</div>
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>Klaviyo</strong><br>אימייל + SMS → עגלה נטושה<br><span class="cf h">HIGH</span> 83.5% נטישת עגלה בישראל</div>
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>Yotpo / Loox</strong><br>ביקורות + UGC מ-M2<br><span class="cf m">MED</span> הוכחה חברתית = CVR</div>
      </div>
    </div>
  </div>
</div>
""")


# ── עמודים 3-5: אסטרטגיית מותגים ───────────────────────────────────────────
html_parts.append(f"""
<!-- עמוד 3: Ed Hardy Israel -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a0033,#5b1fa8)"><img src="{chrome_uri}" alt=""><span class="wm">02 — Ed Hardy Israel — אסטרטגיית מותג</span><span class="ey">Brand Strategy</span></div>
  <div class="stag" style="color:#5b1fa8">02 — ED HARDY ISRAEL — BRAND STRATEGY</div>
  <div class="stit">Y2K Revival · Tattoo-Flash Art · תרבות לילה תל אביבית</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi"><div class="kl">שיא המותג</div><div class="kv sm">$700M</div><div class="ks"><span class="cf h">HIGH</span> 2004-2009 · ירידה חדה (91%) מאז</div></div>
    <div class="kpi go"><div class="kl">Y2K Revival</div><div class="kv sm">פעיל</div><div class="ks"><span class="cf h">HIGH</span> אסתטיקת Gen-Z 2024-2026</div></div>
    <div class="kpi gn"><div class="kl">AOV יעד</div><div class="kv sm">₪387</div><div class="ks"><span class="cf m">MED</span> חבילות ₪500+ מ-M4</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>ניתוח היסטורי — לקחים לישראל</h2>
      <div class="box dk" style="font-size:8px;margin-bottom:2mm">
        <strong>ציר זמן:</strong> שיא עולמי 2004-2008 → ישראל בפיגור 6-12 חודש → חנות ת"א נפתחה 2007 → סגרה ~2011 עם קריסת ה-wholesale<br>
        <strong>3 סיבות לקריסה:</strong> רישוי-יתר (70 sub-licensees) · אפקט Gosselin · הפצה המונית ב-Macy's<br>
        <strong>לקח לישראל:</strong> שוק מרוכז = סטורציה מהירה. מחזור מותג 3-5 שנים מקסימום.
      </div>

      <h2>פוזישנינג — 2026</h2>
      <div class="box" style="font-size:8.5px">
        <strong>Premium Tattoo Streetwear · לא נוסטלגיה — revival</strong><br>
        לא מוכרים את העבר — מוכרים אסתטיקת tattoo-flash עכשווית שחוזרת עם דור Z. Ed Hardy הוא הכלי, לא הסיפור.
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin-top:2mm">
        <div style="background:#1a0033;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#d6c6f0;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">קהל יעד ראשוני</div>
          <div style="color:#fff;font-size:8.5px">גיל 18-28, ת"א + גוש דן<br>אחרי צבא, חיי לילה<br>תרבות טאטו, מוזיקה</div>
        </div>
        <div style="background:#2a0055;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#d6c6f0;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">טווח מחיר יעד</div>
          <div style="color:#fff;font-size:8.5px">חולצה: ₪250-320<br>קפוצ'ון: ₪380-480<br>חבילה: ₪500+</div>
        </div>
      </div>

      <h2 style="margin-top:2mm">ערוצי הפצה — D2C ראשון</h2>
      <ul style="font-size:8.5px">
        <li><strong>Shopify EDH.co.il</strong> — ראשוני, מותאם RTL, Bit + תשלומים</li>
        <li><strong>אינסטגרם + TikTok אורגני</strong> — שיתופי פעולה עם אמני טאטו</li>
        <li><strong>WhatsApp VIP Drops</strong> — שחרורים מוגבלים → FOMO + דחיפות</li>
        <li><strong>Klaviyo Welcome Series</strong> — 5 מיילים: סיפור המותג + תרבות הטאטו</li>
      </ul>
    </div>
    <div>
      <h2>אסטרטגיית קריאטיב Ed Hardy</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>שלב</th><th>פורמט</th><th>כיוון תוכן</th></tr></thead>
        <tbody>
          <tr><td>M1 זרע</td><td>6 Static</td><td>קלוז-אפ על flash tattoo, מודל + אווירת לילה</td></tr>
          <tr><td>M2 השקה</td><td>6S + 1V</td><td>מאחורי הקלעים טאטו, lifestyle תל אביב</td></tr>
          <tr><td>M3+</td><td>UGC ראשון</td><td>לקוחות אמיתיים = הוכחה חברתית עיקרית</td></tr>
        </tbody>
      </table>

      <h2 style="margin-top:2mm">קמפיין Meta — ספציפיקות Ed Hardy</h2>
      <div class="box bl" style="font-size:8px">
        <strong>טירגוט:</strong> גיל 18-28, ישראל · תחומי עניין: טאטו, streetwear, פסטיבלי מוזיקה<br>
        <strong>אי-כלול:</strong> גיל 35+ · קהלים משפחתיים<br>
        <span class="cf m">MED</span> CTR baseline 1.5-2.5% · CVR cold start 0.8-1.2%
      </div>

      <div class="box re" style="margin-top:2mm;font-size:8px">
        <span class="cf l">RISK</span> <strong>IP — חובה לבדוק לפני השקה!</strong><br>
        IP מוחזק על-ידי <strong>Hardy Way LLC / Iconix Brand Group</strong>. Intermax חייב לאמת שהסכם הרישיון מכסה D2C ישראלי לפני כל פרסום.
      </div>

      <div class="box go" style="margin-top:2mm;font-size:8.5px">
        <strong>הזדמנות Y2K 2026:</strong> טרנד "Bring Back Ed Hardy" פעיל ב-TikTok. חיפושים ב-Pinterest עלו 340% לשנה. דור Z לא חווה את שלב הרוויה — הם רואים בזה וינטג' אותנטי.
        <span class="cf h">HIGH</span>
      </div>

      <h2 style="margin-top:2mm">KPIs — Ed Hardy (בנצ'מרק)</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5mm">
        <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center;font-size:8px"><strong>CVR M1</strong><br><span style="color:#5b1fa8;font-weight:800">0.8-1.2%</span><br><span class="cf m">MED</span></div>
        <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center;font-size:8px"><strong>CVR M6+</strong><br><span style="color:#1a7a4a;font-weight:800">1.8-2.4%</span><br><span class="cf m">MED</span></div>
        <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center;font-size:8px"><strong>חוזרים 90 יום</strong><br><span style="color:#c49a2a;font-weight:800">22%</span><br><span class="cf m">MED</span></div>
      </div>
    </div>
  </div>
</div>

<!-- עמוד 4: Umbro Israel -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#001a3f,#1a3fa8)"><img src="{chrome_uri}" alt=""><span class="wm">03 — Umbro Israel — אסטרטגיית מותג</span><span class="ey">Brand Strategy</span></div>
  <div class="stag" style="color:#1a3fa8">03 — UMBRO ISRAEL — BRAND STRATEGY</div>
  <div class="stit">Sports Authority · ריצה · קיטי כדורגל · פאדל</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi bl"><div class="kl">שוק ספורט ישראל</div><div class="kv sm">$1.72B</div><div class="ks"><span class="cf h">HIGH</span> CAGR +5% עד 2032</div></div>
    <div class="kpi gn"><div class="kl">ריצה — ספורט מוביל</div><div class="kv sm">28%</div><div class="ks"><span class="cf m">MED</span> צמיחה מהירה · 2024</div></div>
    <div class="kpi go"><div class="kl">מועדוני כדורגל חובבים</div><div class="kv sm">1,200+</div><div class="ks"><span class="cf m">MED</span> הזדמנות קיטים B2B</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>פוזישנינג — Umbro Israel 2026</h2>
      <div class="box bl" style="font-size:8.5px">
        <strong>Technical Sports Authority — לא רק כדורגל</strong><br>
        Umbro נכנסת לישראל כפלטפורמת ביצועי ספורט. כדורגל כעוגן → ריצה כמנוע צמיחה → פאדל כהתרחבות.
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;margin-top:2mm">
        <div style="background:#001a3f;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#b0c0e8;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">כדורגל</div>
          <div style="color:#fff;font-size:8px">עוגן ה-DNA · קיטים B2B<br>ליגות חובבים<br>AOV ₪280 לקיט</div>
        </div>
        <div style="background:#002b5c;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#b0c0e8;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">ריצה</div>
          <div style="color:#fff;font-size:8px">מנוע צמיחה עיקרי<br>28% CAGR ישראל<br>AOV ₪380 head-to-toe</div>
        </div>
        <div style="background:#1a3fa8;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#fff;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">פאדל</div>
          <div style="color:#fff;font-size:8px">הזדמנות נישה<br>130 מגרשים · 36 בבנייה<br><span class="cf l">LOW</span> 2K שחקנים ייעודיים</div>
        </div>
      </div>

      <h2 style="margin-top:2mm">הזדמנות B2B — קיטים מועדונים</h2>
      <div class="box gn" style="font-size:8px">
        <strong>1,200+ מועדוני כדורגל חובבים בישראל.</strong> אין ספק D2C ישראלי לקיטים. עסקת קיט: חולצה ₪120 + מכנס ₪80 + גרב ₪30 = <strong>₪230/שחקן × 18 שחקנים = ₪4,140/קיט.</strong> 4 קיטים/חודש = ₪16,560 הכנסת B2B נוספת.
      </div>

      <h2 style="margin-top:2mm">אסטרטגיית קריאטיב Umbro</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>שלב</th><th>פורמט</th><th>תוכן</th></tr></thead>
        <tbody>
          <tr><td>M1</td><td>6 Static</td><td>אקשן שוטס · ריצה בישראל · אסתטיקת מגרש פאדל</td></tr>
          <tr><td>M2</td><td>6S + 1V</td><td>וידאו אימון כדורגל · תצוגת קיט · תחושת קהילה</td></tr>
          <tr><td>M3+</td><td>UGC</td><td>מועדונים מרוצים · שחקנים אמיתיים</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h2>פלחי קהל יעד — Umbro</h2>
      <div style="display:grid;gap:1.5mm;margin-top:1mm">
        <div class="box bl" style="font-size:8px">
          <strong>עיקרי: רץ נלהב גיל 25-40</strong><br>
          גוש דן · עניין באפליקציות ריצה (Strava, Nike Run) · תקציב ₪400-600/שנה על ציוד
        </div>
        <div class="box" style="font-size:8px">
          <strong>משני: לוחם סוף שבוע גיל 28-45</strong><br>
          ליגות חובבים · קברניט הקבוצה = מקבל ההחלטות לרכישת קיט
        </div>
        <div class="box go" style="font-size:8px">
          <strong>שלישוני: שחקן פאדל גיל 30-50</strong><br>
          <span class="cf l">LOW</span> רק ~2,000 שחקנים ייעודיים. לא לבנות תחזית ראשית על פאדל. נקודת כניסה לשוק הרחב.
        </div>
      </div>

      <h2 style="margin-top:2mm">Meta Ads — טירגוט ספציפי Umbro</h2>
      <div class="box bl" style="font-size:8px">
        <strong>תחומי עניין:</strong> ריצה, כדורגל, כושר, ביגוד ספורטיבי, פאדל, Strava<br>
        <strong>גיל:</strong> 25-45 | <strong>מיקום:</strong> ישראל ארצית (לא רק המרכז)<br>
        <strong>Lookalike:</strong> רשימת אימייל של לקוחות קיטים B2B (LTV גבוה)<br>
        <span class="cf m">MED</span> CAC צפוי ₪180-220 התחלה → ₪100-130 מ-M6
      </div>

      <h2 style="margin-top:2mm">KPIs — Umbro (בנצ'מרק)</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm">
        <div class="box bl" style="font-size:8px;text-align:center">
          <strong>ROAS יעד M6</strong><br>
          <span style="font-size:16px;font-weight:900;color:#1a3fa8">2.8×</span><br>
          <span class="cf m">MED</span> בנצ'מרק אופנת ספורט IL
        </div>
        <div class="box gn" style="font-size:8px;text-align:center">
          <strong>שיעור חוזרים (90 יום)</strong><br>
          <span style="font-size:16px;font-weight:900;color:#1a7a4a">22%</span><br>
          <span class="cf m">MED</span> קונים עונתיים
        </div>
      </div>

      <div class="box re" style="margin-top:2mm;font-size:8px">
        <span class="cf l">RISK</span> <strong>תחרות ישירה:</strong> Nike, Adidas, New Balance לא נעלמות. Umbro מנצחת על DNA כדורגל + מחיר mid-tier (₪200-400 לעומת ₪500+ Nike). לא להתחרות ישירות — להשתלט על נישת קיטי כדורגל + פאדל.
      </div>
    </div>
  </div>
</div>

<!-- עמוד 5: Intermax Hub -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a3a00,#c49a2a)"><img src="{chrome_uri}" alt=""><span class="wm">04 — Intermax Group Hub</span><span class="ey">Multi-Brand Strategy</span></div>
  <div class="stag" style="color:#c49a2a">04 — INTERMAX GROUP HUB — MULTI-BRAND STRATEGY</div>
  <div class="stit">nine72.com / intermax.co.il · Fast Simon AI · נאמנות רב-מותגית</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi go"><div class="kl">עלייה במכירות צולבות</div><div class="kv sm">+18%</div><div class="ks"><span class="cf m">MED</span> AOV רב-מותגי לעומת חנות בודדת</div></div>
    <div class="kpi gn"><div class="kl">שיפור LTV בנאמנות</div><div class="kv sm">×2.5</div><div class="ks"><span class="cf m">MED</span> חבר מועדון לעומת לקוח רגיל</div></div>
    <div class="kpi bl"><div class="kl">Fast Simon — שיפור CVR</div><div class="kv sm">+22%</div><div class="ks"><span class="cf l">LOW</span> חיפוש AI לעומת סטנדרטי</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>תפקיד ה-Hub — גשר בין שני עולמות</h2>
      <div class="box go" style="font-size:8.5px">
        ה-Hub אינו "עוד חנות" — הוא התשתית שמאפשרת ל-Ed Hardy ו-Umbro לשתף נתונים, לקוחות ולמנף מכירות צולבות. לקוח שמגיע ל-Ed Hardy יכול לגלות Umbro, ולהיפך.
      </div>

      <h2 style="margin-top:2mm">Fast Simon AI — יכולות</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>פיצ'ר</th><th>תיאור</th><th>השפעה</th></tr></thead>
        <tbody>
          <tr><td>חיפוש AI</td><td>הבנת כוונה, שגיאות כתיב, עברית</td><td class="pos">CVR +15-22%</td></tr>
          <tr><td>סינון חכם</td><td>סינון דינמי לפי התנהגות</td><td class="pos">נטישה -18%</td></tr>
          <tr><td>התאמה אישית</td><td>מוצרים לפי התנהגות</td><td class="pos">AOV +12%</td></tr>
          <tr><td>המלצה רב-מותגית</td><td>קונה Ed Hardy → הצעת Umbro</td><td class="pos">מכירה צולבת</td></tr>
        </tbody>
      </table>
      <div style="margin-top:1.5mm;font-size:7px;color:#888">עלות Fast Simon: ₪200-400/חודש. החזר ROI על שיפור CVR בתוך M2.</div>

      <h2 style="margin-top:2mm">ארכיטקטורת נאמנות</h2>
      <div class="box" style="font-size:8px">
        <strong>מערכת נקודות רב-מותגית:</strong><br>
        קנייה ב-Ed Hardy = נקודות שניתן להשתמש ב-Umbro, ולהיפך.<br>
        "נאמנות קבוצתית" — הסיבה לבוא ל-Hub ולא לחנות בודדת.<br>
        כלי: Yotpo Loyalty / Smile.io — <span class="cf m">MED</span> ₪150-300/חודש
      </div>
    </div>
    <div>
      <h2>מסע הלקוח הרב-מותגי</h2>
      <div style="display:flex;flex-direction:column;gap:2mm;margin-top:1mm">
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#5b1fa8;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">1</div>
          <div style="background:#f0eaf9;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">לקוח נחשף לפרסומת Ed Hardy במטא → מגיע לאתר</div>
        </div>
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#5b1fa8;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">2</div>
          <div style="background:#f0eaf9;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">קונה חולצה Ed Hardy → מצטרף למועדון הנאמנות</div>
        </div>
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#c49a2a;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">3</div>
          <div style="background:#fdf6e3;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">ה-Hub מציג: "אוהבי Ed Hardy אוהבים גם Umbro Running" → מכירה צולבת</div>
        </div>
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#1a7a4a;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">4</div>
          <div style="background:#e8f5ee;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">Klaviyo: 30 ימים אחרי קנייה → הצעת Umbro + נקודות<br>LTV גדל בשני המותגים</div>
        </div>
      </div>

      <h2 style="margin-top:2mm">תועלת ה-Hub לעסק</h2>
      <ul style="font-size:8.5px">
        <li><strong>Pixel משותף:</strong> כל לקוח של מותג אחד מאמן את הסיגנל לשני</li>
        <li><strong>רשימת אימייל משותפת:</strong> Klaviyo אחד לשני המותגים — חיסכון בעלויות</li>
        <li><strong>דשבורד מאוחד:</strong> LTV, CAC, הכנסה לכל לקוח — מבט אחד</li>
        <li><strong>פורטל B2B:</strong> ספקי קיטי כדורגל יכולים להזמין דרך ה-Hub</li>
      </ul>

      <div class="box gn" style="margin-top:2mm;font-size:8px">
        <span class="cf m">MED</span> <strong>יעד שנה 1 לHub:</strong> 15% מסך ההכנסות מרכישות צולבות. כל מכירה צולבת = מרווח מלא ללא CAC נוסף → מינוף.
      </div>
    </div>
  </div>
</div>
""")


# ── עמוד 6: ניתוח פיננסי — נקודת איזון 90% מרווח גולמי ─────────────────────
m1_be = MD[1]['be_threshold']
m1_rev = MD[1]['total_rev']
m5_be  = MD[5]['be_threshold']
m5_rev = MD[5]['total_rev']

html_parts.append(f"""
<!-- עמוד 6: ניתוח פיננסי -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">05 — ניתוח פיננסי</span><span class="ey">Breakeven + Scenarios</span></div>
  <div class="stag">05 — FINANCIAL FOUNDATION</div>
  <div class="stit">נקודת איזון + השוואת תרחישים H1</div>
  <div class="c2" style="margin-bottom:3mm">
    <div>
      <div class="c4" style="margin-bottom:2.5mm">
        <div class="kpi go"><div class="kl">מרווח גולמי Intermax</div><div class="kv">90%</div><div class="ks">בקירוב — מוצר+רויאלטי נמוך</div></div>
        <div class="kpi rd"><div class="kl">נ.א. M1 הכנסה</div><div class="kv sm">{fmt(m1_be)}</div><div class="ks">בסיס 90% GM − RS 8%</div></div>
        <div class="kpi"><div class="kl">הכנסה בפועל M1</div><div class="kv sm">{fmt(m1_rev)}</div><div class="ks">שלב למידה — לפי תקציב</div></div>
        <div class="kpi gn"><div class="kl">ציר סבלנות</div><div class="kv">5</div><div class="ks">חודשים עד רווחיות ראשונה</div></div>
      </div>
      <h2>נוסחת נקודת האיזון — 90% מרווח גולמי</h2>
      <div class="box go" style="font-size:8.5px;margin-top:1mm">
        <strong>נוסחה:</strong> הכנסות מינימום = (LGG + מדיה + קריאטיב + Ext + הוצ׳ קבועות) ÷ 0.82<br>
        <span style="font-size:7.5px;color:#555">0.82 = מרווח גולמי 90% − RS 8% = הרווח הנקי על כל שקל הכנסה</span><br><br>
        <strong>דוגמה M1:</strong> (₪8,000 + ₪11,220 + ₪780 + ₪715 + ₪1,200) ÷ 0.82 = <strong>{fmt(m1_be)}</strong><br>
        <strong>הכנסה בפועל M1: {fmt(m1_rev)}</strong> — שלב למידה, הצפי ל-M5 הוא חצייה של נקודת האיזון
      </div>
      <div class="box gn" style="margin-top:1.5mm;font-size:8px">
        <strong>M5 — חציית נקודת האיזון:</strong><br>
        הכנסה M5: <strong>{fmt(m5_rev)}</strong> | נ.א. M5: <strong>{fmt(m5_be)}</strong><br>
        מ-M5 ואילך — ההכנסה עוברת את נקודת האיזון ב-90% מרווח גולמי. <span class="cf h">HIGH</span>
      </div>
      <div style="margin-top:1.5mm;font-size:7.5px;color:#888;background:#f9f9f9;border-radius:3px;padding:2mm">
        <strong>הבהרה:</strong> הרווח הנקי המדויק תלוי במרווח הגולמי האמיתי של Intermax. הלקוח יחשב את הרווח לפי עלויות ה-COGS שלו. הצגת נתוני הכנסות ועלויות בלבד — ללא נטו.
      </div>
    </div>
    <div>
      <h2>השוואת תרחישים M1-M6</h2>
      <table style="margin-top:1mm;font-size:8px">
        <thead>
          <tr>
            <th rowspan="2">חודש</th>
            <th rowspan="2" style="background:#7a5a10">נ.א. 90%</th>
            <th rowspan="2" style="background:#555;width:1.5mm"></th>
            <th colspan="2" style="background:#8b2222;text-align:center">שמרני 🔴</th>
            <th rowspan="2" style="background:#555;width:1.5mm"></th>
            <th colspan="2" style="background:#7a5a10;text-align:center">בסיס 🟡</th>
            <th rowspan="2" style="background:#555;width:1.5mm"></th>
            <th colspan="2" style="background:var(--g);text-align:center">אגרסיבי 🟢</th>
          </tr>
          <tr>
            <th style="background:#a03030">הכנסה</th><th style="background:#a03030">✓/✗</th>
            <th class="ga">הכנסה</th><th class="ga">✓/✗</th>
            <th class="gc">הכנסה</th><th class="gc">✓/✗</th>
          </tr>
        </thead>
        <tbody>{sc_rows}</tbody>
      </table>
      <div class="box go" style="margin-top:1.5mm;font-size:8px">
        <span class="cf m">MED</span> <strong>✓ = הכנסה מעל נקודת האיזון ב-90% מרווח גולמי.</strong><br>
        הלקוח מחשב את הרווח הנקי לפי מרווח הגולמי האמיתי שלו. נקודת האיזון מחושבת: (עלויות ידועות) ÷ 0.82.
      </div>
    </div>
  </div>
</div>

<!-- עמוד 7: תחזית שנתית -->
<div class="page" style="padding:8mm 10mm 6mm">
  <div class="ph" style="margin:-8mm -10mm 3.5mm">
    <img src="{chrome_uri}" alt="">
    <span class="wm">06 — תחזית שנתית M0-M12</span>
    <span class="ey">Drive Format — All KPIs</span>
  </div>
  <div class="stag">06 — ANNUAL FORECAST (BASE SCENARIO)</div>
  <div class="stit" style="font-size:15px;margin-bottom:2.5mm">תחזית מלאה — כל ה-KPIs | M0 עד M12 | נ.א. = נקודת איזון ב-90% מרווח גולמי</div>
  {drive_tbl}
</div>
""")


# ── עמודים 8-9: טיימליין + מסגרת אי-ודאות ───────────────────────────────────
html_parts.append(f"""
<!-- עמוד 8: טיימליין -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">07 — טיימליין ביצוע</span><span class="ey">90-Day Roadmap + 12-Month Milestones</span></div>
  <div class="stag">07 — TIMELINE</div>
  <div class="stit">90 ימים ראשונים + אבני דרך שנה ראשונה</div>

  <div class="c2">
    <div>
      <h2>90 ימים ראשונים — שלב אחר שלב</h2>
      <div class="timeline-row">
        <div class="tl-month">M0<br>שבוע 1-2</div>
        <div class="tl-dot"><div class="d" style="background:#5b1fa8"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#f0eaf9">
          <strong style="color:#5b1fa8">הקמה טכנולוגית</strong><br>
          ✓ Shopify × 3 — עברית + RTL<br>
          ✓ PayPlus / Cardcom סליקה<br>
          ✓ Facebook Pixel על 3 חנויות<br>
          ✓ דומיין ×3 + הגדרת אימייל
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M0<br>שבוע 3-4</div>
        <div class="tl-dot"><div class="d" style="background:#5b1fa8"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#f0eaf9">
          <strong style="color:#5b1fa8">תוכן + קריאטיב ראשוני</strong><br>
          ✓ התקנת Fast Simon<br>
          ✓ Klaviyo: ברוכים הבאים + עגלה נטושה<br>
          ✓ 6 נכסי Static לכל מותג (צילום)<br>
          ✓ חימום חשבון הפרסום
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M1<br>שבוע 1-4</div>
        <div class="tl-dot"><div class="d" style="background:#c49a2a"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#fdf6e3">
          <strong style="color:#c49a2a">השקה רכה — Meta Ads</strong><br>
          ✓ CBO Broad + אופטימיזציה להוספה לעגלה<br>
          ✓ שלב למידה — אל תצפה ל-ROAS גבוה<br>
          ✓ אירועי Pixel: PageView → ATC → Purchase<br>
          ✓ יעד: 50+ הוספות לעגלה (יציאה מלמידה)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M2-M3</div>
        <div class="tl-dot"><div class="d" style="background:#c49a2a"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#fdf6e3">
          <strong style="color:#c49a2a">בדיקת קריאטיב + רטרגטינג</strong><br>
          ✓ A/B בין Static לוידאו לכל מותג<br>
          ✓ קמפייני רטרגטינג חיים<br>
          ✓ בניית קהלי Lookalike<br>
          ✓ יעד: 10 קניות/שבוע (בשלות Pixel)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M4-M6</div>
        <div class="tl-dot"><div class="d" style="background:#1a7a4a"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#e8f5ee">
          <strong style="color:#1a7a4a">אופטימיזציה + רווחיות ראשונה</strong><br>
          ✓ הגדלת קריאטיב המנצח<br>
          ✓ Lookalike 1% → 3% → 5%<br>
          ✓ Klaviyo מאופטם (יעד: 30%+ open rate)<br>
          ✓ <strong>M5: חציית נקודת האיזון ב-90% מרווח גולמי — הכנסה {fmt(MD[5]["total_rev"])}</strong>
        </div>
      </div>
    </div>
    <div>
      <h2>M7-M12 — הרחבת ערוצים</h2>
      <div class="timeline-row">
        <div class="tl-month">M7-M8</div>
        <div class="tl-dot"><div class="d" style="background:#1a3fa8"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#eaeff9">
          <strong style="color:#1a3fa8">השקת Google Ads</strong><br>
          ✓ קמפייני Google Shopping + Search<br>
          ✓ הגנה על מילות מפתח של המותג<br>
          ✓ הגדרת ייחוס רב-ערוצי<br>
          ✓ שכ"ט LGG: ₪{mgmt_fees[7]:,} (Meta + Google)<br>
          ✓ יעד ROAS M8: 3.1× (Google Search — כוונת רכישה גבוהה)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M9-M10</div>
        <div class="tl-dot"><div class="d" style="background:#c41414"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#fff0f0">
          <strong style="color:#c41414">השקת TikTok Ads</strong><br>
          ✓ Ed Hardy: תוכן וידאו אסתטיקת Y2K<br>
          ✓ שילוב TikTok Shop (אם זמין בישראל)<br>
          ✓ טירגוט Gen-Z — DNA מתאים ל-Ed Hardy<br>
          ✓ שכ"ט LGG: ₪{mgmt_fees[9]:,} (3 ערוצים)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M11-M12</div>
        <div class="tl-dot"><div class="d" style="background:#1a7a4a"></div></div>
        <div class="tl-content" style="background:#e8f5ee">
          <strong style="color:#1a7a4a">סקייל מלא + עונתיות</strong><br>
          ✓ קמפיין חנוכה (סטים Ed Hardy מתנה)<br>
          ✓ דחיפת ציוד ריצה חורפי של Umbro<br>
          ✓ חבילות חגים → AOV ₪500+<br>
          ✓ יעד M12: הכנסה {fmt(MD[12]["total_rev"])} | ריטיינר: ₪{mgmt_fees[12]:,}
        </div>
      </div>

      <h2 style="margin-top:2mm">אבני דרך — Go / No-Go</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>חודש</th><th>אבן דרך</th><th>Go אם</th><th>No-Go אם</th></tr></thead>
        <tbody>
          <tr><td>סוף M1</td><td>נתוני Pixel</td><td class="pos">50+ הוספות לעגלה</td><td class="neg">&lt;20 הוספות לעגלה</td></tr>
          <tr><td>סוף M3</td><td>ROAS ראשון</td><td class="pos">ROAS ≥1.5×</td><td class="neg">ROAS &lt;1.0×</td></tr>
          <tr><td>סוף M5</td><td>נקודת איזון 90%</td><td class="pos">הכנסה ≥ {fmt(m5_be)}</td><td class="neg">הכנסה &lt; ₪{round(m5_be*0.7):,}</td></tr>
          <tr><td>סוף M6</td><td>צמיחה</td><td class="pos">הכנסה {fmt(MD[6]["total_rev"])}</td><td class="neg">גרעון רצוף</td></tr>
          <tr><td>M7</td><td>Go Google</td><td class="pos">M6 מעל נקודת איזון</td><td class="neg">טרם הגיע לנקודת איזון</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- עמוד 9: מסגרת אי-ודאות -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">08 — מסגרת אי-ודאות</span><span class="ey">Uncertainty + Expectations Framework</span></div>
  <div class="stag">08 — UNCERTAINTY FRAMEWORK</div>
  <div class="stit">רמות ביטחון · הנחות · סיכונים ידועים</div>

  <div class="c3" style="margin-bottom:3mm">
    <div style="background:#d8f0e5;border:1px solid #aadcc0;border-radius:5px;padding:3mm;text-align:center">
      <div style="font-size:9px;font-weight:800;color:#1a7a4a;margin-bottom:1mm">HIGH — ביטחון גבוה</div>
      <div style="font-size:7.5px;color:#333">מקורות ראשוניים מוכחים<br>נתוני שוק ישראל 2024-2026<br>קבועים עסקיים</div>
    </div>
    <div style="background:#fdf3d8;border:1px solid #e8cc80;border-radius:5px;padding:3mm;text-align:center">
      <div style="font-size:9px;font-weight:800;color:#c49a2a;margin-bottom:1mm">MEDIUM — ביטחון בינוני</div>
      <div style="font-size:7.5px;color:#333">מחקר גלובלי מותאם לישראל<br>בנצ'מרקים תעשייתיים<br>הנחות מבוססות ניסיון</div>
    </div>
    <div style="background:#fde8e8;border:1px solid #f0b0b0;border-radius:5px;padding:3mm;text-align:center">
      <div style="font-size:9px;font-weight:800;color:#c41414;margin-bottom:1mm">LOW — ביטחון נמוך</div>
      <div style="font-size:7.5px;color:#333">הנחות תחזית עתידיות<br>שוק ישראל ייחודי<br>גורמים חיצוניים</div>
    </div>
  </div>

  <div class="c2">
    <div>
      <h2>מפת ביטחון KPI</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>KPI</th><th>ערך</th><th>רמה</th><th>מקור</th></tr></thead>
        <tbody>
          <tr><td>Shopify Payments — לא ב-IL</td><td>PayPlus/Cardcom</td><td><span class="cf h">HIGH</span></td><td>Shopify ישראל</td></tr>
          <tr><td>תשלומים — ציפייה תרבותית</td><td>חובה</td><td><span class="cf h">HIGH</span></td><td>מחקר ישראל</td></tr>
          <tr><td>Bit — שימוש ברכישות</td><td>53%</td><td><span class="cf h">HIGH</span></td><td>בנק ישראל 2024</td></tr>
          <tr><td>שיעור נטישת עגלה</td><td>83.5% ישראל</td><td><span class="cf h">HIGH</span></td><td>Baymard + IL</td></tr>
          <tr><td>Meta CPM ישראל</td><td>₪40-85</td><td><span class="cf m">MED</span></td><td>Meta benchmarks</td></tr>
          <tr><td>Meta CTR — אופנה IL</td><td>1.5-2.5%</td><td><span class="cf m">MED</span></td><td>Wordstream + IL</td></tr>
          <tr><td>CVR התחלה קרה</td><td>0.8-1.2%</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>CVR M6+ (בשל)</td><td>1.8-2.4%</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>CAC התחלה קרה</td><td>₪180-220</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>CAC M6+</td><td>₪100-130</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>שיעור חוזרים 90 יום</td><td>22-28%</td><td><span class="cf m">MED</span></td><td>אופנה גלובלית מותאם</td></tr>
          <tr><td>שיעור החזרות</td><td>12-18%</td><td><span class="cf m">MED</span></td><td>אופנה ישראל</td></tr>
          <tr><td>ROAS M1</td><td>1.0-1.5×</td><td><span class="cf m">MED</span></td><td>baseline התחלה</td></tr>
          <tr><td>ROAS M6</td><td>2.5-3.5×</td><td><span class="cf m">MED</span></td><td>D2C בשל IL</td></tr>
          <tr><td>ROAS M12</td><td>3.0-4.5×</td><td><span class="cf l">LOW</span></td><td>תחזית</td></tr>
          <tr><td>אורך מחזור מותג Ed Hardy</td><td>3-5 שנים</td><td><span class="cf m">MED</span></td><td>דוח מחקר</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h2>תרחישי Upside / Downside</h2>
      <div class="box gn" style="font-size:8px;margin-bottom:1.5mm">
        <strong>🟢 Upside — מה עשוי להיות טוב יותר</strong><br>
        · ROAS מהיר יותר — קריאטיב מנצח ב-M2 (קורה ~15% מהמקרים)<br>
        · עסקת קיט Umbro גדולה — מועדון עם 200+ שחקנים ב-M1<br>
        · רגע ויראלי Ed Hardy — TikTok אורגני × ממומן<br>
        · שיעור חוזרים 30%+ — מעל ציפיות<br>
        · <strong>השפעה:</strong> חציית נקודת האיזון ב-M4 במקום M5
      </div>
      <div class="box re" style="font-size:8px;margin-bottom:1.5mm">
        <strong>🔴 Downside — מה עשוי לקחת יותר זמן</strong><br>
        · שלב למידה מורחב — אלגוריתם Meta לא מתכנס ב-M1-M2<br>
        · CVR נמוך — אתר לא מותאם מספיק (תשלומים, UX)<br>
        · CPM עולה — תמחור עונתי Q4<br>
        · בעיית IP של Ed Hardy — עיכוב משפטי לפני ההשקה<br>
        · <strong>השפעה:</strong> חציית נקודת האיזון ב-M7-M8 במקום M5
      </div>
      <div class="box go" style="font-size:8px">
        <strong>⚠️ מה שלא בשליטתנו</strong><br>
        · שינויי אלגוריתם Meta / iOS<br>
        · עליית CPM בתחרות עונתית<br>
        · חקיקה ישראלית על נתוני צרכנים<br>
        · הסלמה ביטחונית — אמון צרכנים<br>
        <span class="cf l">LOW</span> כולם קיימים — מגולמים בציר הסבלנות של 5 חודשים
      </div>

      <h2 style="margin-top:2mm">מדדי הצלחה</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>מדד</th><th>M3</th><th>M6</th><th>M12</th></tr></thead>
        <tbody>
          <tr><td>ROAS בסיס</td><td class="pur">≥1.5×</td><td class="pos">≥2.8×</td><td class="pos">≥3.5×</td></tr>
          <tr><td>הכנסה (₪)</td><td class="pur">{fmt(MD[3]["total_rev"])}</td><td class="pos">{fmt(MD[6]["total_rev"])}</td><td class="pos">{fmt(MD[12]["total_rev"])}</td></tr>
          <tr><td>הזמנות/חודש</td><td class="pur">{MD[3]["total_orders"]}</td><td class="pos">{MD[6]["total_orders"]}</td><td class="pos">{MD[12]["total_orders"]}</td></tr>
          <tr><td>מעל נקודת איזון 90%</td><td class="neg">לא</td><td class="pos">כן</td><td class="pos">כן</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
""")


# ── עמודים 10-11: ההצעה + חתימה ─────────────────────────────────────────────
_offer_channel_cards = ""
for name,act,disc,rs_m1,rs_m2,fg,bg in [
    ("Meta Ads","M1",CHANNEL_DISCOUNTED,MD[1]['rs'],MD[2]['rs'],"#5b1fa8","#f0eaf9"),
    ("Google Ads","M7",CHANNEL_DISCOUNTED,MD[7]['rs'],MD[8]['rs'],"#1a3fa8","#eaeff9"),
    ("TikTok Ads","M9",CHANNEL_DISCOUNTED,MD[9]['rs'],MD[10]['rs'],"#c41414","#ffeaea"),
]:
    orig=RETAINER_PER_CHANNEL; pct=CHANNEL_DISCOUNT_PCT; saving=orig-disc
    _offer_channel_cards += f"""<div style="background:{bg};border:2px solid {fg};border-radius:6px;padding:4mm 5mm;flex:1;min-width:0">
  <div style="font-size:9px;font-weight:800;color:{fg};margin-bottom:2mm">ניהול {name}</div>
  <div style="display:flex;align-items:baseline;gap:2mm;margin-bottom:1.5mm">
    <span style="font-size:10px;color:#aaa;text-decoration:line-through">₪{orig:,}</span>
    <span style="font-size:20px;font-weight:900;color:{fg}">₪{disc:,}</span>
    <span style="background:{fg};color:#fff;border-radius:3px;padding:1px 4px;font-size:7px;font-weight:800">{pct}% OFF</span>
  </div>
  <div style="font-size:7.5px;color:#555;margin-bottom:1mm">חיסכון: <strong>₪{saving:,}/חודש</strong> | הפעלה: <strong>{act}</strong></div>
  <div style="border-top:1px solid {fg}44;padding-top:1.5mm;font-size:7px;color:#666">
    RS ({act}): <strong style="color:{fg}">₪{rs_m1:,}</strong> → חודש לאחר מכן: <strong style="color:{fg}">₪{rs_m2:,}</strong>
  </div>
</div>"""

html_parts.append(f"""
<!-- עמוד 10: ההצעה -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">09 — ההצעה</span><span class="ey">The Offer</span></div>
  <div class="stag">09 — THE OFFER</div>
  <div class="stit">מחירון שירותים + תנאי התקשרות</div>

  <div style="display:flex;gap:3mm;margin-bottom:3.5mm">
    {_offer_channel_cards}
  </div>

  <div class="c2" style="margin-bottom:3mm">
    <div>
      <h2>קריאטיב — מחיר מוסכם ליחידה</h2>
      <div style="display:flex;gap:2.5mm;margin-top:1.5mm">
        <div style="background:#fafaf7;border:1px solid #ddd;border-radius:6px;padding:3mm 4mm;flex:1">
          <div style="font-size:8.5px;font-weight:800;color:#444;margin-bottom:1.5mm">Static (פר תמונה)</div>
          <div style="display:flex;align-items:baseline;gap:2mm">
            <span style="font-size:16px;font-weight:900;color:#1a7a4a">₪{STATIC_PRICE}</span>
            <span style="background:#1a7a4a;color:#fff;border-radius:3px;padding:1px 4px;font-size:7px">מחיר מוסכם</span>
          </div>
          <div style="font-size:7px;color:#777;margin-top:1mm">טווח מוסכם: ₪115-150 | M1: 6 Static → ₪{STATIC_PRICE*6:,}</div>
        </div>
        <div style="background:#fafaf7;border:1px solid #ddd;border-radius:6px;padding:3mm 4mm;flex:1">
          <div style="font-size:8.5px;font-weight:800;color:#444;margin-bottom:1.5mm">וידאו (פר וידאו)</div>
          <div style="display:flex;align-items:baseline;gap:2mm">
            <span style="font-size:9px;color:#aaa;text-decoration:line-through">₪2,200</span>
            <span style="font-size:16px;font-weight:900;color:#333">₪{VIDEO_PRICE:,}</span>
            <span style="background:#333;color:#fff;border-radius:3px;padding:1px 4px;font-size:7px">20% OFF</span>
          </div>
          <div style="font-size:7px;color:#777;margin-top:1mm">M2: וידאו ראשון → ₪{VIDEO_PRICE:,}</div>
        </div>
      </div>
      <div class="box go" style="margin-top:2mm;font-size:8px">
        <strong>הערה לגבי עלות וידאו:</strong> עלות הוידאו עשויה לעלות בהתאם למורכבות ההפקה — before/after, אנימציה, בימוי, עריכה ופוסט-פרודקשן מגדילים את היקף העבודה.<br>
        <strong>כל עלייה בעלות הוידאו תיספג על-ידי Los Gardios Group כחלק מההסכם — הלקוח מוגן.</strong>
      </div>
      <div style="margin-top:1.5mm;font-size:8px;color:var(--im)">
        M1: 6 Static (₪{STATIC_PRICE*6:,}) = <strong>₪{STATIC_PRICE*6:,}</strong> — כלול בתקציב ₪20K<br>
        M6: 10 Static (₪{STATIC_PRICE*10:,}) + 2 וידאו (₪{VIDEO_PRICE*2:,}) = <strong>₪{STATIC_PRICE*10+VIDEO_PRICE*2:,}</strong>
      </div>
    </div>
    <div>
      <h2>מה כלול בריטיינר ₪{CHANNEL_DISCOUNTED:,}/ערוץ</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin-top:1.5mm">
        <div style="background:var(--gp);border:1.5px solid var(--gm);border-right:4px solid var(--g);border-radius:4px;padding:2.5mm">
          <div style="font-size:8px;font-weight:800;color:var(--g);margin-bottom:1mm">✓ כלול</div>
          <ul style="font-size:8px;padding-right:3mm;line-height:1.7">
            <li>ניהול קמפיינים יומי</li>
            <li>אסטרטגיה + A/B testing</li>
            <li>CRO + אופטימיזציה</li>
            <li>דוח שבועי ב-Drive</li>
            <li>Klaviyo Flows</li>
            <li>ייעוץ Shopify</li>
          </ul>
        </div>
        <div style="background:var(--rp);border:1.5px solid #f0b0b0;border-right:4px solid var(--r);border-radius:4px;padding:2.5mm">
          <div style="font-size:8px;font-weight:800;color:var(--r);margin-bottom:1mm">✗ לא כלול</div>
          <ul style="font-size:8px;padding-right:3mm;line-height:1.7">
            <li>תקציב מדיה</li>
            <li>קריאטיב (פר יחידה)</li>
            <li>Shopify + Klaviyo + Fast Simon</li>
            <li>Google / TikTok (M7/M9)</li>
            <li>PayPlus עמלות (2-3%)</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="c2">
    <div>
      <h2>סיכום השקעה חודשי + הכנסה</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>חודש</th><th>ערוצים</th><th>LGG</th><th>מדיה</th><th>קריאטיב</th><th>השקעה</th><th>הכנסה</th><th>נ.א.?</th></tr></thead>
        <tbody>{_inv_rows}</tbody>
        <tfoot><tr>
          <td colspan="5">סה"כ שנה ראשונה</td>
          <td>{fmt(sum(MD[m]["total_invest"] for m in range(13)))}</td>
          <td>{fmt(sum(MD[m]["total_rev"] for m in range(13)))}</td>
          <td>—</td>
        </tr></tfoot>
      </table>
    </div>
    <div>
      <h2>תנאי RS ודוגמאות</h2>
      <div class="box gn" style="margin-top:1mm;font-size:8px">
        <strong>RS 8% — על הכנסות ברוטו, מחוץ ל-₪20K:</strong><br>
        · מ-M1, על כל הכנסה גולמית (גם בחודשים לפני האיזון)<br>
        · גדל עם ההצלחה — אינטרס משותף<br>
        · M1: ₪{MD[1]["rs"]:,} | M6: ₪{MD[6]["rs"]:,} | M12: ₪{MD[12]["rs"]:,}
      </div>
      <div class="box go" style="margin-top:1.5mm;font-size:8px">
        <strong>תנאי ריטיינר:</strong><br>
        · ₪{CHANNEL_DISCOUNTED:,}/ערוץ ({CHANNEL_DISCOUNT_PCT}% הנחה מ-₪{RETAINER_PER_CHANNEL:,})<br>
        · חוזה 6 חודשים + חידוש עם הודעה 30 יום<br>
        · ציר סבלנות: 5 חודשים<br>
        · חריגה מ-₪20K — מותרת רק כשהפרויקט מעל נקודת האיזון
      </div>
      <div class="box" style="margin-top:1.5mm;font-size:7.5px">
        <strong>נקודת האיזון — 90% מרווח גולמי:</strong><br>
        הכנסה מינימום = (LGG + מדיה + קריאטיב + Ext + הוצ׳) ÷ 0.82<br>
        הלקוח מחשב את הרווח הנקי לפי מרווח הגולמי האמיתי שלו.
      </div>
    </div>
  </div>
</div>

<!-- עמוד 11: חתימה -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">10 — אישור והתחייבות</span><span class="ey">Agreement &amp; Signature</span></div>
  <div class="stag">10 — AGREEMENT</div>
  <div class="stit">אישור הצעה — חתימה</div>
  <div class="c2">
    <div>
      <div class="box dk" style="margin-bottom:3mm;font-size:8.5px">
        <strong>תנאים מרכזיים שאושרו:</strong><br><br>
        ✓ תקציב חודשי: <strong>₪20,000 כולל LGG + מדיה + קריאטיב</strong><br>
        ✓ RS: <strong>8% מהכנסות ברוטו</strong> — מחוץ לתקציב, מ-M1<br>
        ✓ ציר סבלנות: <strong>5 חודשים</strong><br>
        ✓ ריטיינר: <strong>₪{CHANNEL_DISCOUNTED:,}/ערוץ/חודש</strong> ({CHANNEL_DISCOUNT_PCT}% הנחה)<br>
        ✓ Static: <strong>₪{STATIC_PRICE} (מחיר מוסכם, טווח ₪115-150)</strong><br>
        ✓ וידאו: <strong>₪{VIDEO_PRICE:,} — כל עלייה נספגת על-ידי LGG</strong><br>
        ✓ מרווח גולמי Intermax: <strong>~90%</strong> — הלקוח מחשב רווח נקי<br>
        ✓ Ed Hardy IP — <strong>חובה לאמת Hardy Way LLC לפני השקה</strong><br>
        ✓ 3 חנויות: Ed Hardy Israel, Umbro Israel, Intermax Hub
      </div>
      <h2>חתימת Los Gardios Group</h2>
      <div style="margin-top:4mm;font-size:9px;line-height:2.5">
        <strong>נציג LGG:</strong> ________________________________<br>
        <strong>תפקיד:</strong> ________________________________<br>
        <strong>חתימה:</strong> ________________________________<br>
        <strong>תאריך:</strong> ________________________________
      </div>
    </div>
    <div>
      <h2>חתימת Intermax Group</h2>
      <div style="display:flex;flex-direction:column;gap:2.5mm;margin-top:1.5mm">
        {''.join([
          f'<div style="border:1px solid #ddd;border-radius:4px;padding:3mm">'
          f'<strong style="font-size:8.5px">{store}</strong><br>'
          f'<div style="font-size:8px;margin-top:1.5mm;line-height:2">שם: ___________________<br>חתימה: ___________________<br>תאריך: ___________________</div>'
          f'</div>'
          for store in ["Ed Hardy Israel","Umbro Israel","Intermax Group Hub"]
        ])}
      </div>
      <div style="margin-top:3mm;font-size:7.5px;color:var(--im)">
        קראתי והבנתי את תנאי ההתקשרות כמפורט במסמך זה. אני מאשר/ת את מבנה ה-RS, הריטיינרים, ציר הסבלנות, מחירי הקריאטיב המוסכמים, ואת כל התנאים הפיננסיים.
      </div>
    </div>
  </div>
  <div style="margin-top:5mm;text-align:center;font-size:7px;color:var(--im);border-top:1px solid var(--rule);padding-top:2mm">
    © 2026 Los Gardios Group | ח.פ. 516819257 | losgardios.com | LGG-IMX-2026-001 | v16 | מסמך סודי — לא להפצה
  </div>
</div>

</body>
</html>""")

# ── כתיבת HTML + יצירת PDF ────────────────────────────────────────────────────
html = "".join(html_parts)
html_path = f"{S}/intermax-lgg-proposal-v16.html"
pdf_path  = f"{S}/intermax-lgg-proposal-v16.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML נכתב: {html_path} ({len(html)//1024}KB)")

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
        args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']
    )
    page = browser.new_page()
    page.goto(f"file://{html_path}", wait_until='networkidle', timeout=30000)
    page.wait_for_timeout(2000)
    page.pdf(
        path=pdf_path,
        format='A4',
        landscape=True,
        print_background=True,
        margin={'top':'0','bottom':'0','left':'0','right':'0'}
    )
    browser.close()

size = os.path.getsize(pdf_path)
print(f"PDF נוצר: {pdf_path} ({size//1024}KB)")
