from .models import *
from .exceptions import *

def invalid_user_exception(user_id):
    if not User.objects.filter(pk=user_id).exists():
        raise InvalidUserException

def invalid_group_exception(group_id):
    if not Group.objects.filter(pk=group_id).exists():
        raise InvalidGroupException

def invalid_group_name_exception(name):
    if not name:
        raise InvalidGroupNameException
    
def invalid_member_exception(new_member_id):
    if not User.objects.filter(pk=new_member_id).exists():
        raise InvalidMemberException

def user_not_in_group_exception(group_id,member_id):
    if not Membership.objects.filter(group_id=group_id,member_id=member_id).exists():
        raise UserNotInGroupException
    
    
    


#2
def create_group(user_id, name, member_ids):
    invalid_user_exception(user_id)
    invalid_group_name_exception(name)
    
    member_ids=list(set(member_ids))
    if User.objects.filter(pk__in=member_ids).count()!=len(member_ids):
        raise InvalidMemberException
    
    group=Group.objects.create(name=name)
    
    list_of_members=[]
    list_of_members.append( Membership(group_id=group.id,member_id=user_id,is_admin=True) )
    for ids in member_ids:
        if ids!=user_id:
            list_of_members.append( 
                                    Membership(
                                                group_id=group.id,
                                                member_id=ids
                                               ) 
                                    )
            
    Membership.objects.bulk_create(list_of_members)
    return group.id

#3
def add_member_to_group(user_id, new_member_id, group_id):
    
    invalid_user_exception(user_id)
    
    invalid_member_exception(new_member_id)
    
    invalid_group_exception(group_id)
        
    membership=Membership.objects.filter(group_id=group_id,member_id=user_id)    
    len(membership)
    
    if not membership.exists():
        raise UserNotInGroupException
        
    if not membership[0].is_admin:
        raise UserIsNotAdminException
    if not Membership.objects.filter(group_id=group_id,member_id=new_member_id).exists():
        print('yes it is working')
        Membership.objects.create(
            group_id=group_id,
            member_id=new_member_id
        )        

#4
def remove_member_from_group(user_id, member_id, group_id):
    invalid_user_exception(user_id)
    
    invalid_member_exception(member_id)
    invalid_group_exception(group_id)
    
    user_not_in_group_exception(group_id,member_id)
    
    membership=Membership.objects.filter(group_id=group_id,member_id=user_id)    
    len(membership)
    
    if not membership.exists():
        raise UserNotInGroupException
        
    if not membership[0].is_admin:
        raise UserIsNotAdminException
    
    Membership.objects.filter(group_id=group_id,member_id=member_id).delete()
    
#5
def make_member_as_admin(user_id, member_id, group_id):
    # make memeber as admin
    # if member is already admin do nothing
    
    invalid_user_exception(user_id)
    invalid_member_exception(member_id)
    invalid_group_exception(group_id)
    
    member_as_admin=Membership.objects.filter(group_id=group_id,member_id=member_id)
    len(member_as_admin)
    if not member_as_admin.exists(): 
        raise UserNotInGroupException
        
    elif member_as_admin[0].is_admin:
        return 
        
    user_as_admin=Membership.objects.filter(group_id=group_id,member_id=user_id)    
    len(user_as_admin)
    if not user_as_admin.exists():
        raise UserNotInGroupException
    if not user_as_admin[0].is_admin:
        raise UserIsNotAdminException
    print('yes it is worikgn')
    member_as_admin.upadate(is_admin=True)
    
