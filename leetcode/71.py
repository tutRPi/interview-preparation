class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = path.split("/")
        new_path = []
        for elem in queue:
            if elem and elem != ".":
                if elem == "..":
                    if new_path:
                        new_path.pop()
                else:
                    new_path.append(elem)

        return "/" if not new_path else "/" + "/".join(new_path)