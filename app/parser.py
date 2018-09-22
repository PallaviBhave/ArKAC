import datetime, time

def parse(events):
    people = { i.name for i in events }
    people = list(people)

    results = []

    for person in people:
        all_entries = filter(lambda x : x.name == person, events)

        rem_dupes = []
        code = 0

        for entry in all_entries:
            if entry.code == code:
                rem_dupes.append(entry)
                code = 1 - code

        first_entry = datetime.datetime.fromtimestamp(rem_dupes[0].time)

        if rem_dupes[-1].code == 0:
            rem_dupes = rem_dupes[:-1]

        tic = 0
        for i in range(0, len(rem_dupes) - 1, 2):
            tic += rem_dupes[i+1].time - rem_dupes[i].time

        result = {}
        try:
            last_exit = datetime.datetime.fromtimestamp(rem_dupes[-1].time)
            result['last_exit'] = last_exit.strftime('%H:%M:%S, %b %d %Y')
        except:
            result['last_exit'] = '-'

        result['name'] = person
        result['first_entry'] = first_entry.strftime('%H:%M:%S, %b %d %Y')
        result['time_in_class'] = "%0.2f minutes" % (tic / 60.0)
        result['present'] = "Present" if tic > 1 * 60 else "Absent"

        results.append(result)

    return results
