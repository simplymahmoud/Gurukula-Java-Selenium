# -*- coding: utf-8 -*-
import logging
import os
from base import BaseTest


# Initiate testsuite logger
logger = logging.getLogger('portal_testsuite')
if not os.path.exists('logs/portal_testsuite.log'):
    os.mkdir('logs')
handler = logging.FileHandler('logs/portal_testsuite.log')
formatter = logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                              '%d-%m-%Y %H:%M:%S %Z')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

#element paths we use during test
BaseTest.elements = {'login': "//html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/a",
                     'login_text': "//html/body/div[3]/div[1]/div/div/div[2]/div/div[1]",
                     'account_menu': ".//*[@id='navbar-collapse']/ul/li[3]/a/span",
                     'logout': ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[4]/a/span[2]",
                     'rememberme': ".//*[@id='rememberMe']",
                     'username': ".//*[@id='username']",
                     'password': ".//*[@id='password']",
                     'login_button': "//html/body/div[3]/div[1]/div/div/div/form/button",
                     'logged': "//html/body/div[3]/div[1]/div/div/div[2]/div/div",                     
                     'authentication_error': "//html/body/div[3]/div[1]/div/div/div/div[1]",
                     'register_new_user': "//html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/a",
                     'register_login': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/input",
                     'register_email': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/input",
                     'register_newpasswd': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/input",
                     'register_passwdcfm': "//html/body/div[3]/div[1]/div/div/div/form/div[4]/input",
                     'register_button': "// html/body/div[3]/div[1]/div/div/div/form/button",
                     'registration_error': "//html/body/div[3]/div[1]/div/div/div/div[2]",
                     'registration_loginreq': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div/p[1]",
                     'registration_invalidlogin': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div/p[4]",
                     'registration_mailreq': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[1]",
                     'registration_invalidmail': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[2]",
                     'registration_invalidmaillenght': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[3]",
                     'registration_invalidpasswdlenght': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div[1]/p[2]",
                     'registration_maxpasswdlenght': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div[1]/p[3]",
                     'registration_passwdreq': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div[1]/p[1]",
                     'registration_invalidcnfpasswdlenght': "//html/body/div[3]/div[1]/div/div/div/form/div[4]/div/p[2]",
                     'registration_cnfpasswdreq': "//html/body/div[3]/div[1]/div/div/div/form/div[4]/div/p[1]",
                     'registration_passmissmatch': "//html/body/div[3]/div[1]/div/div/div/div[5]",
                     'registration_passbar1': ".//*[@id='strengthBar']/li[1]",
                     'registration_passbar2': ".//*[@id='strengthBar']/li[2]",
                     'registration_passbar3': ".//*[@id='strengthBar']/li[3]",
                     'registration_passbar4': ".//*[@id='strengthBar']/li[4]",
                     'registration_passbar5': ".//*[@id='strengthBar']/li[5]",
                     }