def pasre(srt_data):
    #with open('./balbla.srt', 'r') as f:
    #    srt_data = f.read()

    srt_data = srt_data.split("\n\n")
    finished_segments = []
    for segment in srt_data:
        print(segment)
        # split the string by line break
        segment = segment.split("\n")
        # split the start time and end time
        time_split = segment[1].split(" --> ")
        print(time_split)
        # get the start time in seconds
        start_split = time_split[0].split(":")
        print(start_split)
        start_hours = int(start_split[0])
        start_hours = start_hours*3600
        start_minutes = int(start_split[1])
        start_minutes = start_minutes*60
        start_seconds = start_split[2]
        start_seconds = start_seconds.replace(",", "." )
        start_seconds = float(start_seconds)
        start_time_seconds = start_hours + start_minutes + start_seconds
        # get the end time in seconds
        end_split = time_split[1].split(":")
        end_hours = int(end_split[0])
        end_hours = end_hours*3600
        end_minutes = int(end_split[1])
        end_minutes = end_minutes*60
        end_seconds = end_split[2]
        end_seconds = end_seconds.replace(",", "." )
        end_seconds = float(end_seconds)
        end_time_seconds = end_hours + end_minutes + end_seconds
        # get the duration in seconds
        duration = end_time_seconds - start_time_seconds
        # bild back the content of the captions
        content = ""
        for line in segment[1:]:
            content = content + line + "\n"
        # create and append a dictionary to the finished)segments list
        full = {"Start": start_time_seconds, "End": end_time_seconds, "Duration": duration, "Content": content}
        finished_segments.append(full)
    print(finished_segments)

    return finished_segments