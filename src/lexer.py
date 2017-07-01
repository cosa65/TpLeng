'''
V : true | false | \x:T.M | n
M : x | true | false | if M1 then M2 else M3 | \x:T.M | M1 M2 | 0 | succ(M) | pred(M) | iszero(M)
T : Bool | Nat | T1 -> T2
'''

t_BOOL(t):
	r'true|false'
	t.value = True if (t.value == "true") else False
	return t

t_NAT(t):
	r'(?!-)\d+'
	t.value = int(t.value)

t_IFTHENELSE = r'if .* then .* else .*'

t_FUNCTION = r'\\.:.*\..*'

#t_APPLICATION = r''

#Creo que flayie cualquiera aca, pero bueno