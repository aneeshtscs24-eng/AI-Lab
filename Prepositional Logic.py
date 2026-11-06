def knowledge_base_reasoning():
  R = True  
  W = R    
  A = W  
  print(f"1. Is it raining (R)? {R}")
  print(f"2. Does the road become wet (W)? {W} (Derived from R)")
  print(f"3. Do accidents occur (A)? {A} (Derived from W)")
  print("Conclusion: Because it is raining, the road becomes wet, which leads to accidents occurring.")
knowledge_base_reasoning()

def prove_student_degree():
  S = True 
  E = S   
  D = E   
  print(f"Premise: Student studies (S) = {S}")
  print(f"Step 1: Student passes exam (E) = {E} (derived via S → E)")
  print(f"Step 2: Student gets degree (D) = {D} (derived via E → D)")
  print("Result: Proven successfully — the student gets a degree[cite: 1]!")
prove_student_degree()