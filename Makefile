vars="x,y"
deleteQ="T"
output="TeXGramMatrix"
output="Certificate"
output="TeXCertificate"

P="6 - x^2 - 2*x^4 + x^6 - y^2 - 3*x^2*y^2 + 3*x^4*y^2 - 2*y^4 + 3*x^2*y^4 + y^6"
P="21/20 - x^2 - (16679880978201*x^20)/26559922791424 + (16679880978201*x^22)/26559922791424 - y^2 + x^2*y^2 - (16679880978201*y^20)/26559922791424 + (16679880978201*y^22)/26559922791424"

#'s' = show
#'c' = copy to clipboard

.PHONY: s c

s:
	./getSumsOfSquares.py ${P} ${vars} ${deleteQ} ${output}

c:
	./getSumsOfSquares.py ${P} ${vars} ${deleteQ} ${output} | pbcopy
