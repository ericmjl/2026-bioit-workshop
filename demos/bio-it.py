# /// script
# dependencies = [
#     "anywidget==0.11.0",
#     "cloudscraper==1.2.71",
#     "marimo",
#     "numpy==2.4.6",
#     "plotly==6.7.0",
#     "polars==1.40.1",
#     "requests==2.34.2",
#     "traitlets==5.15.0",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def imports():
    import json
    from io import BytesIO

    import anywidget
    import cloudscraper
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    import polars as pl
    import traitlets
    from _plotly_utils import optional_imports as plotly_optional_imports

    return (
        BytesIO,
        anywidget,
        cloudscraper,
        go,
        json,
        mo,
        pl,
        plotly_optional_imports,
        traitlets,
    )


@app.cell(hide_code=True)
def supplementary_data_markdown(mo):
    mo.md("""
    ## Supplementary data

    Load ACS supplementary CSV as a Polars dataframe.
    """)
    return


@app.cell(hide_code=True)
def load_supplementary_polars_dataframe(BytesIO, cloudscraper, pl):
    supplementary_csv_url = "https://pubs.acs.org/doi/suppl/10.1021/acscatal.1c02786/suppl_file/cs1c02786_si_002.csv"
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "darwin", "mobile": False}
    )
    response = scraper.get(supplementary_csv_url, timeout=90)
    response.raise_for_status()
    si_df = pl.read_csv(BytesIO(response.content))
    si_df
    return (si_df,)


@app.cell(hide_code=True)
def filter_single_point_mutants(pl, si_df):
    single_point_mutants_df = si_df.filter(
        pl.col("mutation").is_not_null()
        & pl.col("mutation").str.strip_chars().str.contains(r"^[A-Z][0-9]+[A-Z]$")
    )
    single_point_mutants_df
    return (single_point_mutants_df,)


@app.cell(hide_code=True)
def heatmap_position_mutant_letter_mean(
    go,
    pl,
    plotly_optional_imports,
    single_point_mutants_df,
):
    # The notebook kernel persists across package installs; clear stale failed-import cache.
    plotly_optional_imports._not_importable.discard("numpy")

    single_point_with_coords_df = single_point_mutants_df.with_columns(
        [
            pl.col("mutation")
            .str.extract(r"^[A-Z]([0-9]+)[A-Z]$", group_index=1)
            .cast(pl.Int64)
            .alias("position"),
            pl.col("mutation")
            .str.extract(r"^[A-Z][0-9]+([A-Z])$", group_index=1)
            .alias("mutant_letter"),
        ]
    )

    heatmap_long_df = single_point_with_coords_df.group_by(
        ["position", "mutant_letter"]
    ).agg(pl.col("mean").mean().alias("mean"))

    heatmap_matrix_df = heatmap_long_df.pivot(
        values="mean",
        index="mutant_letter",
        on="position",
        aggregate_function="first",
    ).sort("mutant_letter")

    position_columns = [
        c for c in heatmap_matrix_df.columns if c != "mutant_letter"
    ]
    position_columns = sorted(position_columns, key=int)

    z_values = heatmap_matrix_df.select(position_columns).to_numpy()
    y_values = heatmap_matrix_df["mutant_letter"].to_list()
    x_values = [int(c) for c in position_columns]

    fig = go.Figure(
        data=go.Heatmap(
            z=z_values,
            x=x_values,
            y=y_values,
            colorscale="Viridis",
            colorbar={"title": "mean"},
        )
    )
    fig.update_layout(
        title="Single-point mutants heatmap",
        xaxis_title="position",
        yaxis_title="mutant letter",
    )
    fig
    return


@app.cell(hide_code=True)
def pdb_anywidget_markdown(mo):
    mo.md("""
    ## 3Dmol.js structure viewer

    Interactive anywidget-backed viewer that fetches structure `7OG3` directly from RCSB PDB.
    """)
    return


@app.cell(hide_code=True)
def custom_3dmoljs_anywidget_viewer(
    anywidget,
    json,
    pl,
    single_point_mutants_df,
    traitlets,
):
    class ThreeDMolWidget(anywidget.AnyWidget):
        """Anywidget wrapper around a 3Dmol.js viewer."""

        _esm = """
        async function load3Dmol() {
          if (window.$3Dmol) return window.$3Dmol;

          return await new Promise((resolve, reject) => {
            const existing = document.querySelector("script[data-3dmoljs='true']");

            if (existing) {
              existing.addEventListener("load", () => resolve(window.$3Dmol), { once: true });
              existing.addEventListener("error", () => reject(new Error("Failed to load 3Dmol.js")), { once: true });
              return;
            }

            const script = document.createElement("script");
            script.src = "https://unpkg.com/3dmol@2.5.2/build/3Dmol-min.js";
            script.async = true;
            script.dataset["3dmoljs"] = "true";
            script.addEventListener("load", () => resolve(window.$3Dmol), { once: true });
            script.addEventListener("error", () => reject(new Error("Failed to load 3Dmol.js")), { once: true });
            document.head.appendChild(script);
          });
        }

        const VIRIDIS = [
          "#440154", "#482878", "#3E4989", "#31688E", "#26828E",
          "#1F9E89", "#35B779", "#6DCD59", "#B4DE2C", "#FDE725"
        ];

        function hexToRgb(hex) {
          const clean = hex.replace("#", "");
          return {
            r: parseInt(clean.slice(0, 2), 16),
            g: parseInt(clean.slice(2, 4), 16),
            b: parseInt(clean.slice(4, 6), 16),
          };
        }

        function rgbToHex(r, g, b) {
          const toHex = (value) => Math.max(0, Math.min(255, Math.round(value))).toString(16).padStart(2, "0");
          return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
        }

        function interpolateViridis(t) {
          const clamped = Math.max(0, Math.min(1, t));
          const scaled = clamped * (VIRIDIS.length - 1);
          const lower = Math.floor(scaled);
          const upper = Math.ceil(scaled);

          if (lower === upper) {
            return VIRIDIS[lower];
          }

          const fraction = scaled - lower;
          const c0 = hexToRgb(VIRIDIS[lower]);
          const c1 = hexToRgb(VIRIDIS[upper]);

          return rgbToHex(
            c0.r + (c1.r - c0.r) * fraction,
            c0.g + (c1.g - c0.g) * fraction,
            c0.b + (c1.b - c0.b) * fraction
          );
        }

        function parseResidueScores(model) {
          try {
            const parsed = JSON.parse(model.get("residue_scores_json") || "{}");
            const scoreMap = {};
            for (const [key, value] of Object.entries(parsed)) {
              const numericValue = Number(value);
              if (Number.isFinite(numericValue)) {
                scoreMap[String(key)] = numericValue;
              }
            }
            return scoreMap;
          } catch (_error) {
            return {};
          }
        }

        function hideTooltip(tooltip) {
          tooltip.style.display = "none";
        }

        function getEventCoordinates(event, container) {
          const rect = container.getBoundingClientRect();
          const rawX = event?.clientX ?? event?.pageX ?? (rect.left + rect.width / 2);
          const rawY = event?.clientY ?? event?.pageY ?? (rect.top + rect.height / 2);

          return {
            x: rawX - rect.left,
            y: rawY - rect.top,
            width: rect.width,
            height: rect.height,
          };
        }

        function showTooltip(tooltip, container, event, htmlContent) {
          const coords = getEventCoordinates(event, container);
          const x = Math.max(8, Math.min(coords.width - 220, coords.x + 12));
          const y = Math.max(8, Math.min(coords.height - 90, coords.y + 12));

          tooltip.innerHTML = htmlContent;
          tooltip.style.left = `${x}px`;
          tooltip.style.top = `${y}px`;
          tooltip.style.display = "block";
        }

        async function fetchPdbText(pdbId) {
          const normalized = String(pdbId).trim().toUpperCase();
          const url = `https://files.rcsb.org/download/${normalized}.pdb`;
          const response = await fetch(url);

          if (!response.ok) {
            throw new Error(`Failed to fetch PDB ${normalized}: ${response.status}`);
          }

          return await response.text();
        }

        async function renderViewer(model, container, status, tooltip, clickState) {
          const $3Dmol = await load3Dmol();
          const pdbId = model.get("pdb_id");
          const background = model.get("background");

          const residueScores = parseResidueScores(model);
          const scoreValues = Object.values(residueScores);
          const minScore = scoreValues.length ? Math.min(...scoreValues) : 0;
          const maxScore = scoreValues.length ? Math.max(...scoreValues) : 1;

          const scoreForResidue = (resi) => residueScores[String(resi)];

          const colorForResidue = (resi) => {
            const score = scoreForResidue(resi);
            if (!Number.isFinite(score)) {
              return "#9CA3AF";
            }
            if (maxScore <= minScore) {
              return VIRIDIS[VIRIDIS.length - 1];
            }
            const t = (score - minScore) / (maxScore - minScore);
            return interpolateViridis(t);
          };

          const pdbText = await fetchPdbText(pdbId);

          container.innerHTML = "";
          const viewer = $3Dmol.createViewer(container, { backgroundColor: background });
          viewer.addModel(pdbText, "pdb");

          const proteinCartoonStyle = {
            cartoon: {
              colorfunc: (atom) => colorForResidue(atom.resi),
            },
          };
          viewer.setStyle({ chain: "A", hetflag: false }, proteinCartoonStyle);
          viewer.setStyle({ chain: "B", hetflag: false }, proteinCartoonStyle);

          viewer.setClickable({ hetflag: false }, true, (atom, _viewer, event) => {
            if (!atom) return;

            clickState.skipNextBackgroundClear = true;

            const residueScore = scoreForResidue(atom.resi);
            const scoreText = Number.isFinite(residueScore)
              ? residueScore.toFixed(4)
              : "not available";

            const htmlContent = `
              <div style="font-weight:600; margin-bottom:4px;">Residue ${atom.resn ?? "?"}${atom.resi ?? "?"}</div>
              <div>Chain: ${atom.chain ?? "?"}</div>
              <div>Max single mutation effect: ${scoreText}</div>
            `;

            showTooltip(tooltip, container, event, htmlContent);
          });

          viewer.setStyle({ resn: ["HOH", "WAT"] }, { hidden: true });

          viewer.setStyle(
            { hetflag: true, not: { resn: ["HOH", "WAT"] } },
            {
              stick: { radius: 0.2, colorscheme: "greenCarbon" },
              sphere: { scale: 0.28, colorscheme: "greenCarbon" },
            }
          );

          viewer.zoomTo();
          viewer.render();

          if (scoreValues.length) {
            status.textContent = `Loaded ${String(pdbId).toUpperCase()} | max single mutation effect range: ${minScore.toFixed(3)} to ${maxScore.toFixed(3)}`;
          } else {
            status.textContent = `Loaded ${String(pdbId).toUpperCase()} | no residue scores provided`;
          }
        }

        function render({ model, el }) {
          el.innerHTML = "";
          el.style.position = "relative";

          const clickState = { skipNextBackgroundClear: false };

          const container = document.createElement("div");
          container.style.width = model.get("width");
          container.style.height = model.get("height");
          container.style.border = "1px solid #e5e7eb";
          container.style.borderRadius = "8px";
          container.style.overflow = "hidden";
          container.style.background = model.get("background");
          el.appendChild(container);

          const tooltip = document.createElement("div");
          tooltip.style.position = "absolute";
          tooltip.style.display = "none";
          tooltip.style.minWidth = "180px";
          tooltip.style.maxWidth = "260px";
          tooltip.style.padding = "8px 10px";
          tooltip.style.background = "rgba(17, 24, 39, 0.94)";
          tooltip.style.color = "#f9fafb";
          tooltip.style.borderRadius = "8px";
          tooltip.style.fontSize = "0.8rem";
          tooltip.style.lineHeight = "1.3";
          tooltip.style.pointerEvents = "none";
          tooltip.style.zIndex = "10";
          el.appendChild(tooltip);

          const status = document.createElement("div");
          status.style.marginTop = "0.5rem";
          status.style.fontSize = "0.85rem";
          status.style.color = "#4b5563";
          el.appendChild(status);

          container.addEventListener("click", () => {
            if (clickState.skipNextBackgroundClear) {
              clickState.skipNextBackgroundClear = false;
              return;
            }
            hideTooltip(tooltip);
          });

          const rerender = async () => {
            hideTooltip(tooltip);
            clickState.skipNextBackgroundClear = false;
            status.textContent = `Loading ${String(model.get("pdb_id")).toUpperCase()} from RCSB...`;
            try {
              await renderViewer(model, container, status, tooltip, clickState);
            } catch (error) {
              status.textContent = error.message;
            }
          };

          rerender();

          model.on("change:pdb_id", rerender);
          model.on("change:background", rerender);
          model.on("change:width", () => { container.style.width = model.get("width"); rerender(); });
          model.on("change:height", () => { container.style.height = model.get("height"); rerender(); });
          model.on("change:residue_scores_json", rerender);
        }

        export default { render };
        """

        pdb_id = traitlets.Unicode("7OG3").tag(sync=True)
        residue_scores_json = traitlets.Unicode("{}").tag(sync=True)
        background = traitlets.Unicode("white").tag(sync=True)
        width = traitlets.Unicode("100%").tag(sync=True)
        height = traitlets.Unicode("620px").tag(sync=True)


    residue_scores_df = (
        single_point_mutants_df.with_columns(
            pl.col("mutation")
            .str.extract(r"^[A-Z]([0-9]+)[A-Z]$", group_index=1)
            .cast(pl.Int64)
            .alias("position")
        )
        .group_by("position")
        .agg(pl.col("mean").max().alias("max_single_mutation_effect"))
        .sort("position")
    )

    residue_scores = {
        str(row["position"]): float(row["max_single_mutation_effect"])
        for row in residue_scores_df.iter_rows(named=True)
    }

    viewer_3dmol = ThreeDMolWidget(
        pdb_id="7OG3",
        residue_scores_json=json.dumps(residue_scores),
        background="#ffffff",
        width="100%",
        height="620px",
    )

    viewer_3dmol
    return


if __name__ == "__main__":
    app.run()
