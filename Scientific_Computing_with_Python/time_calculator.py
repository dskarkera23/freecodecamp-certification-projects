def add_time(start, duration,start_day=None):
  def time_extractor(start):
    time_split = start.split(":")
    hour= int(time_split[0])
    minute,meridian= time_split[1].split( )
    minute= int(minute)
    if meridian == "PM":
      hour += 12
    return hour,minute,meridian
  def duration_extractor(duration):
    duration_split= duration.split(":")
    dhour= int(duration_split[0])
    dmin= int(duration_split[1])
    return dhour,dmin
  
  wd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  start_hour, start_minute, meridian = time_extractor(start)
  duration_hours, duration_minutes = duration_extractor(duration)

  upd_hour = start_hour + duration_hours
  upd_min = start_minute + duration_minutes

  if upd_min >= 60:
      upd_hour += 1
      upd_min -= 60

  days_later = 0

  while upd_hour >= 24:
      upd_hour -= 24
      days_later += 1

  if start_day:
      new_day_idx = (wd.index(start_day.lower().capitalize()) + days_later) % 7
  else:
      new_day_idx = None

  if new_day_idx is not None:
      new_day = wd[new_day_idx]
  else:
      new_day = None

  new_time = str((upd_hour - 1) % 12 + 1) + ":" + str(upd_min).zfill(2) 
  new_time += " " + ('AM' if upd_hour < 12 else 'PM')
  if start_day and new_day:
    new_time += ", " + str(new_day)
  if days_later > 0:
      if days_later == 1:
          new_time += " (next day)"
      else:
          new_time += " ({} days later)".format(days_later)

  

  return new_time