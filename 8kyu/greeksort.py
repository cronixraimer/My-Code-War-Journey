#After finishing this task I will better solution on this task
def greek_comparator(lhs, rhs):
    greek_alphabet = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta','eta', 'theta', 'iota', 'kappa', 'lambda', 'mu','nu', 'xi', 'omicron', 'pi', 'rho', 'sigma','tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

    index_1 = greek_alphabet.index(lhs) if lhs in greek_alphabet else None
    index_2 = greek_alphabet.index(rhs) if rhs in greek_alphabet else None

    if index_1 is not None and index_2 is not None:
        comparison_result = index_1 - index_2

        if comparison_result == 0:
            return 0
        elif comparison_result < 0:
            return -1
        else:
            return 1

    return f"One or both of the elements are not in the list."

lhs = 'upsilon'
rhs = 'rho'
result = greek_comparator(lhs, rhs)
print(result)
#best solution : return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
