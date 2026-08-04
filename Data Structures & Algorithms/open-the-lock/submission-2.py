class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1
        
        if target == "0000":
            return 0

        begin_set = {"0000"}
        end_set = {target}
        turns = 0


        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()
            for lock in begin_set:
                if lock in end_set:
                    return turns

                if lock in deadends_set:
                    continue

                deadends_set.add(lock)

                for i in range(4):
                    c = int(lock[i])

                    for d in (-1, 1):
                        new_digit = str((c + d) % 10)
                        new_lock = lock[: i] + new_digit + lock[i + 1:]
                        if new_lock not in deadends_set:
                            next_set.add(new_lock)

            begin_set = next_set
            turns += 1

        return -1