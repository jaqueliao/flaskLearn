import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from phone_record.auth import login_required
from phone_record.database import db
from phone_record.model import Phone, BorrowLog

bp = Blueprint('phone', __name__)


@bp.route("/")
@login_required
def index():
    phones = queryAllPhone()
    myPhones = []
    for phone in phones:
        if g.phone == phone.borrowerPhone:
            myPhones.append(phone)

    return render_template('phone/index.html', phones=phones, myPhones=myPhones)


@bp.route("/borrow")
@login_required
def borrow():
    phoneIds = request.values.getlist("phoneId")
    print(phoneIds)
    for phoneId in phoneIds:
        borrowPhone(int(phoneId))
    return redirect(url_for('index'))


@bp.route("/giveBack")
@login_required
def giveBack():
    phoneIds = request.values.getlist("phoneId")
    print(phoneIds)
    for phoneId in phoneIds:
        givebackPhone(int(phoneId))
    return redirect(url_for('index'))


Base = declarative_base()


class Phone1(Base):
    __tablename__ = 'phone'

    #表的结构:
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    detail = Column(String(255))
    picUrl = Column(String(255))
    borrowerName = Column(String(255))
    borrowerPhone = Column(String(255))
    borrowTime = Column(Date())
    status = Column(Integer())

    def __str__(self):
        return 'Sentence object (name="%s")' % self.name

    __repr__ = __str__


class BorrowLog1(Base):
    __tablename__ = 'borrow_log'

    #表的结构:
    logId = Column(Integer(), primary_key=True)
    phoneId = Column(Integer())
    phoneName = Column(String(255))
    borrowerName = Column(String(255))
    borrowerPhone = Column(String(255))
    createTime = Column(Date())
    status = Column(Integer())

    def __str__(self):
        return 'Sentence object (phoneName="%s")' % self.phoneName

    __repr__ = __str__


def queryAllPhone():
    """
    查询所有信息
    :return:
    """
    startTime = datetime.now()
    phones = Phone.query().all()
    endTime = datetime.now()
    print(endTime-startTime)
    return phones


def borrowPhone(phoneId):
    phoneInfo = Phone.query().filter_by(id == phoneId).first()
    phoneInfo.borrowerName = g.username
    phoneInfo.borrowerPhone = g.phone
    phoneInfo.borrowTime = datetime.now()
    phoneInfo.status = 1
    borrowLog = BorrowLog(phoneId=phoneId,
                          phoneName=phoneInfo.name,
                          borrowerName=g.username,
                          borrowerPhone=g.phone,
                          createTime=datetime.now(),
                          status=0)
    db.session.add(borrowLog)
    db.session.commit()


def givebackPhone(phoneId):
    phoneInfo = Phone.query().filter_by(id == phoneId).first()
    phoneInfo.borrowerName = ''
    phoneInfo.borrowerPhone = ''
    phoneInfo.borrowTime = datetime.now()
    phoneInfo.status = 0
    borrowLog = BorrowLog(phoneId=phoneId,
                          phoneName=phoneInfo.name,
                          borrowerName=g.username,
                          borrowerPhone=g.phone,
                          createTime=datetime.now(),
                          status=1)
    db.session.add(borrowLog)
    db.session.commit()


