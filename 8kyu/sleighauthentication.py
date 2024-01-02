class Sleigh(object):
    def authenticate(self, name, password):
        name_ = 'Santa Clause'
        password_ = 'Ho Ho Ho!'
        if name == name_ and password == password_:
            return True
        else:
            return False
