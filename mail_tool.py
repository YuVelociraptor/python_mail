import os
import email
from email.header import decode_header


# メールの件名を取得
def get_email_subject(email_object):
    (subject, subject_charaset) = decode_header(email_object['Subject'])[0]

    if subject_charaset == None:
        email_subject = subject
    else:
        email_subject = subject.decode(subject_charaset)

    return email_subject


def get_addresses(email_obj, address_type):
    return email_obj[address_type]


def get_from(email_obj):
    return get_addresses(email_obj, 'From')


def get_to(email_obj):
    ret = get_addresses(email_obj, 'To')

    if ret is not None:
        ret = ret.replace(' ', '').replace('\n', '').replace('\t', '').split(',')

    return ret


def get_cc(email_obj):
    ret = get_addresses(email_obj, 'Cc')

    if ret is not None:
        ret = ret.replace(' ', '').replace('\n', '').replace('\t', '').split(',')

    return ret


def get_bcc(email_obj):
    ret = get_addresses(email_obj, 'Bcc')

    if ret is not None:
        ret = ret.replace(' ', '').replace('\n', '').replace('\t', '')

    return ret



for file in os.listdir(dir):


    f = open(dir + file)
    data = f.read()
    f.close()

    email_object = email.message_from_string(data)

    print(file)
    print(get_email_subject(email_object))

    print(email_object.keys())
    # print(email_object['From'])
    # print(email_object['To'])
    # print(email_object['Cc'])
    # print(email_object['Bcc'])
    print(get_bcc(email_object))
    print('\n\n')
