from phone_record.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __repr__(self):
        return '<User %r>' % self.usernam


class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    detail = db.Column(db.String(255))
    picUrl = db.Column(db.String(255))
    borrowerName = db.Column(db.String(255))
    borrowerPhone = db.Column(db.String(255))
    borrowTime = db.Column(db.Date)
    status = db.Column(db.Integer)

    def __init__(self, id, name, detail, picUrl, borrowerName, borrowerPhone, borrowTime, status):
        self.id = id
        self.name = name
        self.detail = detail
        self.picUrl = picUrl
        self.borrowerName = borrowerName
        self.borrowerPhone = borrowerPhone
        self.borrowTime = borrowTime
        self.status = status

    def __str__(self):
        return 'Sentence object (name="%s")' % self.name

    __repr__ = __str__


class BorrowLog(db.Model):
    __tablename__ = 'borrow_log'

    #表的结构:
    logId = db.Column(db.Integer, primary_key=True)
    phoneId = db.Column(db.Integer)
    phoneName = db.Column(db.String(255))
    borrowerName = db.Column(db.String(255))
    borrowerPhone = db.Column(db.String(255))
    createTime = db.Column(db.Date)
    status = db.Column(db.Integer)

    def __init__(self, logId, phoneId, phoneName, borrowerName, borrowerPhone, createTime, status):
        self.logId = logId
        self.phoneId = phoneId
        self.phoneName = phoneName
        self.borrowerName = borrowerName
        self.borrowerPhone = borrowerPhone
        self.createTime = createTime
        self.status = status

    def __str__(self):
        return 'Sentence object (phoneName="%s")' % self.phoneName

    __repr__ = __str__





