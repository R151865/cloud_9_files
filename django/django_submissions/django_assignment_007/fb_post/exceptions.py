class Error(Exception):
    pass



class InvalidUserException(Error):
    pass

class InvalidMemberException(Error):
    pass



class InvalidGroupNameException(Error):
    pass
class InvalidGroupException(Error):
    pass

class UserNotInGroupException(Error):
    pass
class UserIsNotAdminException(Error):
    pass
