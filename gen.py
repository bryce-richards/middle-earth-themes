import json, os

OUT = "/home/claude/middle-earth/themes"
os.makedirs(OUT, exist_ok=True)

def mix(c1, c2, t):
    c1 = c1.lstrip("#"); c2 = c2.lstrip("#")
    r = round(int(c1[0:2],16)*(1-t)+int(c2[0:2],16)*t)
    g = round(int(c1[2:4],16)*(1-t)+int(c2[2:4],16)*t)
    b = round(int(c1[4:6],16)*(1-t)+int(c2[4:6],16)*t)
    return "#%02x%02x%02x" % (r,g,b)

def fg_on(c):
    c = c.lstrip("#")
    lum = 0.2126*int(c[0:2],16)+0.7152*int(c[2:4],16)+0.0722*int(c[4:6],16)
    return "#16140f" if lum > 150 else "#f3efe6"

BLACK="#000000"; WHITE="#ffffff"

# ---- derive structural UI shades when a palette omits them (new palettes) ----
def norm(p):
    dark = p["mode"] == "dark"
    bg, fg = p["bg"], p["fg"]
    def d(k, v): p.setdefault(k, v)
    if dark:
        d("bgDark", mix(bg, BLACK, 0.22)); d("bgDarker", mix(bg, BLACK, 0.40))
        d("bgTab", mix(bg, BLACK, 0.30)); d("border", mix(bg, BLACK, 0.55))
    else:
        d("bgDark", mix(bg, BLACK, 0.06)); d("bgDarker", mix(bg, BLACK, 0.13))
        d("bgTab", mix(bg, BLACK, 0.08)); d("border", mix(bg, BLACK, 0.20))
    d("lineHL", mix(bg, fg, 0.06))
    d("listActive", mix(bg, fg, 0.13)); d("listHover", mix(bg, fg, 0.07))
    d("indent", mix(bg, fg, 0.16)); d("indentActive", p.get("gutter", mix(bg, fg, 0.35)))
    d("widgetBorder", mix(bg, fg, 0.16))
    d("selBase", mix(bg, p["accent"], 0.45))
    d("accentFg", fg_on(p["accent"]))
    d("variable", fg)
    return p

P = {}

# ============================ ORIGINAL FIVE ============================
P["shire-dark"] = dict(mode="dark", label="The Shire (Dark)", file="bag-end.ts", slug="shire",
    bg="#181d15", fg="#e6dfc8", bgDark="#14180f", bgDarker="#10130b", bgTab="#12160d",
    border="#0c0e08", lineHL="#1e2418", selBase="#334225", gutter="#4d573e", gutterActive="#c9b079",
    cursor="#e0b86a", accent="#5a8c4a", accentFg="#0f1209", statusBg="#2d3a23", statusFg="#dcd3b0",
    listActive="#2e3a22", listHover="#1e2418", indent="#2a3120", indentActive="#4d573e", widgetBorder="#2a3120",
    error="#cf6a52", warning="#e0b86a", info="#8cb36a",
    comment="#6f7d5b", keyword="#8cb36a", func="#e0b86a", string="#aebd83", number="#d2885c", typ="#c9dba6",
    variable="#e6dfc8", prop="#d8cfa8", operator="#9aa37a", constant="#c79a6a", thisKw="#c9b079", link="#9dc183")
P["shire-light"] = dict(mode="light", label="The Shire (Light)", file="bag-end.ts", slug="shire",
    bg="#f2e8cf", fg="#3d3c28", bgDark="#ece0c2", bgDarker="#e2d5b3", bgTab="#e8dbbb",
    border="#d8cba6", lineHL="#ebddbc", selBase="#d8c993", gutter="#b6a877", gutterActive="#8a5a28",
    cursor="#8a5a28", accent="#5a7a3a", accentFg="#f3ead2", statusBg="#5a7a3a", statusFg="#f3ead2",
    listActive="#ddd0a4", listHover="#e8dbbb", indent="#ddcfa6", indentActive="#b6a877", widgetBorder="#d8cba6",
    error="#a8442a", warning="#97632a", info="#5a7a3a",
    comment="#8f895f", keyword="#4a6b32", func="#97632a", string="#6a7a36", number="#a8542a", typ="#5a7a3a",
    variable="#3d3c28", prop="#57543a", operator="#6a6648", constant="#8a5a3a", thisKw="#8a5a28", link="#4a6b32")

P["rohan-dark"] = dict(mode="dark", label="Rohan (Dark)", file="edoras.ts", slug="rohan",
    bg="#1d1a12", fg="#ece0b8", bgDark="#17140c", bgDarker="#120f08", bgTab="#16140d",
    border="#0d0b06", lineHL="#221e14", selBase="#3f3a22", gutter="#5a5238", gutterActive="#d9a94a",
    cursor="#d9a94a", accent="#c9912f", accentFg="#1d1a12", statusBg="#6e3326", statusFg="#e7d8b0",
    listActive="#2f2a1a", listHover="#242014", indent="#322c1d", indentActive="#5a5238", widgetBorder="#322c1d",
    error="#c0503a", warning="#d9a94a", info="#8a9b52",
    comment="#7d6f50", keyword="#8a9b52", func="#d9a94a", string="#b0a05e", number="#b5503a", typ="#d8c98a",
    variable="#ece0b8", prop="#cabf90", operator="#9a8e62", constant="#c08a4a", thisKw="#c9a45a", link="#a8b56a")
P["rohan-light"] = dict(mode="light", label="Rohan (Light)", file="edoras.ts", slug="rohan",
    bg="#ece0b0", fg="#3a3220", bgDark="#e4d7a2", bgDarker="#d8c98a", bgTab="#e0d49a",
    border="#cbbb86", lineHL="#e3d69e", selBase="#d6c688", gutter="#b0a05e", gutterActive="#8a5a1e",
    cursor="#8a5a1e", accent="#97651e", accentFg="#f3ead2", statusBg="#8a3a28", statusFg="#f3e8d0",
    listActive="#ddcf90", listHover="#e3d69e", indent="#d4c688", indentActive="#b0a05e", widgetBorder="#cbbb86",
    error="#97402a", warning="#8a5a1e", info="#4a5e28",
    comment="#8a7e58", keyword="#4a5e28", func="#9a6b1e", string="#6e7330", number="#97402a", typ="#5a6e30",
    variable="#3a3220", prop="#57502e", operator="#6e6442", constant="#8a5a2a", thisKw="#8a5a1e", link="#4a5e28")

P["rivendell-dark"] = dict(mode="dark", label="Rivendell (Dark)", file="imladris.ts", slug="rivendell",
    bg="#14181f", fg="#d6dde6", bgDark="#11151c", bgDarker="#0d1016", bgTab="#0f131a",
    border="#080a0e", lineHL="#1b212a", selBase="#2a4452", gutter="#495260", gutterActive="#d4ac5e",
    cursor="#d4ac5e", accent="#4a8a9e", accentFg="#0d1016", statusBg="#2f5a6e", statusFg="#d6e2e8",
    listActive="#1e2630", listHover="#181e26", indent="#2a323d", indentActive="#495260", widgetBorder="#2a323d",
    error="#cf6a52", warning="#d4ac5e", info="#7fa8c4",
    comment="#5e6a78", keyword="#7fa8c4", func="#d4ac5e", string="#8fbfa8", number="#c98b6e", typ="#b3aed4",
    variable="#d6dde6", prop="#b8c2cc", operator="#8590a0", constant="#c98b6e", thisKw="#b3aed4", link="#7fbfd4")
P["rivendell-light"] = dict(mode="light", label="Rivendell (Light)", file="imladris.ts", slug="rivendell",
    bg="#e6eaee", fg="#2c333d", bgDark="#dce1e6", bgDarker="#ccd4dc", bgTab="#d8dee4",
    border="#c2cbd3", lineHL="#dde3e9", selBase="#cdd8e0", gutter="#9aa4b0", gutterActive="#2f6f86",
    cursor="#2f6f86", accent="#2f6f86", accentFg="#eef4f8", statusBg="#2f6f86", statusFg="#eef4f8",
    listActive="#cfdae2", listHover="#dde3e9", indent="#d0d8de", indentActive="#9aa4b0", widgetBorder="#c2cbd3",
    error="#a8442a", warning="#9a7224", info="#2f6f86",
    comment="#7a8694", keyword="#2f6f86", func="#9a7224", string="#3f7a68", number="#a25c3a", typ="#5a5a86",
    variable="#2c333d", prop="#50596a", operator="#6a7484", constant="#a25c3a", thisKw="#5a5a86", link="#2f6f86")

P["lothlorien-dark"] = dict(mode="dark", label="Lothlórien (Dark)", file="caras-galadhon.ts", slug="lorien",
    bg="#181610", fg="#ece2c0", bgDark="#141209", bgDarker="#100e07", bgTab="#131109",
    border="#070600", lineHL="#211e13", selBase="#3a3a1e", gutter="#5a5640", gutterActive="#e6c15c",
    cursor="#e6c15c", accent="#5a7a3a", accentFg="#0e0c06", statusBg="#4a5e2e", statusFg="#ece2c0",
    listActive="#2a2614", listHover="#201d12", indent="#322d1b", indentActive="#5a5640", widgetBorder="#322d1b",
    error="#cf6a52", warning="#e6c15c", info="#9bbf9a",
    comment="#6e7a62", keyword="#9bbf9a", func="#e6c15c", string="#c8c184", number="#a9c2bd", typ="#c9d4c0",
    variable="#ece2c0", prop="#d2caa4", operator="#9a9670", constant="#cdb06a", thisKw="#c8c184", link="#9bbf9a")
P["lothlorien-light"] = dict(mode="light", label="Lothlórien (Light)", file="caras-galadhon.ts", slug="lorien",
    bg="#f0e7c4", fg="#34381f", bgDark="#e8ddb4", bgDarker="#dccf9e", bgTab="#e4d9ac",
    border="#cdc090", lineHL="#e7dcab", selBase="#dccf96", gutter="#b0a86e", gutterActive="#8a6b1e",
    cursor="#8a6b1e", accent="#5a7a3a", accentFg="#f3ead2", statusBg="#4f6e3e", statusFg="#f3ead2",
    listActive="#ddd09e", listHover="#e7dcab", indent="#d8cc94", indentActive="#b0a86e", widgetBorder="#cdc090",
    error="#a8442a", warning="#9a7a1e", info="#4f6e3e",
    comment="#84876a", keyword="#4f6e3e", func="#9a7a1e", string="#6e7330", number="#5a6b66", typ="#58703a",
    variable="#34381f", prop="#555a36", operator="#6e6c46", constant="#8a6b2a", thisKw="#8a6b1e", link="#4f6e3e")

P["barad-dur-dark"] = dict(mode="dark", label="Barad-dûr (Dark)", file="darktower.ts", slug="mordor",
    bg="#131316", fg="#c4c2c0", bgDark="#0f0f12", bgDarker="#0b0b0e", bgTab="#0d0d0f",
    border="#060608", lineHL="#1a1a1e", selBase="#2e3036", gutter="#45474c", gutterActive="#d9624a",
    cursor="#e0452e", accent="#b54033", accentFg="#f0e8e6", statusBg="#7a2018", statusFg="#e6dcd8",
    listActive="#26262b", listHover="#1c1c20", indent="#2a2a2f", indentActive="#45474c", widgetBorder="#2a2a2f",
    error="#e0452e", warning="#e08a3c", info="#9aa6ac",
    comment="#5a5d61", keyword="#b54033", func="#d9624a", string="#8a8f8c", number="#e08a3c", typ="#9aa6ac",
    variable="#c4c2c0", prop="#aeb2b4", operator="#8a8d92", constant="#e08a3c", thisKw="#c0726a", link="#9aa6ac")
P["barad-dur-light"] = dict(mode="light", label="Barad-dûr — Ashlands (Light)", file="darktower.ts", slug="mordor",
    bg="#d6d3cf", fg="#2a2a2c", bgDark="#cbc8c3", bgDarker="#bdbab5", bgTab="#c8c5c0",
    border="#b0ada8", lineHL="#cdcac5", selBase="#bdb6b0", gutter="#9a9792", gutterActive="#962f24",
    cursor="#a32a1e", accent="#962f24", accentFg="#f2eeea", statusBg="#3a3a3d", statusFg="#e0ddd9",
    listActive="#c2bfb9", listHover="#cdcac5", indent="#c4c1bc", indentActive="#9a9792", widgetBorder="#b0ada8",
    error="#962f24", warning="#9a5a1e", info="#4a5258",
    comment="#7a7d80", keyword="#962f24", func="#b5491f", string="#5e615e", number="#9a5a1e", typ="#4a5258",
    variable="#2a2a2c", prop="#54565a", operator="#6a6d70", constant="#9a5a1e", thisKw="#8a3a2e", link="#4a5258")

# ============================ EIGHT NEW REALMS ============================
# (minimal palettes; structural shades derived by norm)

P["minas-tirith-dark"] = dict(mode="dark", label="Minas Tirith (Dark)", file="white-city.ts", slug="gondor",
    bg="#14161c", fg="#dde0e6", gutter="#4a4f5c", gutterActive="#d8b86a", cursor="#d8b86a",
    accent="#4a6e96", statusBg="#2a2e3a", statusFg="#dde0e6", error="#c66a5e", warning="#d8b86a", info="#7f9fc4",
    comment="#646b78", keyword="#7f9fc4", func="#d8b86a", string="#8fb6b0", number="#c66a5e", typ="#aeb0cc",
    prop="#b4b8c2", operator="#8a909c", constant="#c2a06a", thisKw="#aeb0cc", link="#7f9fc4")
P["minas-tirith-light"] = dict(mode="light", label="Minas Tirith (Light)", file="white-city.ts", slug="gondor",
    bg="#edeef1", fg="#2b2f36", gutter="#a8adb6", gutterActive="#3a5f8a", cursor="#9a7b2e",
    accent="#3a5f8a", statusBg="#2b2f36", statusFg="#d6d9de", error="#973a3a", warning="#9a7b2e", info="#3a5f8a",
    comment="#8a8f96", keyword="#3a5f8a", func="#9a7b2e", string="#3f6e6a", number="#973a3a", typ="#5a5f7a",
    prop="#50545e", operator="#6a6e76", constant="#7a5a2a", thisKw="#5a5f7a", link="#3a5f8a")

P["mordor-dark"] = dict(mode="dark", label="Mordor (Dark)", file="gorgoroth.ts", slug="gorgoroth",
    bg="#16140f", fg="#c9c4b6", gutter="#4d4a40", gutterActive="#c98a3a", cursor="#e0531f",
    accent="#8a5a22", statusBg="#5a3318", statusFg="#d8c9b0", error="#d8431f", warning="#d99a2a", info="#9a9683",
    comment="#5e5a4e", keyword="#b58a3a", func="#d9882f", string="#9a9374", number="#d8431f", typ="#b0a98a",
    prop="#ada587", operator="#877f68", constant="#d99a2a", thisKw="#c0a05a", link="#b58a3a")
P["mordor-light"] = dict(mode="light", label="Mordor (Light)", file="gorgoroth.ts", slug="gorgoroth",
    bg="#d8d2c4", fg="#2e2b22", gutter="#a39c8a", gutterActive="#8a4a1a", cursor="#b5431a",
    accent="#8a5a22", statusBg="#4a3a26", statusFg="#d8cdb6", error="#a53318", warning="#8a5a1a", info="#6e6a52",
    comment="#8a8470", keyword="#7a5520", func="#a55a1e", string="#6e6a4a", number="#a53318", typ="#6a6448",
    prop="#57523c", operator="#6e6850", constant="#8a5a1a", thisKw="#6a6448", link="#7a5520")

P["moria-dark"] = dict(mode="dark", label="Moria (Dark)", file="khazad-dum.ts", slug="moria",
    bg="#101216", fg="#c6cbd2", gutter="#454a54", gutterActive="#c9a94a", cursor="#c9a94a",
    accent="#5a7a96", statusBg="#2a3038", statusFg="#c6cbd2", error="#c45a4a", warning="#c9a94a", info="#7fa0b8",
    comment="#5a606a", keyword="#7fa0b8", func="#b9c2cc", string="#8aa6a0", number="#c9a94a", typ="#9fa6c4",
    prop="#aab0ba", operator="#828892", constant="#c9a94a", thisKw="#9fa6c4", link="#7fa0b8")
P["moria-light"] = dict(mode="light", label="Moria (Light)", file="khazad-dum.ts", slug="moria",
    bg="#dadde0", fg="#262a30", gutter="#a0a5ac", gutterActive="#8a6a1e", cursor="#4a6a86",
    accent="#4a6a86", statusBg="#2a3038", statusFg="#c6cbd2", error="#a5402e", warning="#8a6a1e", info="#4a6a86",
    comment="#80868e", keyword="#3a5e7a", func="#5a6478", string="#3f6a64", number="#8a6a1e", typ="#555a78",
    prop="#4e525c", operator="#6a6e78", constant="#8a6a1e", thisKw="#555a78", link="#3a5e7a")

P["fangorn-dark"] = dict(mode="dark", label="Fangorn (Dark)", file="entwood.ts", slug="fangorn",
    bg="#14160f", fg="#cdc9ad", gutter="#4a4d38", gutterActive="#9aa85a", cursor="#9aa85a",
    accent="#5a6e38", statusBg="#2e3a22", statusFg="#cdc9ad", error="#bf6a48", warning="#b59a4a", info="#8fa86a",
    comment="#5e6a4e", keyword="#8fa86a", func="#b59a4a", string="#9aa572", number="#c08a5a", typ="#a8b58a",
    prop="#b4b890", operator="#828a6a", constant="#b59a4a", thisKw="#a8b58a", link="#8fa86a")
P["fangorn-light"] = dict(mode="light", label="Fangorn (Light)", file="entwood.ts", slug="fangorn",
    bg="#e2ddc4", fg="#33371f", gutter="#aaa580", gutterActive="#6a5a1e", cursor="#5a6e2e",
    accent="#5a6e2e", statusBg="#3a4a26", statusFg="#d8d6b6", error="#9a4a2a", warning="#6a5a1e", info="#5a6e3a",
    comment="#84876a", keyword="#4a5e2e", func="#7a601e", string="#5e6a36", number="#8a5a2e", typ="#54703a",
    prop="#555a36", operator="#6a6c46", constant="#7a601e", thisKw="#54703a", link="#4a5e2e")

P["erebor-dark"] = dict(mode="dark", label="Erebor (Dark)", file="lonely-mountain.ts", slug="erebor",
    bg="#18130d", fg="#e6dcc0", gutter="#574a38", gutterActive="#e0b840", cursor="#e0b840",
    accent="#a8762a", statusBg="#6e2f24", statusFg="#ecd9b0", error="#d65a44", warning="#e0b840", info="#c89a4a",
    comment="#6e6048", keyword="#c98f3a", func="#e8bf52", string="#c2a85e", number="#d65a44", typ="#d4b87a",
    prop="#d2c294", operator="#9a8a64", constant="#d65a44", thisKw="#cf9e5a", link="#c98f3a")
P["erebor-light"] = dict(mode="light", label="Erebor (Light)", file="lonely-mountain.ts", slug="erebor",
    bg="#ece0c0", fg="#3a2e1a", gutter="#b4a374", gutterActive="#8a5a1a", cursor="#8a5a1a",
    accent="#a8762a", statusBg="#6e2f24", statusFg="#ecd9b0", error="#a5402a", warning="#8a5a1a", info="#97651e",
    comment="#8a7c58", keyword="#97651e", func="#b5832a", string="#7a6a2a", number="#a5402a", typ="#8a6a2e",
    prop="#5a4e30", operator="#6e6244", constant="#a5402a", thisKw="#8a6a2e", link="#97651e")

P["grey-havens-dark"] = dict(mode="dark", label="The Grey Havens (Dark)", file="mithlond.ts", slug="havens",
    bg="#121820", fg="#d2dade", gutter="#455260", gutterActive="#c8b885", cursor="#aed0d8",
    accent="#5a8a96", statusBg="#243845", statusFg="#d2dade", error="#c47868", warning="#c8b885", info="#8fbcc8",
    comment="#5a6672", keyword="#8fbcc8", func="#c8b885", string="#9ac4bc", number="#c49a8a", typ="#b0bcd0",
    prop="#b6c0c8", operator="#828e98", constant="#c8b885", thisKw="#b0bcd0", link="#8fbcc8")
P["grey-havens-light"] = dict(mode="light", label="The Grey Havens (Light)", file="mithlond.ts", slug="havens",
    bg="#e6ebee", fg="#2c343a", gutter="#9fabb2", gutterActive="#2f6a7a", cursor="#2f6a7a",
    accent="#4a8090", statusBg="#3a5a66", statusFg="#e6eef0", error="#a5564a", warning="#8a6a3a", info="#2f6a7a",
    comment="#7e8a92", keyword="#2f6a7a", func="#8a6a3a", string="#3a7a6e", number="#9a5a4a", typ="#5a5e80",
    prop="#515a62", operator="#6a7680", constant="#8a6a3a", thisKw="#5a5e80", link="#2f6a7a")

P["isengard-dark"] = dict(mode="dark", label="Isengard (Dark)", file="orthanc.ts", slug="isengard",
    bg="#15171a", fg="#c4c6c8", gutter="#474a4e", gutterActive="#d97a2a", cursor="#e06a1e",
    accent="#6a7378", statusBg="#3a2a1e", statusFg="#d4c8b8", error="#d8512e", warning="#d97a2a", info="#8a9498",
    comment="#5a5e62", keyword="#8a9498", func="#d97a2a", string="#9aa098", number="#d8512e", typ="#a6acae",
    prop="#aab0b2", operator="#82888c", constant="#d97a2a", thisKw="#b0a890", link="#8a9498")
P["isengard-light"] = dict(mode="light", label="Isengard (Light)", file="orthanc.ts", slug="isengard",
    bg="#d6d7d4", fg="#2a2c2e", gutter="#9b9d9a", gutterActive="#a85420", cursor="#b5491c",
    accent="#6a7378", statusBg="#3a2a1e", statusFg="#d4c8b8", error="#a5402a", warning="#a85420", info="#5a6468",
    comment="#82868a", keyword="#4a5458", func="#a85420", string="#5a6458", number="#a5402a", typ="#5a6064",
    prop="#50565a", operator="#6a7074", constant="#a85420", thisKw="#5a6064", link="#4a5458")

P["mirkwood-dark"] = dict(mode="dark", label="Mirkwood (Dark)", file="greenwood.ts", slug="mirkwood",
    bg="#0f1410", fg="#c0c8ba", gutter="#3e4a3e", gutterActive="#8aa86a", cursor="#8aa86a",
    accent="#4a6a4a", statusBg="#2a2438", statusFg="#c4c2cc", error="#c45a52", warning="#b5a84a", info="#7fa87a",
    comment="#56624e", keyword="#7fa87a", func="#b5b84a", string="#8aa882", number="#b07ab0", typ="#9a9ec4",
    prop="#aab4a2", operator="#7a846e", constant="#b5a84a", thisKw="#9a9ec4", link="#7fa87a")
P["mirkwood-light"] = dict(mode="light", label="Mirkwood (Light)", file="greenwood.ts", slug="mirkwood",
    bg="#d6dcc8", fg="#2a3024", gutter="#a0a888", gutterActive="#5a6a2a", cursor="#5a6a2a",
    accent="#4a6a4a", statusBg="#2e2842", statusFg="#cac8d2", error="#97402a", warning="#6a6a1e", info="#4a6a4a",
    comment="#7e846a", keyword="#4a6a44", func="#6a6a1e", string="#5a6a3a", number="#7a4a7a", typ="#5a5a86",
    prop="#545a3e", operator="#6a7050", constant="#6a6a1e", thisKw="#5a5a86", link="#4a6a44")


def build(p):
    p = norm(p)
    light = p["mode"] == "light"
    selA = "aa" if light else "88"
    muted = mix(p["fg"], p["bg"], 0.42)
    inact = mix(p["fg"], p["bg"], 0.55)
    bright = mix(p["fg"], WHITE, 0.25)

    colors = {
        "focusBorder": p["accent"], "foreground": p["fg"], "descriptionForeground": muted,
        "errorForeground": p["error"], "icon.foreground": muted, "selection.background": p["selBase"],
        "editor.background": p["bg"], "editor.foreground": p["fg"],
        "editorLineNumber.foreground": p["gutter"], "editorLineNumber.activeForeground": p["gutterActive"],
        "editorCursor.foreground": p["cursor"], "editor.selectionBackground": p["selBase"] + selA,
        "editor.selectionHighlightBackground": p["selBase"] + "55", "editor.lineHighlightBackground": p["lineHL"],
        "editor.wordHighlightBackground": p["selBase"] + "55", "editor.wordHighlightStrongBackground": p["accent"] + "44",
        "editor.findMatchBackground": p["number"] + "66", "editor.findMatchHighlightBackground": p["func"] + "33",
        "editor.hoverHighlightBackground": p["selBase"] + "55", "editorBracketMatch.background": p["accent"] + "33",
        "editorBracketMatch.border": p["keyword"], "editorIndentGuide.background1": p["indent"],
        "editorIndentGuide.activeBackground1": p["indentActive"], "editorWhitespace.foreground": p["indent"],
        "editorRuler.foreground": p["indent"], "editorGutter.background": p["bg"],
        "editorError.foreground": p["error"], "editorWarning.foreground": p["warning"], "editorInfo.foreground": p["info"],
        "editorBracketHighlight.foreground1": p["keyword"], "editorBracketHighlight.foreground2": p["func"],
        "editorBracketHighlight.foreground3": p["number"], "editorBracketHighlight.foreground4": p["typ"],
        "editorBracketHighlight.foreground5": p["string"], "editorBracketHighlight.foreground6": p["gutterActive"],
        "editorWidget.background": p["bgDark"], "editorWidget.border": p["widgetBorder"],
        "editorSuggestWidget.background": p["bgDark"], "editorSuggestWidget.border": p["widgetBorder"],
        "editorSuggestWidget.selectedBackground": p["listActive"], "editorSuggestWidget.highlightForeground": p["func"],
        "editorHoverWidget.background": p["bgDark"], "editorHoverWidget.border": p["widgetBorder"],
        "editorGroupHeader.tabsBackground": p["bgTab"], "editorGroupHeader.noTabsBackground": p["bgTab"],
        "editorGroup.border": p["border"], "tab.activeBackground": p["bg"], "tab.inactiveBackground": p["bgTab"],
        "tab.activeForeground": p["fg"], "tab.inactiveForeground": inact, "tab.activeBorderTop": p["func"],
        "tab.activeBorder": p["bg"], "tab.border": p["border"], "tab.hoverBackground": p["lineHL"],
        "titleBar.activeBackground": p["bgTab"], "titleBar.activeForeground": mix(p["fg"], p["bg"], 0.15),
        "titleBar.inactiveBackground": p["bgTab"], "titleBar.inactiveForeground": muted, "titleBar.border": p["border"],
        "activityBar.background": p["bgDarker"], "activityBar.foreground": mix(p["fg"], p["bg"], 0.15),
        "activityBar.inactiveForeground": muted, "activityBar.activeBorder": p["func"], "activityBar.border": p["border"],
        "activityBarBadge.background": p["accent"], "activityBarBadge.foreground": p["accentFg"],
        "sideBar.background": p["bgDark"], "sideBar.foreground": mix(p["fg"], p["bg"], 0.12), "sideBar.border": p["border"],
        "sideBarTitle.foreground": mix(p["fg"], p["bg"], 0.12), "sideBarSectionHeader.background": p["bgTab"],
        "sideBarSectionHeader.foreground": mix(p["fg"], p["bg"], 0.12), "sideBarSectionHeader.border": p["border"],
        "list.activeSelectionBackground": p["listActive"], "list.activeSelectionForeground": p["fg"],
        "list.inactiveSelectionBackground": p["listHover"], "list.hoverBackground": p["listHover"],
        "list.focusBackground": p["listActive"], "list.highlightForeground": p["func"],
        "list.errorForeground": p["error"], "list.warningForeground": p["warning"], "tree.indentGuidesStroke": p["indent"],
        "statusBar.background": p["statusBg"], "statusBar.foreground": p["statusFg"], "statusBar.border": p["border"],
        "statusBar.noFolderBackground": p["statusBg"], "statusBar.debuggingBackground": p["func"],
        "statusBar.debuggingForeground": p["accentFg"], "statusBarItem.remoteBackground": p["accent"],
        "statusBarItem.remoteForeground": p["accentFg"], "statusBarItem.hoverBackground": mix(p["statusBg"], WHITE, 0.12),
        "panel.background": p["bgDark"], "panel.border": p["border"], "panelTitle.activeForeground": p["fg"],
        "panelTitle.activeBorder": p["func"], "panelTitle.inactiveForeground": muted,
        "terminal.background": p["bgDark"], "terminal.foreground": p["fg"], "terminalCursor.foreground": p["cursor"],
        "terminal.ansiBlack": p["bgDarker"], "terminal.ansiBrightBlack": p["gutter"], "terminal.ansiRed": p["error"],
        "terminal.ansiBrightRed": p["number"], "terminal.ansiGreen": p["keyword"],
        "terminal.ansiBrightGreen": mix(p["keyword"], p["fg"], 0.25), "terminal.ansiYellow": p["gutterActive"],
        "terminal.ansiBrightYellow": p["func"], "terminal.ansiBlue": p["typ"],
        "terminal.ansiBrightBlue": mix(p["typ"], p["fg"], 0.2), "terminal.ansiMagenta": p["constant"],
        "terminal.ansiBrightMagenta": p["thisKw"], "terminal.ansiCyan": p["string"],
        "terminal.ansiBrightCyan": mix(p["string"], p["fg"], 0.2), "terminal.ansiWhite": p["fg"],
        "terminal.ansiBrightWhite": bright,
        "button.background": p["accent"], "button.foreground": p["accentFg"],
        "button.hoverBackground": mix(p["accent"], WHITE, 0.12), "button.secondaryBackground": p["listActive"],
        "button.secondaryForeground": p["fg"], "badge.background": p["accent"], "badge.foreground": p["accentFg"],
        "input.background": p["bgDarker"] if not light else mix(p["bg"], WHITE, 0.3), "input.foreground": p["fg"],
        "input.border": p["widgetBorder"], "input.placeholderForeground": muted, "inputOption.activeBorder": p["func"],
        "dropdown.background": p["bgDarker"] if not light else mix(p["bg"], WHITE, 0.3), "dropdown.foreground": p["fg"],
        "dropdown.border": p["widgetBorder"], "checkbox.background": p["bgDarker"] if not light else mix(p["bg"], WHITE, 0.3),
        "checkbox.border": p["widgetBorder"], "scrollbar.shadow": "#00000000",
        "scrollbarSlider.background": p["gutter"] + "55", "scrollbarSlider.hoverBackground": p["gutter"] + "88",
        "scrollbarSlider.activeBackground": p["accent"] + "88", "minimap.findMatchHighlight": p["func"],
        "minimapSlider.background": p["gutter"] + "33", "minimapSlider.hoverBackground": p["gutter"] + "55",
        "gitDecoration.modifiedResourceForeground": p["gutterActive"], "gitDecoration.deletedResourceForeground": p["error"],
        "gitDecoration.untrackedResourceForeground": p["keyword"], "gitDecoration.ignoredResourceForeground": p["gutter"],
        "gitDecoration.conflictingResourceForeground": p["number"], "editorGutter.modifiedBackground": p["gutterActive"],
        "editorGutter.addedBackground": p["keyword"], "editorGutter.deletedBackground": p["error"],
        "peekView.border": p["accent"], "peekViewEditor.background": p["bgTab"], "peekViewResult.background": p["bgDark"],
        "peekViewTitle.background": p["bgDark"], "breadcrumb.foreground": muted, "breadcrumb.focusForeground": p["fg"],
        "breadcrumb.activeSelectionForeground": p["func"], "breadcrumbPicker.background": p["bgDark"],
        "menu.background": p["bgDark"], "menu.foreground": p["fg"], "menu.selectionBackground": p["listActive"],
        "menu.separatorBackground": p["widgetBorder"], "menubar.selectionBackground": p["listActive"],
        "widget.shadow": "#00000033" if not light else "#7a6a3a22", "editorLink.activeForeground": p["func"],
        "textLink.foreground": p["link"], "textLink.activeForeground": mix(p["link"], p["fg"], 0.2),
    }

    def tok(s, fg, st=None):
        d = {"foreground": fg}
        if st: d["fontStyle"] = st
        return {"scope": s, "settings": d}

    tokenColors = [
        tok(["comment", "punctuation.definition.comment", "string.comment"], p["comment"], "italic"),
        tok(["keyword", "keyword.control", "storage.type", "storage.modifier", "keyword.operator.new",
             "keyword.operator.expression", "keyword.operator.logical"], p["keyword"]),
        tok(["entity.name.function", "support.function", "meta.function-call.generic", "meta.function-call"], p["func"]),
        tok(["entity.name.type", "entity.name.class", "support.type", "support.class",
             "entity.other.inherited-class", "entity.name.namespace"], p["typ"]),
        tok(["string", "string.quoted", "string.template", "punctuation.definition.string"], p["string"]),
        tok(["constant.numeric", "constant.language", "constant.language.boolean", "constant.language.null",
             "support.constant"], p["number"]),
        tok(["constant.character.escape", "constant.other.placeholder", "constant.character"], p["constant"]),
        tok(["variable", "variable.other.readwrite", "meta.definition.variable.name", "variable.parameter"], p["variable"]),
        tok(["variable.other.constant", "variable.other.enummember"], p["number"]),
        tok(["variable.other.property", "support.variable.property", "meta.object-literal.key"], p["prop"]),
        tok(["variable.language", "variable.language.this", "keyword.other.self"], p["thisKw"], "italic"),
        tok(["keyword.operator", "punctuation.separator", "punctuation.terminator", "punctuation.accessor"], p["operator"]),
        tok(["entity.name.tag", "punctuation.definition.tag"], p["keyword"]),
        tok(["entity.other.attribute-name"], p["func"]),
        tok(["support.type.property-name.css", "support.type.property-name"], p["typ"]),
        tok(["markup.heading", "markup.heading entity.name", "entity.name.section"], p["func"], "bold"),
        tok(["markup.bold"], p["number"], "bold"),
        tok(["markup.italic"], p["string"], "italic"),
        tok(["markup.inline.raw", "markup.fenced_code", "markup.raw"], p["gutterActive"]),
        tok(["markup.quote"], p["comment"], "italic"),
        tok(["markup.underline.link", "string.other.link"], p["link"]),
        tok(["punctuation.definition.list.begin.markdown", "markup.list"], p["func"]),
        tok(["invalid", "invalid.illegal"], p["error"]),
        tok(["entity.name.label", "keyword.control.directive", "meta.preprocessor"], p["constant"]),
        tok(["meta.decorator", "punctuation.decorator", "entity.name.function.decorator"], p["thisKw"], "italic"),
    ]
    semantic = {"parameter": p["prop"], "property": p["prop"], "variable.constant": p["number"],
                "function": p["func"], "method": p["func"], "class": p["typ"], "enumMember": p["number"],
                "*.declaration": {"fontStyle": "bold"}}
    return {"name": p["label"], "type": p["mode"], "semanticHighlighting": True,
            "colors": colors, "tokenColors": tokenColors, "semanticTokenColors": semantic}


order = [
    "shire-dark","shire-light","grey-havens-dark","grey-havens-light",
    "rivendell-dark","rivendell-light","moria-dark","moria-light",
    "lothlorien-dark","lothlorien-light","fangorn-dark","fangorn-light",
    "mirkwood-dark","mirkwood-light","erebor-dark","erebor-light",
    "rohan-dark","rohan-light","isengard-dark","isengard-light",
    "minas-tirith-dark","minas-tirith-light","mordor-dark","mordor-light",
    "barad-dur-dark","barad-dur-light",
]

contributes, preview = [], {}
for key in order:
    p = P[key]
    theme = build(p)
    with open(os.path.join(OUT, f"{key}-color-theme.json"), "w") as f:
        json.dump(theme, f, indent=2, ensure_ascii=False)
    contributes.append({"label": p["label"], "uiTheme": "vs-dark" if p["mode"] == "dark" else "vs",
                        "path": f"./themes/{key}-color-theme.json"})
    preview[key] = {k: p[k] for k in ("bg","fg","gutter","comment","keyword","func","string","number",
                    "typ","prop","statusBg","statusFg","bgTab","error","file","slug")}

pkg = {"name": "middle-earth-themes", "displayName": "Middle-earth Themes",
       "description": "Twenty-six color themes drawn from thirteen realms of Middle-earth, each in a dark and a light mode.",
       "version": "1.0.0", "publisher": "bryce", "engines": {"vscode": "^1.70.0"},
       "categories": ["Themes"], "contributes": {"themes": contributes}}
with open("/home/claude/middle-earth/package.json", "w") as f:
    json.dump(pkg, f, indent=2, ensure_ascii=False)
with open("/home/claude/middle-earth/preview-colors.json", "w") as f:
    json.dump(preview, f, indent=2, ensure_ascii=False)

print(f"Generated {len(order)} themes across 13 realms.")
