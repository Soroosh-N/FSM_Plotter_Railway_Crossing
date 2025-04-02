import graphviz

if __name__ == '__main__':
    dot = graphviz.Digraph(comment='North-South Train Problem Finite State Machine')
    dot.engine = "neato"
    dot.attr(splines="curved")
    dot.graph_attr['label'] = '' \
    'North-South Train Problem Finite State Machine\n' \
    '\nS_A: South Train Approaching' \
    '\nN_A: North Train Approaching' \
    '\nS_D: South Train Departing' \
    '\nN_D: North Train Departing' \
    '\nCNT: Timer Counter' \
    '\nT_CNT: Train Counter' \
    '\n++: Increase by 1' \
    '\n--: Decrease by 1'

    AND = "\u2227"      # Logical And
    OR = "\u2228"       # Logical OR
    CHECK = "\u2713"    # Check mark sign
    WRONG = "\u2716"    # Wrong mark sign
    LE = "\u2264"       # LESS-THAN OR EQUAL TO
    GE = "\u2265"       # GREATER-THAN OR EQUAL TO
    RST_C = "CNT := 0"  # Reset Counter

    BLK = "#000000"
    RED = "#ff0000"
    GRN = "#007700"
    BLU = "#0000ff"

    st0 = f"Start"
    st1 = f"Alarm {WRONG}\nBarrier {WRONG}"
    st2 = f"Alarm {CHECK}\nBarrier {WRONG}\n(Train arriving)"
    st3 = f"Alarm {CHECK}\nBarrier {CHECK}"
    st4 = f"Alarm {CHECK}\nBarrier {WRONG}\n(Train leaving)"

    nodes = {
        (st0, "point"): "0,0!",
        (st1, "circle"): "3,0!",
        (st2, "circle"): "9,0!",
        (st3, "circle"): "9,-4!",
        (st4, "circle"): "3,-4!",
    }

    # Nodes
    for (node, shape), position in nodes.items():
        dot.node(node, shape=shape, pos=position)

    edges = {
        (st0, st1, f"{RST_C}\nT_CNT := 0"): BLK,
        (st1, st2, f"(N_A) {OR} (S_A) / (Alarm {CHECK})\n{RST_C}\nT_CNT := 1"): BLK,
        (st2, st2, f"CNT++\n(Time-Triggered Interruption)\t"): RED,
        (st2, st2, f"(N_A) {OR} (S_A) / T_CNT++\n(Event-Triggered Interruption)\t"): BLU,
        (st2, st3, f"(CNT {GE} 10) / (Barrier {CHECK})"): BLK,
        (st3, st3, f"(N_D) / -\t\t\nT_CNT--"): RED,
        (st3, st3, f"(S_D) / -\t\t\nT_CNT--"): BLU,
        (st3, st3, f"(N_A) / -\t\t\nT_CNT++"): GRN,
        (st3, st3, f"(S_A) / -\t\t\nT_CNT++"): BLK,
        (st3, st4, f"T_CNT {LE} 0 / (Barrier {WRONG})\n{RST_C}"): BLK,
        (st4, st4, f"CNT++"): RED,
        (st4, st1, f"(CNT {GE} 10) / (Alarm {WRONG})\n{RST_C}"): BLK,
        (st4, st2, f"(N_A) {OR} (S_A) / (T_CNT := 1)\n{RST_C}"): GRN,
    }

    # Edges
    for (first_node, next_node, lbl), CLR   in edges.items():
        dot.edge(first_node, next_node, label=lbl, color=CLR, fontcolor=CLR)
    
    dot.render(filename="fsm", format="svg", view=True)
