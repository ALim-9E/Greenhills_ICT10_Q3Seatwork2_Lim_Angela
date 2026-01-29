# SEATWORK 2
from pyscript import when, document

@when("change", "#confirm_box")
def present_intrams_team(e):
        registration = document.querySelector('input[name="online"].checked').value

        clearance = document.querySelector('input[name="medical"].checked').value

        document.getElementById('output').innerHTML = ' '

        if registration == 'no':
            display(f'Please register your account.', target='output')
        else:
            display(f'Invalid input', target='output')


        if clearance == 'no':
            display(f'Please get your medical clearance.', target='output')
        else:
            display(f'Invalid input', target='output')
        


