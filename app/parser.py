import datetime

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

        if rem_dupes[-1].code == 0:
            rem_dupes = rem_dupes[:-1]

        tic = 0
        for i in range(0, len(rem_dupes) - 1, 2):
            tic += rem_dupes[i+1].time - rem_dupes[i].time


        first_entry = datetime.datetime.fromtimestamp(rem_dupes[0].time)
        last_exit = datetime.datetime.fromtimestamp(rem_dupes[-1].time)

        print("Time in class", tic)

        result = {}
        result['name'] = person
        result['first_entry'] = first_entry.strftime('%H:%M:%S, %b %d %Y')
        result['last_exit'] = last_exit.strftime('%H:%M:%S, %b %d %Y')
        result['time_in_class'] = str(tic / 60) + " minutes"
        result['present'] = "Present" if tic > 1 * 60 else "Absent"

        results.append(result)

    return results
