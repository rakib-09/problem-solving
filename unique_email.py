from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_set = set()
        for email in emails:
            s_e = email.split('@', 1)
            local = s_e[0]
            domain = s_e[1]
            s = local.replace('.', '')
            s = s.split('+', 1)
            n_e = s[0] + '@' + domain
            if n_e not in unique_set:
                unique_set.add(n_e)
        print(unique_set)
        return len(unique_set)
