# Middle-earth Themes

Twenty-six VS Code color themes drawn from thirteen realms of Middle-earth —
each with a dark and a light mode.

| Realm | Mood | Signature colors |
|-------|------|------------------|
| **The Shire** | Cozy hobbit-hole | leaf green, candlelight amber, terracotta, parchment |
| **The Grey Havens** | Sea-mist & departure | sea-foam teal, dawn rose, lamp gold, silver-blue |
| **Rivendell** | Misty elven valley | blue-slate, autumn gold, twilight lavender, copper |
| **Moria** | Cold dwarven deep | mithril silver, steel blue, gold vein, black stone |
| **Lothlórien** | The Golden Wood | luminous gold, mallorn green, silver, golden cream |
| **Fangorn** | Ancient dim forest | lichen green, bark amber, mushroom tan, mossy parchment |
| **Mirkwood** | Spider-shadow & murk | murky green, venom purple, sickly chartreuse, shadow violet |
| **Erebor** | Dwarven treasure hall | dragon gold, ruby/garnet, bronze, warm stone |
| **Rohan** | Windswept golden hall | wheat-gold, field green, banner red, dark timber |
| **Isengard** | Industrial pits | furnace orange, iron grey, pewter, machine black |
| **Minas Tirith** | The White City | white stone, steel blue, crown gold, garnet (sable & silver chrome) |
| **Mordor** | Ashen waste | sulfur bronze, lava orange, ember red, dead-grass, ash |
| **Barad-dûr** | The Dark Tower | charcoal, ash-grey, blood red, ember (light = "Ashlands" grey & rust) |

Each theme styles the full workbench — editor, sidebar, tabs, terminal, git
gutters, bracket pairs, status bar — plus TextMate and semantic syntax tokens.

## Install (local, no marketplace needed)

1. Copy the entire `middle-earth` folder into your VS Code extensions directory:
   - **macOS / Linux:** `~/.vscode/extensions/`
   - **Windows:** `%USERPROFILE%\.vscode\extensions\`
2. Fully quit and reopen VS Code.
3. Command Palette (`Cmd/Ctrl + Shift + P`) → **Preferences: Color Theme** →
   all twenty-six themes appear grouped together. Pick one.

## Install (package as .vsix to share)

From inside the `middle-earth` folder:

```bash
npm install -g @vscode/vsce
vsce package
```

This produces `middle-earth-themes-1.0.0.vsix`. Install it with:

```bash
code --install-extension middle-earth-themes-1.0.0.vsix
```

### Before publishing to the Marketplace

Two values in `package.json` are placeholders to personalize first:

- `publisher` — must exactly match the publisher ID you register on the
  Visual Studio Marketplace (currently `bryce`).
- `repository` / `bugs` / `homepage` — point these at your actual GitHub repo
  (currently `github.com/brycerichards/middle-earth-themes`).

The `LICENSE` (MIT), `icon.png`, and `CHANGELOG.md` are already in place. The
`.vscodeignore` keeps `gen.py` and `preview-colors.json` out of the packaged
`.vsix` while leaving them in the repo.

## Tweaking & extending

Every theme lives in `themes/` as plain JSON: UI colors under `colors`, syntax
under `tokenColors` / `semanticTokenColors`. Edit a hex value, run
**Developer: Reload Window**, and the change is live. **Developer: Inspect
Editor Tokens and Scopes** shows the exact scope under your cursor.

All themes are generated from `gen.py`. The original realms carry fully
hand-tuned palettes; newer realms supply only the essential colors and the
script derives the structural UI shades (panels, borders, selection, etc.) by
blending. To add a fourteenth realm — Bree, Helm's Deep, the Dead Marshes —
copy a palette block, give it the minimal keys (bg, fg, gutter, gutterActive,
cursor, accent, statusBg/Fg, error/warning/info, and the syntax roles), add the
key to the `order` list, and rerun the script. `package.json` and the preview
data regenerate automatically.
