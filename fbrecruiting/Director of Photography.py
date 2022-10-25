# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    artistic = 0
    for i in range(len(C)):
        if C[i] == "A":
            has_photograph, has_backdrop = 0, 0
            # search left
            for j in range(i - Y, i - X + 1):
                if j >= 0:
                    if C[j] == "P":
                        has_photograph += 1
                    elif C[j] == "B":
                        has_backdrop += 1
            # search right
            for j in range(i + X, i + Y + 1):
                if j < len(C):
                    if C[j] == "P":
                        artistic += has_backdrop
                    elif C[j] == "B":
                        artistic += has_photograph

    return artistic