"""
--- Day 4: Repose Record ---

You've sneaked into another supply closet - this time, it's across from the
prototype suit manufacturing lab. You need to sneak inside and fix the issues
with the suit, but there's a guard stationed outside the lab, so this is as
close as you can safely get.

As you search the closet for anything that might help, you discover that you're
not the first person to want to sneak in. Covering the walls, someone has spent
an hour starting every midnight for the past few months secretly observing this
guard post! They've been writing down the ID of the one guard on duty that
night - the Elves seem to have decided that one guard was enough for the
overnight shift - as well as when they fall asleep or wake up while at their
post (your puzzle input).

For example, consider the following records, which have already been organized
into chronological order:

    [1518-11-01 00:00] Guard #10 begins shift
    [1518-11-01 00:05] falls asleep
    [1518-11-01 00:25] wakes up
    [1518-11-01 00:30] falls asleep
    [1518-11-01 00:55] wakes up
    [1518-11-01 23:58] Guard #99 begins shift
    [1518-11-02 00:40] falls asleep
    [1518-11-02 00:50] wakes up
    [1518-11-03 00:05] Guard #10 begins shift
    [1518-11-03 00:24] falls asleep
    [1518-11-03 00:29] wakes up
    [1518-11-04 00:02] Guard #99 begins shift
    [1518-11-04 00:36] falls asleep
    [1518-11-04 00:46] wakes up
    [1518-11-05 00:03] Guard #99 begins shift
    [1518-11-05 00:45] falls asleep
    [1518-11-05 00:55] wakes up

Timestamps are written using year-month-day hour:minute format. The guard
falling asleep or waking up is always the one whose shift most recently
started. Because all asleep/awake times are during the midnight hour (00:00 -
00:59), only the minute portion (00 - 59) is relevant for those events.

Visually, these records show that the guards are asleep at these times:

    Date   ID   Minute
                000000000011111111112222222222333333333344444444445555555555
                012345678901234567890123456789012345678901234567890123456789
    11-01  #10  .....####################.....#########################.....
    11-02  #99  ........................................##########..........
    11-03  #10  ........................#####...............................
    11-04  #99  ....................................##########..............
    11-05  #99  .............................................##########.....

The columns are Date, which shows the month-day portion of the relevant day;
ID, which shows the guard on duty that day; and Minute, which shows the minutes
during which the guard was asleep within the midnight hour. (The Minute
column's header shows the minute's ten's digit in the first row and the one's
digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count
as awake on the minute they wake up. For example, because Guard #10 wakes up at
00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time,
you might be able to trick that guard into working tonight so you can have the
best chance of sneaking in. You have two strategies for choosing the best
guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does
that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50
minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes
(10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas
any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are
in the order you found them. You'll need to organize them before they can be
analyzed.

PART 1: What is the ID of the guard you chose multiplied by the minute you
        chose? (In the above example, the answer would be 10 * 24 = 240.)
"""

import re
from datetime import datetime


class WatchRecord:
    def __init__(self, raw_datafile: str):
        self.times = []
        self.events = []
        self.guards = set()

        with open(raw_datafile, "r") as fp:
            for line in fp.readlines():
                event_df = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", line)

                # Ensure the line is valid
                if event_df is not None:
                    self.times.append(
                        datetime.strptime(event_df.group(0), r"%Y-%m-%d %H:%M")
                    )

                    # Determine the nature of the event
                    if "falls" in line:
                        self.events.append("falls")

                    elif "wakes" in line:
                        self.events.append("wakes")

                    elif "#" in line:
                        temp_guard = int(re.search(r"#(\d+)", line).group(1))
                        self.events.append(temp_guard)
                        self.guards.add(temp_guard)

        # Sort the event earliest to latest
        self.times, self.events = zip(*sorted(zip(self.times, self.events)))
        self.times = list(self.times)
        self.events = list(self.events)

    def generate_guard_sleep_record(self):
        """
        For every minute from 00:00 to 00:59 count the number of times the guard
        is asleep.
        """
        self.guard_sleep_record = {x: [0] * 60 for x in self.guards}
        curr_guard = None
        guard_awake = True

        # Iterate over every event and determine when a guard sleeps
        for event_idx in range(len(self.events)):

            # A guard falls asleep
            if self.events[event_idx] == "falls":
                guard_awake = False

            # A guard wakes up
            elif self.events[event_idx] == "wakes":
                guard_awake = True

                # When was the guard first asleep in the late hour
                if self.times[event_idx - 1].hour > 0:
                    start_min = 0
                else:
                    start_min = self.times[event_idx - 1].minute

                # Make a record of each minute the guard was asleep
                for min_idx in range(start_min, self.times[event_idx].minute):
                    self.guard_sleep_record[curr_guard][min_idx] += 1

            # A new guard goes on shift
            elif isinstance(self.events[event_idx], int):

                # See if a guard finished the previous shift asleep
                if not guard_awake:
                    for min_idx in range(self.times[event_idx - 1].minute, 60):
                        self.guard_sleep_record[curr_guard][min_idx] += 1

                curr_guard = self.events[event_idx]
                guard_awake = True

        # See if a guard finished the last shift asleep
        if not guard_awake:
            for min_idx in range(self.times[event_idx - 1].minute, 60):
                self.guard_sleep_record[curr_guard][min_idx] += 1

    def bypass_strat_01(self) -> int:
        """
        Find the guard that has the most minutes asleep and return the minute
        that the guard is most likely to be asleep times by the guard id.
        """
        self.generate_guard_sleep_record()

        sleepiest_guard = 0
        sleepiest_time = 0

        # Find the guard who sleeps the most
        for guard in self.guards:
            if sum(self.guard_sleep_record[guard]) > sleepiest_time:
                sleepiest_time = sum(self.guard_sleep_record[guard])
                sleepiest_guard = guard

        min_largest = 0
        min_idx = 0

        # For that guard find the minute he was most likley to be asleep
        for sl_min in range(0, 60):
            if self.guard_sleep_record[sleepiest_guard][sl_min] > min_largest:
                min_largest = self.guard_sleep_record[sleepiest_guard][sl_min]
                min_idx = sl_min

        return min_idx * sleepiest_guard


if __name__ == "__main__":
    print(f"Part 1 = {WatchRecord('./data/input_0.txt').bypass_strat_01()}")
