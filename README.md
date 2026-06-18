# Middle-earth Themes

Twenty-six VS Code color themes drawn from thirteen realms of Middle-earth —
each with a dark and a light mode. From the cozy green of the Shire to the
ember glow of Mordor, pick the realm that suits your mood.

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

## Install

1. Open the **Extensions** view in VS Code (`Cmd/Ctrl + Shift + X`).
2. Search for **Middle-earth Themes** and click **Install**.
3. Open the theme picker with `Cmd/Ctrl + K` then `Cmd/Ctrl + T`
   (or Command Palette → **Preferences: Color Theme**).
4. All twenty-six themes appear grouped together — pick one.

Prefer the command line?

```bash
code --install-extension brycerichards.middle-earth-themes
```

## Switching themes

Use `Cmd/Ctrl + K` `Cmd/Ctrl + T` at any time to preview themes — arrow through
the list and the editor updates live, so you can wander from Rivendell to
Mordor and back before committing.

## Feedback

Found a color that feels off, or want a realm that isn't here yet? Open an
issue at
[github.com/bryce-richards/middle-earth-themes/issues](https://github.com/bryce-richards/middle-earth-themes/issues).

## Contributing

The themes are generated from `gen.py`; each lives in `themes/` as plain JSON
(UI colors under `colors`, syntax under `tokenColors` / `semanticTokenColors`).
To tweak a theme, edit a hex value and run **Developer: Reload Window**. To add
a new realm, add a palette block and key to the `order` list in `gen.py` and
rerun it — `package.json` and the preview data regenerate automatically. See
the [repository](https://github.com/bryce-richards/middle-earth-themes) for
details.

## License

[MIT](LICENSE)
