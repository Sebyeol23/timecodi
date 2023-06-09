from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserSchema(BaseModel):
    id: str
    pw: str
    name: str

class EventSchema(BaseModel):
    cname: str
    visibility: str
    sdatetime: datetime
    edatetime: datetime
    weekly: int
    enddate: Optional[date]

class displayEvent(BaseModel):
    cid: int
    cname: str
    visibility: str
    sdatetime: datetime
    edatetime: datetime
    weekly: int
    enddate: Optional[date]
    
class GroupSchema(BaseModel):
    gname: str

class MemberSchema(BaseModel):
    gid: int

class InviteSchema(BaseModel):
    uid: str
    gid: int
    
class MeetingSchema(BaseModel):
    gid: int
    title: str
    sdatetime: datetime
    edatetime: datetime
    location: str
    loc_detail: str
    memo: str
    
class displayMeeting(BaseModel):
    meetid: int
    title: str
    sdatetime: datetime
    edatetime: datetime
    location: str
    loc_detail: str
    memo: str

class FriendSchema(BaseModel):
    fid: str

class VoteTimeSchema(BaseModel):
    gid: int
    sdatetime: date
    edatetime: date
    meetingtime: str
    
class VoteSchema(BaseModel):
    gid: int
    vidlist: list