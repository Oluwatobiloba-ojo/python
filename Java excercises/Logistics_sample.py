base_pay = 5000
result = 0


def allowance(percentage):

        if percentage < 50:
            result = percentage * 160 + base_pay
        elif percentage <= 59:
            result = percentage * 200 + base_pay
        elif percentage <= 69:
            result = percentage * 250 + base_pay
        else:
            result = percentage * 500 + base_pay
        return result

