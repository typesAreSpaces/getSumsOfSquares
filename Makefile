vars="x"
vars="x, y"
deleteQ="T"
output="TeXGramMatrix"
output="Certificate"
output="TeXCertificate"

P="6 - x^2 - 2*x^4 + x^6 - y^2 - 3*x^2*y^2 + 3*x^4*y^2 - 2*y^4 + 3*x^2*y^4 + y^6"
P="21/20 - x^2 - (16679880978201*x^20)/26559922791424 + (16679880978201*x^22)/26559922791424 - y^2 + x^2*y^2 - (16679880978201*y^20)/26559922791424 + (16679880978201*y^22)/26559922791424"
P="x+1+9/10*x^2"
P="(x + 1)^3 + ((x + 1)*(x - 1))^3/8"
P="308/100*x^2 - 616/100*x*y + 308/100*y^2 + 7422/1000"
P="(154*x^2)/25 + (154*x^4)/25 - (308*x*y)/25 - (154*x^3*y)/25 + (154*y^2)/25 - (154*x*y^3)/25 + (154*y^4)/25"

#'s' = show
#'c' = copy to clipboard

.PHONY: s c

s:
	./getSumsOfSquares.py ${P} ${vars} ${deleteQ} ${output}

c:
	./getSumsOfSquares.py ${P} ${vars} ${deleteQ} ${output} | pbcopy
