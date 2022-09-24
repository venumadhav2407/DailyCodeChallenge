# Time Conversion


def timeConversion(s):
    
    hr = int(s[0:2])
    if 'PM' in s and hr != 12:
        hr += 12
        s = str(hr)+s[2:8]
    elif 'AM' in s and hr == 12:
        s = '00'+s[2:8]
    return s[0:8]

 s = input() # In the format of "00:00:00AM/PM"
