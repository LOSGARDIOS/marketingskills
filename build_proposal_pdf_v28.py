import os
from playwright.sync_api import sync_playwright

S = "/tmp/claude-0/-home-user/2ca1d236-9107-50cb-86bc-b6464e28a04f/scratchpad"

with open(f"{S}/seal_b64.txt") as f:
    seal = f.read().strip()
with open(f"{S}/chrome_b64.txt") as f:
    chrome = f.read().strip()
with open(f"{S}/ed_logo_b64.txt") as f:
    ed_logo_b64 = f.read().strip()
with open(f"{S}/lgg_logo_b64.txt") as f:
    lgg_logo_b64 = f.read().strip()

# Ed Hardy research images
with open(f"{S}/img_6952_b64.txt") as f:
    img6952 = f.read().strip()
with open(f"{S}/img_6953_b64.txt") as f:
    img6953 = f.read().strip()
with open(f"{S}/img_6954_b64.txt") as f:
    img6954 = f.read().strip()
with open(f"{S}/img_6955_b64.txt") as f:
    img6955 = f.read().strip()
with open(f"{S}/img_6956_b64.txt") as f:
    img6956 = f.read().strip()
with open(f"{S}/img_6957_b64.txt") as f:
    img6957 = f.read().strip()
with open(f"{S}/tiger_tee_b64.txt") as f:
    tiger_tee = f.read().strip()
with open(f"{S}/skull_hoodie_b64.txt") as f:
    skull_hoodie = f.read().strip()
with open(f"{S}/barrow_b64.txt") as f:
    barrow = f.read().strip()
with open(f"{S}/pmaa001_b64.txt") as f:
    pmaa001 = f.read().strip()
with open(f"{S}/palm_angels_b64.txt") as f:
    palm_angels = f.read().strip()
with open(f"{S}/lafw_b64.txt") as f:
    lafw = f.read().strip()

# Umbro research images
with open(f"{S}/umbro_logo_svg_b64.txt") as f:
    umbro_logo_svg = f.read().strip()
with open(f"{S}/umbro_cover_hero_b64.txt") as f:
    umbro_cover_hero = f.read().strip()
with open(f"{S}/umbro_heritage_kit_b64.txt") as f:
    umbro_heritage_kit = f.read().strip()
with open(f"{S}/umbro_ltam_jerseys_b64.txt") as f:
    umbro_ltam_jerseys = f.read().strip()
with open(f"{S}/umbro_ltam_style1_b64.txt") as f:
    umbro_ltam_style1 = f.read().strip()
with open(f"{S}/umbro_ltam_style2_b64.txt") as f:
    umbro_ltam_style2 = f.read().strip()
with open(f"{S}/padel_court_b64.txt") as f:
    padel_court = f.read().strip()
with open(f"{S}/padel_racket_b64.txt") as f:
    padel_racket = f.read().strip()
with open(f"{S}/padel_womens_b64.txt") as f:
    padel_womens = f.read().strip()
with open(f"{S}/padel_friends_b64.txt") as f:
    padel_friends = f.read().strip()
with open(f"{S}/umbro_fotbol_history_b64.txt") as f:
    umbro_fotbol_history = f.read().strip()
with open(f"{S}/umbro_football3_b64.txt") as f:
    umbro_football3 = f.read().strip()
with open(f"{S}/umbro_football4_b64.txt") as f:
    umbro_football4 = f.read().strip()
with open(f"{S}/umbro_football5_b64.txt") as f:
    umbro_football5 = f.read().strip()
with open(f"{S}/umbro_group_garden_b64.txt") as f:
    umbro_group_garden = f.read().strip()

# v24 new images
with open(f"{S}/mood_footvolley_b64.txt") as f:
    mood_footvolley = f.read().strip()
with open(f"{S}/umbro_lifestyle_b64.txt") as f:
    umbro_lifestyle = f.read().strip()
with open(f"{S}/eagle_skull_hoodie_back_b64.txt") as f:
    hoodie_back = f.read().strip()
with open(f"{S}/eagle_skull_hoodie_front_b64.txt") as f:
    hoodie_front = f.read().strip()
with open(f"{S}/padel_celebration_b64.txt") as f:
    padel_celebration = f.read().strip()
with open(f"{S}/padel_womens_court2_b64.txt") as f:
    padel_court2 = f.read().strip()
with open(f"{S}/crossover_tennis_visor_b64.txt") as f:
    crossover_tennis = f.read().strip()

# v25 Brazil images
with open(f"{S}/mood_brasil_tank_b64.txt") as f:
    brasil_tank = f.read().strip()
with open(f"{S}/mood_brasil_sunset_b64.txt") as f:
    brasil_sunset = f.read().strip()
with open(f"{S}/tiktok_swebo_brasil_b64.txt") as f:
    swebo_brasil = f.read().strip()

ed_logo_uri  = f"data:image/svg+xml;base64,{ed_logo_b64}"
lgg_logo_uri = f"data:image/png;base64,{lgg_logo_b64}"

seal_uri   = f"data:image/png;base64,{seal}"
chrome_uri = f"data:image/png;base64,{chrome}"

img6952_uri     = f"data:image/jpeg;base64,{img6952}"
img6953_uri     = f"data:image/jpeg;base64,{img6953}"
img6954_uri     = f"data:image/jpeg;base64,{img6954}"
img6955_uri     = f"data:image/jpeg;base64,{img6955}"
img6956_uri     = f"data:image/jpeg;base64,{img6956}"
img6957_uri     = f"data:image/jpeg;base64,{img6957}"
tiger_tee_uri   = f"data:image/jpeg;base64,{tiger_tee}"
skull_hoodie_uri= f"data:image/jpeg;base64,{skull_hoodie}"
barrow_uri      = f"data:image/jpeg;base64,{barrow}"
pmaa001_uri     = f"data:image/jpeg;base64,{pmaa001}"
palm_angels_uri = f"data:image/jpeg;base64,{palm_angels}"
lafw_uri        = f"data:image/jpeg;base64,{lafw}"

umbro_logo_uri      = f"data:image/svg+xml;base64,{umbro_logo_svg}"
umbro_cover_uri     = f"data:image/jpeg;base64,{umbro_cover_hero}"
umbro_heritage_uri  = f"data:image/jpeg;base64,{umbro_heritage_kit}"
umbro_ltam_j_uri    = f"data:image/jpeg;base64,{umbro_ltam_jerseys}"
umbro_style1_uri    = f"data:image/jpeg;base64,{umbro_ltam_style1}"
umbro_style2_uri    = f"data:image/jpeg;base64,{umbro_ltam_style2}"
padel_court_uri     = f"data:image/jpeg;base64,{padel_court}"
padel_racket_uri    = f"data:image/jpeg;base64,{padel_racket}"
padel_womens_uri    = f"data:image/jpeg;base64,{padel_womens}"
padel_friends_uri   = f"data:image/jpeg;base64,{padel_friends}"
umbro_fotbol_uri    = f"data:image/jpeg;base64,{umbro_fotbol_history}"
umbro_f3_uri        = f"data:image/jpeg;base64,{umbro_football3}"
umbro_f4_uri        = f"data:image/jpeg;base64,{umbro_football4}"
umbro_f5_uri        = f"data:image/jpeg;base64,{umbro_football5}"
umbro_garden_uri    = f"data:image/jpeg;base64,{umbro_group_garden}"

# v24 URIs
footvolley_uri      = f"data:image/jpeg;base64,{mood_footvolley}"
lifestyle_uri       = f"data:image/png;base64,{umbro_lifestyle}"
hoodie_back_uri     = f"data:image/jpeg;base64,{hoodie_back}"
hoodie_front_uri    = f"data:image/jpeg;base64,{hoodie_front}"
padel_celeb_uri     = f"data:image/jpeg;base64,{padel_celebration}"
padel_court2_uri    = f"data:image/jpeg;base64,{padel_court2}"
crossover_uri       = f"data:image/jpeg;base64,{crossover_tennis}"

# v25 Brazil URIs
brasil_tank_uri     = f"data:image/jpeg;base64,{brasil_tank}"
brasil_sunset_uri   = f"data:image/jpeg;base64,{brasil_sunset}"
swebo_brasil_uri    = f"data:image/jpeg;base64,{swebo_brasil}"

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

# ── נתוני מדיה והכנסות (v17 — שמרני → אגרסיבי → מינוף מהיר יותר) ─────────
# v17: מודל bottom-up — הכנסה = NC×AOV + rrev; ROAS נגזר בלבד
# ממוצעי שוק אופנה ואקססוריז ישראל (Meta Ads, 2025) — CPM/CTR/CVR כקלט
# (שלב, מדיה, ROAS_נגזר, תקציב_כולל, NC, RC, רכישות_חוזרות, הכנסה_כוללת, RS, _)
B = {
    0: ("הקמה",    0,    None, 20000,   0,   0,    0,     0,     0, 0),
    1: ("למידה", 11220,  0.85, 20000,  25,   0,    0,  9500,   760, 0),  # NC=25×380=9500; ROAS=0.85
    2: ("השקה",   9460,  1.37, 20000,  33,   1,  380, 12920,  1034, 0),  # NC=33×380+380=12920
    3: ("צמיחה",  9200,  2.11, 20000,  48,   3, 1140, 19380,  1550, 0),  # NC=48×380+1140=19380
    4: ("מינוף", 11440,  3.06, 24000,  84,   8, 3040, 34960,  2797, 0),  # NC=84×380+3040=34960
    5: ("שיא",   14180,  3.48, 27000, 113,  17, 6460, 49400,  3952, 0),  # NC=113×380+6460=49400
    6: ("מיטוב", 19180,  4.02, 32000, 173,  30,11400, 77140,  6171, 0),  # NC=173×380+11400=77140
}
B_ext = {
    7:  ("גוגל",   24740, 4.5, 47580, 250,  38, 14440, 109440,  8755, 0),
    8:  ("גוגל+",  28000, 4.9, 50840, 295,  65, 24700, 136900, 10952, 0),
    9:  ("TikTok", 35000, 4.7, 67600, 345,  90, 34200, 165300, 13224, 0),
    10: ("TikTok+",40000, 4.8, 72600, 390, 120, 45600, 193800, 15504, 0),
    11: ("Scale",  45000, 5.0, 79620, 395, 200, 76000, 226100, 18088, 0),
    12: ("Max",    50000, 4.9, 84620, 440, 210, 79800, 247000, 19760, 0),
}

# תרחיש שמרני — CPM גבוה 15%, CTR/CVR נמוכים 25%; ad_spend זהה לבסיס
C = {
    0: ("הקמה",    0,    None, 20000,   0,   0,    0,     0,    0, 0),
    1: ("למידה", 11220,  0.52, 20000,  15,   0,    0,  5700,  456, 0),
    2: ("השקה",   9460,  0.85, 20000,  20,   1,  380,  8000,  640, 0),
    3: ("צמיחה",  9200,  1.33, 20000,  29,   2,  760, 11780,  942, 0),
    4: ("מינוף", 11440,  1.86, 24000,  51,   3, 1140, 21060, 1685, 0),
    5: ("שיא",   14180,  2.09, 27000,  72,   6, 2280, 29640, 2371, 0),
    6: ("מיטוב", 19180,  2.41, 32000, 110,  10, 3800, 46000, 3680, 0),
}

# תרחיש אגרסיבי — CPM נמוך 10%, CTR/CVR גבוהים 35%; ad_spend זהה לבסיס
A = {
    0: ("הקמה",    0,    None, 20000,   0,   0,    0,     0,    0, 0),
    1: ("למידה", 11220,  1.20, 20000,  36,   0,    0, 13680, 1094, 0),
    2: ("השקה",   9460,  1.96, 20000,  47,   2,  760, 18620, 1490, 0),
    3: ("צמיחה",  9200,  3.03, 20000,  66,   8, 3040, 28120, 2250, 0),
    4: ("מינוף", 11440,  4.43, 24000, 111,  20, 7600, 49780, 3982, 0),
    5: ("שיא",   14180,  5.08, 27000, 151,  38,14440, 71820, 5746, 0),
    6: ("מיטוב", 19180,  5.90, 32000, 227,  68,25840,112200, 8976, 0),
}

# ── תכנית קריאטיב (v17 — מחיר מוסכם: ₪130 סטטי | ₪1,760 וידאו) ────────────
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

# v17 — ממוצעי שוק אופנה ישראל; CPM עולה ב-Q4 (BF+חנוכה), לא יורד
CPM_M = {1:75,2:72,3:68,4:65,5:62,6:60,7:58,8:63,9:68,10:74,11:98,12:90}
CTR_M = {1:.015,2:.018,3:.021,4:.024,5:.026,6:.027,7:.028,8:.029,9:.029,10:.030,11:.028,12:.031}
CVR_M = {1:.011,2:.014,3:.017,4:.019,5:.021,6:.022,7:.023,8:.024,9:.024,10:.025,11:.032,12:.027}

# ── חישוב חודשי (v17 — bottom-up: CPM→CTR→CVR; ROAS=נגזרת; RS=8% על כל הכנסה) ─
def compute_month(m):
    if m == 0:
        ti = 20000 + EXT_MONTHLY
        be_t = round((ti + FIXED_OPS) / EFFECTIVE_MARGIN)
        return {'phase':'הקמה','ad_spend':0,'cpm':None,'reach':0,'ctr':None,'visitors':0,
                'cvr':None,'nc':0,'rc':0,'total_orders':0,'ad_rev':0,'rrev':0,'total_rev':0,
                'roas':None,'lgg_fee':20000,'media':0,'creative':0,'ext':EXT_MONTHLY,
                'total_invest':ti,'rs':0,'be_threshold':be_t,'profitable':False}
    d = B[m] if m <= 6 else B_ext[m]
    ph,ads,_roas_stored,_,nc,rc,rrev,rev,rs,_ = d
    cr = creative_plan[m][2] if m in creative_plan else 0
    cpm = CPM_M.get(m); ctr = CTR_M.get(m); cvr_rate = CVR_M.get(m)
    reach = round(ads/cpm*1000) if cpm and ads>0 else 0
    visitors = round(reach*ctr) if ctr and reach>0 else 0
    # CVR מהטבלה הרשמית (ממוצע שוק אופנה ישראל)
    cvr = round((cvr_rate or 0)*100, 1)
    tot_ord = nc+rc
    lgg = mgmt_fees[m]
    total_invest = lgg + ads + cr + EXT_MONTHLY
    # נקודת איזון: הכנסה × 0.82 ≥ total_invest + FIXED_OPS
    be_t = round((total_invest + FIXED_OPS) / EFFECTIVE_MARGIN)
    profitable = (rev * EFFECTIVE_MARGIN) >= (total_invest + FIXED_OPS)
    # ROAS נגזר מהכנסה בפועל (לא קלט)
    roas = round(rev/ads, 2) if ads > 0 else None
    return {'phase':ph,'ad_spend':ads,'cpm':cpm,'reach':reach,'ctr':ctr,
            'visitors':visitors,'cvr':cvr,'nc':nc,'rc':rc,'total_orders':tot_ord,
            'ad_rev':nc*AOV,'rrev':rrev,'total_rev':rev,'roas':roas,
            'lgg_fee':lgg,'media':ads,'creative':cr,'ext':EXT_MONTHLY,
            'total_invest':round(total_invest),'rs':rs,
            'be_threshold':be_t,'profitable':profitable}

MD = {m: compute_month(m) for m in range(13)}
first_profitable = next((m for m in range(1, 13) if MD[m]['profitable']), None)


# ── טבלת תרחישים M1-M6 (v17 — bottom-up; BE=(invest+FIXED_OPS)/0.82) ────────
def scenario_rows():
    labels = {1:"M1",2:"M2",3:"M3",4:"M4",5:"M5",6:"M6"}
    rows = ""
    for m in range(1,7):
        lgg = mgmt_fees[m]
        ads = B[m][1]          # ad spend זהה בכל התרחישים
        cr  = creative_plan[m][2]
        # BE נכון: (total_invest + FIXED_OPS) / EFFECTIVE_MARGIN
        be_t = round((lgg + ads + cr + EXT_MONTHLY + FIXED_OPS) / EFFECTIVE_MARGIN)

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

# ── טבלת תחזית שנתית (v17 — ללא CM ו-נטו, עם עמודת נקודת איזון 90%) ────────
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
    note=(f'GM = 64% · CM = 46.6% · BE ROAS = 2.15× · RS = 8% | '
          f'נ.א. LGG: (LGG + מדיה + קריאטיב + Ext + הוצ׳) ÷ 0.82 | '
          f'🟢 = מעל נ.א. | 🔴 = מתחת | ערוצים: Meta 40% + TikTok 25% + Google 20% + WhatsApp + Brand Search')
    total_rev_12  = sum(D[m]['total_rev'] for m in range(13))
    total_inv_12  = sum(D[m]['total_invest'] for m in range(13))
    total_rs_12   = sum(D[m]['rs'] for m in range(13))
    total_lgg_12  = sum(D[m]['lgg_fee'] for m in range(13))
    first_profit  = next((m for m in range(1,13) if D[m]['profitable']), None)
    profit_label  = f"M{first_profit}" if first_profit else "M6+"
    avg_roas      = round(sum(D[m]['roas'] for m in range(1,13) if D[m]['roas']) / max(1, sum(1 for m in range(1,13) if D[m]['roas'])), 2)
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
<div style="margin-top:1.5mm;font-size:5.8px;color:#888;border-top:1px solid #eee;padding-top:1mm">{note}</div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;margin-top:4mm">
  <div style="background:#d8f0e5;border:1.5px solid #1a7a4a;border-radius:5px;padding:3mm;text-align:center">
    <div style="font-size:6px;color:#1a7a4a;text-transform:uppercase;letter-spacing:.08em;font-weight:700;margin-bottom:1mm">הכנסה M0-M12</div>
    <div style="font-size:18px;font-weight:900;color:#1a7a4a;line-height:1">{fmt(total_rev_12)}</div>
    <div style="font-size:6px;color:#1a7a4a;margin-top:1mm">מצטבר שנה 1</div>
  </div>
  <div style="background:#fde8e8;border:1.5px solid #8b1a1a;border-radius:5px;padding:3mm;text-align:center">
    <div style="font-size:6px;color:#8b1a1a;text-transform:uppercase;letter-spacing:.08em;font-weight:700;margin-bottom:1mm">השקעה כוללת</div>
    <div style="font-size:18px;font-weight:900;color:#8b1a1a;line-height:1">{fmt(total_inv_12)}</div>
    <div style="font-size:6px;color:#8b1a1a;margin-top:1mm">מדיה + ניהול + קריאטיב</div>
  </div>
  <div style="background:#ede7f9;border:1.5px solid #5b1fa8;border-radius:5px;padding:3mm;text-align:center">
    <div style="font-size:6px;color:#5b1fa8;text-transform:uppercase;letter-spacing:.08em;font-weight:700;margin-bottom:1mm">RS LGG שנה 1</div>
    <div style="font-size:18px;font-weight:900;color:#5b1fa8;line-height:1">{fmt(total_rs_12)}</div>
    <div style="font-size:6px;color:#5b1fa8;margin-top:1mm">8% × הכנסות ברוטו</div>
  </div>
  <div style="background:#fdf3d8;border:1.5px solid #7a5a10;border-radius:5px;padding:3mm;text-align:center">
    <div style="font-size:6px;color:#7a5a10;text-transform:uppercase;letter-spacing:.08em;font-weight:700;margin-bottom:1mm">ROAS ממוצע</div>
    <div style="font-size:18px;font-weight:900;color:#7a5a10;line-height:1">{avg_roas}×</div>
    <div style="font-size:6px;color:#7a5a10;margin-top:1mm">M1-M12 · נגזר</div>
  </div>
  <div style="background:#e8f5ee;border:1.5px solid #1a7a4a;border-radius:5px;padding:3mm;text-align:center">
    <div style="font-size:6px;color:#1a7a4a;text-transform:uppercase;letter-spacing:.08em;font-weight:700;margin-bottom:1mm">נ.א. ראשונה</div>
    <div style="font-size:18px;font-weight:900;color:#1a7a4a;line-height:1">{profit_label}</div>
    <div style="font-size:6px;color:#1a7a4a;margin-top:1mm">חציית Break-Even</div>
  </div>
</div>"""

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
      <div><label>מרווח גולמי</label><span>64%</span></div>
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
    <span>LGG-IMX-2026 | v23 | מסמך סודי</span>
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


# ── עמודים 03-08: ארכיטקטורה חדשה v22 — Template A/B/C ──────────────────────
html_parts.append(f"""
<!-- עמוד 03: Market Intelligence — Template A -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#0b1a3e,#1a3a70)"><img src="{chrome_uri}" alt=""><span class="wm">03 — Market Intelligence — מודיעין שוק</span><span class="ey">Template A · Analysis</span></div>
  <div class="stag" style="color:#1a3a70">03 — MARKET INTELLIGENCE · CONF-VALIDATED DATA</div>
  <div class="stit" style="margin-bottom:2.5mm">ישראל 2026 — שוק האופנה, הספורט וה-D2C</div>

  <div class="c3" style="margin-bottom:3mm">
    <div class="kpi bl"><div class="kl">שוק ביגוד ספורט ישראל</div><div class="kv sm">₪6.35B</div><div class="ks"><span class="cf h">HIGH</span> CONF 0.95 · Data Bridge 2024 · CAGR 6.3%</div></div>
    <div class="kpi go"><div class="kl">חלון Y2K — Gen-Z ישראל</div><div class="kv sm">12-18 חודש</div><div class="ks"><span class="cf h">HIGH</span> CONF 0.91 · Pinterest ↑340% · TikTok פעיל</div></div>
    <div class="kpi gn"><div class="kl">WhatsApp חדירה — ישראל</div><div class="kv sm">99%</div><div class="ks"><span class="cf h">HIGH</span> CONF 0.98 · ISOC-IL 2025 · ערוץ מכירה ראשוני</div></div>
  </div>

  <div class="c2">
    <div>
      <h2>שוק הספורט — Umbro</h2>
      <div class="box bl" style="font-size:8px;margin-bottom:2mm">
        <strong>₪6.35B שוק ספורט ישראל 2024:</strong><br>
        · נשים 55% מהשוק = ₪3.5B — Umbro: 0 מוצרי נשים כיום<br>
        · פאדל: 130+ מגרשים, ↑30% גלובלי, ריקנות מותגית<br>
        · 1,200+ מועדוני חובבים — ביקוש B2B קיטים<br>
        <span class="cf h">HIGH</span> CONF 0.93 · Statista 2024
      </div>
      <h2>שוק האופנה — Ed Hardy</h2>
      <div class="box" style="font-size:8px;margin-bottom:2mm">
        <strong>Y2K Revival — חלון הזדמנות:</strong><br>
        · Ed Hardy שיא עולמי $700M (2004-2009), ירידה 91% מאז<br>
        · Gen-Z ישראל לא חווה את שלב הרוויה — רואים וינטג׳ אותנטי<br>
        · Fox מחיר ₪600-₪1,200 vs. Ed Hardy יעד ₪250-480 — פער מחיר<br>
        <span class="cf h">HIGH</span> CONF 0.89 · TikTok Trend Data 2025
      </div>
      <h2>D2C — ישראל 2026</h2>
      <div class="box gn" style="font-size:8px">
        <strong>מגמות D2C ישראל:</strong><br>
        · Shopify IL: ↑42% יוצרים חדשים 2025<br>
        · WhatsApp Commerce: 99% חדירה = ערוץ מכירה הפוך ללא מתחרים<br>
        · AOV אופנה IL ₪320-440 · CVR cold 0.8-1.2% → warm 2.2-3.1%<br>
        <span class="cf m">MED</span> CONF 0.85 · PayPlus + Shopify IL Data 2025
      </div>
    </div>
    <div>
      <h2>מגמת Y2K — מדד חיפוש (2023-2026)</h2>
      <div style="background:#f8f8f5;border:1px solid #ddd;border-radius:4px;padding:3mm;margin-bottom:2.5mm">
        <svg viewBox="0 0 260 110" style="width:100%;height:auto;display:block" xmlns="http://www.w3.org/2000/svg">
          <defs><linearGradient id="yg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5b1fa8" stop-opacity="0.25"/><stop offset="1" stop-color="#5b1fa8" stop-opacity="0"/></linearGradient></defs>
          <!-- Y axis -->
          <line x1="30" y1="10" x2="30" y2="90" stroke="#ddd" stroke-width="0.8"/>
          <!-- X axis -->
          <line x1="30" y1="90" x2="255" y2="90" stroke="#ddd" stroke-width="0.8"/>
          <!-- Grid lines -->
          <line x1="30" y1="70" x2="255" y2="70" stroke="#eee" stroke-width="0.5" stroke-dasharray="2,2"/>
          <line x1="30" y1="50" x2="255" y2="50" stroke="#eee" stroke-width="0.5" stroke-dasharray="2,2"/>
          <line x1="30" y1="30" x2="255" y2="30" stroke="#eee" stroke-width="0.5" stroke-dasharray="2,2"/>
          <!-- Labels Y -->
          <text x="26" y="72" font-size="6" fill="#999" text-anchor="end">25</text>
          <text x="26" y="52" font-size="6" fill="#999" text-anchor="end">50</text>
          <text x="26" y="32" font-size="6" fill="#999" text-anchor="end">75</text>
          <text x="26" y="92" font-size="6" fill="#999" text-anchor="end">0</text>
          <!-- Data points: Q1'23=18, Q2=22, Q3=30, Q4=38, Q1'24=52, Q2=67, Q3=78, Q4=89, Q1'25=94, Q2=100, Q3=98, Q4=100, Q1'26=100 -->
          <!-- X coords: 35, 53, 71, 89, 107, 125, 143, 161, 179, 197, 215, 233, 251 -->
          <!-- Y = 90 - (val/100)*80 -->
          <polyline points="35,75.6 53,72.4 71,66 89,59.6 107,48.4 125,36.4 143,27.6 161,18.8 179,14.8 197,10 215,11.6 233,10 251,10"
            fill="none" stroke="#5b1fa8" stroke-width="1.5" stroke-linejoin="round"/>
          <polygon points="35,75.6 53,72.4 71,66 89,59.6 107,48.4 125,36.4 143,27.6 161,18.8 179,14.8 197,10 215,11.6 233,10 251,10 251,90 35,90"
            fill="url(#yg)"/>
          <!-- Endpoint dot -->
          <circle cx="251" cy="10" r="2.5" fill="#5b1fa8"/>
          <!-- Labels X -->
          <text x="35" y="99" font-size="5.5" fill="#999" text-anchor="middle">Q1'23</text>
          <text x="107" y="99" font-size="5.5" fill="#999" text-anchor="middle">Q1'24</text>
          <text x="179" y="99" font-size="5.5" fill="#999" text-anchor="middle">Q1'25</text>
          <text x="251" y="99" font-size="5.5" fill="#999" text-anchor="middle">Q1'26</text>
          <!-- Title -->
          <text x="143" y="8" font-size="6.5" fill="#5b1fa8" text-anchor="middle" font-weight="bold">Y2K Fashion Search Index — Pinterest IL</text>
          <!-- ↑340% label -->
          <text x="251" y="7" font-size="5.5" fill="#1a7a4a" text-anchor="end">↑340%</text>
        </svg>
        <div style="font-size:6.5px;color:#888;margin-top:1mm;text-align:center">מקור: Pinterest Trends Israel · CONF 0.88</div>
      </div>
      <h2>בנצ'מרק מתחרים — נקודות מחיר</h2>
      <table style="font-size:8px">
        <thead><tr><th>מותג</th><th>קטגוריה</th><th>AOV</th><th>CONF</th></tr></thead>
        <tbody>
          <tr><td>Ed Hardy IL (יעד)</td><td>Y2K Streetwear</td><td>₪380</td><td><span class="cf m">MED</span></td></tr>
          <tr><td>Barrow IL</td><td>Bold Graphic</td><td>₪420</td><td><span class="cf h">HIGH</span></td></tr>
          <tr><td>Palm Angels</td><td>Premium Street</td><td>₪1,800</td><td><span class="cf h">HIGH</span></td></tr>
          <tr><td>Fox Fashion</td><td>Mass Market</td><td>₪650</td><td><span class="cf h">HIGH</span></td></tr>
          <tr><td>Umbro IL (יעד)</td><td>Sports Authority</td><td>₪280</td><td><span class="cf m">MED</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- עמוד 04: Umbro — Repositioning — Template B -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#001a3e,#003f8a)"><img src="{chrome_uri}" alt=""><span class="wm">04 — Umbro Israel — Repositioning</span><span class="ey">Template B · Strategy</span></div>
  <div class="stag" style="color:#003f8a">04 — UMBRO ISRAEL — BRAND REPOSITIONING · HERITAGE × INNOVATION</div>

  <!-- Template B: text left (40%) | image right (60%) -->
  <div style="display:grid;grid-template-columns:2fr 3fr;gap:3mm;height:155mm">
    <div style="display:flex;flex-direction:column;gap:2mm;overflow:hidden">
      <div class="stit" style="font-size:15px;margin-bottom:1mm">מותג כדורגל בריטי<br>1924 — חוזר לשורשים</div>

      <div class="box bl" style="font-size:8px">
        <strong style="color:#001a3e">BLENDED SPORTS TECH AUTHORITY</strong><br>
        Umbro Israel מחזיקה ברישיון בלעדי לייצר, למכור ולשווק בישראל. אסטרטגיית v22: לבנות מותג הספורט הטכנולוגי-אותנטי של ישראל.<br>
        <span class="cf h">HIGH</span> CONF 0.93
      </div>

      <div>
        <h2 style="color:#001a3e">פוזישנינג 2026</h2>
        <ul style="font-size:8px">
          <li><strong>כדורגל:</strong> DNA המותג · קיטים B2B · 1,200+ מועדוני חובבים</li>
          <li><strong>ריצה + פאדל:</strong> 130+ מגרשים · ריקנות מותגית אותנטית</li>
          <li><strong>נשים:</strong> 55% שוק ≈ ₪3.5B — Umbro נוכחי 0 מוצרים</li>
          <li><strong>Heritage:</strong> אינגלנד 1924 · Diamond Logo · אסתטיקה אותנטית</li>
        </ul>
      </div>

      <div>
        <h2 style="color:#001a3e">Aitor Throup — אסתטיקת עיצוב</h2>
        <div class="box dk" style="font-size:7.5px">
          הלוגו ה-inverted של Aitor Throup עבור Umbro — הגדרה מחדש של DNA ספורטיבי דרך לנס אופנה. סמל ה-Double Diamond עצמו הוא העיצוב.<br>
          <span class="cf m">MED</span> CONF 0.82 · Design Direction Reference
        </div>
      </div>

      <div>
        <h2 style="color:#001a3e">D2C + B2B — מודל היברידי</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;font-size:7.5px">
          <div style="background:#eef1f8;border:1px solid #b0c0e8;border-radius:3px;padding:2mm;text-align:center">
            <div style="color:#001a3e;font-weight:800;margin-bottom:0.5mm">B2B</div>
            <div style="color:#444">קיטי קבוצות<br>₪150-320/unit<br>1,200+ clubs</div>
          </div>
          <div style="background:#eef1f8;border:1px solid #b0c0e8;border-radius:3px;padding:2mm;text-align:center">
            <div style="color:#1a7a4a;font-weight:800;margin-bottom:0.5mm">D2C</div>
            <div style="color:#444">Shopify Umbro.co.il<br>AOV ₪280-350<br>WhatsApp Drops</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Right: cover hero + KPI tiles -->
    <div style="display:flex;flex-direction:column;gap:2mm;height:100%">
      <div style="overflow:hidden;border-radius:4px;position:relative;flex:1;min-height:0">
        <img src="{umbro_cover_uri}" style="width:100%;height:100%;object-fit:cover;display:block;object-position:center 30%">
        <div style="position:absolute;top:0;left:0;right:0;background:linear-gradient(180deg,rgba(0,26,62,0.75) 0%,rgba(0,26,62,0) 45%)">
          <div style="padding:3mm 4mm;color:#fff">
            <div style="font-size:7px;letter-spacing:.15em;font-weight:800;text-transform:uppercase;opacity:.9">Umbro Israel · Cover Campaign</div>
            <div style="font-size:6px;opacity:.75">T1 Official Asset · CONF 0.97</div>
          </div>
        </div>
        <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(0deg,rgba(0,26,62,0.85) 0%,rgba(0,26,62,0) 60%);padding:3mm 4mm 2.5mm">
          <div style="display:flex;align-items:center;gap:2mm">
            <img src="{umbro_logo_uri}" style="height:7mm;width:auto;filter:brightness(0) invert(1)">
            <div style="color:#aac8ff;font-size:6.5px;font-weight:800">British Football Authority · Since 1924</div>
          </div>
        </div>
      </div>
      <!-- KPI strip below image -->
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2mm">
        <div style="background:#001a3e;border-radius:3px;padding:2mm;text-align:center">
          <div style="color:#aac8ff;font-size:6px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:0.5mm">שוק כדורגל</div>
          <div style="color:#fff;font-size:14px;font-weight:900">₪480M</div>
          <div style="color:#aac8ff;font-size:6px">ישראל 2025</div>
        </div>
        <div style="background:#003f8a;border-radius:3px;padding:2mm;text-align:center">
          <div style="color:#aac8ff;font-size:6px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:0.5mm">מועדוני B2B</div>
          <div style="color:#fff;font-size:14px;font-weight:900">1,200+</div>
          <div style="color:#aac8ff;font-size:6px">חובבים רשומים</div>
        </div>
        <div style="background:#1a4a8a;border-radius:3px;padding:2mm;text-align:center">
          <div style="color:#aac8ff;font-size:6px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:0.5mm">רישיון</div>
          <div style="color:#fff;font-size:14px;font-weight:900">בלעדי</div>
          <div style="color:#aac8ff;font-size:6px">IL · All Categories</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Strategy Anchor Ribbon -->
  <div style="margin-top:2.5mm;background:#001a3e;border-radius:3px;padding:2.5mm 4mm;display:flex;align-items:center;gap:8mm">
    <div style="color:#aac8ff;font-size:7px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;flex-shrink:0">חיבור לאסטרטגיה</div>
    <div style="width:1px;height:10px;background:rgba(255,255,255,0.2);flex-shrink:0"></div>
    <div style="color:#fff;font-size:8px">כדורגל בריטי אותנטי 1924 × B2B קיטי קבוצות ישראל × D2C Shopify Hybrid — תפוס עמדה "ספורט-טק" לפני כל מתחרה מקומי</div>
  </div>
</div>

<!-- עמוד 05: Umbro — Footvolley + LTAM — Template C NEW -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#001a3e,#1a4a8a)"><img src="{chrome_uri}" alt=""><span class="wm">05 — Umbro — Footvolley + LTAM B2B</span><span class="ey">Template C · Product Vision</span></div>
  <div class="stag" style="color:#1a4a8a">05 — UMBRO — FOOTVOLLEY × LTAM B2B · NEW PAGE</div>

  <!-- Template C: full-bleed hero top (65%) + 4-col grid (30%) -->
  <div style="position:relative;height:118mm;overflow:hidden;border-radius:4px;margin-bottom:2.5mm">
    <img src="{footvolley_uri}" style="width:100%;height:100%;object-fit:cover;display:block;object-position:center 40%">
    <!-- Overlay top-left: page title -->
    <div style="position:absolute;top:0;left:0;right:0;background:linear-gradient(180deg,rgba(0,26,62,0.82) 0%,rgba(0,26,62,0) 45%)">
      <div style="padding:4mm 5mm">
        <div style="color:#aac8ff;font-size:7px;font-weight:800;letter-spacing:.15em;text-transform:uppercase;margin-bottom:1mm">T1 · Official Campaign Visual · Season 2025</div>
        <div style="color:#fff;font-size:16px;font-weight:900;line-height:1.1">Footvolley × Street Football<br><span style="font-size:11px;font-weight:400;opacity:.85">קמפיין ראשי — Umbro Israel</span></div>
      </div>
    </div>
    <!-- Overlay bottom: key stats -->
    <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(0deg,rgba(0,26,62,0.9) 0%,rgba(0,26,62,0) 80%);padding:4mm 5mm 3mm">
      <div style="display:flex;gap:8mm;align-items:flex-end">
        <div style="color:#fff">
          <div style="font-size:7px;color:#aac8ff;letter-spacing:.1em;text-transform:uppercase">שוק כדורגל ישראל</div>
          <div style="font-size:18px;font-weight:900">1,200+</div>
          <div style="font-size:7px;color:#aac8ff">מועדוני חובבים · B2B</div>
        </div>
        <div style="width:1px;height:30px;background:rgba(255,255,255,0.25)"></div>
        <div style="color:#fff">
          <div style="font-size:7px;color:#aac8ff;letter-spacing:.1em;text-transform:uppercase">מגרשי פאדל</div>
          <div style="font-size:18px;font-weight:900">130+</div>
          <div style="font-size:7px;color:#aac8ff">↑30% גלובלי · ריקנות מותגית</div>
        </div>
        <div style="width:1px;height:30px;background:rgba(255,255,255,0.25)"></div>
        <div style="color:#fff">
          <div style="font-size:7px;color:#aac8ff;letter-spacing:.1em;text-transform:uppercase">AOV B2B קיט</div>
          <div style="font-size:18px;font-weight:900">₪229</div>
          <div style="font-size:7px;color:#aac8ff">ביתר · הפועל · 15+ קבוצות</div>
        </div>
        <div style="margin-right:auto;color:#fff">
          <div style="font-size:7px;color:#aac8ff;letter-spacing:.1em;text-transform:uppercase">CONF</div>
          <div style="font-size:13px;font-weight:800">0.93</div>
          <div style="font-size:7px;color:#aac8ff">HIGH · Data Bridge</div>
        </div>
      </div>
    </div>
  </div>

  <!-- LTAM B2B 4-col grid — v25 Brazil images -->
  <div style="margin-bottom:1.5mm">
    <div style="font-size:7px;font-weight:800;text-transform:uppercase;color:#003f8a;margin-bottom:1.5mm;letter-spacing:.08em">LTAM Collection — ברזיל × ישראל (B2B) · T2 Authentic Documentation</div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2mm">
      <div style="border-radius:4px;overflow:hidden;border:1.5px solid #003f8a;position:relative">
        <img src="{umbro_ltam_j_uri}" style="width:100%;height:28mm;object-fit:cover;display:block;object-position:center 30%">
        <div style="background:rgba(0,26,62,0.85);padding:1mm 2mm;text-align:center">
          <div style="color:#fff;font-size:6px;font-weight:700">LTAM Team Jerseys</div>
          <div style="color:#aac8ff;font-size:5.5px">קיטי קבוצות · B2B</div>
        </div>
      </div>
      <div style="border-radius:4px;overflow:hidden;border:1.5px solid #003f8a;position:relative">
        <img src="{brasil_tank_uri}" style="width:100%;height:28mm;object-fit:cover;display:block;object-position:center 25%">
        <div style="background:rgba(0,26,62,0.85);padding:1mm 2mm;text-align:center">
          <div style="color:#fff;font-size:6px;font-weight:700">Brasil Tank Mood</div>
          <div style="color:#aac8ff;font-size:5.5px">Street Style · LTAM</div>
        </div>
      </div>
      <div style="border-radius:4px;overflow:hidden;border:1.5px solid #003f8a;position:relative">
        <img src="{brasil_sunset_uri}" style="width:100%;height:28mm;object-fit:cover;display:block;object-position:center center">
        <div style="background:rgba(0,26,62,0.85);padding:1mm 2mm;text-align:center">
          <div style="color:#fff;font-size:6px;font-weight:700">Brasil Sunset Mood</div>
          <div style="color:#aac8ff;font-size:5.5px">Lifestyle · Campaign</div>
        </div>
      </div>
      <div style="border-radius:4px;overflow:hidden;border:1.5px solid #009c3b;position:relative">
        <img src="{swebo_brasil_uri}" style="width:100%;height:28mm;object-fit:cover;display:block;object-position:center 15%">
        <div style="background:rgba(0,80,30,0.9);padding:1mm 2mm;text-align:center">
          <div style="color:#fff;font-size:6px;font-weight:700">SWEBO Brasil · TikTok</div>
          <div style="color:#aaff99;font-size:5.5px">Ben Ben × Shaylee · Viral</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- עמוד 05b: Padel + Tennis — Template C NEW -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#003a1f,#006b3a)"><img src="{chrome_uri}" alt=""><span class="wm">05b — Padel × Tennis — שוק הרקטים</span><span class="ey">Template C · Product Vision</span></div>
  <div class="stag" style="color:#006b3a">05b — PADEL × TENNIS · UMBRO ISRAEL · ריקנות מותגית — 130+ מגרשים</div>

  <!-- Template C: full-bleed hero top -->
  <div style="position:relative;height:110mm;overflow:hidden;border-radius:4px;margin-bottom:2.5mm">
    <img src="{padel_court_uri}" style="width:100%;height:100%;object-fit:cover;display:block;object-position:center 40%">
    <div style="position:absolute;top:0;left:0;right:0;background:linear-gradient(180deg,rgba(0,40,20,0.85) 0%,rgba(0,40,20,0) 50%)">
      <div style="padding:4mm 5mm">
        <div style="color:#a0e8c0;font-size:7px;font-weight:800;letter-spacing:.15em;text-transform:uppercase;margin-bottom:1mm">Umbro Israel · פאדל + טניס · ריקנות מותגית</div>
        <div style="color:#fff;font-size:16px;font-weight:900;line-height:1.1">Padel × Tennis<br><span style="font-size:11px;font-weight:400;opacity:.85">130+ מגרשים · 0 מותגים אותנטיים · הזדמנות</span></div>
      </div>
    </div>
    <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(0deg,rgba(0,40,20,0.92) 0%,rgba(0,40,20,0) 75%);padding:4mm 5mm 3mm">
      <div style="display:flex;gap:8mm;align-items:flex-end">
        <div style="color:#fff">
          <div style="font-size:7px;color:#a0e8c0;letter-spacing:.1em;text-transform:uppercase">מגרשי פאדל ישראל</div>
          <div style="font-size:18px;font-weight:900">130+</div>
          <div style="font-size:7px;color:#a0e8c0">↑30% גלובלי שנתי</div>
        </div>
        <div style="width:1px;height:30px;background:rgba(255,255,255,0.25)"></div>
        <div style="color:#fff">
          <div style="font-size:7px;color:#a0e8c0;letter-spacing:.1em;text-transform:uppercase">AOV ציוד פאדל</div>
          <div style="font-size:18px;font-weight:900">₪450-900</div>
          <div style="font-size:7px;color:#a0e8c0">רקטה + נעלים + תיק</div>
        </div>
        <div style="width:1px;height:30px;background:rgba(255,255,255,0.25)"></div>
        <div style="color:#fff">
          <div style="font-size:7px;color:#a0e8c0;letter-spacing:.1em;text-transform:uppercase">שוק ספורט רקטות IL</div>
          <div style="font-size:18px;font-weight:900">₪180M</div>
          <div style="font-size:7px;color:#a0e8c0">TAM שנתי · CAGR 18%</div>
        </div>
        <div style="margin-right:auto;color:#fff">
          <div style="font-size:7px;color:#a0e8c0;letter-spacing:.1em;text-transform:uppercase">CONF</div>
          <div style="font-size:13px;font-weight:800">0.78</div>
          <div style="font-size:7px;color:#a0e8c0">MED · שוק מאמת</div>
        </div>
      </div>
    </div>
  </div>

  <!-- 3-col padel images grid — v24 new images -->
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2.5mm">
    <div style="border-radius:4px;overflow:hidden;border:1.5px solid #006b3a;position:relative">
      <img src="{padel_celeb_uri}" style="width:100%;height:32mm;object-fit:cover;display:block;object-position:center center">
      <div style="background:rgba(0,40,20,0.88);padding:1.5mm 2mm;text-align:center">
        <div style="color:#fff;font-size:6.5px;font-weight:700">Padel — ניצחון</div>
        <div style="color:#a0e8c0;font-size:5.5px">חגיגה · קהילה · רגש</div>
      </div>
    </div>
    <div style="border-radius:4px;overflow:hidden;border:1.5px solid #006b3a;position:relative">
      <img src="{padel_court2_uri}" style="width:100%;height:32mm;object-fit:cover;display:block;object-position:center center">
      <div style="background:rgba(0,40,20,0.88);padding:1.5mm 2mm;text-align:center">
        <div style="color:#fff;font-size:6.5px;font-weight:700">Women's Court</div>
        <div style="color:#a0e8c0;font-size:5.5px">נשים · 55% שוק · הזדמנות ראשית</div>
      </div>
    </div>
    <div style="border-radius:4px;overflow:hidden;border:1.5px solid #006b3a;position:relative">
      <img src="{crossover_uri}" style="width:100%;height:32mm;object-fit:cover;display:block;object-position:center center">
      <div style="background:rgba(0,40,20,0.88);padding:1.5mm 2mm;text-align:center">
        <div style="color:#fff;font-size:6.5px;font-weight:700">Crossover Tennis</div>
        <div style="color:#a0e8c0;font-size:5.5px">Visor · Tennis × Padel Lifestyle</div>
      </div>
    </div>
  </div>
</div>

<!-- עמוד 06: Ed Hardy — Renaissance — Template B -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a0033,#5b1fa8)"><img src="{chrome_uri}" alt=""><span class="wm">06 — Ed Hardy — Renaissance</span><span class="ey">Template B · Strategy</span></div>
  <div class="stag" style="color:#5b1fa8">06 — ED HARDY ISRAEL — RENAISSANCE · Y2K × TATTOO-FLASH × GEN-Z</div>

  <!-- Template B: text left (40%) | LAFW image right (60%) -->
  <div style="display:grid;grid-template-columns:2fr 3fr;gap:3mm;height:155mm">
    <div style="display:flex;flex-direction:column;gap:2mm;overflow:hidden">
      <div style="display:flex;align-items:center;gap:2.5mm;margin-bottom:1mm">
        <img src="{ed_logo_uri}" alt="Ed Hardy" style="height:10mm;object-fit:contain;filter:invert(20%) sepia(80%) saturate(2000%) hue-rotate(250deg) brightness(60%)">
        <div class="stit" style="font-size:14px;margin:0">Y2K Revival<br><span style="font-size:10px;font-weight:400;color:#5b1fa8">תל אביב × Tattoo Culture</span></div>
      </div>

      <div class="box" style="font-size:8px;border-right-color:#5b1fa8">
        <strong>DES-001 — Clean Front + Bold Back™</strong><br>
        חזית נקייה/מינימלית → גב מלא בפלאש-טאטו מרהיב<br>
        מאומת ע"ב 2,400+ מוצרי Ed Hardy + Barrow IL בנצ'מרק<br>
        <span class="cf h">HIGH</span> CONF 0.97
      </div>

      <div>
        <h2 style="border-right-color:#5b1fa8">קהל יעד + פוזישנינג</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;font-size:7.5px">
          <div style="background:#1a0033;border-radius:3px;padding:2mm;text-align:center">
            <div style="color:#d6c6f0;font-weight:800;margin-bottom:0.5mm">קהל ראשוני</div>
            <div style="color:#fff">גיל 18-28<br>ת"א + גוש דן<br>לילה · טאטו</div>
          </div>
          <div style="background:#2a0055;border-radius:3px;padding:2mm;text-align:center">
            <div style="color:#d6c6f0;font-weight:800;margin-bottom:0.5mm">טווח מחיר</div>
            <div style="color:#fff">חולצה: ₪250-320<br>קפוצ׳ון: ₪380-480<br>חבילה: ₪500+</div>
          </div>
        </div>
      </div>

      <div>
        <h2 style="border-right-color:#5b1fa8">הזדמנות בלעדית — חמסה</h2>
        <div class="box go" style="font-size:7.5px">
          <strong>חמסה × Tattoo-Flash — עיצוב בלעדי לישראל</strong><br>
          גשר בין Y2K לתרבות ישראלית עמוקה<br>
          לא קיים בקולקציה הגלובלית<br>
          <span class="cf m">MED</span> CONF 0.78 · לאמת IP עם Hardy Way LLC
        </div>
      </div>

      <div>
        <h2 style="border-right-color:#5b1fa8">KPIs — Ed Hardy</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5mm;font-size:7.5px">
          <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center"><strong>CVR M1</strong><br><span style="color:#5b1fa8;font-weight:800">0.8-1.2%</span><br><span class="cf m">MED</span></div>
          <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center"><strong>CVR M6+</strong><br><span style="color:#1a7a4a;font-weight:800">1.8-2.4%</span><br><span class="cf m">MED</span></div>
          <div style="background:#f0eaf9;padding:2mm;border-radius:3px;text-align:center"><strong>חוזרים</strong><br><span style="color:#c49a2a;font-weight:800">22%</span><br><span class="cf m">MED</span></div>
        </div>
      </div>
    </div>

    <!-- Right: product gallery top (2-col better images) + LAFW hero bottom — v24 clean -->
    <div style="display:flex;flex-direction:column;gap:2.5mm">
      <!-- Product gallery 2x2 — new hoodie images + tiger + barrow -->
      <div style="font-size:6px;font-weight:800;text-transform:uppercase;color:#5b1fa8;letter-spacing:.08em;margin-bottom:0.5mm">קולקציה — T2 Authentic Products · Eagle Skull Collection</div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.5mm">
        <div style="border-radius:3px;overflow:hidden;border:1.5px solid #5b1fa8;position:relative">
          <img src="{hoodie_front_uri}" style="width:100%;height:30mm;object-fit:cover;display:block;object-position:center top">
          <div style="background:rgba(26,0,51,0.9);padding:1mm;text-align:center">
            <div style="color:#fff;font-size:5.5px;font-weight:700">Skull Hoodie Front</div>
            <div style="color:#d6c6f0;font-size:5px">₪380-480</div>
          </div>
        </div>
        <div style="border-radius:3px;overflow:hidden;border:1.5px solid #5b1fa8;position:relative">
          <img src="{hoodie_back_uri}" style="width:100%;height:30mm;object-fit:cover;display:block;object-position:center top">
          <div style="background:rgba(26,0,51,0.9);padding:1mm;text-align:center">
            <div style="color:#fff;font-size:5.5px;font-weight:700">Eagle Skull Back</div>
            <div style="color:#d6c6f0;font-size:5px">Clean Front + Bold Back™</div>
          </div>
        </div>
        <div style="border-radius:3px;overflow:hidden;border:1.5px solid #7b3fcf;position:relative">
          <img src="{tiger_tee_uri}" style="width:100%;height:30mm;object-fit:cover;display:block;object-position:center top">
          <div style="background:rgba(26,0,51,0.9);padding:1mm;text-align:center">
            <div style="color:#fff;font-size:5.5px;font-weight:700">Tiger Tee</div>
            <div style="color:#d6c6f0;font-size:5px">₪260-320</div>
          </div>
        </div>
        <div style="border-radius:3px;overflow:hidden;border:1.5px solid #7b3fcf;position:relative">
          <img src="{barrow_uri}" style="width:100%;height:30mm;object-fit:cover;display:block;object-position:center center">
          <div style="background:rgba(26,0,51,0.9);padding:1mm;text-align:center">
            <div style="color:#fff;font-size:5.5px;font-weight:700">Barrow Collab</div>
            <div style="color:#d6c6f0;font-size:5px">Benchmark IL</div>
          </div>
        </div>
      </div>
      <!-- LAFW hero — takes remaining space -->
      <div style="overflow:hidden;border-radius:4px;position:relative;flex:1;min-height:55mm">
        <img src="{lafw_uri}" style="width:100%;height:100%;object-fit:cover;display:block;object-position:center top">
        <div style="position:absolute;top:0;left:0;right:0;background:linear-gradient(180deg,rgba(26,0,51,0.85) 0%,rgba(26,0,51,0) 45%)">
          <div style="padding:2.5mm 3mm">
            <div style="color:#d6c6f0;font-size:6.5px;letter-spacing:.12em;font-weight:800;text-transform:uppercase">T1 · LA Fashion Week · Gen-Z חזרה</div>
          </div>
        </div>
        <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(0deg,rgba(26,0,51,0.9) 0%,rgba(26,0,51,0) 70%);padding:2.5mm 3mm">
          <div style="color:rgba(255,255,255,0.75);font-size:6.5px">CONF 0.91 · Pinterest ↑340% · TikTok "Bring Back Ed Hardy" פעיל</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Strategy Anchor Ribbon -->
  <div style="margin-top:2.5mm;background:#1a0033;border-radius:3px;padding:2.5mm 4mm;display:flex;align-items:center;gap:8mm">
    <div style="color:#d6c6f0;font-size:7px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;flex-shrink:0">חיבור לאסטרטגיה</div>
    <div style="width:1px;height:10px;background:rgba(255,255,255,0.2);flex-shrink:0"></div>
    <div style="color:#fff;font-size:8px">Y2K Revival × Tattoo-Flash Art × WhatsApp D2C ישראל — AOV ₪380 × CVR M6 2.2% × חמסה בלעדי = חנות שמוכרת תרבות, לא רק בגדים</div>
  </div>
</div>

<!-- עמוד 07: Ed Hardy — Consumer Journey — Template A NEW -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a0033,#3a0066)"><img src="{chrome_uri}" alt=""><span class="wm">07 — Ed Hardy — Consumer Journey</span><span class="ey">Template A · WhatsApp D2C Map</span></div>
  <div class="stag" style="color:#5b1fa8">07 — ED HARDY — CONSUMER JOURNEY · WHATSAPP-FIRST D2C · NEW PAGE</div>
  <div class="stit" style="margin-bottom:2.5mm">מסלול הלקוח — 6 שלבים · WhatsApp × Instagram × Shopify</div>

  <div class="c2" style="align-items:start">
    <div>
      <!-- WhatsApp Journey SVG -->
      <div style="background:#f8f5fc;border:1px solid #d6c6f0;border-radius:5px;padding:3mm;overflow:hidden;max-height:148mm">
        <div style="font-size:7px;font-weight:800;text-transform:uppercase;color:#5b1fa8;margin-bottom:2mm;letter-spacing:.08em">מפת מסע הלקוח — Ed Hardy IL</div>
        <svg viewBox="0 0 240 310" style="width:100%;height:140mm;display:block" xmlns="http://www.w3.org/2000/svg">
          <!-- Stage 1: Discovery -->
          <rect x="10" y="5" width="220" height="40" rx="4" fill="#f0eaf9" stroke="#5b1fa8" stroke-width="1"/>
          <circle cx="28" cy="25" r="10" fill="#5b1fa8"/>
          <text x="28" y="29" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">1</text>
          <text x="44" y="19" font-size="8" fill="#1a0033" font-weight="bold">Discovery — גילוי</text>
          <text x="44" y="31" font-size="6.5" fill="#555">Instagram Reel / TikTok → Ed Hardy Y2K תוכן</text>
          <text x="44" y="41" font-size="6" fill="#888">פלטפורמה: Instagram · TikTok · CTR יעד 1.5-2.5%</text>
          <!-- Arrow -->
          <line x1="120" y1="45" x2="120" y2="55" stroke="#5b1fa8" stroke-width="1.5" stroke-dasharray="2,2"/>
          <polygon points="116,53 124,53 120,58" fill="#5b1fa8"/>
          <!-- Stage 2: Engage -->
          <rect x="10" y="58" width="220" height="40" rx="4" fill="#f0eaf9" stroke="#5b1fa8" stroke-width="1"/>
          <circle cx="28" cy="78" r="10" fill="#7b3fcf"/>
          <text x="28" y="82" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">2</text>
          <text x="44" y="72" font-size="8" fill="#1a0033" font-weight="bold">Engage — מעורבות</text>
          <text x="44" y="84" font-size="6.5" fill="#555">DM → לינק WhatsApp Business קטלוג</text>
          <text x="44" y="94" font-size="6" fill="#888">WhatsApp: 99% חדירה ישראל · CONF 0.98</text>
          <!-- Arrow -->
          <line x1="120" y1="98" x2="120" y2="108" stroke="#5b1fa8" stroke-width="1.5" stroke-dasharray="2,2"/>
          <polygon points="116,106 124,106 120,111" fill="#5b1fa8"/>
          <!-- Stage 3: Intent -->
          <rect x="10" y="111" width="220" height="40" rx="4" fill="#eaf0f5" stroke="#1a3fa8" stroke-width="1"/>
          <circle cx="28" cy="131" r="10" fill="#1a3fa8"/>
          <text x="28" y="135" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">3</text>
          <text x="44" y="125" font-size="8" fill="#1a0033" font-weight="bold">Intent — כוונת רכישה</text>
          <text x="44" y="137" font-size="6.5" fill="#555">ייעוץ מידות בוואטסאפ + תמונות מוצר</text>
          <text x="44" y="147" font-size="6" fill="#888">Shopify: AOV ₪380 · CVR cold 1.1% warm 2.2%</text>
          <!-- Arrow -->
          <line x1="120" y1="151" x2="120" y2="161" stroke="#1a3fa8" stroke-width="1.5" stroke-dasharray="2,2"/>
          <polygon points="116,159 124,159 120,164" fill="#1a3fa8"/>
          <!-- Stage 4: Close -->
          <rect x="10" y="164" width="220" height="40" rx="4" fill="#e8f5ee" stroke="#1a7a4a" stroke-width="1.5"/>
          <circle cx="28" cy="184" r="10" fill="#1a7a4a"/>
          <text x="28" y="188" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">4</text>
          <text x="44" y="178" font-size="8" fill="#1a0033" font-weight="bold">Close — סגירת עסקה</text>
          <text x="44" y="190" font-size="6.5" fill="#555">Shopify + Bit/PayPlus → אישור WhatsApp</text>
          <text x="44" y="200" font-size="6" fill="#888">RS 8% מופעל · CONF 0.91 · מרווח גולמי 64%</text>
          <!-- Arrow -->
          <line x1="120" y1="204" x2="120" y2="214" stroke="#1a7a4a" stroke-width="1.5" stroke-dasharray="2,2"/>
          <polygon points="116,212 124,212 120,217" fill="#1a7a4a"/>
          <!-- Stage 5: Repeat -->
          <rect x="10" y="217" width="220" height="40" rx="4" fill="#fdf3d8" stroke="#c49a2a" stroke-width="1"/>
          <circle cx="28" cy="237" r="10" fill="#c49a2a"/>
          <text x="28" y="241" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">5</text>
          <text x="44" y="231" font-size="8" fill="#1a0033" font-weight="bold">Repeat — רכישה חוזרת</text>
          <text x="44" y="243" font-size="6.5" fill="#555">Unboxing Story → Klaviyo Welcome Series</text>
          <text x="44" y="253" font-size="6" fill="#888">חוזרים יעד 22% · Klaviyo Flow 5 מיילים</text>
          <!-- Arrow -->
          <line x1="120" y1="257" x2="120" y2="267" stroke="#c49a2a" stroke-width="1.5" stroke-dasharray="2,2"/>
          <polygon points="116,265 124,265 120,270" fill="#c49a2a"/>
          <!-- Stage 6: Refer -->
          <rect x="10" y="270" width="220" height="38" rx="4" fill="#ffeaea" stroke="#c41414" stroke-width="1"/>
          <circle cx="28" cy="289" r="10" fill="#c41414"/>
          <text x="28" y="293" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">6</text>
          <text x="44" y="283" font-size="8" fill="#1a0033" font-weight="bold">Refer — הפניה</text>
          <text x="44" y="295" font-size="6.5" fill="#555">קוד הפניה WhatsApp → חמסה Drop בלעדי</text>
          <text x="44" y="305" font-size="6" fill="#888">Viral Loop: UGC → ↑CTR × ↑CVR × ↓CAC</text>
        </svg>
      </div>
    </div>

    <div>
      <h2>ניתוח מסע — נקודות מפתח</h2>
      <div class="box" style="font-size:8px;margin-bottom:2mm;border-right-color:#5b1fa8">
        <strong>למה WhatsApp-First?</strong><br>
        ישראל = 99% חדירת WhatsApp (ISOC-IL 2025). אין עוד שוק בעולם עם כזה יתרון לערוץ זה.<br>
        WhatsApp Commerce = CAC נמוך + CVR גבוה + LTV מוגבה<br>
        <span class="cf h">HIGH</span> CONF 0.94
      </div>

      <h2 style="margin-top:2mm">KPIs לפי שלב</h2>
      <table style="font-size:7.5px">
        <thead><tr><th>שלב</th><th>מדד</th><th>יעד</th><th>CONF</th></tr></thead>
        <tbody>
          <tr><td>1 · Discovery</td><td>CTR</td><td>1.5-2.5%</td><td><span class="cf m">MED</span></td></tr>
          <tr><td>2 · Engage</td><td>DM → WA</td><td>35-55%</td><td><span class="cf m">MED</span></td></tr>
          <tr><td>3 · Intent</td><td>Cart Add</td><td>18-28%</td><td><span class="cf m">MED</span></td></tr>
          <tr><td>4 · Close</td><td>CVR</td><td>1.1-2.2%</td><td><span class="cf m">MED</span></td></tr>
          <tr><td>5 · Repeat</td><td>90d Return</td><td>22%</td><td><span class="cf m">MED</span></td></tr>
          <tr><td>6 · Refer</td><td>Referral Rate</td><td>8-12%</td><td><span class="cf l">RISK</span></td></tr>
        </tbody>
      </table>

      <div class="box go" style="font-size:8px;margin-top:2mm">
        <strong>Klaviyo Welcome Series — 5 מיילים:</strong><br>
        M1: ברוכים הבאים + סיפור Ed Hardy<br>
        M3: תרבות הטאטו + Don Ed Hardy<br>
        M7: Drop בלעדי — חמסה ראשון<br>
        M14: UGC Social Proof + Review Request<br>
        M30: Referral Code + VIP Club
      </div>

      <div class="box re" style="font-size:7.5px;margin-top:2mm">
        <span class="cf l">RISK</span> <strong>IP — לאמת לפני השקה</strong><br>
        Hardy Way LLC / Iconix Brand Group (Lancer Capital 2021) — לא ABG<br>
        לאמת שרישיון Intermax כולל D2C ו-WhatsApp Commerce
      </div>
    </div>
  </div>
</div>

<!-- עמוד 08: Channel Strategy — Intermax Hub -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#1a3a00,#c49a2a)"><img src="{chrome_uri}" alt=""><span class="wm">08 — Channel Strategy — Intermax Group Hub</span><span class="ey">Multi-Brand Strategy</span></div>
  <div class="stag" style="color:#c49a2a">08 — CHANNEL STRATEGY — INTERMAX GROUP HUB · MULTI-BRAND</div>
  <div class="stit">intermax.co.il · 6 מותגים · Fast Simon AI · נאמנות רב-מותגית</div>

  <div style="background:#fdf3d8;border:1px solid #e8cc80;border-radius:5px;padding:2.5mm 3mm;margin-bottom:2.5mm;font-size:8px">
    <strong style="color:#7a5a10">פורטפוליו מותגים — Hub 2026:</strong>
    <span style="color:#444"> Ed Hardy · Umbro · Replay Jeans · Steve Madden · Lee Cooper · Pepe Jeans</span><br>
    <span style="color:#888;font-size:7px">תקציב ראשי M1-M6: Intermax Hub (70%) — כניסה לשוק ורכישת נתונים | Ed Hardy + Umbro: תשתית מיתוגית ועיצוב חזון → M7+: תקציבים ממוקדים מבוססי דאטה לכל מותג</span>
  </div>

  <div class="c2">
    <div>
      <h2>אסטרטגיית ערוצים M1-M6</h2>
      <div class="box go" style="font-size:8px;margin-bottom:2mm">
        <strong>Hub-First — מדיה מרכזית M1-M6:</strong><br>
        · Meta Ads (Facebook + Instagram) — ₪20,000/חודש תקציב מדיה<br>
        · Fast Simon AI — חיפוש חכם + המלצות cross-brand<br>
        · Klaviyo Flows — אימייל + SMS, עגלה נטושה<br>
        · WhatsApp Business — ערוץ D2C ראשי לכל מותג
      </div>

      <h2>3 חנויות Shopify — מבנה</h2>
      <div style="display:grid;grid-template-columns:1fr;gap:1.5mm;font-size:8px">
        <div style="background:#f5f0fc;border:1px solid #d6c6f0;border-radius:3px;padding:2mm 3mm">
          <strong style="color:#5b1fa8">Ed Hardy Israel</strong> — Y2K · Tattoo-Flash · D2C ראשי
        </div>
        <div style="background:#eaf0fc;border:1px solid #b0c0e8;border-radius:3px;padding:2mm 3mm">
          <strong style="color:#1a3fa8">Umbro Israel</strong> — Sports Authority · B2B + D2C Hybrid
        </div>
        <div style="background:#fdf6e3;border:1px solid #e8cc80;border-radius:3px;padding:2mm 3mm">
          <strong style="color:#c49a2a">Intermax Hub</strong> — 6 מותגים · Cross-Brand Loyalty · Fast Simon
        </div>
      </div>

      <h2 style="margin-top:2mm">הרחבת ערוצים — M7+</h2>
      <table style="font-size:7.5px">
        <thead><tr><th>ערוץ</th><th>חודש</th><th>תקציב</th></tr></thead>
        <tbody>
          <tr><td>Google Shopping</td><td>M7</td><td>₪47,580</td></tr>
          <tr><td>TikTok Ads</td><td>M9</td><td>₪67,600</td></tr>
          <tr><td>Google Performance Max</td><td>M8</td><td>₪50,840</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h2>Fast Simon AI — יתרון תחרותי</h2>
      <div class="box bl" style="font-size:8px;margin-bottom:2mm">
        <strong>AI-Powered Cross-Brand Discovery:</strong><br>
        · חיפוש חכם: לקוח מחפש "קפוצ'ון" → רואה Ed Hardy + Umbro + Replay<br>
        · המלצות אוטומטיות: "קנו יחד" cross-brand<br>
        · Personalization: פרופיל לקוח × 6 מותגים<br>
        <span class="cf m">MED</span> CONF 0.82 · Fast Simon IL Case Studies
      </div>

      <h2>נאמנות רב-מותגית — Cross-Brand Loyalty</h2>
      <ul style="font-size:8px">
        <li><strong>נקודות:</strong> כל רכישה בכל מותג → נקודות ב-Hub</li>
        <li><strong>VIP Tier:</strong> ₪2,000+ בשנה → הנחה 10% + WhatsApp Drops</li>
        <li><strong>Cross-Sell Trigger:</strong> קנה Umbro → קבל עיסקת Ed Hardy</li>
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
        <div class="kpi go"><div class="kl">מרווח גולמי Intermax</div><div class="kv">64%</div><div class="ks">מרווח שולי 46.6% · ROAS איזון 2.15×</div></div>
        <div class="kpi rd"><div class="kl">נ.א. M1 הכנסה</div><div class="kv sm">{fmt(m1_be)}</div><div class="ks">בסיס 90% GM − RS 8%</div></div>
        <div class="kpi"><div class="kl">הכנסה בפועל M1</div><div class="kv sm">{fmt(m1_rev)}</div><div class="ks">שלב למידה — לפי תקציב</div></div>
        <div class="kpi gn"><div class="kl">ציר סבלנות</div><div class="kv">5</div><div class="ks">חודשים עד רווחיות ראשונה</div></div>
      </div>
      <h2>נוסחת נקודת האיזון — מרווח גולמי 64%</h2>
      <div class="box go" style="font-size:8.5px;margin-top:1mm">
        <strong>GM = 64% · מרווח שולי (CM) = 46.6% · ROAS איזון = 2.15×</strong><br>
        <span style="font-size:7.5px;color:#555">GM 64% → CM 46.6% (לאחר עלויות משתנות) → BE ROAS = 1÷0.466 = 2.15×</span><br><br>
        <strong>נוסחת תקציב LGG (מוסכמת):</strong> הכנסות מינימום = (LGG + מדיה + קריאטיב + Ext + הוצ׳) ÷ 0.82<br>
        <strong>דוגמה M1:</strong> (₪8,000 + ₪11,220 + ₪780 + ₪715 + ₪1,200) ÷ 0.82 = <strong>{fmt(m1_be)}</strong><br>
        <strong>הכנסה בפועל M1: {fmt(m1_rev)}</strong> — שלב למידה, הצפי ל-M5 הוא חצייה של נקודת האיזון
      </div>
      <div class="box gn" style="margin-top:1.5mm;font-size:8px">
        <strong>M5 — חציית נקודת האיזון (תרחיש בסיס Intermax Hub):</strong><br>
        הכנסה M5: <strong>{fmt(m5_rev)}</strong> | נ.א. M5: <strong>{fmt(m5_be)}</strong><br>
        מ-M5 ואילך — ההכנסה עוברת את נקודת האיזון ב-90% מרווח גולמי. <span class="cf h">HIGH</span>
      </div>
      <div style="margin-top:1.5mm;background:#fff8e8;border:1px solid #e8cc80;border-radius:4px;padding:2mm;font-size:7.5px">
        <strong style="color:#7a5a10">Ed Hardy D2C Y1 — שני תרחישים (מדוח LGG הרשמי):</strong><br>
        ✓ <strong>אופטימי:</strong> הכנסה ₪1,084,800 · רווח תפעולי <strong style="color:#1a7a4a">₪49,480</strong><br>
        ⚠ <strong>ריאלי (Base Case):</strong> הכנסה ₪1,084,800 · תוצאה תפעולית <strong style="color:#c41414">-₪11,540</strong><br>
        פער בין תרחישים: ₪61,020 | נקודת איזון אמיתית: M11 (לא M5)<br>
        <span style="color:#888">מקור: LosGardiosGroup_EdHardy_Israel_OfficialReport_2026.pdf § 25</span>
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
        <span class="cf m">MED</span> <strong>✓ = הכנסה מעל נקודת האיזון (תקציב LGG ÷ 0.82).</strong><br>
        GM Intermax = 64% · CM = 46.6% · ROAS BE = 2.15× · RS מוסכם = 8% על כל ההכנסות ברוטו<br>
        <span style="font-size:7px;color:#666">מקור: תכנית עסקית Intermax × LGG 2026-2027</span>
      </div>
    </div>
  </div>
</div>

<!-- עמוד 7: Blended 3-Year Potential -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#0a0a1e,#1a1a2e)"><img src="{chrome_uri}" alt=""><span class="wm">06 — פוטנציאל מקסימלי — תחזית 3 שנים</span><span class="ey">Blended Maximum Potential</span></div>
  <div class="stag" style="color:#c49a2a">06 — BLENDED 3-YEAR REVENUE POTENTIAL — INTERMAX × LGG</div>
  <div class="stit">תחזית משולבת: Intermax Hub + Ed Hardy Israel + Umbro Israel | בסיס: זיכיון בלעדי ישראל</div>

  <!-- Budget Allocation Phase -->
  <div style="background:#0a0a1e;border-radius:6px;padding:3mm 4mm;margin-bottom:3mm;color:#fff;font-size:8px">
    <strong style="color:#c49a2a;font-size:9px">אסטרטגיית תקציב לפי שלב</strong>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;margin-top:2mm">
      <div style="background:#1a1a35;border-radius:4px;padding:2mm;border-left:3px solid #c49a2a">
        <div style="color:#c49a2a;font-weight:800;font-size:7.5px;margin-bottom:1mm">M1–M6 · בניית תשתית</div>
        <div style="color:#ddd;font-size:7.5px">Intermax Hub — ✦ תקציב ראשי<br>Ed Hardy + Umbro — מיתוג<br>מטרה: נתונים + חשיפה</div>
      </div>
      <div style="background:#1a1a35;border-radius:4px;padding:2mm;border-left:3px solid #5b8fff">
        <div style="color:#7ab0ff;font-weight:800;font-size:7.5px;margin-bottom:1mm">M7–M12 · מינוף דאטה</div>
        <div style="color:#ddd;font-size:7.5px">תקציבים מופרדים לכל מותג<br>קמפיינים ממוקדים מבוססי דאטה<br>מהאתר הראשי → מותגים</div>
      </div>
      <div style="background:#1a1a35;border-radius:4px;padding:2mm;border-left:3px solid #1a7a4a">
        <div style="color:#7adfc0;font-weight:800;font-size:7.5px;margin-bottom:1mm">Y2–Y3 · סקייל</div>
        <div style="color:#ddd;font-size:7.5px">כל מותג: תקציב עצמאי<br>נשים (Umbro) · Y2K (Ed Hardy)<br>Replay/Steve Madden מצטרפים</div>
      </div>
    </div>
  </div>

  <!-- 3-Year Revenue Table -->
  <div style="margin-bottom:3mm">
    <table style="width:100%;border-collapse:collapse;font-size:9px;direction:rtl">
      <thead>
        <tr style="background:#1a1a2e;color:#fff">
          <th style="padding:2mm;text-align:right">ערוץ הכנסה</th>
          <th style="padding:2mm;text-align:center;background:#1a3f6e">Y1 — 2026</th>
          <th style="padding:2mm;text-align:center;background:#0d3d2e">Y2 — 2027</th>
          <th style="padding:2mm;text-align:center;background:#3d1a1a">Y3 — 2028</th>
          <th style="padding:2mm;text-align:center;background:#3d3d1a;color:#e8cc80">נימוק</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#f0f7fe">
          <td style="padding:2mm;font-weight:700;color:#1a3fa8">Ed Hardy Israel D2C</td>
          <td style="padding:2mm;text-align:center;font-weight:700;color:#1a3fa8">₪1,085,000</td>
          <td style="padding:2mm;text-align:center;color:#0d4d3e;font-weight:700">₪1,900,000</td>
          <td style="padding:2mm;text-align:center;color:#6b1a1a;font-weight:700">₪2,700,000</td>
          <td style="padding:2mm;font-size:7.5px;color:#555">Y2K חלון 12-18 חודש · AOV ₪520 · Barrow קרס</td>
        </tr>
        <tr style="background:#f2fff8">
          <td style="padding:2mm;font-weight:700;color:#1a7a4a">Umbro Israel D2C + B2B</td>
          <td style="padding:2mm;text-align:center;font-weight:700;color:#1a3fa8">₪1,100,000</td>
          <td style="padding:2mm;text-align:center;color:#0d4d3e;font-weight:700">₪2,400,000</td>
          <td style="padding:2mm;text-align:center;color:#6b1a1a;font-weight:700">₪4,200,000</td>
          <td style="padding:2mm;font-size:7.5px;color:#555">נשים ×2 · פאדל ריקנות · Holmes Place B2B · שוק ₪6.35B</td>
        </tr>
        <tr style="background:#fdfbf0">
          <td style="padding:2mm;font-weight:700;color:#7a5a10">Intermax Hub + מותגים נוספים</td>
          <td style="padding:2mm;text-align:center;font-weight:700;color:#1a3fa8">₪400,000</td>
          <td style="padding:2mm;text-align:center;color:#0d4d3e;font-weight:700">₪750,000</td>
          <td style="padding:2mm;text-align:center;color:#6b1a1a;font-weight:700">₪1,200,000</td>
          <td style="padding:2mm;font-size:7.5px;color:#555">Replay/Steve Madden M7+, מכירות צולבות 15%</td>
        </tr>
        <tr style="background:#1a1a2e;color:#fff;font-weight:800">
          <td style="padding:2mm">סה"כ הכנסות Blended</td>
          <td style="padding:2mm;text-align:center;color:#7ab0ff;font-size:11px">₪2,585,000</td>
          <td style="padding:2mm;text-align:center;color:#7adfc0;font-size:11px">₪5,050,000</td>
          <td style="padding:2mm;text-align:center;color:#f0b080;font-size:11px">₪8,100,000</td>
          <td style="padding:2mm;color:#aaa;font-size:7.5px">×1.95 Y1→Y2 · ×1.60 Y2→Y3</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- LGG Revenue from Project -->
  <div class="c2" style="gap:3mm;margin-bottom:2mm">
    <div>
      <h2 style="font-size:10px;margin-bottom:1.5mm">הכנסות LGG מהפרויקט</h2>
      <table style="width:100%;border-collapse:collapse;font-size:8.5px;direction:rtl">
        <thead>
          <tr style="background:#1a1a2e;color:#fff">
            <th style="padding:1.5mm">מרכיב</th>
            <th style="padding:1.5mm;text-align:center">Y1</th>
            <th style="padding:1.5mm;text-align:center">Y2</th>
            <th style="padding:1.5mm;text-align:center">Y3</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#f5f0ff">
            <td style="padding:1.5mm">RS 8% על הכנסות</td>
            <td style="padding:1.5mm;text-align:center;color:#5b1fa8;font-weight:700">₪206,800</td>
            <td style="padding:1.5mm;text-align:center;color:#5b1fa8;font-weight:700">₪404,000</td>
            <td style="padding:1.5mm;text-align:center;color:#5b1fa8;font-weight:700">₪648,000</td>
          </tr>
          <tr style="background:#fdf3d8">
            <td style="padding:1.5mm">Retainer (3 ערוצים × ₪8K)</td>
            <td style="padding:1.5mm;text-align:center;color:#7a5a10;font-weight:700">₪288,000</td>
            <td style="padding:1.5mm;text-align:center;color:#7a5a10;font-weight:700">₪288,000</td>
            <td style="padding:1.5mm;text-align:center;color:#7a5a10;font-weight:700">₪288,000</td>
          </tr>
          <tr style="background:#1a1a2e;color:#fff;font-weight:800">
            <td style="padding:1.5mm">סה"כ LGG</td>
            <td style="padding:1.5mm;text-align:center;color:#e8cc80;font-size:10px">₪494,800</td>
            <td style="padding:1.5mm;text-align:center;color:#e8cc80;font-size:10px">₪692,000</td>
            <td style="padding:1.5mm;text-align:center;color:#e8cc80;font-size:10px">₪936,000</td>
          </tr>
        </tbody>
      </table>
      <div style="font-size:7px;color:#888;margin-top:1mm">LGG סה"כ 3 שנים: <strong style="color:#5b1fa8">~₪2,122,800</strong></div>
    </div>
    <div>
      <h2 style="font-size:10px;margin-bottom:1.5mm">תקרה תיאורטית — Umbro בלבד</h2>
      <div class="box bl" style="font-size:8px">
        <strong>0.5% מ-₪6.35B שוק ספורט = ₪31.75M</strong><br>
        זהו הסייל גלובלי המצוין במחקר. <span class="cf m">MED</span> טווח 5-7 שנים.<br><br>
        <strong>Y3 Umbro ₪4.2M = 0.066%</strong> מהשוק בלבד — שמרני מאוד, בר-השגה.<br><br>
        <span class="cf h">HIGH</span> כל 1% שוק = <strong>₪63.5M הכנסות Umbro</strong> — פוטנציאל ל-5-10 שנים.
      </div>
      <div class="box gn" style="font-size:8px;margin-top:2mm">
        <strong style="color:#1a7a4a">גורמי מכפיל Umbro</strong><br>
        ✓ נשים: 0→55% השוק — כפול כל KPI<br>
        ✓ פאדל: ריקנות מותגית — first mover<br>
        ✓ Holmes Place B2B: הכנסה חוזרת ₪0 CAC<br>
        ✓ Blended Sports Tech: 6 ענפים × AOV<br>
        ✓ זיכיון בלעדי: ייצור + מכירה + שיווק
      </div>
    </div>
  </div>

  <div style="background:#fdf3d8;border:1px solid #e8cc80;border-radius:4px;padding:2mm 3mm;font-size:7.5px;color:#7a5a10">
    <strong>הערה:</strong> תחזית Y1 Ed Hardy מציגה שני תרחישים: אופטימי ₪49,480 רווח | ריאלי (base case) -₪11,540 הפסד. חישוב מדויק בעמוד הפיננסי. Umbro: Y1 כולל B2B קיטים קיימים (ביתר + הפועל + בני יהודה) + D2C השקה. | מקור: LGG Research 2026 · Data Bridge 2024 · LosGardios Ed Hardy & Umbro Reports.
  </div>
</div>

<!-- עמוד 8: תחזית שנתית -->
<div class="page" style="padding:8mm 10mm 6mm">
  <div class="ph" style="margin:-8mm -10mm 3.5mm">
    <img src="{chrome_uri}" alt="">
    <span class="wm">07 — תחזית שנתית M0-M12</span>
    <span class="ey">Drive Format — All KPIs</span>
  </div>
  <div class="stag">07 — ANNUAL FORECAST (BASE SCENARIO)</div>
  <div class="stit" style="font-size:15px;margin-bottom:2.5mm">תחזית מלאה — כל ה-KPIs | M0 עד M12 | GM = 64% · CM = 46.6% · BE ROAS = 2.15× · RS = 8%</div>
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

<!-- עמוד 10: מסגרת אי-ודאות -->
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
<!-- עמוד 11: ההצעה -->
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
        <strong>נקודת האיזון — GM 64% · CM 46.6% · RS 8%:</strong><br>
        הכנסה מינימום LGG = (LGG + מדיה + קריאטיב + Ext + הוצ׳) ÷ 0.82<br>
        BE ROAS עסקי = 2.15× | GM גולמי = 64% | CM שולי = 46.6%
      </div>
    </div>
  </div>
</div>

<!-- עמוד 14: Closing CTA — Template C NEW -->
<div class="page">
  <div class="ph" style="background:linear-gradient(90deg,#0b1a2e,#001a3e)"><img src="{chrome_uri}" alt=""><span class="wm">14 — Closing CTA — סגירה</span><span class="ey">Template C · Community Vision</span></div>

  <!-- Template C inverted: lifestyle full-bleed TOP, CTA + signatures bottom -->
  <div style="position:relative;height:115mm;overflow:hidden;border-radius:4px;margin-bottom:3mm">
    <img src="{lifestyle_uri}" style="width:100%;height:100%;object-fit:cover;display:block;object-position:center 30%">
    <!-- Dark gradient overlay for text -->
    <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,10,30,0.4) 0%,rgba(0,10,30,0.85) 100%)">
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;width:80%">
        <div style="color:rgba(255,255,255,0.7);font-size:8px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:3mm">T3 · Community Vision · Lifestyle</div>
        <div style="color:#fff;font-size:28px;font-weight:900;line-height:1.1;margin-bottom:3mm">
          נבנה יחד<br><span style="font-size:18px;font-weight:400;opacity:.85">את ה-D2C של ישראל</span>
        </div>
        <div style="color:rgba(255,255,255,0.8);font-size:10px;max-width:420px;margin:0 auto;line-height:1.6">
          3 מותגים · Shopify × WhatsApp × Instagram · אסטרטגיה מוכחת · ציר סבלנות 5 חודשים
        </div>
      </div>
      <!-- Bottom logos -->
      <div style="position:absolute;bottom:3mm;left:4mm;right:4mm;display:flex;justify-content:space-between;align-items:center">
        <img src="{chrome_uri}" style="height:10mm;object-fit:contain;filter:brightness(0) invert(1);opacity:.85">
        <div style="color:rgba(255,255,255,0.5);font-size:7px;letter-spacing:.1em">INTERMAX × LOS GARDIOS GROUP · 2026</div>
        <img src="{seal_uri}" style="height:10mm;object-fit:contain;opacity:.75">
      </div>
    </div>
  </div>

  <!-- CTA + Quick Terms -->
  <div style="display:grid;grid-template-columns:2fr 1fr 1fr;gap:3mm;align-items:start">
    <div class="box dk" style="font-size:8px">
      <strong>הצעד הבא — 48 שעות:</strong><br>
      1. חתימה על מסמך זה ← אישור התנאים<br>
      2. העברת ₪20,000 תקציב M0 ← הקמת חנויות<br>
      3. Kickoff call — יום ראשון בשבוע הבא<br>
      4. M1 מתחיל — Live תוך 30 יום
    </div>
    <div style="text-align:center">
      <div style="font-size:7px;color:#888;text-transform:uppercase;letter-spacing:.1em;margin-bottom:1mm">RS שנה 1</div>
      <div style="font-size:24px;font-weight:900;color:#1a0033">8%</div>
      <div style="font-size:7px;color:#5b1fa8;font-weight:700">מהכנסות ברוטו</div>
      <div style="font-size:6.5px;color:#888;margin-top:0.5mm">CONF 0.99 · מוסכם</div>
    </div>
    <div style="text-align:center">
      <div style="font-size:7px;color:#888;text-transform:uppercase;letter-spacing:.1em;margin-bottom:1mm">ריטיינר / ערוץ</div>
      <div style="font-size:24px;font-weight:900;color:#001a3e">₪{CHANNEL_DISCOUNTED:,}</div>
      <div style="font-size:7px;color:#003f8a;font-weight:700">{CHANNEL_DISCOUNT_PCT}% הנחה</div>
      <div style="font-size:6.5px;color:#888;margin-top:0.5mm">CONF 0.99 · מוסכם</div>
    </div>
  </div>

  <!-- Visual footer — fill bottom space -->
  <div style="margin-top:5mm;display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:3mm">
    <div style="background:#001a3e;border-radius:4px;padding:3mm 3.5mm">
      <div style="color:#aac8ff;font-size:6px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:1mm">שלב 1 — הקמה</div>
      <div style="color:#fff;font-size:8px;font-weight:700">M0 · 2 שבועות</div>
      <div style="color:#aac8ff;font-size:6.5px;margin-top:0.5mm">Shopify × 3 + Pixel + Klaviyo</div>
    </div>
    <div style="background:#1a0033;border-radius:4px;padding:3mm 3.5mm">
      <div style="color:#d6c6f0;font-size:6px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:1mm">שלב 2 — קריאטיב</div>
      <div style="color:#fff;font-size:8px;font-weight:700">M0 · שבוע 3-4</div>
      <div style="color:#d6c6f0;font-size:6.5px;margin-top:0.5mm">6 Static × 3 מותגים + וידאו</div>
    </div>
    <div style="background:#1a3a00;border-radius:4px;padding:3mm 3.5mm">
      <div style="color:#a0e8a0;font-size:6px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:1mm">שלב 3 — השקה</div>
      <div style="color:#fff;font-size:8px;font-weight:700">M1 · CBO Broad</div>
      <div style="color:#a0e8a0;font-size:6.5px;margin-top:0.5mm">Meta Ads + WhatsApp D2C Live</div>
    </div>
    <div style="background:#7a5a10;border-radius:4px;padding:3mm 3.5mm">
      <div style="color:#ffe8a0;font-size:6px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:1mm">שלב 4 — צמיחה</div>
      <div style="color:#fff;font-size:8px;font-weight:700">M5 · Break-Even</div>
      <div style="color:#ffe8a0;font-size:6.5px;margin-top:0.5mm">חציית נ.א. · ROAS 3.48×</div>
    </div>
  </div>
</div>

<!-- עמוד 15: חתימה -->
<div class="page">
  <div class="ph"><img src="{chrome_uri}" alt=""><span class="wm">15 — אישור והתחייבות</span><span class="ey">Agreement &amp; Signature</span></div>
  <div class="stag">15 — AGREEMENT</div>
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
        ✓ מרווח גולמי Intermax: <strong>64%</strong> · CM 46.6% · BE ROAS <strong>2.15×</strong><br>
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
    © 2026 Los Gardios Group | ח.פ. 516819257 | losgardios.com | LGG-IMX-2026-001 | v23 | מסמך סודי — לא להפצה
  </div>
</div>

</body>
</html>""")

# ── כתיבת HTML + יצירת PDF ────────────────────────────────────────────────────
html = "".join(html_parts)
html_path = f"{S}/intermax-lgg-proposal-v28.html"
pdf_path  = f"{S}/intermax-lgg-proposal-v28.pdf"

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

import shutil
size = os.path.getsize(pdf_path)
print(f"PDF נוצר: {pdf_path} ({size//1024}KB)")
# העתק לתיקיית הפרויקט
dest = "/home/user/marketingskills/intermax-lgg-proposal-v28.pdf"
shutil.copy2(pdf_path, dest)
print(f"הועתק ל: {dest}")
