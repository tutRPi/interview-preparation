class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = "".join(local.split("."))

            unique_email = local + "@" + domain
            unique.add(unique_email)

        return len(unique)