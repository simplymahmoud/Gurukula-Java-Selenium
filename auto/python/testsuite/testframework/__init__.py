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
                     'account_settings': ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[1]/a/span[2]",
                     'settings_title': "//html/body/div[3]/div[1]/div/div/div/h2",
                     'settings_firstname': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/input",
                     'settings_firstnamereq': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div/p[1]",
                     'settings_lastname': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/input",
                     'settings_lastnamereq': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[1]",
                     'settings_email': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/input",
                     'settings_invalidmail': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div/p[2]",
                     'settings_invalidmaillenght': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div/p[3]",
                     'settings_mailreq': "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div/p[1]",
                     'settings_language': "//html/body/div[3]/div[1]/div/div/div/form/div[4]/select",
                     'settings_save_button': "//html/body/div[3]/div[1]/div/div/div/form/button",
                     'settings_saved': "//html/body/div[3]/div[1]/div/div/div/div[1]",
                     'settings_notsaved': "//html/body/div[3]/div[1]/div/div/div/div[3]/strong",
                     'account_passwords': ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[2]/a/span[2]",
                     'passwords_title': "//html/body/div[3]/div[1]/div/div/div/h2",
                     'passwords_newpasswd': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/input",
                     'passwords_invalidpasswdlenght': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div[1]/p[2]",
                     'passwords_passwdreq': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div[1]/p[1]",
                     'passwords_maxpasswdlenght': "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div[1]/p[3]",
                     'passwords_passwdcnf': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/input",
                     'passwords_invalidpasswdcnflenght': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[2]",
                     'passwords_passwdcnfreq': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[1]",
                     'passwords_maxcnfpasswdlenght': "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[3]",
                     'passwords_save_button': "//html/body/div[3]/div[1]/div/div/div/form/button",
                     'passwords_notsaved': "//html/body/div[3]/div[1]/div/div/div/div[2]/strong",
                     'passwords_passmissmatch': "//html/body/div[3]/div[1]/div/div/div/div[3]",
                     'account_session': ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[3]/a/span[2]",
                     'entities_menu': ".//*[@id='navbar-collapse']/ul/li[2]/a/span/span[2]",
                     'entities_branch': ".//*[@id='navbar-collapse']/ul/li[2]/ul/li[1]/a/span[2]",
                     'entities_staff': ".//*[@id='navbar-collapse']/ul/li[2]/ul/li[2]/a/span[2]",
                     'create_new_branch_button': "//html/body/div[3]/div[1]/div/div[1]/div/div[1]/button",
                     'search_branch_button': "//html/body/div[3]/div[1]/div/div[1]/div/div[2]/form/button",
                     'new_branch_id': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[1]/input",
                     'new_branch_name': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/input",
                     'new_branch_name_req': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[1]",
                     'new_branch_name_invalid_length': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[2]",
                     'new_branch_name_invalid': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[4]",
                     'new_branch_name_invalid_maxlength': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[3]",
                     'new_branch_code': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/input",
                     'new_branch_code_req': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[1]",
                     'new_branch_code_invalid_length': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[2]",
                     'new_branch_code_invalid': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[4]",
                     'new_branch_code_invalid_maxlength': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[3]",
                     'cancel_branch_button': ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[1]",
                     'save_branch_button': ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[2]",
                     'search_branch_text': ".//*[@id='searchQuery']",
                     'search_branch_button': "//html/body/div[3]/div[1]/div/div[1]/div/div[2]/form/button",
                     'search_branch_cancel_delete': ".//*[@id='deleteBranchConfirmation']/div/div/form/div[3]/button[1]",
                     'search_branch_confirm_delete': ".//*[@id='deleteBranchConfirmation']/div/div/form/div[3]/button[2]",
                     'search_branch_table': "//html/body/div[3]/div[1]/div/div[4]/table",
                     'search_branch_view_name': "//html/body/div[3]/div[1]/div/div/table/tbody/tr[1]/td[2]/input",
                     'search_branch_view_code': "//html/body/div[3]/div[1]/div/div/table/tbody/tr[2]/td[2]/input",
                     'view_back_button': "//html/body/div[3]/div[1]/div/button",
                     'edit_branch_name': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/input",
                     'new_branch_code': ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/input",
                     'save_edit_branch_button': ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[2]",
                     'cancel_edit_branch_button': ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[1]",
                     'new_staff_id': ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[1]/input",
                     'new_staff_name': ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/input",
                     'new_staff_name_req': ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/div/p[1]",
                     'new_staff_name_invalid': ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/div/p[4]",
                     'new_staff_name_invalid_maxlength': ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/div/p[3]",
                     'staff_dropdown': ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[3]/select",
                     'save_staff_button': ".//*[@id='saveStaffModal']/div/div/form/div[3]/button[2]",
                     'search_staff_confirm_delete': ".//*[@id='deleteStaffConfirmation']/div/div/form/div[3]/button[2]",
                     'cancel_staff_button': ".//*[@id='saveStaffModal']/div/div/form/div[3]/button[1]",
                     'search_staff_view_name': "//html/body/div[3]/div[1]/div/div/table/tbody/tr[1]/td[2]/input",
                     'search_staff_view_branch': "//html/body/div[3]/div[1]/div/div/table/tbody/tr[2]/td[2]/input",
                     'save_edit_staff_button': ".//*[@id='saveStaffModal']/div/div/form/div[3]/button[2]",
                     'staff_paging_first_page': "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[1]/a",
                     'staff_paging_previos_page': "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[2]/a",
                     'staff_paging_next_page': "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[3]/a",
                     'staff_paging_last_page': "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[4]/a",
                     }