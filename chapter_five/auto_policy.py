class auto_policy:
    def __init__(self):
        self._account_number = 00000
        self._make_model = ''
        self._state = ''

    def set_account_number(self, account):
        self._account_number = account

    def get_auto_policy(self):
        return self._account_number

    def set_make_model(self, model):
        self._make_model = model

    def get_make_model(self):
        return self._make_model

    def setstate(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def is_no_fault_state(self):
        validate_state = ''
        if self._state.__contains__(' '):
            first_character = self._state[0]
            white_space = self._state.find(" ")
            validate_state = first_character.upper() + self._state[white_space + 1].upper()
        else:
            first = self._state[0].upper()
            last = self._state[len(self._state) - 1].upper()
            validate_state = first + last
        return validate_state == "NY" or validate_state == 'NJ' or validate_state == 'NH' or validate_state == 'CT'\
            or validate_state == 'VT' or validate_state == 'ME' or \
            self._state[0] + self._state[1] == 'MA' or validate_state == 'PA'
