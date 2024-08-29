
# This took me ~25 minutes. Didn't have any help either; I'm proud of myself.

def isValidSudoko(board: list[list[str]]) -> bool:
	rows, cols, squares = defaultdict(list), defaultdict(list), defaultdict(list)

	for r in range(9):
		for c in range(9):
			point = board[r][c]
			if point != ".":
				square = (r//3, c//3)
				if point in rows.get(r, []) or point in cols.get(c, []) or point in squares.get(square, []):
					return False
				rows[r].append(point)
				cols[c].append(point)
				squares[square].append(point)

	return True
