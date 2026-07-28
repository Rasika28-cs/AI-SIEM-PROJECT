from collectors.windows_logs import collect_windows_events


events = collect_windows_events()


for event in events:
    print(event)