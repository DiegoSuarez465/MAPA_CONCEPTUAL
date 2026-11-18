"""
MAPA CONCEPTUAL | Análisis y verificación de programas
Genera versiones PNG, PDF y SVG en la carpeta "resultado".
Requisito: pip install matplotlib
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Lienzo horizontal de alta resolución
W, H = 18, 11
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor("#F4F7FB")
ax.set_facecolor("#F4F7FB")
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis("off")

# Paleta sobria
NAVY = "#102A43"
BLUE = "#1D4E89"
TEAL = "#0F766E"
CYAN = "#DDF3F2"
PALE_BLUE = "#E7EFF9"
PALE_GOLD = "#FFF4D6"
PALE_PURPLE = "#F0EAFE"
INK = "#243B53"
MUTED = "#52667A"
WHITE = "#FFFFFF"
LINE = "#7890A8"

def rounded_box(x, y, w, h, title, body="", face=WHITE, edge=BLUE,
                title_color=NAVY, body_color=INK, title_size=10.5,
                body_size=8.2, lw=1.5, radius=0.16):
    """Dibuja un nodo con título y contenido."""
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.03,rounding_size={radius}",
        linewidth=lw, edgecolor=edge, facecolor=face, zorder=3
    )
    ax.add_patch(patch)
    if body:
        ax.text(x + w/2, y + h*0.68, title, ha="center", va="center",
                fontsize=title_size, fontweight="bold", color=title_color,
                wrap=True, zorder=4)
        ax.text(x + w/2, y + h*0.31, body, ha="center", va="center",
                fontsize=body_size, color=body_color, linespacing=1.35,
                wrap=True, zorder=4)
    else:
        ax.text(x + w/2, y + h/2, title, ha="center", va="center",
                fontsize=title_size, fontweight="bold", color=title_color,
                wrap=True, zorder=4)
    return (x, y, w, h)

def link(x1, y1, x2, y2, label="", color=LINE, rad=0.0, label_offset=(0, 0),
         lw=1.35, style="-|>"):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style, mutation_scale=12,
        linewidth=lw, color=color,
        connectionstyle=f"arc3,rad={rad}", zorder=2
    )
    ax.add_patch(arrow)
    if label:
        mx, my = (x1+x2)/2 + label_offset[0], (y1+y2)/2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center", fontsize=7.1,
                color=NAVY, fontweight="semibold",
                bbox=dict(boxstyle="round,pad=0.22", fc="#F4F7FB",
                          ec="none", alpha=0.98), zorder=5)

# Encabezado
ax.text(0.65, 10.62, "MAPA CONCEPTUAL", fontsize=10, fontweight="bold",
        color=TEAL, va="center")
ax.text(0.65, 10.12, "ANÁLISIS Y VERIFICACIÓN DE PROGRAMAS",
        fontsize=21, fontweight="bold", color=NAVY, va="center")
ax.text(0.67, 9.77,
        "Relaciones entre especificación, demostración de corrección y eficiencia algorítmica",
        fontsize=9.5, color=MUTED, va="center")
ax.plot([0.65, 17.35], [9.48, 9.48], color="#C8D5E2", lw=1)

# Concepto central
rounded_box(5.75, 8.35, 6.5, 0.78,
            "ANÁLISIS Y VERIFICACIÓN DE PROGRAMAS",
            "permite establecer si un programa es correcto, termina y utiliza recursos de forma adecuada",
            face=NAVY, edge=NAVY, title_color=WHITE, body_color="#D9E7F5",
            title_size=13, body_size=8.6, lw=0)

# Cuatro conceptos principales
cols = [0.65, 4.95, 9.25, 13.55]
cw = 3.8
main_y, main_h = 6.72, 0.92
main_nodes = [
    ("1. TRIPLAS DE HOARE", "Especifican la relación entre\nel estado inicial y el final", BLUE, PALE_BLUE),
    ("2. CORRECCIÓN DE PROGRAMAS", "Determina las condiciones\npara garantizar un resultado", TEAL, CYAN),
    ("3. PROGRAMAS ITERATIVOS", "Verifica ciclos mediante\ninvariantes y cotas", "#7655A6", PALE_PURPLE),
    ("4. ANÁLISIS DE ALGORITMOS", "Estudia el costo computacional\nen función del tamaño de entrada", "#A36A12", PALE_GOLD),
]
for x, (title, body, edge, face) in zip(cols, main_nodes):
    rounded_box(x, main_y, cw, main_h, title, body, face=face, edge=edge,
                title_color=edge, title_size=10.2, body_size=8.1)

# Enlaces desde el concepto central a las cuatro ramas
central_bottom = 8.35
for x in cols:
    target_x = x + cw/2
    link(9.0, central_bottom, target_x, main_y + main_h,
         "se estudia mediante", color="#8297AA",
         label_offset=(0, 0.12), lw=1.15)

# Detalles de cada rama: nodos de segundo nivel
detail_y = 4.83
detail_h = 1.30
detail = [
    [
        ("PRECONDICIÓN\n(Q)", "Condición previa\na la ejecución."),
        ("PROGRAMA\n(S)", "Instrucciones que\ntransforman el estado."),
        ("POSCONDICIÓN\n(R)", "Propiedad que se cumple\nal finalizar."),
    ],
    [
        ("PRECONDICIÓN\nMÁS DÉBIL", "Condición que asegura\nla poscondición."),
        ("REGLAS DE\nVERIFICACIÓN", "Asignación, instrucción\nvacía, condicional y\ncomposición."),
        ("TRIPLA\nVÁLIDA", "Desde Q, el programa\nproduce un estado\nque satisface R."),
    ],
    [
        ("INVARIANTE\nDE CICLO", "Propiedad que se mantiene\nen cada iteración."),
        ("INICIALIZACIÓN Y\nCONSERVACIÓN", "El ciclo inicia cumpliendo\nel invariante y lo mantiene."),
        ("COTA DE\nCICLO", "Disminuye en cada iteración\ny tiene límite inferior."),
    ],
    [
        ("COMPLEJIDAD\nT(n)", "Cuenta operaciones según\nel tamaño de entrada n."),
        ("CASOS DE\nANÁLISIS", "Mejor, peor y, cuando\naplica, caso promedio."),
        ("NOTACIÓN\nASINTÓTICA", "O: superior · Ω: inferior\nΘ: ajustada."),
    ],
]
branch_colors = [BLUE, TEAL, "#7655A6", "#A36A12"]
branch_faces = [PALE_BLUE, CYAN, PALE_PURPLE, PALE_GOLD]
node_w = 1.20
node_gap = 0.08
for i, x in enumerate(cols):
    start = x + 0.06
    for j, (title, body) in enumerate(detail[i]):
        nx = start + j*(node_w + node_gap)
        rounded_box(nx, detail_y, node_w, detail_h, title, body,
                    face=WHITE, edge=branch_colors[i],
                    title_color=branch_colors[i], title_size=6.6,
                    body_size=6.0, lw=1.0, radius=0.10)
        # Conector desde el concepto principal hacia cada concepto secundario
        link(x + cw/2, main_y, nx + node_w/2, detail_y + detail_h,
             ["se representa con", "se demuestra mediante",
              "se comprueba con", "se cuantifica mediante"][i]
             if j == 1 else "",
             color=branch_colors[i], lw=1.0,
             label_offset=(0, 0.02))

# Franja de integración: relación entre las cuatro lecturas
rounded_box(2.05, 2.70, 13.9, 0.88,
            "INTEGRACIÓN DE LOS CUATRO ENFOQUES",
            "La especificación define qué debe cumplir el programa; la verificación demuestra que lo cumple; "
            "el análisis de complejidad estima los recursos que necesita.",
            face="#E8EEF5", edge="#486581", title_color=NAVY,
            body_color=INK, title_size=11.0, body_size=8.7, lw=1.4)

# Flechas desde los bloques secundarios hacia la integración
for x in cols:
    link(x + cw/2, detail_y, 9.0, 3.58, "",
         color="#9AABBA", lw=1.0, rad=0.0)

# Resultado conceptual
rounded_box(4.25, 1.18, 9.5, 0.86,
            "PROPÓSITO",
            "Desarrollar programas confiables: correctos respecto a su especificación, "
            "con terminación justificada y eficiencia evaluada.",
            face=NAVY, edge=NAVY, title_color=WHITE,
            body_color="#D9E7F5", title_size=11.5, body_size=8.8, lw=0)
link(9.0, 2.70, 9.0, 2.06, "contribuye a", color=TEAL, label_offset=(0.7, 0))

# Pie de página
ax.text(0.68, 0.48, "SÍNTESIS DE LAS CUATRO LECTURAS FUNDAMENTALES",
        fontsize=7.5, color=MUTED, fontweight="bold")
ax.text(17.3, 0.48, "Politécnico Grancolombiano  |  2026",
        fontsize=7.5, color=MUTED, ha="right")

plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.03)
output = Path(__file__).parent / "resultado"
output.mkdir(exist_ok=True)
for ext in ("png", "pdf", "svg"):
    fig.savefig(output / f"mapa_conceptual.{ext}",
                dpi=300, bbox_inches="tight",
                facecolor=fig.get_facecolor())
plt.close(fig)
print("Listo. Archivos generados en:", output.resolve())
