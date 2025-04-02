import graphviz

if __name__ == '__main__':
    dot = graphviz.Digraph(comment='North-South Train Problem Finite State Machine')
    dot.engine = "neato"
    dot.attr(splines="curved")
    dot.graph_attr['label'] = '' \
    'North-South Train Problem Finite State Machine'

    AND = "\u2227"      # Logical And
    OR = "\u2228"       # Logical OR
    CHECK = "\u2713"    # Check mark sign
    WRONG = "\u2716"    # Wrong mark sign
    LE = "\u2264"       # LESS-THAN OR EQUAL TO
    GE = "\u2265"       # GREATER-THAN OR EQUAL TO
    RST_C = "timer := 0"  # Reset Counter

    BLK = "#000000"
    RED = "#ff0000"
    GRN = "#007700"
    BLU = "#0000ff"

    st0 = f"Start"
    st1 = f"Default State"
    st2 = f"Alarm State"
    st3 = f"Barrier State"
   # st4 = f"Alarm {CHECK}\nBarrier {WRONG}\n(Train leaving)"

    nodes = {
        (st0, "point"): "0,0!",
        (st1, "circle"): "3,0!",
        (st2, "circle"): "9,0!",
        (st3, "circle"): "12,-4!",
#        (st4, "circle"): "3,-4!",
    }

    # Nodes
    for (node, shape), position in nodes.items():
        dot.node(node, shape=shape, pos=position)

    edges = {
        (st0, st1, f"{RST_C}\ltrains := 0"): BLK,
        (st1, st2, f"(northbound_approach) {OR} (southbound_approach) / (Alarm {CHECK})\n{RST_C}\ntrains := 1"): BLK,
        (st2, st2, f"timer++\n(Time-Triggered Interruption)\t"): RED,
        (st2, st2, f"(northbound_approach) {OR} (southbound_approach) / trains++\n(Event-Triggered Interruption)\t"): BLU,
        (st2, st3, f"(timer {GE} 10) / (Barrier {CHECK})"): BLK,
        (st3, st3, f"(N_D) / -\t\t\ntrains--"): RED,
        (st3, st3, f"(S_D) / -\t\t\ntrains--"): BLU,
        (st3, st3, f"(northbound_approach) / -\t\t\ntrains++"): GRN,
        (st3, st3, f"(southbound_approach) / -\t\t\ntrains++"): BLK,
        # (st3, st4, f"trains {LE} 0 / (Barrier {WRONG})\n{RST_C}"): BLK,
        # (st4, st4, f"timer++"): RED,
        # (st4, st1, f"(timer {GE} 10) / (Alarm {WRONG})\n{RST_C}"): BLK,
        # (st4, st2, f"(northbound_approach) {OR} (southbound_approach) / (trains := 1)\n{RST_C}"): GRN,
    }

    # Edges
    for (first_node, next_node, lbl), CLR   in edges.items():
        dot.edge(first_node, next_node, label=lbl, color=CLR, fontcolor=CLR)

        # Additional information nodes
    dot.node("Inputs", "Inputs:\lnorthbound_approach\lsouthbound_approach\lnorthbound_depart\lsouthbound_depart\lclock",
             shape="box", style="filled", fillcolor="lightgray", pos="-5,3!")

    dot.node("Outputs", "Outputs:\lalarm_enable\lalarm_disable\lbarrier_lower\lbarrier_raise", 
             shape="box", style="filled", fillcolor="lightblue", pos="-5,0!")

    dot.node("Variables", "Variables:\ltimer: Timer Counter\ltrains: Train Counter", 
             shape="box", style="filled", fillcolor="lightgreen", pos="-5,-3!")
    
#    dot.node("Assumptions", )
    dot.save(filename="fsm.dot")
    dot.render(filename="fsm", format="svg", view=True)
