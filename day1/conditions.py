# conditional statements

is_Warm = True
is_Cold = True

if is_Warm:
    print('Today is hot')

elif is_Cold:
    print('Today is cold')

if is_Cold and is_Warm:
    print('Today is normal too')
if is_Cold or is_Warm:
    print('Nothing')

else:
    print('Today is normal')