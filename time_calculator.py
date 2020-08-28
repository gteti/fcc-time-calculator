def add_time(start, duration, optional=None):
  daysOfWeek =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  slots = ["AM","PM"]

  inputTime = start.split()
  temp = inputTime[0].split(":")
  hoursStart = temp[0]
  minutesStart = temp[1]
  timeSlot = inputTime[1]
  #print(hoursStart)
  #print(minutesStart)
  #print(timeSlot)

  inputDuration = duration.split(":")
  hoursDuration = inputDuration[0]
  minutesDuration = inputDuration[1]
 # print(hoursDuration+":"+minutesDuration)

  if hoursDuration == 0 and minutesDuration == 0:
    return start
  
  hoursSum    = (int(hoursStart)) + (int(hoursDuration))
  minutesSum  = (int(minutesStart)) + (int(minutesDuration))
  countDay = 0
  outTime = ""

  #Handles minutes and hours overflow
  if minutesSum >=60:
      hoursSum = hoursSum +1
      minutesSum = minutesSum -60
  

  while hoursSum>=24:
      hoursSum = hoursSum -24
      countDay = countDay +1
  
  indexSlot = slots.index(timeSlot)

  if hoursSum >= 12:
    indexSlotRes = (indexSlot+1) %2
    if (timeSlot == "PM"):
      countDay = countDay + 1
  else:
    indexSlotRes = (indexSlot) %2

  if(hoursSum)>12:
    hoursSum = hoursSum -12
   
  outTime = outTime + str(hoursSum) + ":" 


  if len(str(minutesSum)) ==1:
      outTime = outTime + '0' + str(minutesSum) 
  else:
      outTime = outTime + str(minutesSum)

  outTime = outTime +" " + slots[indexSlotRes]

  if optional is not None:
    dayOfw = optional.lower()
    indexValue = daysOfWeek.index(dayOfw)    
    daysSum = indexValue + countDay
    daysResult = daysSum % 7
    outTime = outTime + ", " + daysOfWeek[daysResult].capitalize()

  #Handles the next day and N days later
  if (countDay == 1):
    outTime = outTime + " (next day)"
  elif(countDay >1):
    outTime = outTime + " ("+str(countDay)+" days later)"



  new_time = outTime




  return new_time