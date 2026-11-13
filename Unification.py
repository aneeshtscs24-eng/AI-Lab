def trace_unify(x, y, subst=None, depth=0):
    indent = "  " * depth
    if subst is None:
        subst = {}
    
    print(f"{indent}Unifying: {x} with {y} | Current Subst: {subst}")
    
    x_val = get_value(x, subst)
    y_val = get_value(y, subst)
    
    if x_val != x or y_val != y:
        print(f"{indent}  -> Resolved values: {x_val} and {y_val}")
        
    if x_val == y_val:
        print(f"{indent}  -> Match! Terms are identical.")
        return subst
        
    if is_variable(x_val):
        print(f"{indent}  -> '{x_val}' is a variable. Binding...")
        return trace_unify_var(x_val, y_val, subst, depth)
        
    if is_variable(y_val):
        print(f"{indent}  -> '{y_val}' is a variable. Binding...")
        return trace_unify_var(y_val, x_val, subst, depth)
        
    if isinstance(x_val, tuple) and isinstance(y_val, tuple):
        if x_val[0] != y_val[0] or len(x_val) != len(y_val):
            print(f"{indent}  -> Mismatch: Functors or arity differ ('{x_val[0]}' vs '{y_val[0]}'). Fails.")
            return None
        print(f"{indent}  -> Compound terms match functor '{x_val[0]}'. Unifying arguments recursively...")
        for xa, ya in zip(x_val[1:], y_val[1:]):
            subst = trace_unify(xa, ya, subst, depth + 1)
            if subst is None:
                return None
        return subst
        
    print(f"{indent}  -> Cannot unify constants '{x_val}' and '{y_val}'. Fails.")
    return None

def is_variable(term):
    return isinstance(term, str) and term.startswith('?')

def get_value(term, subst):
    while is_variable(term) and term in subst:
        term = subst[term]
    return term

def occurs_check(var, term, subst):
    term = get_value(term, subst)
    if term == var:
        return True
    if isinstance(term, tuple):
        return any(occurs_check(var, arg, subst) for arg in term[1:])
    return False

def trace_unify_var(var, x, subst, depth):
    indent = "  " * depth
    if occurs_check(var, x, subst):
        print(f"{indent}  -> Occurs check failed: variable '{var}' appears inside term '{x}'.")
        return None
    subst[var] = x
    print(f"{indent}  -> Bound {var} = {x}. Updated Subst: {subst}")
    return subst

print("=== EXAMPLE 1: Unifying Compound Predicates ===")
term1 = ('Knows', '?x', 'Python')
term2 = ('Knows', 'Alice', '?y')
result = trace_unify(term1, term2)
print(f"\nFinal Substitution Result: {result}\n")
print("=== EXAMPLE 2: Failing Unification (Functor Mismatch) ===")
term3 = ('Likes', 'Bob', 'Coding')
term4 = ('Hates', 'Bob', 'Coding')
trace_unify(term3, term4)