# Using get() to Access Values - alien_no_points.py
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])  # This returns ERROR as POINTS don't EXIST

point_value = alien_0.get('points', 'No point value assigned.')  # Use get() method to set a default value that will
print(point_value)                                               # be returned if the requested key doesn’t exist
