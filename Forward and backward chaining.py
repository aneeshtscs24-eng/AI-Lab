def forward_chaining_trace(rules, facts, goal):
    inferred = set(facts)
    print(f"--- FORWARD CHAINING (Data-Driven) ---")
    print(f"Starting Facts: {inferred}")
    print(f"Target Goal: {goal}\n")
    step = 1
    while True:
        new_fact_added = False
        for premise, conclusion in rules:
            if premise.issubset(inferred) and conclusion not in inferred:
                print(f"Step {step}: Premise {premise} satisfied from facts. Implies new fact -> '{conclusion}'")
                inferred.add(conclusion)
                new_fact_added = True
                if conclusion == goal:
                    print(f"Goal '{goal}' reached successfully!\n")
                    return True
        if not new_fact_added:
            print("No more rules can fire.\n")
            break
        step += 1
    return goal in inferred

def backward_chaining_trace(rules, facts, goal, depth=0):
    indent = "  " * depth
    print(f"{indent}Checking goal:'{goal}'")
    if goal in facts:
        print(f"{indent}Found in known facts! Validated.")
        return True
    for premise, conclusion in rules:
        if conclusion == goal:
            print(f"{indent}Rule found: If {premise} Then '{goal}'. Must verify premises:")
            if all(backward_chaining_trace(rules, facts, p, depth + 1) for p in premise):
                print(f"{indent}All premises for '{goal}' satisfied.")
                return True
    print(f"{indent}Cannot prove '{goal}'.")
    return False
    
rules = [({"wings"}, "flies"),({"feather", "flies"}, "bird"),({"bird", "breathes"}, "animal")]
initial_facts = {"feather", "wings", "breathes"}
target_goal = "animal"
forward_chaining_trace(rules, initial_facts, target_goal)
print("--- BACKWARD CHAINING (Goal-Driven) ---")
result = backward_chaining_trace(rules, initial_facts, target_goal)
print(f"\nBackward Chaining Result for goal '{target_goal}': {result}")