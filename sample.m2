needsPackage("SumsOfSquares")
R = QQ[x]
p = 1/64*x^2-15/64*x+15/32-27573/19524464*(x+2)*(x-1)*(x-13)+561/2665739*(1/64*x^2-15/64*x+15/32-27573/19524464*(x+2)*(x-1)*(x-13))*(x+3)*(2+561/2665739*(x+3)*(x+2)*(x-1)*(x-13)+(1+561/2665739*(x+3)*(x+2)*(x-1)*(x-13))^2+(1+561/2665739*(x+3)*(x+2)*(x-1)*(x-13))^3+(1+561/2665739*(x+3)*(x+2)*(x-1)*(x-13))^4+(1+561/2665739*(x+3)*(x+2)*(x-1)*(x-13))^5)*(x+2)*(x-1)*(x-13)
sol = solveSOS (p, RoundTol => 3, TraceObj => false)
print tex sosPoly sol
print tex sol#GramMatrix
print tex sol#Monomials
quit
