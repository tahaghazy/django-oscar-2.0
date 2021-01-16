import oscar.apps.customer.apps as apps


class CustomerConfig(apps.CustomerConfig):
    label = 'customer'
    name = 'apps.customer'
    verbose_name = 'Customer'
