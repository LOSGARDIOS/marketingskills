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

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
AOV           = 380
COGS_PCT      = 0.38
VAR_PCT       = 0.04
FIXED_PER_ORD = 8
FIXED_OPS     = 1200
CM_PER_ORDER  = round(AOV * (1 - COGS_PCT - VAR_PCT) - FIXED_PER_ORD, 1)  # 212.4
BE_ROAS       = round(AOV / CM_PER_ORDER, 2)  # 1.79
EXT_MONTHLY   = 715
RETAINER_PER_CHANNEL = 10000
CHANNEL_DISCOUNT_PCT = 20
CHANNEL_DISCOUNTED   = int(RETAINER_PER_CHANNEL * (1 - CHANNEL_DISCOUNT_PCT / 100))  # 8000

STATIC_PRICE = round(550 * 0.8)   # 440
VIDEO_PRICE  = round(2200 * 0.8)  # 1760

mgmt_fees = {
    0:20000,
    1:8000,2:8000,3:8000,4:8000,5:8000,6:8000,
    7:16000,8:16000,
    9:24000,10:24000,11:24000,12:24000,
}

# ── MEDIA & REVENUE DATA  (phase, ads, roas, _, nc, rc, rrev, rev, rs, _) ────
B = {
    0:("הקמה",0,None,20000,0,0,0,0,0,-20000),
    1:("קריאטיב",5000,1.2,13000,16,0,0,6000,480,-9280),
    2:("השקה",12000,1.6,20000,51,2,760,19960,1597,-7625),
    3:("צמיחה",14400,2.3,20000,87,10,3800,36920,2954,2890),
    4:("סקייל",17280,2.8,20000,127,23,8740,57124,4570,15417),
    5:("בשלות",20736,3.2,20000,175,42,15960,82315,6585,31035),
    6:("מיטוב",24883,3.5,20000,229,68,25840,112931,9034,50017),
}
B_ext = {
    7:("גוגל",29860,3.3,22000,259,103,39140,137678,11014,63360),
    8:("גוגל+",35832,3.1,25000,292,141,53580,164660,13173,77089),
    9:("TikTok",42998,3.2,26000,362,185,70300,207900,16632,102898),
    10:("TikTok+",51598,3.0,29000,407,240,91200,246000,19680,123520),
    11:("Scale",61918,3.3,30000,538,301,114380,318700,25496,167594),
    12:("Max",74302,3.5,31000,684,381,144780,404840,32387,220001),
}
# Conservative & Aggressive scenario data (same format as B)
C = {
    0:("הקמה",0,None,20000,0,0,0,0,0,-20000),
    1:("קריאטיב",5000,0.8,13000,11,0,0,4000,320,-10520),
    2:("השקה",12000,1.2,20000,38,1,380,14780,1182,-10895),
    3:("צמיחה",13200,1.6,20000,56,6,2280,23380,1870,-5425),
    4:("סקייל",14520,2.0,20000,76,13,4940,33920,2714,3296),
    5:("בשלות",15972,2.4,20000,101,22,8360,46700,3736,11218),
    6:("מיטוב",17569,2.8,20000,129,33,12540,61737,4939,23277),
}
A = {
    0:("הקמה",0,None,20000,0,0,0,0,0,-20000),
    1:("קריאטיב",5000,1.5,13000,20,0,0,7500,600,-8650),
    2:("השקה",12000,2.2,20000,70,4,1520,28000,2240,-4640),
    3:("צמיחה",15000,3.5,20000,138,18,6840,59040,4723,16565),
    4:("סקייל",18750,4.5,20000,222,45,17100,101250,8100,44775),
    5:("בשלות",23438,5.5,20000,340,81,30780,159530,12762,78906),
    6:("מיטוב",29297,6.5,20000,502,148,56240,247075,19766,133227),
}

# ── CREATIVE PLAN (v15 — DISCOUNTED prices: ₪440 static, ₪1,760 video) ───────
creative_plan = {
    # m: (n_static, n_video, total_cost)
    1:(4,1,STATIC_PRICE*4+VIDEO_PRICE*1),    # 1760+1760=3520
    2:(5,2,STATIC_PRICE*5+VIDEO_PRICE*2),    # 2200+3520=5720
    3:(6,2,STATIC_PRICE*6+VIDEO_PRICE*2),    # 2640+3520=6160
    4:(8,3,STATIC_PRICE*8+VIDEO_PRICE*3),    # 3520+5280=8800
    5:(8,3,STATIC_PRICE*8+VIDEO_PRICE*3),    # 8800
    6:(10,4,STATIC_PRICE*10+VIDEO_PRICE*4),  # 4400+7040=11440
    7:(10,4,STATIC_PRICE*10+VIDEO_PRICE*4),  # 11440
    8:(12,4,STATIC_PRICE*12+VIDEO_PRICE*4),  # 5280+7040=12320
    9:(12,5,STATIC_PRICE*12+VIDEO_PRICE*5),  # 5280+8800=14080
    10:(12,5,STATIC_PRICE*12+VIDEO_PRICE*5), # 14080
    11:(14,6,STATIC_PRICE*14+VIDEO_PRICE*6), # 6160+10560=16720
    12:(14,6,STATIC_PRICE*14+VIDEO_PRICE*6), # 16720
}

CPM_M = {1:65,2:65,3:55,4:55,5:50,6:50,7:48,8:48,9:52,10:50,11:48,12:45}
CTR_M = {1:.020,2:.025,3:.025,4:.030,5:.030,6:.030,7:.030,8:.030,9:.028,10:.030,11:.032,12:.035}

# ── COMPUTE MONTHS (v15 FIXED net formula) ────────────────────────────────────
def compute_month(m):
    if m == 0:
        ti = 20000 + EXT_MONTHLY
        return {'phase':'הקמה','ad_spend':0,'cpm':None,'reach':0,'ctr':None,'visitors':0,
                'cvr':None,'nc':0,'rc':0,'total_orders':0,'ad_rev':0,'rrev':0,'total_rev':0,
                'roas':None,'cm_per':CM_PER_ORDER,'cm_total':0,
                'lgg_fee':20000,'media':0,'creative':0,'ext':EXT_MONTHLY,
                'total_invest':ti,'rs':0,'net':-(ti+FIXED_OPS)}
    d = B[m] if m <= 6 else B_ext[m]
    ph,ads,roas,_,nc,rc,rrev,rev,rs,_ = d
    cr = creative_plan[m][2] if m in creative_plan else 0
    cpm = CPM_M.get(m); ctr = CTR_M.get(m)
    reach = round(ads/cpm*1000) if cpm and ads>0 else 0
    visitors = round(reach*ctr) if ctr and reach>0 else 0
    cvr = round(nc/visitors*100,1) if visitors>0 else 0
    tot_ord = nc+rc
    cm_total = round(tot_ord*CM_PER_ORDER)
    lgg = mgmt_fees[m]
    # v15 FIX: total_invest includes media + creative + ext
    total_invest = lgg + ads + cr + EXT_MONTHLY
    # v15 FIX: net deducts total_invest + FIXED_OPS + rs
    net = cm_total - total_invest - FIXED_OPS - rs
    return {'phase':ph,'ad_spend':ads,'cpm':cpm,'reach':reach,'ctr':ctr,
            'visitors':visitors,'cvr':cvr,'nc':nc,'rc':rc,'total_orders':tot_ord,
            'ad_rev':nc*AOV,'rrev':rrev,'total_rev':rev,'roas':roas,
            'cm_per':CM_PER_ORDER,'cm_total':cm_total,
            'lgg_fee':lgg,'media':ads,'creative':cr,'ext':EXT_MONTHLY,
            'total_invest':round(total_invest),'rs':rs,'net':round(net)}

MD = {m: compute_month(m) for m in range(13)}

# ── SCENARIO TABLE (v15 FIXED — also deducts media + creative) ───────────────
def scenario_rows():
    labels = {1:"M1",2:"M2",3:"M3",4:"M4",5:"M5",6:"M6"}
    rows = ""
    for m in range(1,7):
        lgg = mgmt_fees[m]
        ads = B[m][1]  # same media budget for all scenarios
        cr  = creative_plan[m][2]
        _,_,_,_,cnc,crc,_,crev,crs,_ = C[m]
        _,_,_,_,bnc,brc,_,brev,brs,_ = B[m]
        _,_,_,_,anc,arc,_,arev,ars,_ = A[m]
        # v15 FIX: include ads + cr + EXT in cost base
        base_cost = lgg + ads + cr + EXT_MONTHLY + FIXED_OPS
        cnet = round((cnc+crc)*CM_PER_ORDER - base_cost - crs)
        bnet = round((bnc+brc)*CM_PER_ORDER - base_cost - brs)
        anet = round((anc+arc)*CM_PER_ORDER - base_cost - ars)
        cn = "color:#c41414;font-weight:700" if cnet<0 else "color:#1a7a4a;font-weight:700"
        bn = "color:#c41414;font-weight:700" if bnet<0 else "color:#1a7a4a;font-weight:700"
        hl = ' style="background:#f0eaf9"' if (bnet>0 and m>=4) else (' style="background:#e8f5ee"' if (bnet>0) else "")
        rows += f'<tr{hl}><td>{labels[m]}</td>'
        rows += f'<td>{fmt(crev)}</td><td style="{cn}">{fmt(cnet,True)}</td>'
        rows += f'<td style="background:#f0f0f0;width:2mm"></td>'
        rows += f'<td>{fmt(brev)}</td><td style="{bn}">{fmt(bnet,True)}</td>'
        rows += f'<td style="background:#f0f0f0;width:2mm"></td>'
        rows += f'<td>{fmt(arev)}</td><td style="color:#1a7a4a;font-weight:700">{fmt(anet,True)}</td>'
        rows += f'</tr>'

    def st_total(d):
        return sum(round((d[m][4]+d[m][5])*CM_PER_ORDER
                         - mgmt_fees[m] - B[m][1] - creative_plan[m][2] - EXT_MONTHLY
                         - FIXED_OPS - d[m][8])
                   for m in range(1,7))
    cr2=st_total(C); br2=st_total(B); ar2=st_total(A)
    cr2c="color:#aadcc0" if cr2>0 else "color:#f0b0b0"
    br2c="color:#aadcc0" if br2>0 else "color:#f0b0b0"
    rows += f'<tr style="background:#1a1a2e;color:#fff;font-weight:800"><td>H1 סה"כ</td>'
    rows += f'<td>{fmt(sum(C[m][7] for m in range(1,7)))}</td><td style="{cr2c}">{fmt(cr2,True)}</td>'
    rows += f'<td style="background:#333"></td>'
    rows += f'<td>{fmt(sum(B[m][7] for m in range(1,7)))}</td><td style="{br2c}">{fmt(br2,True)}</td>'
    rows += f'<td style="background:#333"></td>'
    rows += f'<td>{fmt(sum(A[m][7] for m in range(1,7)))}</td><td style="color:#aadcc0">{fmt(ar2,True)}</td></tr>'
    return rows

sc_rows = scenario_rows()

# ── DRIVE TABLE (months=rows, KPIs=columns) ───────────────────────────────────
def drive_table_transposed():
    D = MD
    CAM=("#ede7f9","#5b1fa8"); CON=("#dce6f7","#1a3fa8"); REV=("#d8f0e5","#1a7a4a")
    MAR=("#fdf3d8","#7a5a10"); EXP=("#fde8e8","#8b1a1a"); RS_=("#ede7f9","#5b1fa8")
    NET=("#e6e6f0","#1a1a2e")
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
        ("CM כולל",MAR,lambda m:fmt(D[m]['cm_total']) if D[m]['cm_total']>0 else "—"),
        ("LGG שכ׳׳ט",EXP,lambda m:fmt(D[m]['lgg_fee'])),
        ("קריאטיב",EXP,lambda m:fmt(D[m]['creative']) if D[m]['creative']>0 else "—"),
        ("הוצ׳ נוספות",EXP,lambda m:fmt(D[m]['ext'])),
        ("סה׳׳כ השקעה",EXP,lambda m:fmt(D[m]['total_invest'])),
        ("RS 8%",RS_,lambda m:fmt(D[m]['rs']) if D[m]['rs']>0 else "—"),
        ("נטו ★",NET,lambda m:fmt(D[m]['net'],plus=True) if D[m]['net']!=0 else "—"),
    ]
    sec1 = '<th colspan="2" style="background:#1a1a2e;color:#fff;font-size:6px;padding:1mm 0.5mm;text-align:center">חודש / KPI</th>'
    for label,span,token in [("קמפיין",5,CAM),("המרה",4,CON),("הכנסות",4,REV),("מרז׳ין",1,MAR),("הוצאות",4,EXP),("RS",1,RS_),("נטו",1,NET)]:
        sec1 += f'<th colspan="{span}" style="background:{token[0]};color:{token[1]};font-size:6.5px;font-weight:800;text-align:center;padding:1mm">{label}</th>'
    sec2 = '<th style="background:#1a1a2e;color:#fff;font-size:6px;padding:0.8mm;width:9mm">חודש</th>'
    sec2 += '<th style="background:#1a1a2e;color:#fff;font-size:6px;padding:0.8mm;width:13mm">שלב</th>'
    for lbl,token,_ in cols:
        sec2 += f'<th style="background:{token[0]};color:{token[1]};font-size:5.5px;padding:0.7mm 0.4mm;text-align:center;white-space:nowrap;width:12mm">{lbl}</th>'
    rows_html = ""
    for m in range(13):
        net=D[m]['net']; invest=D[m]['total_invest']
        profitable=net>0; over_budget=invest>20000
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
            elif lbl in("הכנ׳ מד׳","הכנ׳ חז׳","הכנסה כוללת","CM כולל"): vc="color:#1a7a4a;font-weight:700" if v!="—" else "color:#ccc"
            elif lbl=="ROAS": vc="color:#7a5a10;font-weight:700" if v!="—" else "color:#ccc"
            elif lbl=="RS 8%": vc="color:#5b1fa8;font-weight:700" if v!="—" else "color:#ccc"
            elif lbl=="נטו ★": vc="color:#1a7a4a;font-weight:900" if net>0 else("color:#c41414;font-weight:900" if net<0 else "color:#888")
            else: vc="color:#444"
            data_cells += f'<td style="font-size:6.5px;{vc};padding:0.7mm 0.4mm;text-align:center;white-space:nowrap">{v}</td>'
        rows_html += f'<tr style="{rbg};border-bottom:1px solid #eee">{m_cell}{phase_cell}{data_cells}</tr>'
    tots={k:sum(D[m][k] for m in range(13)) for k in ['ad_spend','total_rev','cm_total','lgg_fee','creative','ext','total_invest','rs','net']}
    net_total=tots['net']; nc_="color:#aadcc0" if net_total>0 else "color:#f0b0b0"
    ft=f'<td colspan="2" style="background:#1a1a2e;color:#fff;font-size:6.5px;font-weight:800;padding:1mm">סיכום M0-M12</td>'
    ft+=f'<td style="background:#1a1a2e;color:#e0d0f5;font-size:6px">{fmt(tots["ad_spend"])}</td>'
    ft+=f'<td colspan="4" style="background:#1a1a2e;color:#555;font-size:6px;text-align:center">—</td>'
    ft+=f'<td colspan="3" style="background:#1a1a2e;color:#555;font-size:6px;text-align:center">—</td>'
    ft+=f'<td colspan="2" style="background:#1a1a2e;color:#555">—</td>'
    ft+=f'<td style="background:#1a1a2e;color:#aadcc0;font-weight:800;font-size:6.5px">{fmt(tots["total_rev"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#555">—</td>'
    ft+=f'<td style="background:#1a1a2e;color:#e8cc80;font-weight:800;font-size:6.5px">{fmt(tots["cm_total"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-size:6px">{fmt(tots["lgg_fee"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-size:6px">{fmt(tots["creative"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-size:6px">{fmt(tots["ext"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#f0b0b0;font-weight:800;font-size:6.5px">{fmt(tots["total_invest"])}</td>'
    ft+=f'<td style="background:#1a1a2e;color:#d6c6f0;font-weight:800;font-size:6.5px">{fmt(tots["rs"])}</td>'
    ft+=f'<td style="background:#1a1a2e;{nc_};font-weight:900;font-size:6.5px">{fmt(net_total,True)}</td>'
    note=(f'BE.ROAS {BE_ROAS}× | CM ₪{CM_PER_ORDER}/הז׳ | קריאטיב בתוך תקציב ₪20K | '
          f'RS 8% מחוץ ל-₪20K | חריגה מ-₪20K — מותרת רק עם נטו חיובי | 🟢=רווחי | 🔴=גרעון')
    return f"""<div style="overflow-x:hidden">
<table style="width:263mm;border-collapse:collapse;font-variant-numeric:tabular-nums;direction:rtl;font-family:inherit;table-layout:fixed">
  <colgroup><col style="width:9mm"><col style="width:13mm">{"".join(['<col style="width:12mm">']*20)}</colgroup>
  <thead>
    <tr style="border-bottom:1px solid #ddd">{sec1}</tr>
    <tr style="border-bottom:2px solid #ccc">{sec2}</tr>
  </thead>
  <tbody>{rows_html}</tbody>
  <tfoot><tr>{ft}</tr></tfoot>
</table></div>
<div style="margin-top:1.5mm;font-size:5.8px;color:#888;border-top:1px solid #eee;padding-top:1mm">{note}</div>"""

drive_tbl = drive_table_transposed()

# ── HTML START (CSS + Pages 1-3) ──────────────────────────────────────────────
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

<!-- PAGE 1: COVER -->
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
      <div><label>BE ROAS</label><span>{BE_ROAS}×</span></div>
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
    <span>LGG-IMX-2026 | v15 | מסמך סודי</span>
  </div>
</div>

<!-- PAGE 2: OVERALL STRATEGY -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">01 — אסטרטגיה עסקית</span><span class="ey">Business Strategy</span></div>
  <div class="stag">01 — BUSINESS STRATEGY</div>
  <div class="stit">הזדמנות השוק — ישראל D2C ביגוד ואופנה</div>
  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi gn"><div class="kl">שוק אופנה ישראל</div><div class="kv sm">₪6.3B</div><div class="ks"><span class="cf h">HIGH</span> 3.4% YoY · 18M שופרים</div></div>
    <div class="kpi go"><div class="kl">AOV ישראלי D2C</div><div class="kv sm">$190</div><div class="ks"><span class="cf h">HIGH</span> מהגבוה בעולם — ₪380 ספורט</div></div>
    <div class="kpi bl"><div class="kl">פאדל — מגרשים</div><div class="kv sm">130+</div><div class="ks"><span class="cf m">MED</span> 36 בבנייה · חלון כניסה</div></div>
  </div>
  <div class="c2">
    <div>
      <h2>ניתוח תחרות — פערים בשוק</h2>
      <table style="margin-top:1.5mm;font-size:8px">
        <thead><tr><th>קטגוריה</th><th>מה יש היום</th><th>ההזדמנות</th></tr></thead>
        <tbody>
          <tr><td>Tattoo Streetwear D2C</td><td>ייבוא אפור, ASOS</td><td class="pos"><strong>D2C ישראלי, עברית, ₪250-500</strong></td></tr>
          <tr><td>ביגוד פאדל ייעודי</td><td>חנויות ספורט כלליות</td><td class="pos"><strong>מותג פאדל ישראלי ראשון</strong></td></tr>
          <tr><td>קיטים מועדוני חובבים</td><td>B2B offline בלבד</td><td class="pos"><strong>D2C + B2B אותה חנות</strong></td></tr>
          <tr><td>פלטפורמת D2C מאוחדת</td><td>Zara, ASOS מחו"ל</td><td class="pos"><strong>Hub ישראלי רב-מותגי</strong></td></tr>
        </tbody>
      </table>
      <div class="box gn" style="margin-top:2mm;font-size:8px">
        <span class="cf h">HIGH</span> <strong>ממצא מרכזי:</strong> אין D2C ישראלי שמחזיק tattoo streetwear ₪200-400. פער מובנה. שוק ריצה הכי מהיר בישראל — ורק Umbro עם ה-DNA הנכון.
      </div>
      <h2 style="margin-top:2mm">מדוע עכשיו?</h2>
      <ul style="font-size:8.5px">
        <li><strong>iOS 17 Privacy:</strong> מי שיש לו Pixel + Data ינצח. להיכנס עכשיו = יתרון מצטבר</li>
        <li><strong>CPC עולה:</strong> כל שנה יקר יותר — כניסה ראשונה = חיסכון לעתיד</li>
        <li><strong>Shopify IL:</strong> Bit + עברית + Klaviyo RTL = תשתית מלאה</li>
      </ul>
    </div>
    <div>
      <h2>ארכיטקטורת 3 חנויות</h2>
      <div style="display:grid;gap:2mm;margin-top:1.5mm">
        <div class="box" style="font-size:8px">
          <strong style="color:var(--p)">Ed Hardy Israel</strong> — tattoo-flash, post-army 18-28, Tel Aviv/Center<br>
          AOV ₪387 | ROAS M6: 3.5× | פתיחה: M1 | <span class="cf h">HIGH</span> Y2K revival פעיל
        </div>
        <div class="box bl" style="font-size:8px">
          <strong style="color:var(--b)">Umbro Israel</strong> — sports authority, running + padel + football, 25-45<br>
          AOV ₪380 | B2B kit deals | <span class="cf m">MED</span> 130+ padel courts active
        </div>
        <div class="box go" style="font-size:8px">
          <strong style="color:var(--au)">Intermax Hub</strong> — nine72.com / intermax.co.il · cross-brand<br>
          Fast Simon AI · Loyalty cross-brand · Ed Hardy buyer → Umbro upsell
        </div>
      </div>
      <div class="box re" style="margin-top:2mm;font-size:8px">
        <span class="cf l">RISK</span> <strong>מתחילים מאפס D2C.</strong> אין היסטוריית Pixel, אין Email list, אין ROAS benchmark ישראלי קיים. M1-M3 הם learning phase — ציר סבלנות 5 חודשים חיוני.
      </div>
      <h2 style="margin-top:2mm">תשתית טכנולוגית</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm">
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>PayPlus / Cardcom</strong><br>Shopify Payments לא ב-IL<br><span class="cf h">HIGH</span> Bit + tashlumim</div>
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>Fast Simon</strong><br>AI Search + Filter + UX<br><span class="cf m">MED</span> CVR boost 15-25%</div>
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>Klaviyo</strong><br>Email + SMS → Abandon Cart<br><span class="cf h">HIGH</span> 83.5% cart abandon IL</div>
        <div style="font-size:8px;background:#f5f5f5;padding:2mm;border-radius:3px"><strong>Yotpo / Loox</strong><br>Reviews + UGC מ-M2<br><span class="cf m">MED</span> Social proof = CVR</div>
      </div>
    </div>
  </div>
</div>
""")

# ── PAGES 3-5: BRAND STRATEGY PAGES ──────────────────────────────────────────
html_parts.append(f"""
<!-- PAGE 3: ED HARDY BRAND STRATEGY -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a0033,#5b1fa8)"><img src="{chrome_uri}" alt=""><span class="wm">02 — Ed Hardy Israel — אסטרטגיית מותג</span><span class="ey">Brand Strategy</span></div>
  <div class="stag" style="color:#5b1fa8">02 — ED HARDY ISRAEL — BRAND STRATEGY</div>
  <div class="stit">Y2K Revival · Tattoo-Flash Art · Tel Aviv Nightlife Culture</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi"><div class="kl">שיא המותג</div><div class="kv sm">$700M</div><div class="ks"><span class="cf h">HIGH</span> 2004-2009 · נמכר ₪62M (91% צניחה)</div></div>
    <div class="kpi go"><div class="kl">Y2K Revival — TikTok</div><div class="kv sm">פעיל</div><div class="ks"><span class="cf h">HIGH</span> Gen-Z tattoo aesthetic 2024-2026</div></div>
    <div class="kpi gn"><div class="kl">AOV יעד</div><div class="kv sm">₪387</div><div class="ks"><span class="cf m">MED</span> → Bundle ₪500+ M4+</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>ניתוח היסטורי — לקחים לישראל</h2>
      <div class="box dk" style="font-size:8px;margin-bottom:2mm">
        <strong>Timeline:</strong> שיא עולמי 2004-2008 → ישראל בפיגור 6-12 חודש → חנות ת"א נפתחה 2007 (California Apparel News) → סגרה ~2011 עם קריסת ה-wholesale<br>
        <strong>3 סיבות קריסה:</strong> 70 sub-licensees (over-licensing) · Gosselin celebrity contagion · Mass distribution ב-Macy's<br>
        <strong>לקח ישראל:</strong> שוק מרוכז = סטורציה מהירה. מחזור מותג 3-5 שנים מקסימום.
      </div>

      <h2>פוזישנינג — 2026</h2>
      <div class="box" style="font-size:8.5px">
        <strong>Premium Tattoo Streetwear · Not Nostalgia — Revival</strong><br>
        לא מוכרים את העבר — מוכרים אסתטיקת tattoo-flash contemporarית שחוזרת עם Z Generation. Ed Hardy = ה-vehicle, לא ה-story.
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin-top:2mm">
        <div style="background:#1a0033;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#d6c6f0;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">קהל יעד ראשוני</div>
          <div style="color:#fff;font-size:8.5px">גיל 18-28, ת"א + גוש דן<br>Post-Army, Nightlife<br>Tattoo Culture, Music</div>
        </div>
        <div style="background:#2a0055;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#d6c6f0;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">מחיר יעד</div>
          <div style="color:#fff;font-size:8.5px">חולצה: ₪250-320<br>קפוצ'ון: ₪380-480<br>Bundle: ₪500+</div>
        </div>
      </div>

      <h2 style="margin-top:2mm">ערוצי הפצה — D2C First</h2>
      <ul style="font-size:8.5px">
        <li><strong>Shopify EDH.co.il</strong> — ראשוני, מותאם RTL, Bit + tashlumim</li>
        <li><strong>Instagram + TikTok Organic</strong> — Tattoo artist collaborations</li>
        <li><strong>WhatsApp VIP Drops</strong> — Limited drops → FOMO + urgency</li>
        <li><strong>Klaviyo Welcome Series</strong> — 5 emails brand story + tattoo culture</li>
      </ul>
    </div>
    <div>
      <h2>אסטרטגיית קריאטיב Ed Hardy</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>שלב</th><th>סוג</th><th>Content Direction</th></tr></thead>
        <tbody>
          <tr><td>M1 Seed</td><td>4 Static</td><td>Tattoo flash close-ups, Model + בקבוק, Night aesthetic</td></tr>
          <tr><td>M2 Launch</td><td>3S + 1V</td><td>Behind-the-scenes tattoo, Lifestyle Tel Aviv</td></tr>
          <tr><td>M3+</td><td>UGC first</td><td>לקוחות אמיתיים = social proof העיקרי</td></tr>
        </tbody>
      </table>

      <h2 style="margin-top:2mm">קמפיין Meta — Ed Hardy Specifics</h2>
      <div class="box bl" style="font-size:8px">
        <strong>Targeting:</strong> 18-28, IL · Interests: Tattoo Art, Streetwear, Music Festivals, Alternative Fashion<br>
        <strong>Exclude:</strong> 35+ · Family-oriented audiences · כדורגל without streetwear<br>
        <span class="cf m">MED</span> CTR baseline 1.5-2.5% · CVR cold start 0.8-1.2%
      </div>

      <div class="box re" style="margin-top:2mm;font-size:8px">
        <span class="cf l">RISK</span> <strong>IP — חובה לבדוק לפני השקה!</strong><br>
        IP מוחזק ע"י <strong>Hardy Way LLC / Iconix Brand Group</strong> (לא ABG כפי שמדווח לעיתים קרובות שגוי). Intermax חייב לאמת שהסכם הרישיון מכסה D2C ישראל לפני פרסום כלשהו.
      </div>

      <div class="box go" style="margin-top:2mm;font-size:8.5px">
        <strong>הזדמנות Y2K 2026:</strong> TikTok "Bring Back Ed Hardy" trend פעיל. Pinterest searches +340% YoY. Gen-Z לא חוו את שלב ה-oversaturation — הם רואים את זה כ-vintage authentic.
        <span class="cf h">HIGH</span>
      </div>

      <h2 style="margin-top:2mm">KPIs — Ed Hardy (בנצ'מרק)</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5mm">
        <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center;font-size:8px"><strong>CVR M1</strong><br><span style="color:#5b1fa8;font-weight:800">0.8-1.2%</span><br><span class="cf m">MED</span></div>
        <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center;font-size:8px"><strong>CVR M6+</strong><br><span style="color:#1a7a4a;font-weight:800">1.8-2.4%</span><br><span class="cf m">MED</span></div>
        <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center;font-size:8px"><strong>Repeat 90d</strong><br><span style="color:#c49a2a;font-weight:800">22%</span><br><span class="cf m">MED</span></div>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 4: UMBRO BRAND STRATEGY -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#001a3f,#1a3fa8)"><img src="{chrome_uri}" alt=""><span class="wm">03 — Umbro Israel — אסטרטגיית מותג</span><span class="ey">Brand Strategy</span></div>
  <div class="stag" style="color:#1a3fa8">03 — UMBRO ISRAEL — BRAND STRATEGY</div>
  <div class="stit">Sports Authority · Running Nation · Football Kits · Padel</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi bl"><div class="kl">שוק ספורט ישראל</div><div class="kv sm">$1.72B</div><div class="ks"><span class="cf h">HIGH</span> CAGR +5% עד 2032</div></div>
    <div class="kpi gn"><div class="kl">ריצה — ספורט #1 ישראל</div><div class="kv sm">28%</div><div class="ks"><span class="cf m">MED</span> צמיחה מהירה · 2024</div></div>
    <div class="kpi go"><div class="kl">מועדוני כדורגל חובבים</div><div class="kv sm">1,200+</div><div class="ks"><span class="cf m">MED</span> B2B kit opportunity</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>פוזישנינג — Umbro Israel 2026</h2>
      <div class="box bl" style="font-size:8.5px">
        <strong>Technical Sports Authority — Not Just Football</strong><br>
        Umbro נכנסת לישראל לא בתור מותג כדורגל נוסף, אלא כ-sports performance platform. Football כעוגן → Running כמנוע צמיחה → Padel כהתרחבות.
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;margin-top:2mm">
        <div style="background:#001a3f;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#b0c0e8;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">Football</div>
          <div style="color:#fff;font-size:8px">עוגן ה-DNA · B2B קיטים<br>ליגות חובבים<br>AOV ₪280 kit deal</div>
        </div>
        <div style="background:#002b5c;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#b0c0e8;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">Running</div>
          <div style="color:#fff;font-size:8px">מנוע צמיחה עיקרי<br>28% CAGR ישראל<br>AOV ₪380 head-to-toe</div>
        </div>
        <div style="background:#1a3fa8;border-radius:4px;padding:2.5mm;text-align:center">
          <div style="color:#fff;font-size:7px;font-weight:800;text-transform:uppercase;margin-bottom:1mm">Padel</div>
          <div style="color:#fff;font-size:8px">הזדמנות נישה<br>130 מגרשים · 36 בבנייה<br><span class="cf l">LOW</span> 2K dedicated players</div>
        </div>
      </div>

      <h2 style="margin-top:2mm">הזדמנות B2B — קיטים מועדונים</h2>
      <div class="box gn" style="font-size:8px">
        <strong>1,200+ מועדוני כדורגל חובבים ישראל.</strong> אין ספק D2C ישראלי לקיטים. Kit deal: חולצה ₪120 + מכנס ₪80 + גרב ₪30 = <strong>₪230/שחקן × 18 שחקנים = ₪4,140/קיט.</strong> 4 קיטים/חודש = ₪16,560 B2B revenue נוסף.
      </div>

      <h2 style="margin-top:2mm">אסטרטגיית קריאטיב Umbro</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>שלב</th><th>פורמט</th><th>Content</th></tr></thead>
        <tbody>
          <tr><td>M1</td><td>4 Static</td><td>Action shots · Running IL · Padel court aesthetics</td></tr>
          <tr><td>M2</td><td>3S + 1V</td><td>Football training video · Kit showcase · Community feel</td></tr>
          <tr><td>M3+</td><td>UGC</td><td>מועדונים מרוצים · שחקנים אמיתיים</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h2>פלח קהל יעד — Umbro</h2>
      <div style="display:grid;gap:1.5mm;margin-top:1mm">
        <div class="box bl" style="font-size:8px">
          <strong>Primary: Running Enthusiast 25-40</strong><br>
          Gush Dan · Interested in running apps (Strava, Nike Run) · Budget ₪400-600/year on gear
        </div>
        <div class="box" style="font-size:8px">
          <strong>Secondary: Football Weekend Warrior 28-45</strong><br>
          Amateur leagues (DF ספורט, וואטסאפ גרופ) · Team captain = decision maker for kit purchase
        </div>
        <div class="box go" style="font-size:8px">
          <strong>Tertiary: Padel Player 30-50</strong><br>
          <span class="cf l">LOW</span> רק ~2,000 dedicated players. לא לבנות תחזית ראשית על פאדל. Entry point to broader market.
        </div>
      </div>

      <h2 style="margin-top:2mm">Meta Ads — Umbro Specific Targeting</h2>
      <div class="box bl" style="font-size:8px">
        <strong>Interests:</strong> Running, Football, Fitness, Sports Apparel, Padel, Strava<br>
        <strong>Age:</strong> 25-45 | <strong>Location:</strong> Israel national (not just center)<br>
        <strong>Lookalike:</strong> Email list from B2B kit customers (high LTV)<br>
        <span class="cf m">MED</span> CAC צפוי ₪180-220 cold start → ₪100-130 M6+
      </div>

      <h2 style="margin-top:2mm">KPIs — Umbro (בנצ'מרק)</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm">
        <div class="box bl" style="font-size:8px;text-align:center">
          <strong>ROAS יעד M6</strong><br>
          <span style="font-size:16px;font-weight:900;color:#1a3fa8">2.8×</span><br>
          <span class="cf m">MED</span> sports fashion IL baseline
        </div>
        <div class="box gn" style="font-size:8px;text-align:center">
          <strong>Repeat Rate (90d)</strong><br>
          <span style="font-size:16px;font-weight:900;color:#1a7a4a">22%</span><br>
          <span class="cf m">MED</span> seasonal buyers
        </div>
      </div>

      <div class="box re" style="margin-top:2mm;font-size:8px">
        <span class="cf l">RISK</span> <strong>תחרות ישירה:</strong> Nike, Adidas, New Balance לא נעלמות. Umbro ניצחת על DNA כדורגל + מחיר mid-tier (₪200-400 vs ₪500+ Nike). לא להתחרות head-to-head — ל-own את נישת football kits + padel.
      </div>
    </div>
  </div>
</div>

<!-- PAGE 5: HUB STRATEGY -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a3a00,#c49a2a)"><img src="{chrome_uri}" alt=""><span class="wm">04 — Intermax Group Hub</span><span class="ey">Multi-Brand Strategy</span></div>
  <div class="stag" style="color:#c49a2a">04 — INTERMAX GROUP HUB — MULTI-BRAND STRATEGY</div>
  <div class="stit">nine72.com / intermax.co.il · Fast Simon AI · Cross-Brand Loyalty</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi go"><div class="kl">Cross-Sell Uplift</div><div class="kv sm">+18%</div><div class="ks"><span class="cf m">MED</span> multi-brand AOV vs single</div></div>
    <div class="kpi gn"><div class="kl">Loyalty LTV Boost</div><div class="kv sm">×2.5</div><div class="ks"><span class="cf m">MED</span> loyalty member vs non-member</div></div>
    <div class="kpi bl"><div class="kl">Fast Simon CVR Lift</div><div class="kv sm">+22%</div><div class="ks"><span class="cf m">LOW</span> AI search vs standard</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>תפקיד Hub — גשר בין 2 עולמות</h2>
      <div class="box go" style="font-size:8.5px">
        Hub הוא לא "עוד חנות" — הוא ה-infrastructure שמאפשרת ל-Ed Hardy + Umbro לחלוק data, לקוחות ולמנף cross-sell. לקוח שמגיע ל-Ed Hardy יכול לגלות Umbro, ולהיפך.
      </div>

      <h2 style="margin-top:2mm">Fast Simon AI — יכולות</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>פיצ'ר</th><th>תיאור</th><th>Impact</th></tr></thead>
        <tbody>
          <tr><td>AI Search</td><td>הבנת כוונה, שגיאות כתיב, עברית</td><td class="pos">CVR +15-22%</td></tr>
          <tr><td>Smart Filters</td><td>Dynamic filtering by behavior</td><td class="pos">Bounce -18%</td></tr>
          <tr><td>Personalization</td><td>מוצרים לפי התנהגות</td><td class="pos">AOV +12%</td></tr>
          <tr><td>Cross-Brand Rec.</td><td>Ed Hardy buyer → Umbro suggestion</td><td class="pos">Cross-sell</td></tr>
        </tbody>
      </table>
      <div style="margin-top:1.5mm;font-size:7px;color:#888">עלות Fast Simon: ₪200-400/חודש. ROI על CVR lift מחזיר תוך M2.</div>

      <h2 style="margin-top:2mm">Loyalty Architecture</h2>
      <div class="box" style="font-size:8px">
        <strong>Cross-Brand Points System:</strong><br>
        קנה Ed Hardy = נקודות שרצות ב-Umbro ולהיפך.<br>
        "Group Loyalty" — הסיבה לבוא ל-Hub ולא לחנות בודדת.<br>
        Tool: Yotpo Loyalty / Smile.io — <span class="cf m">MED</span> ₪150-300/חודש
      </div>
    </div>
    <div>
      <h2>Cross-Brand Customer Journey</h2>
      <div style="display:flex;flex-direction:column;gap:2mm;margin-top:1mm">
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#5b1fa8;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">1</div>
          <div style="background:#f0eaf9;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">לקוח נחשף ל-Ed Hardy Meta Ad → מגיע לאתר</div>
        </div>
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#5b1fa8;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">2</div>
          <div style="background:#f0eaf9;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">קונה חולצה Ed Hardy → מצטרף ל-Loyalty Club</div>
        </div>
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#c49a2a;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">3</div>
          <div style="background:#fdf6e3;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">Hub מציג: "גם אוהבי Ed Hardy אוהבים Umbro Running" → cross-sell</div>
        </div>
        <div style="display:flex;align-items:center;gap:2mm">
          <div style="background:#1a7a4a;color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:900;flex-shrink:0">4</div>
          <div style="background:#e8f5ee;border-radius:4px;padding:2mm 3mm;font-size:8px;flex:1">Klaviyo sequence: 30 days post-purchase → Umbro offer + נקודות<br>LTV grows across both brands</div>
        </div>
      </div>

      <h2 style="margin-top:2mm">תועלת Hub לעסק</h2>
      <ul style="font-size:8.5px">
        <li><strong>Shared Pixel:</strong> כל לקוח של brand אחד מאמן את הסיגנל לשני</li>
        <li><strong>Shared Email List:</strong> Klaviyo אחד לשני המותגים — חיסכון ₪/חודש</li>
        <li><strong>Consolidated Reporting:</strong> Dashboard אחד — LTV, CAC, Revenue per customer</li>
        <li><strong>B2B Portal:</strong> ספקי קיטי כדורגל יכולים להזמין דרך Hub, לא רק Umbro</li>
      </ul>

      <div class="box gn" style="margin-top:2mm;font-size:8px">
        <span class="cf m">MED</span> <strong>יעד שנה 1 Hub:</strong> 15% מכלל ה-Revenue מ-cross-brand purchases. כל cross-sell = CM מלא ללא CAC נוסף → leverage.
      </div>
    </div>
  </div>
</div>
""")

# ── PAGES 6-8: FINANCIAL + FORECAST ──────────────────────────────────────────
html_parts.append(f"""
<!-- PAGE 6: BREAKEVEN + SCENARIOS -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">05 — ניתוח פיננסי</span><span class="ey">Breakeven + Scenarios</span></div>
  <div class="stag">05 — FINANCIAL FOUNDATION</div>
  <div class="stit">נקודת איזון + השוואת תרחישים H1</div>
  <div class="c2" style="margin-bottom:3mm">
    <div>
      <div class="c4" style="margin-bottom:2.5mm">
        <div class="kpi go"><div class="kl">BE ROAS</div><div class="kv">{BE_ROAS}×</div><div class="ks">AOV ÷ CM/הז׳</div></div>
        <div class="kpi rd"><div class="kl">הז׳ לאיזון M1</div><div class="kv sm">{round((mgmt_fees[1]+FIXED_OPS)/CM_PER_ORDER)}</div><div class="ks">× ₪{int(CM_PER_ORDER)} CM</div></div>
        <div class="kpi"><div class="kl">הכנסה לאיזון M1</div><div class="kv sm">{fmt(round((mgmt_fees[1]+FIXED_OPS)/CM_PER_ORDER)*AOV)}</div><div class="ks">M3-M4 יעד</div></div>
        <div class="kpi gn"><div class="kl">CM/הזמנה</div><div class="kv sm">₪{int(CM_PER_ORDER)}</div><div class="ks">55.9% מרווח</div></div>
      </div>
      <h2>נוסחת CM — בנייה מהיסוד</h2>
      <table style="font-size:8px;margin-top:1mm">
        <thead><tr><th>רכיב</th><th>ערך</th><th>הסבר</th></tr></thead>
        <tbody>
          <tr><td>AOV (מחיר מכירה)</td><td>₪{AOV}</td><td>ממוצע 3 חנויות</td></tr>
          <tr><td>COGS (38%)</td><td class="neg">-₪{round(AOV*COGS_PCT)}</td><td>מוצר + רויאלטי</td></tr>
          <tr><td>עלויות משתנות (4%)</td><td class="neg">-₪{round(AOV*VAR_PCT)}</td><td>PayPlus + Shopify fee</td></tr>
          <tr><td>אריזה + טיפול</td><td class="neg">-₪{FIXED_PER_ORD}</td><td>לפי הזמנה</td></tr>
          <tr class="hl"><td><strong>CM נטו/הזמנה</strong></td><td class="pos"><strong>₪{int(CM_PER_ORDER)}</strong></td><td>55.9% מרווח</td></tr>
        </tbody>
      </table>
      <div class="box dk" style="margin-top:2mm;font-size:8px">
        <strong>נוסחת נטו חודשית (v15):</strong><br>
        נטו = CM_כולל − (LGG + מדיה + קריאטיב + Ext) − FIXED_OPS − RS<br>
        קריאטיב <strong>בתוך</strong> ₪20K. RS 8% = בנפרד מהתקציב, על הכנסות ברוטו.
      </div>
    </div>
    <div>
      <h2>השוואת תרחישים M1-M6</h2>
      <table style="margin-top:1mm;font-size:8px">
        <thead>
          <tr>
            <th rowspan="2">חודש</th>
            <th colspan="2" style="background:#8b2222;text-align:center">שמרני 🔴</th>
            <th rowspan="2" style="background:#555;width:1.5mm"></th>
            <th colspan="2" style="background:#7a5a10;text-align:center">בסיס 🟡</th>
            <th rowspan="2" style="background:#555;width:1.5mm"></th>
            <th colspan="2" style="background:var(--g);text-align:center">אגרסיבי 🟢</th>
          </tr>
          <tr>
            <th style="background:#a03030">הכנסה</th><th style="background:#a03030">נטו</th>
            <th class="ga">הכנסה</th><th class="ga">נטו</th>
            <th class="gc">הכנסה</th><th class="gc">נטו</th>
          </tr>
        </thead>
        <tbody>{sc_rows}</tbody>
      </table>
      <div class="box re" style="margin-top:1.5mm;font-size:8px">
        <span class="cf m">MED</span> <strong>נטו כולל מדיה + קריאטיב!</strong> v15 — תיקון ממודל v14. הנטו כאן הוא אמיתי: CM − LGG − מדיה − קריאטיב − Ext − FIXED_OPS − RS.
      </div>
    </div>
  </div>
</div>

<!-- PAGE 7: DRIVE FORECAST TABLE -->
<div class="page" style="padding:8mm 10mm 6mm">
  <div class="ph" style="margin:-8mm -10mm 3.5mm">
    <img src="{chrome_uri}" alt="">
    <span class="wm">06 — תחזית שנתית M0-M12</span>
    <span class="ey">Drive Format — All KPIs</span>
  </div>
  <div class="stag">06 — ANNUAL FORECAST (BASE SCENARIO)</div>
  <div class="stit" style="font-size:15px;margin-bottom:2.5mm">תחזית מלאה — כל ה-KPIs | M0 עד M12</div>
  {drive_tbl}
</div>
""")

# ── PAGES 8-9: TIMELINE + UNCERTAINTY FRAMEWORK ───────────────────────────────
html_parts.append(f"""
<!-- PAGE 8: TIMELINE -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">07 — טיימליין ביצוע</span><span class="ey">90-Day Roadmap + 12-Month Milestones</span></div>
  <div class="stag">07 — TIMELINE</div>
  <div class="stit">90 יום ראשונים + אבני דרך שנה ראשונה</div>

  <div class="c2">
    <div>
      <h2>90 יום ראשונים — Phase by Phase</h2>
      <div class="timeline-row">
        <div class="tl-month">M0<br>שבוע 1-2</div>
        <div class="tl-dot"><div class="d" style="background:#5b1fa8"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#f0eaf9">
          <strong style="color:#5b1fa8">הקמה טכנולוגית</strong><br>
          ✓ Shopify × 3 — עברית + RTL<br>
          ✓ PayPlus / Cardcom סליקה<br>
          ✓ Facebook Pixel על כל 3 חנויות<br>
          ✓ Domain ×3 + Email setup
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M0<br>שבוע 3-4</div>
        <div class="tl-dot"><div class="d" style="background:#5b1fa8"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#f0eaf9">
          <strong style="color:#5b1fa8">תוכן + קריאטיב Seed</strong><br>
          ✓ Fast Simon installation<br>
          ✓ Klaviyo flows: Welcome + Abandon Cart<br>
          ✓ 4 Static assets per brand (צילום)<br>
          ✓ Ad account warm-up
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M1<br>שבוע 1-4</div>
        <div class="tl-dot"><div class="d" style="background:#c49a2a"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#fdf6e3">
          <strong style="color:#c49a2a">Soft Launch — Meta Ads</strong><br>
          ✓ CBO Broad + Add-to-Cart optimization<br>
          ✓ Learning phase — לא לצפות ROAS גבוה<br>
          ✓ Pixel events: PageView → ViewContent → ATC → Purchase<br>
          ✓ יעד: 50+ ATC events (exit learning)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M2-M3</div>
        <div class="tl-dot"><div class="d" style="background:#c49a2a"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#fdf6e3">
          <strong style="color:#c49a2a">Scale Creative Testing</strong><br>
          ✓ A/B test: Static vs Video per brand<br>
          ✓ Retargeting campaigns live<br>
          ✓ Lookalike audiences seeding<br>
          ✓ יעד: 10 Purchase events/week (Pixel maturity)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M4-M6</div>
        <div class="tl-dot"><div class="d" style="background:#1a7a4a"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#e8f5ee">
          <strong style="color:#1a7a4a">Optimization + First Profitability</strong><br>
          ✓ Winner creative scaled<br>
          ✓ Lookalike 1% → 3% → 5%<br>
          ✓ Email flows optimized (Open rate target 30%+)<br>
          ✓ <strong>M6: נטו חיובי צפוי — +₪{MD[6]["net"]:,}</strong>
        </div>
      </div>
    </div>
    <div>
      <h2>M7-M12 — הרחבת ערוצים</h2>
      <div class="timeline-row">
        <div class="tl-month">M7-M8</div>
        <div class="tl-dot"><div class="d" style="background:#1a3fa8"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#eaeff9">
          <strong style="color:#1a3fa8">Google Ads Launch</strong><br>
          ✓ Google Shopping + Search campaigns<br>
          ✓ Brand keyword protection<br>
          ✓ Cross-channel attribution setup<br>
          ✓ LGG fee: ₪{mgmt_fees[7]:,} (Meta + Google)<br>
          ✓ יעד ROAS M8: 3.1× (Google Search higher intent)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M9-M10</div>
        <div class="tl-dot"><div class="d" style="background:#c41414"></div><div class="l"></div></div>
        <div class="tl-content" style="background:#fff0f0">
          <strong style="color:#c41414">TikTok Ads Launch</strong><br>
          ✓ Ed Hardy: Y2K aesthetic video content<br>
          ✓ TikTok Shop integration (if available IL)<br>
          ✓ Gen-Z targeting — Ed Hardy DNA match<br>
          ✓ LGG fee: ₪{mgmt_fees[9]:,} (3 channels)
        </div>
      </div>
      <div class="timeline-row">
        <div class="tl-month">M11-M12</div>
        <div class="tl-dot"><div class="d" style="background:#1a7a4a"></div></div>
        <div class="tl-content" style="background:#e8f5ee">
          <strong style="color:#1a7a4a">Full Scale + Seasonality</strong><br>
          ✓ Pre-Hanukkah campaign (Ed Hardy gift sets)<br>
          ✓ Umbro winter running gear push<br>
          ✓ Holiday bundles → AOV ₪500+<br>
          ✓ יעד M12: +₪{MD[12]["net"]:,} נטו
        </div>
      </div>

      <h2 style="margin-top:2mm">אבני דרך — Go / No-Go</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>חודש</th><th>אבן דרך</th><th>Go אם</th><th>No-Go אם</th></tr></thead>
        <tbody>
          <tr><td>M1 סוף</td><td>Pixel data</td><td class="pos">50+ ATC events</td><td class="neg">&lt;20 ATC events</td></tr>
          <tr><td>M3 סוף</td><td>First ROAS</td><td class="pos">ROAS ≥1.5×</td><td class="neg">ROAS &lt;1.0×</td></tr>
          <tr><td>M5 סוף</td><td>Break-even</td><td class="pos">נטו ≥ -₪5K</td><td class="neg">נטו &lt; -₪15K</td></tr>
          <tr><td>M6 סוף</td><td>רווחיות</td><td class="pos">נטו חיובי</td><td class="neg">גרעון רצוף</td></tr>
          <tr><td>M7</td><td>Google Go</td><td class="pos">M6 profitable</td><td class="neg">טרם רווחי</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- PAGE 9: UNCERTAINTY FRAMEWORK -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">08 — מסגרת אי-ודאות</span><span class="ey">Uncertainty + Expectations Framework</span></div>
  <div class="stag">08 — UNCERTAINTY FRAMEWORK</div>
  <div class="stit">רמות ביטחון · הנחות · סיכונים ידועים</div>

  <div class="c3" style="margin-bottom:3mm">
    <div style="background:#d8f0e5;border:1px solid #aadcc0;border-radius:5px;padding:3mm;text-align:center">
      <div style="font-size:9px;font-weight:800;color:#1a7a4a;margin-bottom:1mm">HIGH — ביטחון גבוה</div>
      <div style="font-size:7.5px;color:#333">מקורות ראשוניים מוכחים<br>נתוני שוק ישראל 2024-2026<br>קבועי מודל עסקי</div>
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
      <h2>KPI Confidence Map</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>KPI</th><th>ערך</th><th>רמה</th><th>מקור</th></tr></thead>
        <tbody>
          <tr><td>Shopify Payments — לא ב-IL</td><td>PayPlus/Cardcom</td><td><span class="cf h">HIGH</span></td><td>Shopify ישראל</td></tr>
          <tr><td>tashlumim — ציפייה תרבותית</td><td>חובה</td><td><span class="cf h">HIGH</span></td><td>מחקר ישראל</td></tr>
          <tr><td>Bit Payment — שימוש</td><td>53% מרכישות</td><td><span class="cf h">HIGH</span></td><td>BoI 2024</td></tr>
          <tr><td>Cart Abandon Rate</td><td>83.5% ישראל</td><td><span class="cf h">HIGH</span></td><td>Baymard + IL</td></tr>
          <tr><td>Meta CPM Israel</td><td>₪40-85</td><td><span class="cf m">MED</span></td><td>Meta benchmarks</td></tr>
          <tr><td>Meta CTR fashion IL</td><td>1.5-2.5%</td><td><span class="cf m">MED</span></td><td>Wordstream + IL adj</td></tr>
          <tr><td>CVR cold start</td><td>0.8-1.2%</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>CVR M6+ (mature)</td><td>1.8-2.4%</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>CAC cold start</td><td>₪180-220</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>CAC M6+</td><td>₪100-130</td><td><span class="cf m">MED</span></td><td>IL D2C 2025-26</td></tr>
          <tr><td>Repeat rate 90d</td><td>22-28%</td><td><span class="cf m">MED</span></td><td>global fashion adj</td></tr>
          <tr><td>Return rate</td><td>12-18%</td><td><span class="cf m">MED</span></td><td>IL fashion</td></tr>
          <tr><td>ROAS M1</td><td>1.0-1.5×</td><td><span class="cf m">MED</span></td><td>cold start baseline</td></tr>
          <tr><td>ROAS M6</td><td>2.5-3.5×</td><td><span class="cf m">MED</span></td><td>mature D2C IL</td></tr>
          <tr><td>ROAS M12</td><td>3.0-4.5×</td><td><span class="cf l">LOW</span></td><td>projection</td></tr>
          <tr><td>Ed Hardy Brand Peak Length</td><td>3-5 שנים</td><td><span class="cf m">MED</span></td><td>forensic report</td></tr>
          <tr><td>Padel market size</td><td>~2,000 dedicated</td><td><span class="cf m">MED</span></td><td>estimation</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h2>תרחישי Upside / Downside</h2>
      <div class="box gn" style="font-size:8px;margin-bottom:1.5mm">
        <strong>🟢 Upside — מה יכול להיות טוב יותר</strong><br>
        • ROAS מהיר יותר — creative hit בM2 (rare, קורה ~15% מהמקרים)<br>
        • Umbro kit deal גדול — מועדון עם 200+ שחקנים בM1<br>
        • Ed Hardy viral moment — TikTok organic × paid<br>
        • Repeat rate 30%+ — loyalty program above expectations<br>
        • <strong>Impact:</strong> רווחיות בM4 במקום M6
      </div>
      <div class="box re" style="font-size:8px;margin-bottom:1.5mm">
        <strong>🔴 Downside — מה יכול לקחת יותר זמן</strong><br>
        • Learning phase מורחב — Meta אלגוריתם לא converges בM1-M2<br>
        • CVR נמוך — אתר לא מותאם מספיק (tashlumim, UX)<br>
        • CPM עולה — Q4 pricing seasonality<br>
        • Ed Hardy IP issue — עיכוב משפטי לפני launch<br>
        • <strong>Impact:</strong> נטו חיובי בM8 במקום M6 — עדיין OK
      </div>
      <div class="box go" style="font-size:8px">
        <strong>⚠️ מה לא בשליטתנו</strong><br>
        • שינויי אלגוריתם Meta / iOS (Apple)<br>
        • עלייה חדה ב-CPM בתחרות עונתית<br>
        • חקיקה ישראלית על נתוני צרכנים<br>
        • הסלמה ביטחונית — consumer confidence<br>
        <span class="cf l">LOW</span> כל אלה קיימים — מתחשבים בציר סבלנות 5 חודשים
      </div>

      <h2 style="margin-top:2mm">מדדי Success — מה מוגדר כהצלחה</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>מדד</th><th>M3</th><th>M6</th><th>M12</th></tr></thead>
        <tbody>
          <tr><td>ROAS בסיס</td><td class="pur">≥1.5×</td><td class="pos">≥2.8×</td><td class="pos">≥3.5×</td></tr>
          <tr><td>נטו (₪)</td><td class="neg">-₪15K</td><td class="pos">+₪7K</td><td class="pos">+₪76K</td></tr>
          <tr><td>Orders/month</td><td class="pur">97</td><td class="pos">297</td><td class="pos">1,065</td></tr>
          <tr><td>Revenue (₪)</td><td class="pur">₪36K</td><td class="pos">₪113K</td><td class="pos">₪405K</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
""")

# ── PAGES 10-12: OFFER + SIGNATURE + HTML END ─────────────────────────────────
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
    RS ({act}): <strong style="color:{fg}">₪{rs_m1:,}</strong> → חודש שלאחר: <strong style="color:{fg}">₪{rs_m2:,}</strong>
  </div>
</div>"""

_inv_rows = "".join([
    f'<tr{"" if MD[m]["net"]<=0 else " class=hl"}>'
    f'<td>M{m}</td>'
    f'<td style="font-size:7.5px">{"הקמה" if m==0 else "Meta" if m<=6 else "Meta+G" if m<=8 else "Meta+G+TT"}</td>'
    f'<td class="pur">{fmt(mgmt_fees[m])}</td>'
    f'<td>{"—" if m==0 else fmt(B[m][1] if m<=6 else B_ext[m][1])}</td>'
    f'<td>{"—" if m==0 else fmt(creative_plan[m][2])}</td>'
    f'<td style="font-weight:800;{"color:#1a7a4a" if MD[m]["net"]>0 else "color:#c41414"}">{fmt(MD[m]["total_invest"])}</td>'
    f'<td style="font-weight:800;{"color:#1a7a4a" if MD[m]["net"]>0 else "color:#c41414" if MD[m]["net"]<-10000 else "color:#c49a2a"}">{fmt(MD[m]["net"],True)}</td>'
    f'</tr>'
    for m in range(13)
])

html_parts.append(f"""
<!-- PAGE 10: THE OFFER -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">09 — ההצעה</span><span class="ey">The Offer</span></div>
  <div class="stag">09 — THE OFFER</div>
  <div class="stit">מחירון שירותים + תנאי התקשרות</div>

  <div style="display:flex;gap:3mm;margin-bottom:3.5mm">
    {_offer_channel_cards}
  </div>

  <div class="c2" style="margin-bottom:3mm">
    <div>
      <h2>קריאטיב — מחיר יחידה (20% הנחה)</h2>
      <div style="display:flex;gap:2.5mm;margin-top:1.5mm">
        <div style="background:#fafaf7;border:1px solid #ddd;border-radius:6px;padding:3mm 4mm;flex:1">
          <div style="font-size:8.5px;font-weight:800;color:#444;margin-bottom:1.5mm">Static (פר תמונה)</div>
          <div style="display:flex;align-items:baseline;gap:2mm">
            <span style="font-size:9px;color:#aaa;text-decoration:line-through">₪550</span>
            <span style="font-size:16px;font-weight:900;color:#333">₪{STATIC_PRICE}</span>
            <span style="background:#333;color:#fff;border-radius:3px;padding:1px 4px;font-size:7px">20% OFF</span>
          </div>
          <div style="font-size:7px;color:#777;margin-top:1mm">M1: 4 Static → ₪{STATIC_PRICE*4:,}</div>
        </div>
        <div style="background:#fafaf7;border:1px solid #ddd;border-radius:6px;padding:3mm 4mm;flex:1">
          <div style="font-size:8.5px;font-weight:800;color:#444;margin-bottom:1.5mm">Video (פר וידאו)</div>
          <div style="display:flex;align-items:baseline;gap:2mm">
            <span style="font-size:9px;color:#aaa;text-decoration:line-through">₪2,200</span>
            <span style="font-size:16px;font-weight:900;color:#333">₪{VIDEO_PRICE:,}</span>
            <span style="background:#333;color:#fff;border-radius:3px;padding:1px 4px;font-size:7px">20% OFF</span>
          </div>
          <div style="font-size:7px;color:#777;margin-top:1mm">M1: 1 Video → ₪{VIDEO_PRICE:,}</div>
        </div>
      </div>
      <div style="margin-top:2mm;font-size:8px;color:var(--im)">
        M1: 4 Static (₪{STATIC_PRICE*4:,}) + 1 Video (₪{VIDEO_PRICE:,}) = <strong>₪{STATIC_PRICE*4+VIDEO_PRICE:,}</strong> — כלול בתקציב ₪20K<br>
        M6: 10 Static (₪{STATIC_PRICE*10:,}) + 4 Video (₪{VIDEO_PRICE*4:,}) = <strong>₪{STATIC_PRICE*10+VIDEO_PRICE*4:,}</strong>
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
            <li>תקציב מדיה (Media)</li>
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
      <h2>סיכום השקעה חודשי + נטו</h2>
      <table style="font-size:7.5px;margin-top:1mm">
        <thead><tr><th>חודש</th><th>ערוצים</th><th>LGG</th><th>מדיה</th><th>קריאטיב</th><th>סה"כ</th><th>נטו ★</th></tr></thead>
        <tbody>{_inv_rows}</tbody>
        <tfoot><tr>
          <td colspan="5">סה"כ שנה ראשונה</td>
          <td>{fmt(sum(MD[m]["total_invest"] for m in range(13)))}</td>
          <td>{fmt(sum(MD[m]["net"] for m in range(13)),True)}</td>
        </tr></tfoot>
      </table>
    </div>
    <div>
      <h2>תנאי RS ו-RS Examples</h2>
      <div class="box gn" style="margin-top:1mm;font-size:8px">
        <strong>RS 8% — על הכנסות ברוטו, מחוץ ל-₪20K:</strong><br>
        • מ-M1, מכל הכנסה גולמית (גם בחודשים לא רווחיים)<br>
        • גדל עם הצלחה — אינטרס משותף<br>
        • M1: ₪{MD[1]["rs"]:,} | M6: ₪{MD[6]["rs"]:,} | M12: ₪{MD[12]["rs"]:,}
      </div>
      <div class="box go" style="margin-top:1.5mm;font-size:8px">
        <strong>תנאי ריטיינר:</strong><br>
        • ₪{CHANNEL_DISCOUNTED:,}/ערוץ ({CHANNEL_DISCOUNT_PCT}% הנחה מ-₪{RETAINER_PER_CHANNEL:,})<br>
        • חוזה 6 חודשים + חידוש 30 יום הודעה<br>
        • ציר סבלנות: 5 חודשים<br>
        • חריגה מ-₪20K — מותרת רק עם נטו חיובי
      </div>
    </div>
  </div>
</div>

<!-- PAGE 11: SIGNATURE -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">10 — אישור והתחייבות</span><span class="ey">Agreement & Signature</span></div>
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
        ✓ BE.ROAS: <strong>{BE_ROAS}×</strong> | AOV: <strong>₪{AOV}</strong> | CM: <strong>₪{int(CM_PER_ORDER)}/הז׳</strong><br>
        ✓ Static: <strong>₪{STATIC_PRICE}</strong> | Video: <strong>₪{VIDEO_PRICE:,}</strong> (20% הנחה)<br>
        ✓ Ed Hardy IP — <strong>חובה לאמת Hardy Way LLC לפני launch</strong><br>
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
        קראתי והבנתי את תנאי ההתקשרות כמפורט במסמך זה. אני מאשר/ת את מבנה ה-RS, הריטיינרים, ציר הסבלנות וכל התנאים הפיננסיים.
      </div>
    </div>
  </div>
  <div style="margin-top:5mm;text-align:center;font-size:7px;color:var(--im);border-top:1px solid var(--rule);padding-top:2mm">
    © 2026 Los Gardios Group | ח.פ. 516819257 | losgardios.com | LGG-IMX-2026-001 | v15 | מסמך סודי — לא להפצה
  </div>
</div>

</body>
</html>""")

# ── WRITE HTML + GENERATE PDF ─────────────────────────────────────────────────
html = "".join(html_parts)
html_path = f"{S}/intermax-lgg-proposal-v15.html"
pdf_path  = f"{S}/intermax-lgg-proposal-v15.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML written: {html_path} ({len(html)//1024}KB)")

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
print(f"PDF generated: {pdf_path} ({size//1024}KB)")
